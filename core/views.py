from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings
from .models import UserProgress


def home(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    return render(request, 'core/home.html')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            UserProgress.objects.create(user=user)
            login(request, user)
            return redirect('dashboard')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


@login_required
def dashboard(request):
    progress, _ = UserProgress.objects.get_or_create(user=request.user)
    modules = settings.LEARNING_MODULES
    for module in modules:
        module['completed'] = progress.is_module_completed(module['id'])
        module['current'] = module['id'] == progress.current_module
    context = {
        'modules': modules,
        'progress': progress,
        'completed_count': len(progress.completed_modules),
        'total_modules': len(modules),
    }
    return render(request, 'core/dashboard.html', context)


@login_required
def module_detail(request, module_slug):
    progress, _ = UserProgress.objects.get_or_create(user=request.user)
    modules = settings.LEARNING_MODULES
    current_module = next((m for m in modules if m['slug'] == module_slug), None)
    
    if not current_module:
        return redirect('dashboard')
    
    context = {
        'module': current_module,
        'modules': modules,
        'progress': progress,
        'is_completed': progress.is_module_completed(current_module['id']),
    }
    return render(request, 'core/module_detail.html', context)


@login_required
def complete_module(request, module_id):
    if request.method == 'POST':
        progress, _ = UserProgress.objects.get_or_create(user=request.user)
        progress.complete_module(module_id)
    return redirect('dashboard')
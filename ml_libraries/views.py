from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Prefetch
from .models import MLibrary, TrainingStep, LibraryComparison


def library_list(request):
    libraries = MLibrary.objects.filter(is_active=True).prefetch_related('training_steps')
    
    categorized = {}
    for lib in libraries:
        if lib.category not in categorized:
            categorized[lib.category] = []
        categorized[lib.category].append(lib)
    
    category_labels = {
        'classical': 'Classical ML',
        'deep_learning': 'Deep Learning',
        'gradient_boosting': 'Gradient Boosting',
        'data_manipulation': 'Data Manipulation',
        'visualization': 'Visualization',
        'deployment': 'Deployment',
    }
    
    context = {
        'categorized_libraries': categorized,
        'category_labels': category_labels,
    }
    return render(request, 'ml_libraries/library_list.html', context)


def library_detail(request, slug):
    library = get_object_or_404(MLibrary.objects.prefetch_related('training_steps'), slug=slug, is_active=True)
    steps = library.training_steps.all()
    
    context = {
        'library': library,
        'steps': steps,
    }
    return render(request, 'ml_libraries/library_detail.html', context)


def training_pipeline(request):
    libraries = MLibrary.objects.filter(is_active=True, category__in=['classical', 'deep_learning', 'gradient_boosting'])
    
    pipeline_steps = [
        {'id': 'setup', 'name': '1. Setup & Imports', 'icon': 'gear'},
        {'id': 'data_loading', 'name': '2. Load Data', 'icon': 'database'},
        {'id': 'preprocessing', 'name': '3. Preprocess', 'icon': 'filter'},
        {'id': 'feature_engineering', 'name': '4. Feature Engineering', 'icon': 'magic'},
        {'id': 'model_selection', 'name': '5. Select Model', 'icon': 'cpu'},
        {'id': 'training', 'name': '6. Train', 'icon': 'play-circle'},
        {'id': 'evaluation', 'name': '7. Evaluate', 'icon': 'graph-up'},
        {'id': 'tuning', 'name': '8. Tune Hyperparameters', 'icon': 'sliders'},
        {'id': 'deployment', 'name': '9. Deploy', 'icon': 'cloud-upload'},
    ]
    
    context = {
        'libraries': libraries,
        'pipeline_steps': pipeline_steps,
    }
    return render(request, 'ml_libraries/training_pipeline.html', context)


def library_comparison(request):
    comparisons = LibraryComparison.objects.prefetch_related('libraries').all()
    libraries = MLibrary.objects.filter(is_active=True)
    
    context = {
        'comparisons': comparisons,
        'libraries': libraries,
    }
    return render(request, 'ml_libraries/comparison.html', context)


@login_required
def save_library_note(request, slug):
    if request.method == 'POST':
        library = get_object_or_404(MLibrary, slug=slug)
        # Note saving logic would go here
        pass
    return render(request, 'ml_libraries/library_detail.html', {'library': library})
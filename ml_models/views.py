from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import MLModel, Hyperparameter


def model_catalog(request):
    category = request.GET.get('category', '')
    problem_type = request.GET.get('problem_type', '')
    complexity = request.GET.get('complexity', '')
    search = request.GET.get('q', '')

    models_qs = MLModel.objects.all()

    if category:
        models_qs = models_qs.filter(category=category)
    if problem_type:
        models_qs = models_qs.filter(problem_types__contains=[problem_type])
    if complexity:
        models_qs = models_qs.filter(complexity=complexity)
    if search:
        models_qs = models_qs.filter(
            Q(name__icontains=search) |
            Q(description__icontains=search) |
            Q(functionality__icontains=search)
        )

    categorized = {}
    for model in models_qs:
        if model.category not in categorized:
            categorized[model.category] = []
        categorized[model.category].append(model)

    featured = MLModel.objects.filter(is_featured=True)[:6]

    context = {
        'categorized': categorized,
        'category': category,
        'problem_type': problem_type,
        'complexity': complexity,
        'search': search,
        'featured': featured,
        'category_choices': MLModel.CATEGORY_CHOICES,
        'problem_type_choices': MLModel.PROBLEM_TYPE_CHOICES,
        'complexity_choices': MLModel.COMPLEXITY_CHOICES,
    }
    return render(request, 'ml_models/model_catalog.html', context)


def model_detail(request, slug):
    model = get_object_or_404(MLModel, slug=slug)
    hyperparams = model.hyperparams.all()
    related = MLModel.objects.filter(
        category=model.category
    ).exclude(id=model.id)[:4]

    context = {
        'model': model,
        'hyperparams': hyperparams,
        'related': related,
    }
    return render(request, 'ml_models/model_detail.html', context)


def model_compare(request):
    slugs = request.GET.getlist('models')
    models_qs = MLModel.objects.filter(slug__in=slugs) if slugs else MLModel.objects.all()[:3]

    all_models = MLModel.objects.all()

    context = {
        'selected_models': models_qs,
        'all_models': all_models,
        'selected_slugs': slugs,
    }
    return render(request, 'ml_models/model_compare.html', context)
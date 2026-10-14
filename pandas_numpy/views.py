from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import FunctionEntry


def function_list(request):
    library = request.GET.get('library', 'pandas')
    category = request.GET.get('category', '')
    difficulty = request.GET.get('difficulty', '')
    search = request.GET.get('q', '')

    functions = FunctionEntry.objects.filter(library=library)

    if category:
        functions = functions.filter(category=category)
    if difficulty:
        functions = functions.filter(difficulty=difficulty)
    if search:
        functions = functions.filter(
            Q(name__icontains=search) |
            Q(short_description__icontains=search) |
            Q(signature__icontains=search)
        )

    categories = FunctionEntry.objects.filter(library=library).values_list('category', flat=True).distinct()
    category_labels = dict(FunctionEntry.CATEGORY_CHOICES)
    categorized = {}
    for func in functions:
        if func.category not in categorized:
            categorized[func.category] = []
        categorized[func.category].append(func)

    popular = FunctionEntry.objects.filter(library=library, is_popular=True)[:10]

    context = {
        'library': library,
        'category': category,
        'difficulty': difficulty,
        'search': search,
        'categorized': categorized,
        'categories': [(c, category_labels.get(c, c)) for c in categories],
        'popular': popular,
        'library_choices': FunctionEntry.LIBRARY_CHOICES,
        'difficulty_choices': FunctionEntry.DIFFICULTY_CHOICES,
    }
    return render(request, 'pandas_numpy/function_list.html', context)


def function_detail(request, library, name):
    func = get_object_or_404(FunctionEntry, library=library, name=name)
    related = []
    for rel_name in func.related_functions:
        parts = rel_name.split('.')
        if len(parts) == 2:
            rel = FunctionEntry.objects.filter(library=parts[0], name=parts[1]).first()
            if rel:
                related.append(rel)

    same_category = FunctionEntry.objects.filter(
        library=func.library, category=func.category
    ).exclude(id=func.id)[:6]

    context = {
        'func': func,
        'related': related,
        'same_category': same_category,
    }
    return render(request, 'pandas_numpy/function_detail.html', context)


def search_functions(request):
    query = request.GET.get('q', '')
    results = []
    if query:
        results = FunctionEntry.objects.filter(
            Q(name__icontains=query) |
            Q(short_description__icontains=query) |
            Q(signature__icontains=query)
        )[:30]
    context = {'query': query, 'results': results}
    return render(request, 'pandas_numpy/search.html', context)


def playground(request):
    context = {
        'sample_code': request.GET.get('code', '''import pandas as pd
import numpy as np

# Create a sample DataFrame
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana'],
    'Age': [25, 30, 35, 28],
    'City': ['NYC', 'LA', 'Chicago', 'Houston']
})

print("DataFrame:")
print(df)
print("\\nDescribe:")
print(df.describe())
''')
    }
    return render(request, 'pandas_numpy/playground.html', context)
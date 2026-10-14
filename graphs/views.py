import json
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_POST
from django.contrib import messages
from .models import ChartTemplate, SavedChart

CHART_CODE_GENERATORS = {
    'line': {
        'matplotlib': '''import matplotlib.pyplot as plt
import numpy as np

# Your data
x = {x_data}
y = {y_data}

# Create the line chart
plt.figure(figsize=(10, 6))
plt.plot(x, y, marker='o', linewidth=2, markersize=6, label='{y_label}')
plt.title('{title}', fontsize=16, fontweight='bold')
plt.xlabel('{x_label}', fontsize=12)
plt.ylabel('{y_label}', fontsize=12)
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()''',
        'plotly': '''import plotly.express as px
import pandas as pd

# Your data
df = pd.DataFrame({{
    '{x_label}': {x_data},
    '{y_label}': {y_data}
}})

# Create interactive line chart
fig = px.line(df, x='{x_label}', y='{y_label}', title='{title}', markers=True)
fig.update_layout(
    template='plotly_white',
    font=dict(size=12),
    hovermode='x unified'
)
fig.show()''',
        'seaborn': '''import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Your data
df = pd.DataFrame({{
    '{x_label}': {x_data},
    '{y_label}': {y_data}
}})

# Create styled line chart
plt.figure(figsize=(10, 6))
sns.set_theme(style='whitegrid')
sns.lineplot(data=df, x='{x_label}', y='{y_label}', marker='o', linewidth=2)
plt.title('{title}', fontsize=16, fontweight='bold')
plt.tight_layout()
plt.show()'''
    },
    'bar': {
        'matplotlib': '''import matplotlib.pyplot as plt

# Your data
categories = {x_data}
values = {y_data}

# Create bar chart
plt.figure(figsize=(10, 6))
bars = plt.bar(categories, values, color='steelblue', edgecolor='navy', alpha=0.8)
plt.title('{title}', fontsize=16, fontweight='bold')
plt.xlabel('{x_label}', fontsize=12)
plt.ylabel('{y_label}', fontsize=12)
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

# Add value labels on bars
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height,
             f'{height:.0f}', ha='center', va='bottom')
plt.show()''',
        'plotly': '''import plotly.express as px
import pandas as pd

# Your data
df = pd.DataFrame({{
    '{x_label}': {x_data},
    '{y_label}': {y_data}
}})

# Create interactive bar chart
fig = px.bar(df, x='{x_label}', y='{y_label}', title='{title}',
             color='{y_label}', color_continuous_scale='Blues')
fig.update_layout(template='plotly_white', xaxis_tickangle=-45)
fig.show()''',
        'seaborn': '''import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Your data
df = pd.DataFrame({{
    '{x_label}': {x_data},
    '{y_label}': {y_data}
}})

# Create styled bar chart
plt.figure(figsize=(10, 6))
sns.set_theme(style='whitegrid')
sns.barplot(data=df, x='{x_label}', y='{y_label}', palette='Blues_d')
plt.title('{title}', fontsize=16, fontweight='bold')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()'''
    },
    'scatter': {
        'matplotlib': '''import matplotlib.pyplot as plt

# Your data
x = {x_data}
y = {y_data}

# Create scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(x, y, alpha=0.6, edgecolors='navy', s=80)
plt.title('{title}', fontsize=16, fontweight='bold')
plt.xlabel('{x_label}', fontsize=12)
plt.ylabel('{y_label}', fontsize=12)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()''',
        'plotly': '''import plotly.express as px
import pandas as pd

# Your data
df = pd.DataFrame({{
    '{x_label}': {x_data},
    '{y_label}': {y_data}
}})

# Create interactive scatter plot
fig = px.scatter(df, x='{x_label}', y='{y_label}', title='{title}',
                 size_max=15, opacity=0.7)
fig.update_layout(template='plotly_white')
fig.show()''',
        'seaborn': '''import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Your data
df = pd.DataFrame({{
    '{x_label}': {x_data},
    '{y_label}': {y_data}
}})

# Create styled scatter plot
plt.figure(figsize=(10, 6))
sns.set_theme(style='whitegrid')
sns.scatterplot(data=df, x='{x_label}', y='{y_label}', s=80, alpha=0.6)
plt.title('{title}', fontsize=16, fontweight='bold')
plt.tight_layout()
plt.show()'''
    },
    'histogram': {
        'matplotlib': '''import matplotlib.pyplot as plt

# Your data
data = {x_data}

# Create histogram
plt.figure(figsize=(10, 6))
plt.hist(data, bins={bins}, color='steelblue', edgecolor='navy', alpha=0.8)
plt.title('{title}', fontsize=16, fontweight='bold')
plt.xlabel('{x_label}', fontsize=12)
plt.ylabel('Frequency', fontsize=12)
plt.axvline(sum(data)/len(data), color='red', linestyle='--', label=f'Mean: {sum(data)/len(data):.1f}')
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()''',
        'plotly': '''import plotly.express as px
import pandas as pd

# Your data
df = pd.DataFrame({{'{x_label}': {x_data}}})

# Create interactive histogram
fig = px.histogram(df, x='{x_label}', nbins={bins}, title='{title}',
                   marginal='box')
fig.update_layout(template='plotly_white')
fig.show()''',
        'seaborn': '''import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Your data
df = pd.DataFrame({{'{x_label}': {x_data}}})

# Create styled histogram
plt.figure(figsize=(10, 6))
sns.set_theme(style='whitegrid')
sns.histplot(data=df, x='{x_label}', bins={bins}, kde=True)
plt.title('{title}', fontsize=16, fontweight='bold')
plt.tight_layout()
plt.show()'''
    },
    'box': {
        'matplotlib': '''import matplotlib.pyplot as plt

# Your data
data = {data_lists}

# Create box plot
plt.figure(figsize=(10, 6))
plt.boxplot(data, labels={labels})
plt.title('{title}', fontsize=16, fontweight='bold')
plt.ylabel('{y_label}', fontsize=12)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()''',
        'plotly': '''import plotly.express as px
import pandas as pd

# Your data
df = pd.DataFrame({{
    'Category': {all_categories},
    'Value': {all_values}
}})

# Create interactive box plot
fig = px.box(df, x='Category', y='Value', title='{title}', points='all')
fig.update_layout(template='plotly_white')
fig.show()''',
        'seaborn': '''import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Your data
df = pd.DataFrame({{
    'Category': {all_categories},
    'Value': {all_values}
}})

# Create styled box plot
plt.figure(figsize=(10, 6))
sns.set_theme(style='whitegrid')
sns.boxplot(data=df, x='Category', y='Value', palette='Set2')
plt.title('{title}', fontsize=16, fontweight='bold')
plt.tight_layout()
plt.show()'''
    },
    'heatmap': {
        'matplotlib': '''import matplotlib.pyplot as plt
import numpy as np

# Your data (2D array)
data = {data_2d}

# Create heatmap
plt.figure(figsize=(10, 8))
plt.imshow(data, cmap='RdYlBu_r', aspect='auto')
plt.colorbar(label='Value')
plt.title('{title}', fontsize=16, fontweight='bold')
plt.xlabel('{x_label}', fontsize=12)
plt.ylabel('{y_label}', fontsize=12)
plt.tight_layout()
plt.show()''',
        'plotly': '''import plotly.express as px
import pandas as pd
import numpy as np

# Your data (2D array)
data = {data_2d}
labels = {labels}

# Create interactive heatmap
fig = px.imshow(data, labels=dict(x="{x_label}", y="{y_label}", color="Value"),
                x=labels, y=labels, color_continuous_scale='RdYlBu_r',
                title='{title}')
fig.update_layout(template='plotly_white')
fig.show()''',
        'seaborn': '''import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Your data (2D array)
data = {data_2d}
labels = {labels}
df = pd.DataFrame(data, index=labels, columns=labels)

# Create styled heatmap
plt.figure(figsize=(10, 8))
sns.set_theme(style='white')
sns.heatmap(df, annot=True, fmt='.1f', cmap='RdYlBu_r', center=0)
plt.title('{title}', fontsize=16, fontweight='bold')
plt.tight_layout()
plt.show()'''
    },
    'pie': {
        'matplotlib': '''import matplotlib.pyplot as plt

# Your data
labels = {x_data}
sizes = {y_data}

# Create pie chart
plt.figure(figsize=(10, 8))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90,
        shadow=True, explode=[0.05]*len(sizes))
plt.title('{title}', fontsize=16, fontweight='bold')
plt.axis('equal')
plt.tight_layout()
plt.show()''',
        'plotly': '''import plotly.express as px
import pandas as pd

# Your data
df = pd.DataFrame({{
    '{x_label}': {x_data},
    '{y_label}': {y_data}
}})

# Create interactive pie chart
fig = px.pie(df, names='{x_label}', values='{y_label}', title='{title}',
             hole=0.3)
fig.update_traces(textposition='inside', textinfo='percent+label')
fig.show()''',
        'seaborn': '''import matplotlib.pyplot as plt

# Your data
labels = {x_data}
sizes = {y_data}

# Create styled pie chart using matplotlib (seaborn doesn't have native pie)
plt.figure(figsize=(10, 8))
colors = sns.color_palette('pastel')[0:len(sizes)]
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
plt.title('{title}', fontsize=16, fontweight='bold')
plt.axis('equal')
plt.show()'''
    },
    'area': {
        'matplotlib': '''import matplotlib.pyplot as plt

# Your data
x = {x_data}
y = {y_data}

# Create area chart
plt.figure(figsize=(10, 6))
plt.fill_between(x, y, alpha=0.3, color='steelblue')
plt.plot(x, y, color='steelblue', linewidth=2)
plt.title('{title}', fontsize=16, fontweight='bold')
plt.xlabel('{x_label}', fontsize=12)
plt.ylabel('{y_label}', fontsize=12)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()''',
        'plotly': '''import plotly.express as px
import pandas as pd

# Your data
df = pd.DataFrame({{
    '{x_label}': {x_data},
    '{y_label}': {y_data}
}})

# Create interactive area chart
fig = px.area(df, x='{x_label}', y='{y_label}', title='{title}')
fig.update_layout(template='plotly_white', hovermode='x unified')
fig.show()''',
        'seaborn': '''import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Your data
df = pd.DataFrame({{
    '{x_label}': {x_data},
    '{y_label}': {y_data}
}})

# Create styled area chart
plt.figure(figsize=(10, 6))
sns.set_theme(style='whitegrid')
sns.lineplot(data=df, x='{x_label}', y='{y_label}', linewidth=2)
plt.fill_between(df['{x_label}'], df['{y_label}'], alpha=0.3)
plt.title('{title}', fontsize=16, fontweight='bold')
plt.tight_layout()
plt.show()'''
    },
}


def chart_list(request):
    templates = ChartTemplate.objects.all()
    return render(request, 'graphs/chart_list.html', {'templates': templates})


def chart_builder(request, chart_type=None):
    if chart_type:
        template = get_object_or_404(ChartTemplate, chart_type=chart_type)
    else:
        template = ChartTemplate.objects.first()
    
    all_templates = ChartTemplate.objects.all()
    
    context = {
        'template': template,
        'all_templates': all_templates,
    }
    return render(request, 'graphs/chart_builder.html', context)


@require_POST
def generate_code(request):
    try:
        data = json.loads(request.body)
        chart_type = data.get('chart_type', 'line')
        code_type = data.get('code_type', 'matplotlib')
        user_data = data.get('data', {})
        title = data.get('title', 'My Chart')
        x_label = data.get('x_label', 'X')
        y_label = data.get('y_label', 'Y')
        
        generator = CHART_CODE_GENERATORS.get(chart_type, {}).get(code_type)
        if not generator:
            return JsonResponse({'error': 'Chart type or code type not found'}, status=400)
        
        x_data = user_data.get('x', [1, 2, 3, 4, 5])
        y_data = user_data.get('y', [10, 24, 36, 40, 55])
        bins = user_data.get('bins', 10)
        data_lists = user_data.get('data_lists', [[1, 2, 3, 4, 5], [2, 3, 5, 7, 11]])
        labels = user_data.get('labels', ['A', 'B', 'C', 'D', 'E'])
        data_2d = user_data.get('data_2d', [[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        all_categories = user_data.get('all_categories', [])
        all_values = user_data.get('all_values', [])
        
        code = generator.format(
            x_data=repr(x_data),
            y_data=repr(y_data),
            x_label=x_label,
            y_label=y_label,
            title=title,
            bins=bins,
            data_lists=repr(data_lists),
            labels=repr(labels),
            data_2d=repr(data_2d),
            all_categories=repr(all_categories),
            all_values=repr(all_values),
        )
        
        return JsonResponse({'code': code, 'language': code_type})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)


@require_POST
def save_chart(request):
    try:
        data = json.loads(request.body)
        chart = SavedChart.objects.create(
            chart_type=data.get('chart_type', 'line'),
            title=data.get('title', 'Untitled Chart'),
            user_data=data.get('data', {}),
            chart_config=data.get('config', {}),
        )
        return JsonResponse({'success': True, 'id': chart.id})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)


def download_code(request):
    chart_type = request.GET.get('chart_type', 'line')
    code_type = request.GET.get('code_type', 'matplotlib')
    
    generator = CHART_CODE_GENERATORS.get(chart_type, {}).get(code_type, '# Code not available')
    
    response = HttpResponse(generator, content_type='text/plain')
    response['Content-Disposition'] = f'attachment; filename="{chart_type}_chart.py"'
    return response


def saved_charts(request):
    charts = SavedChart.objects.all()[:20]
    return render(request, 'graphs/saved_charts.html', {'charts': charts})
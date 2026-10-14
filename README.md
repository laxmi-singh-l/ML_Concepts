# ML Concepts - Learn Machine Learning by Writing Code

An interactive Django platform for learning machine learning through runnable code, live visualizations, and hands-on examples.

## Features

- **ML Libraries Guide** - Compare scikit-learn, TensorFlow, PyTorch, XGBoost, and more with install commands and Hello World examples
- **Training Pipeline Builder** - Step-by-step pipeline generation with code for each stage
- **Interactive Chart Builder** - 8 chart types with live Plotly preview and code in Matplotlib/Plotly/Seaborn
- **Pandas/NumPy Reference** - 100+ functions with examples, expected output, and test code
- **ML Models Catalog** - 30+ models with starter code, full training examples, and hyperparameter guides
- **Test Generator** - Generate validation, cross-validation, and overfitting detection code
- **Metric Library** - Classification, regression, and clustering metrics with code

## Setup

```bash
# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Seed database with ML content
python manage.py seed_ml_data

# Create admin user (optional)
python manage.py createsuperuser

# Run development server
python manage.py runserver
```

## Apps

| App | Purpose |
|-----|---------|
| `core` | Authentication, dashboard, progress tracking |
| `ml_libraries` | Library guide, training pipeline, comparisons |
| `graphs` | Interactive chart builder with code generation |
| `pandas_numpy` | Pandas & NumPy function reference |
| `ml_models` | ML model catalog with starter code |
| `testing` | Test generator, metric library, validation patterns |

## Learning Path

1. **Libraries & Setup** - Install and explore ML libraries
2. **Data Mastery** - Learn Pandas and NumPy functions
3. **Visualization Lab** - Build charts with code
4. **Model Catalog** - Explore ML models
5. **Training Pipeline** - Build end-to-end pipelines
6. **Testing & Evaluation** - Validate your models

## Tech Stack

- Django 4.2+
- Bootstrap 5
- Plotly.js (interactive charts)
- Prism.js (code highlighting)
- HTMX (dynamic interactions)
- Pyodide (in-browser Python execution)
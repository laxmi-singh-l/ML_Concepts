// Main JavaScript for ML Concepts

document.addEventListener('DOMContentLoaded', function() {
    // Initialize tooltips
    var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    tooltipTriggerList.map(function(tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });

    // Initialize popovers
    var popoverTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="popover"]'));
    popoverTriggerList.map(function(popoverTriggerEl) {
        return new bootstrap.Popover(popoverTriggerEl);
    });

    // Smooth scroll for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                e.preventDefault();
                target.scrollIntoView({ behavior: 'smooth', block: 'start' });
            }
        });
    });

    // Auto-hide alerts after 5 seconds
    setTimeout(() => {
        document.querySelectorAll('.alert:not(.alert-permanent)').forEach(alert => {
            const bsAlert = new bootstrap.Alert(alert);
            bsAlert.close();
        });
    }, 5000);

    // Highlight active nav item
    const currentPath = window.location.pathname;
    document.querySelectorAll('.nav-link, .dropdown-item').forEach(link => {
        if (link.getAttribute('href') === currentPath) {
            link.classList.add('active');
        }
    });

    // Copy code functionality
    window.copyCode = function(button, code) {
        navigator.clipboard.writeText(code).then(() => {
            const original = button.innerHTML;
            button.innerHTML = '<i class="bi bi-check me-1"></i>Copied!';
            button.classList.remove('btn-outline-light');
            button.classList.add('btn-success');
            setTimeout(() => {
                button.innerHTML = original;
                button.classList.remove('btn-success');
                button.classList.add('btn-outline-light');
            }, 2000);
        });
    };

    // Run Python code in browser (using Pyodide if available)
    window.runPythonCode = async function(code, outputElement) {
        if (typeof pyodide !== 'undefined') {
            outputElement.textContent = 'Running...';
            try {
                let output = '';
                const capture = (text) => { output += text + '\n'; };
                await pyodide.runPythonAsync(`
import sys
from io import StringIO
old_stdout = sys.stdout
sys.stdout = StringIO()
${code}
print(sys.stdout.getvalue())
`);
                outputElement.textContent = output || 'No output';
            } catch (err) {
                outputElement.textContent = 'Error: ' + err.message;
            }
        } else {
            outputElement.textContent = 'Pyodide not loaded. Run code in your local environment.';
        }
    };
});

// HTMX configuration
document.body.addEventListener('htmx:configRequest', function(evt) {
    evt.detail.headers['X-CSRFToken'] = document.querySelector('[name=csrfmiddlewaretoken]')?.value;
});

// Form validation enhancement
document.querySelectorAll('form.needs-validation').forEach(form => {
    form.addEventListener('submit', event => {
        if (!form.checkValidity()) {
            event.preventDefault();
            event.stopPropagation();
        }
        form.classList.add('was-validated');
    });
});
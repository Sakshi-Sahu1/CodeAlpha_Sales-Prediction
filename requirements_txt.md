# Core Dependencies for Sales Prediction Project
# Install with: pip install -r requirements.txt

# Data Processing and Analysis
pandas>=1.3.0
numpy>=1.20.0

# Machine Learning
scikit-learn>=1.0.0

# Data Visualization
matplotlib>=3.4.0
seaborn>=0.11.0

# Jupyter and Notebook
jupyter>=1.0.0
jupyterlab>=3.0.0
notebook>=6.0.0
ipython>=7.0.0

# Dataset Management
kagglehub>=0.1.0

# ============================================================================
# Optional Dependencies for Development
# ============================================================================

# Testing
pytest>=6.0.0
pytest-cov>=2.12.0

# Code Quality
black>=21.0
flake8>=3.9.0
mypy>=0.910
pylint>=2.8.0
isort>=5.9.0

# Documentation
sphinx>=4.0.0
sphinx-rtd-theme>=0.5.0

# Performance
numba>=0.54.0
bottleneck>=1.3.0

# Additional Utilities
tqdm>=4.60.0
python-dotenv>=0.19.0
pyyaml>=5.4.0

# ============================================================================
# Version Constraints
# ============================================================================
# 
# Minimum versions are specified for compatibility
# Uses compatible release clauses (~=) where applicable
# 
# Core dependencies: Must be installed
# Optional dependencies: Install for development/testing only
# 
# To install optional dependencies:
#   pip install -r requirements.txt
#   pip install pytest pytest-cov black flake8 mypy
#
# ============================================================================
# Troubleshooting
# ============================================================================
#
# If you encounter issues:
#
# 1. Update pip: pip install --upgrade pip
# 2. Clear cache: pip cache purge
# 3. Reinstall: pip install --force-reinstall -r requirements.txt
# 4. Check compatibility: python --version
# 5. Use conda instead: conda env create -f environment.yml
#
# ============================================================================
# Notes
# ============================================================================
#
# - Python 3.7+ required
# - Works on Windows, macOS, Linux
# - Some packages have system dependencies (check documentation)
# - For production: pin exact versions (example: pandas==1.3.0)
# - For development: use ~= for flexible versioning
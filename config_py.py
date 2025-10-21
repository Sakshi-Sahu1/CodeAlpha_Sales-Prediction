"""
Configuration file for Sales Prediction Project
Contains all configurable parameters for the analysis
"""

import os
from pathlib import Path

# ============================================================================
# PROJECT PATHS
# ============================================================================

# Base project directory
BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
OUTPUT_DIR = BASE_DIR / "outputs"

# Create directories if they don't exist
DATA_DIR.mkdir(exist_ok=True)
OUTPUT_DIR.mkdir(exist_ok=True)

# File paths
DATA_FILE = DATA_DIR / "Advertising.csv"
EDA_PLOT = OUTPUT_DIR / "eda_analysis.png"
MODEL_COMPARISON_PLOT = OUTPUT_DIR / "model_comparison.png"
FEATURE_IMPORTANCE_PLOT = OUTPUT_DIR / "feature_importance.png"

# ============================================================================
# DATASET CONFIGURATION
# ============================================================================

# Kaggle dataset info
KAGGLE_DATASET = "bumba5341/advertisingcsv"
KAGGLE_DATASET_FILE = "Advertising.csv"

# Dataset parameters
TEST_SIZE = 0.2  # 20% for testing, 80% for training
RANDOM_STATE = 42  # For reproducibility
RANDOM_SEED = 42

# Data columns
FEATURE_COLUMNS = ['TV', 'Radio', 'Newspaper']
TARGET_COLUMN = 'Sales'

# ============================================================================
# FEATURE ENGINEERING
# ============================================================================

# Engineered features to create
CREATE_TOTAL_SPEND = True
CREATE_TV_RADIO_INTERACTION = True
CREATE_CHANNEL_RATIOS = True
CREATE_LOG_FEATURES = False

# Feature engineering parameters
EPSILON = 1e-6  # Small value to avoid division by zero

# ============================================================================
# MODEL CONFIGURATION
# ============================================================================

# Models to train
MODELS_TO_TRAIN = {
    'Linear Regression': {
        'enabled': True,
        'params': {}
    },
    'Ridge Regression': {
        'enabled': True,
        'params': {'alpha': 1.0}
    },
    'Lasso Regression': {
        'enabled': True,
        'params': {'alpha': 0.1}
    },
    'Random Forest': {
        'enabled': True,
        'params': {
            'n_estimators': 100,
            'random_state': RANDOM_STATE,
            'n_jobs': -1
        }
    },
    'Gradient Boosting': {
        'enabled': True,
        'params': {
            'n_estimators': 100,
            'random_state': RANDOM_STATE,
            'learning_rate': 0.1
        }
    }
}

# Scaling parameters
USE_SCALER = True
SCALER_TYPE = 'StandardScaler'  # Options: 'StandardScaler', 'MinMaxScaler'

# ============================================================================
# VISUALIZATION CONFIGURATION
# ============================================================================

# Figure parameters
FIGURE_DPI = 300
FIGURE_FORMAT = 'png'
FIGURE_QUALITY = 'high'

# Plot styling
PLOT_STYLE = "whitegrid"
FIGURE_FIGSIZE_MAIN = (15, 12)
FIGURE_FIGSIZE_COMPARISON = (15, 6)
FIGURE_FIGSIZE_FEATURE = (10, 6)

# Color palette
COLOR_PALETTE = {
    'primary': '#FF6B6B',
    'secondary': '#4ECDC4',
    'tertiary': '#45B7D1',
    'accent': '#FFA07A'
}

# Plot parameters
ALPHA_DEFAULT = 0.6
EDGECOLOR_DEFAULT = 'black'

# ============================================================================
# ANALYSIS PARAMETERS
# ============================================================================

# Correlation threshold for significant features
CORRELATION_THRESHOLD = 0.5

# Outlier detection method
OUTLIER_METHOD = 'iqr'  # Options: 'iqr', 'zscore', 'isolation_forest'
OUTLIER_MULTIPLIER = 1.5  # For IQR method

# Cross-validation parameters
CROSS_VALIDATION_SPLITS = 5
CROSS_VALIDATION_SHUFFLE = True

# ============================================================================
# REPORTING & LOGGING
# ============================================================================

# Logging configuration
LOG_LEVEL = 'INFO'  # Options: 'DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'
LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
LOG_FILE = BASE_DIR / "logs" / "sales_prediction.log"

# Create logs directory
(BASE_DIR / "logs").mkdir(exist_ok=True)

# ============================================================================
# PERFORMANCE METRICS
# ============================================================================

# Metrics to calculate
METRICS = ['R2', 'RMSE', 'MAE', 'MSE']

# Display precision
DECIMAL_PLACES = 4
PERCENTAGE_PLACES = 2

# ============================================================================
# MODEL EVALUATION
# ============================================================================

# Best model selection criterion
BEST_MODEL_CRITERION = 'R2'  # Options: 'R2', 'RMSE', 'MAE'
BEST_MODEL_DIRECTION = 'max'  # Options: 'max', 'min'

# Performance threshold for good model
MIN_R2_SCORE = 0.80
MAX_RMSE = 2.0

# ============================================================================
# HYPERPARAMETER TUNING
# ============================================================================

# Grid search parameters (if needed)
USE_GRID_SEARCH = False
GRID_SEARCH_CV_FOLDS = 5

# Ridge alphas to test
RIDGE_ALPHAS = [0.001, 0.01, 0.1, 1.0, 10.0, 100.0]

# Lasso alphas to test
LASSO_ALPHAS = [0.001, 0.01, 0.05, 0.1, 0.5, 1.0]

# Random Forest parameters
RF_N_ESTIMATORS = [50, 100, 200]
RF_MAX_DEPTH = [10, 20, None]

# ============================================================================
# OUTPUT & REPORTING
# ============================================================================

# Save outputs
SAVE_PLOTS = True
SAVE_PREDICTIONS = True
SAVE_MODEL = False

# Report generation
GENERATE_HTML_REPORT = False
GENERATE_PDF_REPORT = False

# Prediction output format
PREDICTION_DECIMALS = 2

# ============================================================================
# BUSINESS PARAMETERS
# ============================================================================

# Channel names for reporting
CHANNEL_NAMES = {
    'TV': 'Television',
    'Radio': 'Radio',
    'Newspaper': 'Newspaper'
}

# Budget constraints (optional)
MIN_BUDGET = 0
MAX_BUDGET = 500

# Currency settings
CURRENCY_SYMBOL = '
CURRENCY_UNIT = 'k'  # thousands

# ============================================================================
# ADVANCED SETTINGS
# ============================================================================

# Feature scaling parameters
FEATURE_SCALING_RANGE = (0, 1)  # For MinMaxScaler

# Handling missing values
MISSING_VALUE_STRATEGY = 'drop'  # Options: 'drop', 'mean', 'median'

# Handling duplicates
REMOVE_DUPLICATES = True

# Date/time settings (if temporal data added)
DATE_FORMAT = '%Y-%m-%d'
TIMEZONE = 'UTC'

# Random seed for reproducibility across runs
NUMPY_RANDOM_SEED = 42
SKLEARN_RANDOM_STATE = 42
PANDAS_RANDOM_STATE = 42

# ============================================================================
# VALIDATION SETTINGS
# ============================================================================

# Data validation
VALIDATE_DATA_TYPES = True
VALIDATE_DATA_RANGES = True
VALIDATE_NO_NEGATIVE_SALES = True

# Model validation
VALIDATE_TRAIN_TEST_SPLIT = True
CHECK_DATA_LEAKAGE = True

# ============================================================================
# DEBUG & DEVELOPMENT
# ============================================================================

# Debug mode
DEBUG = False

# Verbose output
VERBOSE = True

# Show warnings
SHOW_WARNINGS = True

# Test mode (uses smaller dataset)
TEST_MODE = False
TEST_SAMPLE_SIZE = 50  # Number of samples in test mode

# ============================================================================
# DEFAULT VALUES
# ============================================================================

DEFAULT_MODEL = 'Lasso Regression'
DEFAULT_TEST_SIZE = 0.2
DEFAULT_RANDOM_STATE = 42

# ============================================================================
# HELPER FUNCTIONS
# ============================================================================

def get_model_params(model_name):
    """Get parameters for a specific model"""
    return MODELS_TO_TRAIN.get(model_name, {}).get('params', {})


def get_output_path(filename):
    """Get full output path for a file"""
    return OUTPUT_DIR / filename


def get_data_path(filename):
    """Get full data path for a file"""
    return DATA_DIR / filename


def validate_config():
    """Validate configuration parameters"""
    errors = []
    
    if TEST_SIZE <= 0 or TEST_SIZE >= 1:
        errors.append("TEST_SIZE must be between 0 and 1")
    
    if RANDOM_STATE is not None and RANDOM_STATE < 0:
        errors.append("RANDOM_STATE must be non-negative or None")
    
    if MIN_R2_SCORE < 0 or MIN_R2_SCORE > 1:
        errors.append("MIN_R2_SCORE must be between 0 and 1")
    
    if DECIMAL_PLACES < 0:
        errors.append("DECIMAL_PLACES must be non-negative")
    
    return errors


# ============================================================================
# ENVIRONMENT-SPECIFIC SETTINGS
# ============================================================================

# Development environment
DEVELOPMENT = {
    'DEBUG': True,
    'VERBOSE': True,
    'SAVE_PLOTS': True,
    'FIGURE_DPI': 100,  # Lower DPI for faster rendering
}

# Production environment
PRODUCTION = {
    'DEBUG': False,
    'VERBOSE': False,
    'SAVE_PLOTS': True,
    'FIGURE_DPI': 300,  # Higher DPI for publication
}

# Get environment (set via environment variable)
ENVIRONMENT = os.getenv('SALES_PREDICTION_ENV', 'development')
ENV_CONFIG = DEVELOPMENT if ENVIRONMENT == 'development' else PRODUCTION

# Apply environment-specific settings
for key, value in ENV_CONFIG.items():
    if key in globals():
        globals()[key] = value

print(f"Configuration loaded for {ENVIRONMENT} environment")
if DEBUG:
    print(f"Data directory: {DATA_DIR}")
    print(f"Output directory: {OUTPUT_DIR}")
    config_errors = validate_config()
    if config_errors:
        print("Configuration errors found:")
        for error in config_errors:
            print(f"  - {error}")
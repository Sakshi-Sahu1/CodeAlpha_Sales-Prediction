# Sales Prediction Project - Required Files

## Project Structure
```
sales_prediction_project/
├── Sales_Prediction.ipynb
├── data/
│   └── Advertising.csv
├── outputs/
│   ├── eda_analysis.png
│   ├── model_comparison.png
│   └── feature_importance.png
├── requirements.txt
└── README.md
```

## 1. Main Jupyter Notebook
**File**: `Sales_Prediction.ipynb`
- Complete analysis pipeline
- Data exploration and visualization
- Model training and evaluation
- Business insights generation

## 2. Data File
**File**: `data/Advertising.csv`
- Source: Kaggle (bumba5341/advertisingcsv)
- Columns: Unnamed: 0, TV, Radio, Newspaper, Sales
- Rows: 200 samples
- Contains advertising spend across three channels and resulting sales

## 3. Requirements File
**File**: `requirements.txt`
```
pandas>=1.3.0
numpy>=1.20.0
scikit-learn>=1.0.0
matplotlib>=3.4.0
seaborn>=0.11.0
kagglehub>=0.1.0
```

## 4. README Documentation
**File**: `README.md`

```markdown
# Sales Prediction System

## Overview
This project builds a machine learning system to predict product sales based on advertising spend across TV, Radio, and Newspaper channels.

## Installation

### Prerequisites
- Python 3.7+
- pip or conda

### Setup
1. Clone the repository
2. Create virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Download dataset (automatically handled in notebook)
2. Run Jupyter notebook:
   ```bash
   jupyter notebook Sales_Prediction.ipynb
   ```

## Project Structure
- Data exploration with correlation analysis
- Feature engineering (Total_Spend, TV_Radio_Interaction, ratios)
- Train-test split (80-20)
- Feature scaling with StandardScaler
- Model comparison across 5 algorithms

## Models Evaluated
1. **Linear Regression**: R² = 0.9881
2. **Ridge Regression**: R² = 0.9883
3. **Lasso Regression** ⭐ Best: R² = 0.9925, RMSE = 0.4851
4. **Random Forest**: R² = 0.9879
5. **Gradient Boosting**: R² = 0.9860

## Key Insights
- TV advertising impact: 0.782 correlation with sales
- Radio advertising impact: 0.576 correlation with sales
- Newspaper advertising impact: 0.228 correlation with sales

## Recommendations
- Allocate more budget to TV advertising
- Optimize TV and Radio synergy
- Reduce or eliminate newspaper spending
- Use predictions for quarterly budget planning
```

## Key Python Libraries Used
- **pandas**: Data manipulation and analysis
- **numpy**: Numerical computations
- **scikit-learn**: Machine learning models and metrics
- **matplotlib**: Data visualization
- **seaborn**: Statistical data visualization
- **kagglehub**: Dataset downloading from Kaggle

## Generated Output Files
- `eda_analysis.png`: Exploratory data analysis visualizations
- `model_comparison.png`: Model performance comparisons
- `feature_importance.png`: Feature importance analysis

## Models Trained
1. Linear Regression
2. Ridge Regression
3. Lasso Regression (Best model - 99.25% R² score)
4. Random Forest Regressor
5. Gradient Boosting Regressor

## Key Findings
- TV advertising has the strongest correlation with sales (0.782)
- Best model: Lasso Regression with 99.25% accuracy
- Average prediction error: $0.37k
- Dataset contains 200 advertising campaigns with no missing values
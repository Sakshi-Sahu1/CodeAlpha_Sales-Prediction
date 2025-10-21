# CodeAlpha_Sales-Prediction

# Sales Prediction System 📊

A comprehensive machine learning project that predicts product sales based on advertising spending across multiple channels (TV, Radio, Newspaper).

## Overview

This project analyzes the relationship between advertising investments and sales revenue, then builds predictive models to forecast future sales based on advertising budgets. It includes exploratory data analysis, feature engineering, model comparison, and actionable business insights.

## Features

✓ **Data Exploration & Analysis**
- Correlation analysis across advertising channels
- Statistical summaries and data quality checks
- Distribution analysis and outlier detection

✓ **Feature Engineering**
- Total advertising spend calculation
- TV-Radio interaction effects
- Channel ratio features

✓ **Multiple ML Models**
- Linear Regression
- Ridge Regression
- Lasso Regression ⭐ (Best Model)
- Random Forest
- Gradient Boosting

✓ **Comprehensive Visualizations**
- Correlation heatmaps
- Model performance comparisons
- Feature importance analysis
- Actual vs. Predicted scatter plots

✓ **Business Insights**
- Channel effectiveness ranking
- ROI recommendations
- Budget optimization strategies

## Dataset

**Source:** Kaggle - Advertising Dataset  
**Samples:** 200 advertising campaigns  
**Features:** TV, Radio, Newspaper spend (in thousands)  
**Target:** Sales (in thousands)  
**Size:** ~5KB

**Key Statistics:**
- TV spend: $0.7K - $296.4K (avg: $147K)
- Radio spend: $0K - $49.6K (avg: $23K)
- Newspaper spend: $0.3K - $114K (avg: $30K)
- Sales: $1.6K - $27K (avg: $14K)

## Installation

### Prerequisites
- Python 3.7 or higher
- pip or conda package manager

### Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/sales-prediction.git
   cd sales-prediction
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Running the Jupyter Notebook

```bash
jupyter notebook Sales_Prediction.ipynb
```

The notebook will:
1. Download the Advertising dataset from Kaggle (requires kagglehub)
2. Perform exploratory data analysis
3. Engineer new features
4. Train 5 different models
5. Compare performance and select the best model
6. Generate visualizations
7. Provide business recommendations
8. Make sample predictions

### Quick Start Code

```python
import pandas as pd
from sklearn.linear_model import Lasso
from sklearn.preprocessing import StandardScaler

# Load data
df = pd.read_csv('data/Advertising.csv')

# Prepare features and target
X = df[['TV', 'Radio', 'Newspaper']]
y = df['Sales']

# Scale features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Train best model
model = Lasso(alpha=0.1)
model.fit(X_scaled, y)

# Make prediction
new_spend = [[230, 38, 69]]
new_spend_scaled = scaler.transform(new_spend)
predicted_sales = model.predict(new_spend_scaled)
print(f"Predicted sales: ${predicted_sales[0]:.2f}k")
```

## Model Performance

| Model | R² Score | RMSE | MAE |
|-------|----------|------|-----|
| Linear Regression | 0.9881 | 0.6128 | 0.4461 |
| Ridge Regression | 0.9883 | 0.6085 | 0.4480 |
| **Lasso Regression** ⭐ | **0.9925** | **0.4851** | **0.3662** |
| Random Forest | 0.9879 | 0.6179 | 0.4799 |
| Gradient Boosting | 0.9860 | 0.6641 | 0.4815 |

**Best Model:** Lasso Regression
- **Accuracy:** 99.25%
- **Average Error:** $366 (per $1000 sales)

## Key Findings

### Advertising Channel Effectiveness

1. **TV Advertising** 📺 (Strongest Impact)
   - Correlation with sales: **0.782**
   - Most influential channel
   - Recommendation: Prioritize budget allocation

2. **Radio Advertising** 📻 (Moderate Impact)
   - Correlation with sales: **0.576**
   - Secondary channel
   - Works well in combination with TV

3. **Newspaper Advertising** 📰 (Weakest Impact)
   - Correlation with sales: **0.228**
   - Minimal effect on sales
   - Recommendation: Consider reducing or eliminating

### Business Recommendations

1. **Optimize Budget Allocation**
   - Allocate 60-70% to TV advertising
   - Allocate 20-30% to Radio advertising
   - Allocate 5-10% to Newspaper advertising

2. **Leverage Synergies**
   - TV + Radio combination shows strong results
   - Coordinate messaging across channels

3. **Use Predictive Model**
   - Plan quarterly marketing budgets
   - Test different spending scenarios
   - Monitor actual vs. predicted performance

4. **ROI Monitoring**
   - Track performance metrics monthly
   - Adjust strategy based on results
   - A/B test different spending mixes

## Project Structure

```
sales-prediction/
├── Sales_Prediction.ipynb      # Main analysis notebook
├── README.md                    # This file
├── requirements.txt             # Python dependencies
├── environment.yml              # Conda environment file
├── setup.py                     # Package setup
├── config.py                    # Configuration settings
├── data/
│   └── Advertising.csv         # Dataset
└── outputs/
    ├── eda_analysis.png        # EDA visualizations
    ├── model_comparison.png    # Model performance
    └── feature_importance.png  # Feature rankings
```

## Configuration

Edit `config.py` to customize:
- Train/test split ratio
- Random seed for reproducibility
- Model hyperparameters
- Output directories
- Visualization settings

## Output Files

The notebook generates three visualization PNG files:

1. **eda_analysis.png** - Exploratory Data Analysis
   - Correlation heatmap
   - Sales distribution
   - Average spend by platform
   - TV vs. Sales scatter plot

2. **model_comparison.png** - Model Performance
   - R² scores comparison
   - Actual vs. Predicted plots

3. **feature_importance.png** - Feature Importance
   - Feature ranking visualization

## Technologies Used

- **Python 3.9+**
- **Pandas** - Data manipulation
- **NumPy** - Numerical computing
- **Scikit-learn** - Machine learning models
- **Matplotlib** - Data visualization
- **Seaborn** - Statistical visualization
- **Kagglehub** - Dataset downloading

## Requirements

See `requirements.txt` for complete list:
- pandas >= 1.3.0
- numpy >= 1.20.0
- scikit-learn >= 1.0.0
- matplotlib >= 3.4.0
- seaborn >= 0.11.0
- kagglehub >= 0.1.0

## Example Prediction

**Input:**
- TV: $230.1k
- Radio: $37.8k
- Newspaper: $69.2k

**Output:**
- Predicted Sales: **$21.46k**
- Confidence: 99.25%

## Troubleshooting

### Kaggle Authentication Error
If you see "403 - Forbidden" when downloading data:
1. Install Kaggle API: `pip install kaggle`
2. Create API key on kaggle.com (Settings → API → Create)
3. Place `kaggle.json` in `~/.kaggle/`

### Memory Issues
For large datasets, reduce batch size in `config.py` or use `environment.yml` with optimized packages.

### Import Errors
Ensure all dependencies are installed:
```bash
pip install -r requirements.txt --upgrade
```

## Contributing

Contributions welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Submit a pull request with clear descriptions

## License

MIT License - see LICENSE file for details

## Author

Sakshi sahu 

## Contact

- Email: sakshi100sahu@gmail.com
- LinkedIn: https://www.linkedin.com/in/sakshi-sahu-718674331/
- GitHub: github.com/Sakshi-Sahu1
## Acknowledgments

- Dataset from Kaggle (bumba5341/advertisingcsv)
- Scikit-learn documentation and community
- Data science best practices from industry standards

## Citation

If you use this project in your research or work, please cite:

```bibtex
@project{salesprediction2024,
  title={Sales Prediction System},
  author={Sakshi Sahu},
  year={2025},
  url={https://github.com/Sakshi-Sahu1/sales-prediction}
}
```

---

**Last Updated:** 2025
**Version:** 1.0.0  
**Status:** Active

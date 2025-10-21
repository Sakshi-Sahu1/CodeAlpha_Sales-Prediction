# Contributing to Sales Prediction Project

Thank you for your interest in contributing! This document provides guidelines and instructions for contributing to the Sales Prediction project.

## Code of Conduct

- Be respectful and inclusive
- Provide constructive feedback
- Ask questions if unclear
- Help others learn and grow
- Report inappropriate behavior

## How to Contribute

### 1. Report Bugs

If you find a bug, please create an issue with:
- Clear description of the bug
- Steps to reproduce
- Expected behavior
- Actual behavior
- Your environment (OS, Python version, etc.)
- Relevant logs or error messages

**Issue Template:**
```
## Bug Report

### Description
[Brief description of the bug]

### Steps to Reproduce
1. [First step]
2. [Second step]
3. [etc.]

### Expected Behavior
[What should happen]

### Actual Behavior
[What actually happens]

### Environment
- OS: [e.g., Windows 10, macOS, Linux]
- Python: [e.g., 3.9.0]
- Package versions: [list relevant packages]

### Logs/Screenshots
[Attach error messages, screenshots, etc.]
```

### 2. Suggest Features

Have an idea? Create an issue with:
- Clear feature description
- Use case and motivation
- Proposed implementation (optional)
- Alternative approaches considered

**Feature Request Template:**
```
## Feature Request

### Description
[Clear description of the feature]

### Motivation
Why do you want this feature? What problem does it solve?

### Proposed Implementation
[Optional: How you might implement this]

### Alternatives
[Any alternative approaches you've considered]
```

### 3. Submit Code Changes

#### Prerequisites
- Fork the repository
- Clone your fork: `git clone https://github.com/yourusername/sales-prediction.git`
- Create a branch: `git checkout -b feature/your-feature-name`
- Install development dependencies: `pip install -r requirements.txt`

#### Making Changes

1. **Follow PEP 8 Style Guide**
   - Use 4 spaces for indentation
   - Maximum line length: 79 characters
   - Use descriptive variable names
   - Add docstrings to functions

2. **Write Tests**
   - Add unit tests for new features
   - Ensure existing tests pass
   - Aim for >80% code coverage
   - Run: `pytest tests/`

3. **Document Changes**
   - Update README.md if needed
   - Add docstrings to new functions
   - Update CHANGELOG.md
   - Add inline comments for complex logic

4. **Commit Messages**
   ```
   [Type]: Brief description (50 chars max)
   
   Detailed explanation of changes (wrap at 72 chars)
   
   - Point 1
   - Point 2
   
   Fixes #[issue number]
   ```
   
   Types: feat, fix, docs, style, refactor, perf, test, chore

   **Example:**
   ```
   feat: Add feature importance visualization
   
   Implemented feature importance plot for tree-based models
   using built-in feature_importances_ attribute.
   
   - Added horizontal bar chart visualization
   - Integrated with model comparison pipeline
   - Added documentation for interpretation
   
   Fixes #45
   ```

#### Submission Process

1. Push to your fork: `git push origin feature/your-feature-name`
2. Create a Pull Request (PR)
3. Fill out the PR template completely
4. Link related issues
5. Request review from maintainers

**PR Template:**
```
## Description
Brief description of what this PR does

## Related Issues
Fixes #[issue number]

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update
- [ ] Code refactoring
- [ ] Performance improvement

## Changes Made
- [Change 1]
- [Change 2]
- [Change 3]

## Testing
- [ ] Added tests
- [ ] All tests pass
- [ ] Manual testing completed

## Screenshots (if applicable)
[Add screenshots here]

## Checklist
- [ ] Code follows style guidelines
- [ ] Documentation updated
- [ ] Tests added/updated
- [ ] No new warnings generated
- [ ] Changes don't break existing functionality
```

## Development Workflow

### Setup Development Environment

```bash
# Clone repository
git clone https://github.com/yourusername/sales-prediction.git
cd sales-prediction

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
pip install pytest pytest-cov black flake8 mypy

# Verify setup
pytest tests/
```

### Code Quality Standards

**1. Style Check (Black)**
```bash
black . --line-length=79
```

**2. Linting (Flake8)**
```bash
flake8 . --max-line-length=79 --exclude=venv,__pycache__
```

**3. Type Checking (mypy)**
```bash
mypy . --ignore-missing-imports
```

**4. Testing (pytest)**
```bash
pytest tests/ -v --cov=. --cov-report=html
```

### Before Submitting PR

```bash
# 1. Run all checks
black .
flake8 .
mypy .
pytest tests/ -v

# 2. Update documentation
# 3. Add changelog entry
# 4. Commit and push
git add .
git commit -m "your message"
git push origin your-branch
```

## Pull Request Review Process

### What Reviewers Look For:
- Code quality and style compliance
- Test coverage
- Documentation completeness
- Performance impact
- Security considerations
- Compatibility with existing code

### Review Timeline:
- Initial review: 2-3 days
- Response to feedback: 1-2 days
- Final approval: 1-2 days
- Merge: Upon approval

### How to Respond to Feedback:
1. Read feedback carefully
2. Discuss if you disagree (respectfully)
3. Make requested changes
4. Request re-review
5. Don't force-push after review started

## Areas for Contribution

### High Priority
- Bug fixes
- Performance improvements
- Documentation enhancements
- Unit test coverage
- Code style improvements

### Medium Priority
- New visualization types
- Additional model algorithms
- Enhanced error handling
- Example notebooks
- Tutorial content

### Nice to Have
- Alternative interfaces
- Additional datasets
- Comparative analyses
- Blog posts/articles
- Video tutorials

## Development Guidelines

### Python Style
```python
# Good
def calculate_rmse(predictions, actuals):
    """Calculate root mean squared error.
    
    Args:
        predictions: Model predictions
        actuals: Actual values
        
    Returns:
        float: RMSE value
    """
    squared_errors = (predictions - actuals) ** 2
    mse = squared_errors.mean()
    rmse = np.sqrt(mse)
    return rmse

# Avoid
def calc_err(p, a):
    return np.sqrt(((p - a) ** 2).mean())
```

### Documentation
- Add docstrings to all functions
- Use Google-style docstrings
- Include type hints
- Add examples

### Testing
```python
import pytest

def test_rmse_calculation():
    """Test RMSE calculation."""
    predictions = np.array([1, 2, 3])
    actuals = np.array([1, 2, 3])
    assert calculate_rmse(predictions, actuals) == 0
```

## Release Process

1. Increase version number
2. Update CHANGELOG.md
3. Create release tag
4. Create release notes
5. Deploy to PyPI

## Community

- **GitHub Issues**: Ask questions, report bugs
- **Discussions**: General discussions and ideas
- **Email**: your.email@example.com
- **LinkedIn**: Your professional network

## Acknowledgments

Contributors will be recognized in:
- CONTRIBUTORS.md file
- Release notes
- Project README

## Questions?

- Check existing issues/discussions
- Read documentation
- Ask in a new discussion
- Email maintainers

---

**Thank you for contributing to making this project better!**
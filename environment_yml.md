name: sales-prediction
channels:
  - conda-forge
  - defaults
dependencies:
  - python=3.9
  - pip
  - numpy=1.23.5
  - pandas=1.5.3
  - scikit-learn=1.2.1
  - matplotlib=3.6.3
  - seaborn=0.12.2
  - jupyter=1.0.0
  - jupyterlab=3.5.3
  - ipython=8.9.0
  - pip:
    - kagglehub>=0.1.0
    - notebook>=6.5.0
variables:
  PYTHONIOENCODING: utf-8
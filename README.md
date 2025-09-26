
# DS/ML Pro Starter (VS Code)

A batteries-included template that mirrors top-tier company workflows:
- Jupyter notebooks for research
- Modular Python package in `src/` for production code
- Pre-commit with Black, Ruff, and isort
- Testing via pytest
- Optional Streamlit app for interactive demo
- Environment via Conda or Poetry

## Quickstart (Windows PowerShell)

```powershell
# 1) Create env (Conda)
conda create -n ds310 python=3.10 -y
conda activate ds310

# 2) Install deps
python -m pip install --upgrade pip
pip install -r requirements.txt

# 3) Enable pre-commit
pre-commit install

# 4) Make Jupyter see this env
python -m ipykernel install --user --name ds310 --display-name "Python (ds310)"

# 5) Open VS Code here
code .
```

## Quickstart (Poetry alternative)
```powershell
python -m pip install --upgrade pip
pip install poetry
poetry env use 3.10
poetry install
```

## Run examples
```powershell
# Notebook: open notebooks/00_quick_demo.ipynb
# Tests:
pytest -q

# Streamlit demo:
streamlit run src/app/streamlit_app.py
```

## Project structure
```
ds_vscode_starter/
├─ .vscode/               # VS Code project settings
├─ data/                  # (gitignored) datasets
├─ notebooks/             # Jupyter notebooks
├─ src/app/               # Python package (your library code)
├─ tests/                 # Unit tests
├─ scripts/               # CLI scripts / utilities
├─ .pre-commit-config.yaml
├─ pyproject.toml         # (Poetry + tooling config)
├─ requirements.txt       # (pip users)
├─ environment.yml        # (Conda users)
└─ README.md
```

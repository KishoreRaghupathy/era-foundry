# ERA-Foundry (Day 01)
Enterprise-style platform for Financed Emissions & Risk Analytics with DE + MLOps foundations.

## What’s in Day 01
- Repo scaffold
- Base Dockerfiles
- Minimal Python libs (ruff, pytest, pandas, pyarrow, great_expectations)
- SQL DDL for core tables
- Toy CSV data (5–10 rows) to run quick validations
- Jenkins CI skeleton (lint + unit tests)

## Local quickstart
```bash
# 1) Clone or unzip this project
cd era-foundry

# 2) (Optional) Create and activate a venv
python -m venv .venv && source .venv/bin/activate  # on Windows: .venv\Scripts\activate

# 3) Install Python deps
pip install -r requirements.txt

# 4) Run lint & tests
ruff .
pytest -q

# 5) Build Docker images (base then runtime)
docker build -f docker/base.Dockerfile -t era-foundry-base:0.1 .
docker build -f docker/runtime.Dockerfile -t era-foundry:0.1 .
```

## Pushing to GitHub (example)
1. Create an empty repo on GitHub (e.g., `era-foundry`).
2. Run:
```bash
git init
git add .
git commit -m "Day 01: scaffold, Docker, SQL DDL, toy data, CI skeleton"
git branch -M main
git remote add origin https://github.com/<YOUR-USER>/era-foundry.git
git push -u origin main
```
(Replace `<YOUR-USER>` with your GitHub username.)

## Structure
```
era-foundry/
  dags/
  pipelines/
  models/
  libs/pcaf_attribution/
  sql/ddl/
  sql/gold_views/
  notebooks/
  docker/
  ci/
  docs/
  data/raw/
  tests/
```

## Next (Day 02)
- Add first Airflow DAG + Vertex AI component for PCAF compute.
- Great Expectations DQ suites and basic lineage hooks.
- Gold view for corporate loans financed emissions.

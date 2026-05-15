# newtest-1

Python service created from Red Hat Developer Hub

## Layout

```text
.
├── Dockerfile
├── .dockerignore
├── catalog-info.yaml
├── pyproject.toml
├── src/newtest_1/
│   ├── __init__.py
│   ├── __main__.py
│   └── main.py
├── tests/
│   └── test_package.py
└── .github/workflows/
    ├── ci.yml              # pytest matrix (3.11 / 3.12)
    └── container-build.yml # image → ghcr.io/<owner>/<repo>
```

## Local

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -e ".[dev]"
pytest
python -m newtest_1
run   # console script from pyproject [project.scripts]
```

## CI / CD

- **`ci.yml`** — runs on push and PR to `main` (tests + `python -m`).
- **`container-build.yml`** — on push to `main` (and manual dispatch), builds the **Dockerfile** and pushes to **GitHub Container Registry**:
  - `ghcr.io/<owner>/<repo>:latest`
  - `ghcr.io/<owner>/<repo>:sha-<full-git-sha>`
- Uses the default **`GITHUB_TOKEN`** (`packages: write`). After the first push open **GitHub → Packages** and set the package visibility if you want anonymous pulls.

### Local image

```bash
docker build -t newtest-1:local .
docker run --rm newtest-1:local
```

### OpenShift / Quay later

Point `container-build.yml` at another registry (login + tags) or add a second job that mirrors **ghcr.io** → **Quay** with repo secrets.

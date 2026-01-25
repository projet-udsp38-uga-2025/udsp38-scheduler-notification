# 🚀 FastAPI + uv — Guide de démarrage

Ce projet est une API backend développée avec **FastAPI** et gérée avec **uv**, le gestionnaire de packages Python ultra-rapide (remplaçant de `pip`, `pip-tools`, `virtualenv`, etc.).

```
project/
│
├── .venv/
├── app/
│   └── ...
|
├── main.py
├── pyproject.toml
├── uv.lock
└── README.md
```

---


## ⚡ Installation de `uv`
documentation officielle https://docs.astral.sh/uv/getting-started/installation/

### Linux / macOS
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Windows
```bash
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

## Verifier l'installation
```bash
uv --version
```

## Installer les dépendances
documentation officielle: https://docs.astral.sh/uv/concepts/projects/sync/
```bash
uv sync --frozen
```
`--frozen` empêche la mise à jour du lockfile pendant le build

## Variables d'environnement
Créer le fichier `.env` à la racine du projet. Copier dans ce fichier le contenu du fichier `.env.example`, ce sont les variables nécéssaires au bon fonctionnement du projet

## Démarrer le projet
```bash
uv run fastapi dev main.py
```

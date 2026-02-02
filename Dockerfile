FROM ghcr.io/astral-sh/uv:python3.13-bookworm-slim

WORKDIR /app

ARG DATABASE_URL
ARG NEXTJS_BASE_URL

ENV DATABASE_URL=$DATABASE_URL
ENV NEXTJS_BASE_URL=$NEXTJS_BASE_URL

# Empêcher Python de générer des fichiers .pyc et forcer l'affichage des logs
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Activer la compilation bytecode python
ENV UV_COMPILE_BYTECODE=1

# Exclure les dépendances de développement
ENV UV_NO_DEV=1

# Installation des dépendances système si nécessaire (ex: pour psycopg2)
RUN apt-get update && apt-get install -y --no-install-recommends libpq5 && rm -rf /var/lib/apt/lists/*

COPY pyproject.toml uv.lock ./

# Installer les dépendances de production en utilisant le cache de uv
# --frozen empêche la mise à jour du lockfile pendant le build
# --no-install-project installe uniquement les bibliothèques externes excluant le dossier actuel du projet considéré comme package python
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen --no-dev --no-install-project

# Copier le reste du code source
COPY . .

# Placer le dossier .venv/bin en priorité dans le PATH
ENV PATH="/app/.venv/bin:$PATH"

EXPOSE 8000

# Commande de lancement (à adapter selon votre point d'entrée)
CMD ["fastapi", "run", "main.py", "--port", "8000", "--proxy-headers"]

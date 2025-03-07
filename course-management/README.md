# Student Course Management System

This is a boilerplate for a Student Course Management System, providing a basic setup for a Django project with pre-commit hooks. This application enables administrators to manage students and courses through enrollments.

## Tech Stack

- Python (v3.13)
- Django (v5.1.6)
- SQLite

## Prerequisites

Install the following tools on your machine:

- [uv](https://docs.astral.sh/uv): Python package manager
- [pre-commit](https://pre-commit.com/): Framework for managing and maintaining multi-language pre-commit hooks

## Setup and Run the Project

1. Navigate to the `course-management` directory.
2. Set up the environment: Create a `.env` file based on `.env.example` with your own settings.
3. Create and activate the virtual environment:
  ```sh
  uv venv
  source .venv/bin/activate
  ```
4. Install packages:
  - Install all packages:
    ```sh
    uv sync
    ```
  - Install packages excluding dev packages:
    ```sh
    uv sync --no-group dev
    ```
5. Run the development server:
  ```sh
  uv run ./src/manage.py runserver
  ```
6. Run tests with coverage:
  ```sh
  uv run coverage run ./src/manage.py test <folder-app>.tests --keepdb
  uv run coverage report
  uv run coverage html
  ```


## Folder Structure

```
course-management/
├── .venv/
├── src/
│   ├── manage.py
│   ├── config/
│   │   ├── __init__.py
│   │   ├── settings/
│   │   |   ├── __init__.py
│   │   |   ├── base.py
│   │   |   ├── local.py
│   │   |   ├── production.py
│   │   |   ├── test.py
│   │   ├── api_router.py
│   │   ├── asgi.py
│   │   ├── urls.py
│   │   ├── wsgi.py
│   ├── core/
│   │   ├── __init__.py
│   │   ├── api_views.py
│   │   ├── constants.py
│   │   ├── models.py
│   ├── courses/
│   │   ├── migrations/
│   │   ├── static/
│   │   ├── templates/
│   │   ├── tests/
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── urls.py
│   ├── students/
│   │   ├── migrations/
│   │   ├── tests/
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── urls.py
│   │   ├── views.py
│   ├── users/
│   │   ├── migrations/
│   │   ├── static/
│   │   ├── templates/
│   │   ├── tests/
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── urls.py
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── helpers.py
├── .env.example
├── README.md
├── uv.lock
├── pyproject.toml
├── .gitignore
├── .coveragerc
├── .pre-commit-config.yaml
```

## Commands:
### uv
- Add package
  - Add to project: `uv add <package-name>`
  - Add to `dev` group: `uv add --dev <dev-package-name>`
- Install packages:
   - Install all packages: `uv sync`
   - Install except dev packages: `uv sync --no-group dev`
- Run command in virtual environment: `uv run <command>`
- Ruff check: `ruff check`

### pre-commit
- Install hook scripts: `pre-commit install`
- Run pre-commit: `pre-commit run --all-files`

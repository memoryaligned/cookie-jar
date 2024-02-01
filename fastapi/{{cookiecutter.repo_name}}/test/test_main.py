from fastapi import FastAPI
from {{cookiecutter.repo_name}}.app import init_app


def test_init_app():
    app = init_app()
    assert isinstance(app, FastAPI)

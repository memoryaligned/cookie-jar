import unittest.mock

from fastapi import FastAPI
from {{cookiecutter.repo_name}}.app import init_app


def test_init_app():
    app = init_app(False)
    assert isinstance(app, FastAPI)


@unittest.mock.patch("{{cookiecutter.repo_name}}.config.get_db_connection_url")
def test_init_db_url_blank(get_db_connection_url):
    get_db_connection_url.return_value = None
    try:
        _ = init_app()
    except:
        assert True

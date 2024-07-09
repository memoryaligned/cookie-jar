# Cookie Cutter projects

Monorepo of [cookiecutter](https://github.com/cookiecutter/cookiecutter) templated projects that contain reasonable defaults
and full software lifecycle support (automated build and code quality).

<!-- toc -->

- [Python](#python)
  * [ds](#ds)
  * [api_regression](#api_regression)
  * [py](#py)
  * [fastapi](#fastapi)
  * [pymq](#pymq)
  * [pylambda](#pylambda)
- [Go Lang](#go-lang)
  * [go](#go)

<!-- tocstop -->

## Python

### ds

Data Science starter project incorporating best practices and ideas from my own
experience and around github.  The idea is to just use this "and go" for my
work with reasonable defaults.

```bash
cookiecutter ds
```

### api_regression

Host a tensorflow regression model and service inference requests.

```bash
cookiecutter api_regression
```

### py

Python starter project intended for use building generic python modules.
Default command-line support includes sub-commands by default.

```bash
cookiecutter py
```

### fastapi

HTTP Microservice based on [FastAPI](https://fastapi.tiangolo.com/) (asynchronous) with alembic support.
Includes [command-line support](https://docs.python.org/3/library/argparse.html) for sub-command database operations by default.

By default this project:
- installs [git hooks](https://pre-commit.com/hooks.html) to automatically format/check code, types, and pep8 style
- supports environment variables in [.env](https://pypi.org/project/python-dotenv/#getting-started) for rapid development
- runs a [code coverage](https://pytest-cov.readthedocs.io/en/latest/readme.html#usage) report with lines missing test coverage
- builds a HTML code coverage report
- [Docker](https://docs.docker.com/engine/reference/builder/) support out of the box

```bash
cookiecutter fastapi
cd [your project name]
make setup
vim .env
```

![FastAPI cookiecutter speed run](https://github.com/memoryaligned/memoryaligned/blob/main/images/fastapi_speedrun.gif)

### pymq

MQ Microservice with support for SQS and eventually RabbitMQ with reasonable
defaults.

```bash
cookiecutter pymq
```

### pylambda

TODO: implement this

```bash
cookiecutter pylambda
```

## Go Lang

### go

Starter project intended for use building go command-line utilties

```bash
cookiecutter go
```

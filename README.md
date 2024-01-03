# Cookie Cutter projects

Monorepo of [cookiecutter](https://github.com/cookiecutter/cookiecutter) templated projects that contain reasonable defaults
and full software lifecycle support (automated build and code quality).

<!-- toc -->

- [Python](#python)
  * [ds](#ds)
  * [py](#py)
  * [fastapi](#fastapi)
  * [pymq](#pymq)
  * [pylambda](#pylambda)
- [Go Lang](#go-lang)
  * [go](#go)
  * [golambda](#golambda)

<!-- tocstop -->

## Python

### ds

Data Science starter project incorporating best practices and ideas from my own
experience and around github.  The idea is to just use this "and go" for my
work with reasonable defaults.

```bash
cookiecutter ds
```

### py

Python starter project intended for use building generic python modules.
expect to add three additional baselines later for:

```bash
cookiecutter py
```

### fastapi

HTTP Microservice based on FastAPI (asynchronous) with alembic support.

```bash
cookiecutter fastapi
```

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

### golambda

TODO: implement this

```bash
cookiecutter golambda
```

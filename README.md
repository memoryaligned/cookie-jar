# Cookie Cutter projects

Monorepo of cookiecutter templated projects that contain reasonable defaults
and full software lifecycle support (automated build and code quality).

## todo

- microservice built on Flask (synchronous)

## ds

Data Science starter project incorporating best practices and ideas from my own
experience and around github.  The idea is to just use this "and go" for my
work with reasonable defaults.

```bash
cookiecutter ds
```

## py

Python starter project intended for use building generic python modules.
expect to add three additional baselines later for:

```bash
cookiecutter py
```

## fastapi

HTTP Microservice based on FastAPI (asynchronous) with alembic support.

```bash
cookiecutter fastapi
```

## pymq

MQ Microservice with support for SQS and eventually RabbitMQ with reasonable
defaults.

```bash
cookiecutter pymq
```

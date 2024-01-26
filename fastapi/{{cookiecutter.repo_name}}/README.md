# {{cookiecutter.project_name}}

{{cookiecutter.description}}

## docker

```bash
make docker
docker run -p 8080:8080 \
           -e SQLALCHEMY_DATABASE_URL=postgresql://<USER>@127.0.0.1:5432/<DBNAME>
           [name]:[tag]
```

## local system install (dependencies)

Native dependency required by psycopg2.

```bash
sudo apt install libpq5 -y
```

## Pip

file: ./venv/pip.conf

```pre
[global]
extra-index-url = https://REPO
```

## Alembic

NOTE: don't forget to set the sqlalchemy_url in the alembic.ini file

NOTE: don't forget to include your base model in the alembic/env.py file

To create a new database schema revision:

```bash
alembic revision --autogenerate -m "Adding [MODEL] model"
```

To apply proposed database schema changes (including dropping tables):

```bash
alembic upgrade head
```

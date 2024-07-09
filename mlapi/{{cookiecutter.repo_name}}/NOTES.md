# NOTES

## To Get started

1. Create your environment and set the project up

```bash
make setup
```

2. edit your alembic.ini file to configure your project

```bash
vim ./alembic.ini
```

## Database setup

file: alembic.ini

```ini
sqlalchemy.url = postgresql://<user>:@<host>:5432/<dbname>
```

generate an initial version of the Alembic migrations

```bash
alembic revision --autogenerate -m "initial revision"
alembic upgrade head
```

Run the database

```bash
pg_ctl -D /path/data_dir -l /path/logfile.log start
```

## Populate the database with models

```bash
source venv/bin/activate
{{cookiecutter.repo_name}}_init_db
```

## If you have CSV data

In Postgresql:

```SQL
COPY table(col1, col2) FROM '../csv' CSV HEADER DELIMITER ',';
```

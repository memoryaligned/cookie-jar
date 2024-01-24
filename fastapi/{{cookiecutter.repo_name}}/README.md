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

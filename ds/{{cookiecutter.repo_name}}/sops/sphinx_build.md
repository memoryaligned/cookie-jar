# Sphinx Build

When you pip install sphinx you can use the sphinx-quickstart command

All markup is reStructured Text (RST)

## Configuration

conf.py

## Build PDF documentation

```bash
cd doc
make latex
cd _build/latex
make all-pdf
```

## Build HTML documentation

```
make html
```

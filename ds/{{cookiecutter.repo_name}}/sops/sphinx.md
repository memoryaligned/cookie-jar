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

## Table support

```
.. list-table:: Title
   :widths: 225 25 50
   :header-rows: 1

   * - heading row1, col 1
     - heading row1, col 2
     - heading row1, col 3
   * - row 1, col 1
     - row 1, col 2
     - row 1, col 3
```

## Add files to the toc

```
.. toctree:: 
   :maxdepth: 2
   :caption: Contents:

   file_name

// file_name
Title
=====

Text...
```

## Image support

NOTE: you must have a single space before the image directive for this to work.

```
 .. image:; path/to/image.png
    :width: 400
    :alt: Alternative text
```

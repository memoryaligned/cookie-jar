.. {{cookiecutter.repo_name}} documentation master file, created by
   sphinx-quickstart on Sat Apr  6 15:26:16 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

{{cookiecutter.repo_name}} API Reference
======================================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

Introduction
============

You can interact with the API via HTTP requests from any language.  To install
python support:

```python
pip install {{cookiecutter.repo_name}}
```


Making Requests
===============

```bash
curl http://127.0.0.1/ai/{{cookiecutter.model_name}}/inference \
   -d '{
      "input": [
        [ <DATA HERE> ]
      ]
   }'
```


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

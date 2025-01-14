.. _intro:

Introduction
============

Installation
------------

Run this in your terminal to install the library

.. code-block:: bash

    python3 -m pip install nevargs

Example Usage
-------------

.. code-block:: python

    import nevargs
    s = "this is -f True fun -c command"
    nevargs.dictify(s)
    >>> {'args': ['this', 'is', 'fun'], '-f': ['True'], '-c': ['command']}
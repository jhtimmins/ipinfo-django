=============================
ipinfo_django
=============================

.. image:: https://badge.fury.io/py/ipinfo_django.svg
    :target: https://badge.fury.io/py/ipinfo_django

.. image:: https://travis-ci.org/jhtimmins/ipinfo_django.svg?branch=master
    :target: https://travis-ci.org/jhtimmins/ipinfo_django

.. image:: https://codecov.io/gh/jhtimmins/ipinfo_django/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/jhtimmins/ipinfo_django

Middleware to add IP data to Django request.

Documentation
-------------

The full documentation is at https://ipinfo_django.readthedocs.io.

Quickstart
----------

Install ipinfo_django::

    pip install ipinfo_django

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'ipinfo_django.apps.IpinfoDjangoConfig',
        ...
    )

Add ipinfo_django's URL patterns:

.. code-block:: python

    from ipinfo_django import urls as ipinfo_django_urls


    urlpatterns = [
        ...
        url(r'^', include(ipinfo_django_urls)),
        ...
    ]

Features
--------

* TODO

Running Tests
-------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install tox
    (myenv) $ tox

Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage

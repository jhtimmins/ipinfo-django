=====
Usage
=====

To use ipinfo_django in a project, add it to your `INSTALLED_APPS`:

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

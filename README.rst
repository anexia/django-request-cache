====================
Django Request Cache
====================

Django Request Cache provides a cache for each request (within your Django Request/Response cycle).

Quick start
-----------

1. Download and install using `pip install`

.. code-block:: bash

    pip install django-request-cache


2. Add ``UserForeignKeyMiddleware`` and ``RequestCacheMiddleware`` to your ``MIDDLEWARE`` settings like this:

.. code-block:: python

    MIDDLEWARE = (
        ...
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        ...
        'django_userforeignkey.middleware.UserForeignKeyMiddleware',
        'django_request_cache.middleware.RequestCacheMiddleware',
    )


or if you are still using the an older Django version (e.g., Django 1.8) with ``MIDDLEWARE_CLASSES``:

.. code-block:: python

    MIDDLEWARE_CLASSES = (
        ...
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        ...
        'django_userforeignkey.middleware.UserForeignKeyMiddleware',
        'django_request_cache.middleware.RequestCacheMiddleware',
    )


3. Use the per-request cache as a decorator

.. code-block:: python

    from django_request_cache import cache_for_request

    @cache_for_request
    def do_some_complex_calculation(a, b, c):
        print("Calculating... please wait")
        return a * b * c


Try it out by executing do_some_complex_calculation multiple times within your request

Attribution
-----------

``RequestCache`` and ``RequestCacheMiddleware`` (see ``middleware.py``) are from a source code snippet on StackOverflow
https://stackoverflow.com/questions/3151469/per-request-cache-in-django/37015573#37015573
created by coredumperror https://stackoverflow.com/users/464318/coredumperror
Original Question was posted by https://stackoverflow.com/users/7679/chase-seibert
at https://stackoverflow.com/questions/3151469/per-request-cache-in-django
copied on 2017-Dec-20


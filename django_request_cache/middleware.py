from django.core.cache.backends.base import BaseCache
from django.core.cache.backends.locmem import LocMemCache
from django.utils.deprecation import MiddlewareMixin
from django.utils.synch import RWLock

# Attribution: RequestCache and RequestCacheMiddleware are from a source code snippet on StackOverflow
# https://stackoverflow.com/questions/3151469/per-request-cache-in-django/37015573#37015573
# created by coredumperror https://stackoverflow.com/users/464318/coredumperror
# Original Question was posted by https://stackoverflow.com/users/7679/chase-seibert
# at https://stackoverflow.com/questions/3151469/per-request-cache-in-django
# copied on 2017-Dec-20


class RequestCache(LocMemCache):
    """
    RequestCache is a customized LocMemCache which stores its data cache as an instance attribute, rather than
    a global. It's designed to live only as long as the request object that RequestCacheMiddleware attaches it to.
    """

    def __init__(self):
        # We explicitly do not call super() here, because while we want BaseCache.__init__() to run, we *don't*
        # want LocMemCache.__init__() to run, because that would store our caches in its globals.
        BaseCache.__init__(self, {})

        self._cache = {}
        self._expire_info = {}
        self._lock = RWLock()


class RequestCacheMiddleware(MiddlewareMixin):
    """
    For every request, a fresh cache instance is stored in ``request.cache``.
    The cache instance lives only as long as request does.
    """

    def process_request(self, request):
        request.cache = RequestCache()

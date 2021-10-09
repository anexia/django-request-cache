from datetime import datetime

from django_request_cache import cache_for_request


@cache_for_request
def retrieve_time():
    return datetime.now()

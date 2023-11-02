import pandas as pd
from datetime import datetime

from django_request_cache import cache_for_request


@cache_for_request
def retrieve_time():
    return datetime.now()


def retrieve_dataframe_uncached():
    return pd.DataFrame({
        'a': [1, 2, 3],
        'b': [4.0, 5.0, 6.0],
        'c': ['a', 'b', 'c'],
        'd': [True, False, True],
        'e': datetime.now(),
        'f': pd.NA
    })


@cache_for_request
def retrieve_dataframe_cached():
    return retrieve_dataframe_uncached()



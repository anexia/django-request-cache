from django.http import HttpResponse
from testapp.utils import retrieve_time, retrieve_dataframe_cached, retrieve_dataframe_uncached


def index_view(request):
    retrieve_time()
    retrieve_time()
    return HttpResponse()


def pandas_view(request):
    """
    Esure that the cache_for_request decorator works with pandas dataframes.
    """
    df1 = retrieve_dataframe_cached()
    df2 = retrieve_dataframe_cached()

    if not df1.equals(df2):
        raise Exception("Dataframes are not equal")
    
    df3 = retrieve_dataframe_uncached()
    df4 = retrieve_dataframe_uncached()

    if df3.equals(df4):
        raise Exception("Dataframes are equal")
        
    return HttpResponse()

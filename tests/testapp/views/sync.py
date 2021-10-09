from django.http import HttpResponse
from testapp.utils import retrieve_time

def index_view(request):
    retrieve_time()
    retrieve_time()
    return HttpResponse()

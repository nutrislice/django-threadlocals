from django.urls import include, path, re_path

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
from django.http import HttpResponse
from threadlocals.threadlocals import get_current_request


def empty_view(request):
    return HttpResponse("")


def query_view(request):
    content = get_current_request().GET.dict()
    return HttpResponse(str(content))


def exception_view(request):
    raise Exception('Exception in response.')


urlpatterns = [
    # Examples:
    path('', empty_view, name='empty'),
    re_path(r'query/', query_view, name='query'),
    re_path(r'exception/', exception_view, name='exception'),
    # path('testrunner/', include('testrunner.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # path('admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # path('admin/', include(admin.site.urls)),
]

from django.conf.urls import include, url

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
    url(r'^$', empty_view, name='empty'),
    url(r'query/', query_view, name='query'),
    url(r'exception/', exception_view, name='exception'),
    # url(r'^testrunner/', include('testrunner.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
]

Setup/Usage
===========
Install using `pip install django-threadlocals`

Add `threadlocals.middleware.ThreadLocalMiddleware` to your `MIDDLEWARE_CLASSES` setting.
Then use it as follows:

Example usage:
--------------
```python
from threadlocals.threadlocals import get_current_request

request = get_current_request()
```


Caveat Emptor
==================

See [this thread on django-users](https://groups.google.com/forum/?fromgroups=#!topic/django-users/5681nX0YPgQ) for a historical in-depth discussion. This package is production ready, this is the story where it began, a long long time ago:
Having the request in threadlocals is the core piece that allowed us to build a true multi-tenant system on top of django where the site is resolved dynamically based on the current host,
and  objects are filtered based on the current host. With the current version of django, this is nearly impossible to do without the request in threadlocals.  This was a very significant and advanced undertaking, but we're happy with the results.


Tests
-----

To run tests:

`python tester/manage.py test`


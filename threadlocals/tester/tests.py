"""
This file demonstrates two different styles of tests (one doctest and one
unittest). These will both pass when you run "manage.py test".

Replace these with more appropriate tests for your application.
"""
from django.test import RequestFactory, SimpleTestCase
from django.urls import reverse

from threadlocals.threadlocals import (
    set_thread_variable, get_thread_variable, get_current_request,
    # get_current_session
)


class ThreadlocalsTest(SimpleTestCase):

    def setUp(self):
        set_thread_variable('request', None)

    def tearDown(self):
        set_thread_variable('request', None)

    def test_get_thread_variable_default(self):
        gotten = get_thread_variable('unset', 'default value')
        self.assertEqual(gotten, 'default value')

    def test_get_set_thread_variable(self):
        set_thread_variable('test', {'test': 'test'})
        gotten = get_thread_variable('test')
        self.assertEqual(gotten, {'test': 'test'})

    def test_get_current_request(self):
        self.assertEqual(get_current_request(), None)  # tests default (None)
        request = RequestFactory().get(u'/')
        set_thread_variable('request', request)
        self.assertEqual(get_current_request(), request)

    def test_get_current_session(self):
        # c = self.client
        # request = get_current_request()
        # request.session = c.session
        # self.assertEqual(get_current_session(), c.session)
        pass  # not testing for now because it might require a database and the function we're testing is dead simple. Feel free to add if its worth it to you.

    def test_get_current_user(self):
        pass


class ThreadLocalMiddlewareTest(SimpleTestCase):

    def test_process_request(self):
        """
        if ThreadLocalMiddleware is enabled in settings, then running the test client
        should trigger the middleware and set the request in thread locals
        """
        response = self.client.get(''.join([reverse('query'), '?query=test']))
        self.assertEqual(response.content.decode('utf8'), u"{'query': 'test'}")
        # No formal way to order tests, so verify request is deleted here.
        self.assertEqual(get_current_request(), None)

    def test_process_exception(self):
        with self.assertRaises(Exception):
            response = self.client.get(reverse('exception'))
        self.assertEqual(get_current_request(), None)

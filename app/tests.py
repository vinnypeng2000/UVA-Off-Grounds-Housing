
import unittest
import datetime
import os
import unittest
from django.test import TestCase
from django.urls import reverse
from django.test import Client, TestCase
from django.contrib.auth.models import User
import string
import random
from django.urls import reverse
from .models import *
import json
from django.test import SimpleTestCase
from app.forms import CommentForm
# Create your tests here.


class TestForms(SimpleTestCase):
    def review_form(self):
        form = CommentForm(data={
            'housing': '605 14th St NW',
            'review': 'great housing',
            'rating': '5'
        })
        self.assertTrue(form.is_valid())

    def no_data(self):
        form = CommentForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 3)


class DummyTestCase(TestCase):

    def test_dummy_test_case(self):
        x = 1
        y = 2
        z = x + y
        self.assertEqual(z, 3)


class TestOAuth(unittest.TestCase):

    def test_create_new_user(self):
        num = 10
        username = ''.join(random.choices(
            string.ascii_uppercase + string.digits, k=num))
        user = User.objects.create(username=username)
        user.set_password('p@ssword')
        user.save()
        c = Client()
        logged_in = c.login(username=username, password='p@ssword')
        self.assertEqual(logged_in, True)

    def test_user_exists(self):
        c = Client()
        logged_in = c.login(username='testuser', password='123password123')
        self.assertEqual(logged_in, False)

    def test_login_fail(self):
        c = Client()
        logged_in = c.login(username='user-does-not-exist',
                            password='no-password')
        self.assertEqual(logged_in, False)


class URLTests(TestCase):
    def test_testhomepage(self):
        response = self.client.get('/app')
        self.assertEqual(response.status_code, 301)


class TestMapBox(TestCase):

    def test_load_page(self):
        response = self.client.get('/app/filter')
        self.assertEqual(response.status_code, 301)
        # self.assertContains(response, 'UVA off-grounds Housing')

    def test_load_map(self):
        num = 20
        username = ''.join(random.choices(
            string.ascii_uppercase + string.digits, k=num))
        user = User.objects.create(username=username)
        user.set_password('p@ssword')
        user.save()
        c = Client()
        logged_in = c.login(username=username, password='p@ssword')
        self.assertEqual(logged_in, True)
        response = c.get('/app/filter')
        self.assertEqual(response.status_code, 301)
        # self.assertContains(response, 'map')


class ModelTest(TestCase):  # house
    def test_entry(self):
        housing = Housing(
            name="1100 Preston Avenue",
            address="1100 Preston Avenue, Charlottesville, VA 22903",
            lat=38.042003,
            long=-78.491938,
            housing_type="House",
            pub_date=datetime.datetime(2021, 12, 6, 16, 31, 31)
        )
        housing.save()
        record = Housing.objects.get(pk=housing.id)
        self.assertEqual(record, housing)
    # townhouse

    def test_entry1(self):
        housing = Housing(
            name="630 Cabell Ave. Townhome",
            address="630 Cabell Ave, Charlottesville, VA 22903",
            lat=38.041968,
            long=-78.496871,
            housing_type="Town House",
            pub_date=datetime.datetime(2021, 12, 6, 16, 31, 31)
        )
        housing.save()
        record = Housing.objects.get(pk=housing.id)
        self.assertEqual(record, housing)

    def test_entry2(self):  # apartment
        housing = Housing(
            name="Grandmarc",
            address="301 15th St NW, Charlottesville, VA 22903",
            lat=38.037343,
            long=-78.499568,
            housing_type="Apartment",
            pub_date=datetime.datetime(2021, 10, 27, 16, 31, 31)
        )
        housing.save()
        record = Housing.objects.get(pk=housing.id)
        self.assertEqual(record, housing)


# class TestViews(TestCase):
    # def test_project_list_GET(self):
        #client = Client()
        #response = client.get('/app/search_housing/')
        #self.assertEquals(response.status_code, 200)
        # self.assertTemplatedUsed(response, 'app/logout.html')


class BaseTest(TestCase):
    def setup(self):
        self.register_url = reverse('register')
        return super().setUp()


# class RegisterTest(BaseTest):

#     def test_view_page(self):
#         response = self.client.get(self.register_url)
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'app/index.html')

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)


if __name__ == '__main__':
    unittest.main()


class MyTestCase(unittest.TestCase):

    @unittest.skip("demonstrating skipping")
    def test_nothing(self):
        self.fail("shouldn't happen")

    def test_format(self):
        # Tests that work for only a certain version of the library.
        pass

    def test_windows_support(self):
        # windows specific testing code
        pass


class Tests():

    def suite(self):  # Function stores all the modules to be tested

        modules_to_test = []
        test_dir = os.listdir('.')
        for test in test_dir:
            if test.startswith('test') and test.endswith('.py'):
                modules_to_test.append(test.rstrip('.py'))

        alltests = unittest.TestSuite()
        for module in map(__import__, modules_to_test):
            module.testvars = ["variables you want to pass through"]
            alltests.addTest(unittest.findTestCases(module))
        return alltests


if __name__ == '__main__':
    MyTests = Tests()
    unittest.main(defaultTest='MyTests.suite')


class SomeTestSuite(unittest.TestSuite):

    # Tests to be tested by test suite
    def makeRemoveAudioSource():
        suite = unittest.TestSuite()
        suite.AddTest(TestSomething("TestSomeClass"))

        return suite

    def suite():
        return unittest.makeSuite(TestSomething)


if __name__ == '__main__':
    unittest.main()

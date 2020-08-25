from django.urls import resolve
from django.test import TestCase
from resumeapp.views import home, resume, blog, contact


class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home)


class ResumePageTest(TestCase):

    def test_root_url_resolves_to_resume_page_view(self):
        found = resolve('/resume/')
        self.assertEqual(found.func, resume)


class BlogPageTest(TestCase):

    def test_root_url_resolves_to_blog_page_view(self):
        found = resolve('/blog/')
        self.assertEqual(found.func, blog)


class ContactPageTest(TestCase):

    def test_root_url_resolves_to_contact_page_view(self):
        found = resolve('/contact/')
        self.assertEqual(found.func, contact)

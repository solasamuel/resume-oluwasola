from django.urls import resolve
from django.test import TestCase
from resumeapp.views import home, resume, blog, contact


class HomePageTest(TestCase):

    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')


class ResumePageTest(TestCase):

    def test_uses_home_template(self):
        response = self.client.get('/resume/')
        self.assertTemplateUsed(response, 'resume.html')


class BlogPageTest(TestCase):

    def test_uses_home_template(self):
        response = self.client.get('/blog/')
        self.assertTemplateUsed(response, 'blog.html')


class ContactPageTest(TestCase):

    def test_uses_home_template(self):
        response = self.client.get('/contact/')
        self.assertTemplateUsed(response, 'contact.html')

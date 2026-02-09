from django.test import TestCase
from .forms import CollaborateForm

# Create your tests here.


class TestCollaborateForm(TestCase):

    def test_form_is_valid(self):
        """ Test for all fields"""
        form = CollaborateForm({
            'name': 'Author',
            'email': 'test@test.com',
            'message': 'Hello!'
        })
        self.assertTrue(form.is_valid(), msg="About form is not valid")

    def test_name_is_invalid(self):
        form = CollaborateForm({
            'name': '',
            'email': 'test@test.com',
            'message': 'Hello!'
        })
        self.assertFalse(
            form.is_valid(), msg="No name provided, but collaborate form is valid")

    def test_email_is_invalid(self):
        form = CollaborateForm({
            'name': 'Author',
            'email': '',
            'message': 'Hello!'
        })
        self.assertFalse(
            form.is_valid(), msg="No email provided, but collaborate form is valid")

    def test_name_is_invalid(self):
        form = CollaborateForm({
            'name': 'Author',
            'email': 'test@test.com',
            'message': ''
        })
        self.assertFalse(
            form.is_valid(), msg="No message provided, but collaborate form is valid")

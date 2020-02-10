import unittest
from django.test import Client
from django.test import TestCase, TransactionTestCase, RequestFactory, override_settings
from django.contrib.auth.models import AnonymousUser, User
from account.models import Org, Receiver, ChildEduDonor, PoorDonor, HomeDonor
from account.views import log, reg

class SimpleTest(unittest.TestCase):
    def test_home_page(self):
        client = Client()
        response = client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_register_page(self):
        client = Client()
        response = client.get('/register/')
        titleOfWebPage = register.Title
        self.assertTrue(response.status_code, 200)

class TestsPrimaryKey(TransactionTestCase):
    reset_sequences = True

    def test_org_pk(self):
        org = Org.objects.create(org_name="Nhhs", email="nhhs@gmail.com", password="12345", address="ktm", contact=986712345, total_amt=23000, bank_acc=1289)

        # org.pk is guaranteed to always be 1
        self.assertNotEqual(org.pk, 2)


    def setup(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            first_name='satya', last_name= 'shrestha', username= 'satya123',email='satya@gmail.com', password='12345', confirm_password= '12345')

class SimpleTestCase(TestCase):
    def test_org_model(self):
        org = Org.objects.create(org_name="Nhhs", email="nhhs@gmail.com", password="12345", address="ktm", contact=986712345, total_amt=23000, bank_acc=1289)
        val = org.is_valid_organization()
        self.assertTrue(val)

 

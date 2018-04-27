from django.test import TestCase, Client
from .models import Appointment, User
from .forms import StaffLoginForm

class ResponseTestCases(TestCase):

    def setUp(self):
        self.c = Client()

    def test_login_view(self):
        response = self.c.get('/login')
        if(response.status_code == 404):
            self.assertEqual(True, False)
        else:
            self.assertEqual(True, True)

    def test_appointment_view_protection(self):
        response = self.c.get('/appointment/')
        if response.url.startswith('/login'):
            self.assertEqual(True, True)
        else:
            self.assertEqual(False, True)

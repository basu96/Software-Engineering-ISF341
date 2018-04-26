from django.test import TestCase
from .models import Appointment, User

class UserCreationTestCase(TestCase):

    def setUp(self):
        user = User.objects.create(
            username = 'patient1',
            first_name = 'Imaginary',
            user_type = 1,
            last_name = 'Name',
            email = 'gg@wp.com',
            phone = '81392061',
            blood_group = 'A+',
            gender = 'Male',
        )
        self.user = User.objects.get(username = 'patient1')

    def test_user_type(self):
        self.assertEqual(self.user.user_type, 1)

    def test_first_name(self):
        self.assertEqual(self.user.first_name, 'Imaginary')

    def test_last_name(self):
        self.assertEqual(self.user.last_name, 'Name')

    def test_email(self):
        self.assertEqual(self.user.email, 'gg@wp.com')

    def test_phone(self):
        self.assertEqual(self.user.phone, '81392061')

    def test_blood_group(self):
        self.assertEqual(self.user.blood_group, 'A+')

    def test_gender(self):
        self.assertEqual(self.user.gender, 'Male')


class AppointmentTestCase(TestCase):

    def setUp(self):
        pat = User.objects.create(username = 'patient1', user_type = 1)
        doc = User.objects.create(username = 'doctor1', user_type = 2)
        appt = Appointment.objects.create(patient = pat, doctor = doc)

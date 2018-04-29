from django.test import TestCase
from .models import Appointment, User
from datetime import datetime

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
        print('User type test OK')

    def test_first_name(self):
        self.assertEqual(self.user.first_name, 'Imaginary')
        print('User first name test OK')

    def test_last_name(self):
        self.assertEqual(self.user.last_name, 'Name')
        print('User last name test OK')

    def test_email(self):
        self.assertEqual(self.user.email, 'gg@wp.com')
        print('User email test OK')

    def test_phone(self):
        self.assertEqual(self.user.phone, '81392061')
        print('User phone test OK')

    def test_blood_group(self):
        self.assertEqual(self.user.blood_group, 'A+')
        print('User blood group test OK')

    def test_gender(self):
        self.assertEqual(self.user.gender, 'Male')
        print('User gender test OK')


class AppointmentTestCase(TestCase):

    def setUp(self):
        pat = User.objects.create(username = 'patient1', user_type = 1)
        doc = User.objects.create(username = 'doctor1', user_type = 2)
        appt = Appointment.objects.create(
            patient = pat,
            doctor = doc,
            date_time = datetime.now(),
            blood_pressure = '125/89',
            breath_rate = '80',
            pulse_rate = '75',
            body_temperature = '101',
            report = 'Positive report',
            prescription = '4 medicines',
            prognosis = 'Two months course',
        )
        self.appt = Appointment.objects.get(patient = pat)

    def test_doctor(self):
        self.assertEqual(self.appt.doctor.username, 'doctor1')
        print('Appointment doctor test OK')

    def test_blood_pressure(self):
        self.assertEqual(self.appt.blood_pressure, '125/89')
        print('Appointment blood_pressure test OK')

    def test_breath_rate(self):
        self.assertEqual(self.appt.breath_rate, 80)
        print('Appointment breath_rate test OK')

    def test_pulse_rate(self):
        self.assertEqual(self.appt.pulse_rate, 75)
        print('Appointment pulse_rate test OK')


    def test_body_temperature(self):
        self.assertEqual(self.appt.body_temperature, 101)
        print('Appointment body_temperature test OK')


    def test_report(self):
        self.assertEqual(self.appt.report, 'Positive report')
        print('Appointment report test OK')


    def test_prescription(self):
        self.assertEqual(self.appt.prescription, '4 medicines')
        print('Appointment prescription test OK')


    def test_prognosis(self):
        self.assertEqual(self.appt.prognosis, 'Two months course')
        print('Appointment prognosis test OK')


class ObjectRemoveTestCase(TestCase):

    def setUp(self):
        pat = User.objects.create(username = 'patient1', user_type = 1)
        doc = User.objects.create(username = 'doctor1', user_type = 2)
        appt = Appointment.objects.create(
            patient = pat,
            doctor = doc,
        )

        appt.delete()
        pat.delete()
        doc.delete()

    def test_patient_existence(self):
        pat = User.objects.filter(username = 'patient1')
        if len(pat):
            self.assertEqual(True, False)
            print('Object remove patient existence test failed')
        else:
            self.assertEqual(True, True)
            print('Object remove patient existence test OK')


    def test_doctor_existence(self):
        doc = User.objects.filter(username = 'doctor1')
        if len(doc):
            self.assertEqual(True, False)
            print('Object remove patient existence test failed')
        else:
            self.assertEqual(True, True)
            print('Object remove doctor existence test OK')


    def test_appointment_existence(self):
        appt = Appointment.objects.all()
        if len(appt):
            self.assertEqual(True, False)
            print('Object remove appointment existence test failed')
        else:
            self.assertEqual(True, True)
            print('Object remove appointment existence test OK')

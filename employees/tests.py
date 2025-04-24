from django.test import TestCase
from employees.models import Employee

class EmployeeModelTest(TestCase):
    def setup(self):
        self.user = User.objects.create_user(username="testuser", password="password")
# self は自分自身に操作を加えたいときに使うもの
    def test_employee_str_with_user(self):
        employee = Employee.objects.create(
            name="Alice",
            email="alice@example.com",
            department="HR",
            user=self.user
        )
        self.assertEqual(str(employee), "Alice (testuser)")
    def test_employee_str_without_user(self):
        employee = Employee.objects.create(
            name="Bob",
            email="bob@example.com",
            department="Finance"
        )
        self.assertEqual(str(employee), "Bob (No User)")

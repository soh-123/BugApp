from django.test import TestCase
from django.utils import timezone
from .models import Bug
from django.urls import reverse
# Create your tests here.

class BugModelTestCase(TestCase):

    def setUp(self):
        self.bug = Bug.objects.create(
        bug_description="Test bug description",
        bug_type="error",
        report_date=timezone.now(),
        status="To do"
    )

    def test_bug_creation(self):
        self.assertEqual(self.bug.__str__(), "Test bug description")

    def test_bug_type(self):
        self.assertEqual(self.bug.bug_type, "error")

    def test_bug_status_choices(self):
        self.assertEqual(self.bug.status, "To do")

    def test_report_date(self):
        saved_bug = Bug.objects.get(pk=self.bug.pk)
        self.assertEqual(saved_bug.report_date, timezone.now().date())


class BugViewsTest(TestCase):
    def setUp(self):
        self.bug = Bug.objects.create(
            bug_description="Test Bug",
            bug_type="error",
            report_date=timezone.now(),
            status="todo"
        )

    def test_register_bug_view(self):
        """Test the register bug view."""
        url = reverse('register bug')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_bug_detail_view(self):
        """Test the bug detail view."""
        url = reverse('bug details', args=[self.bug.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Bug")

    def test_bug_list_view(self):
        """Test the bug list view."""
        url = reverse('index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Bug")

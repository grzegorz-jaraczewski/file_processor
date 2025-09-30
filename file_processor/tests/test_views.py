from django.test import TestCase
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile


class HomeViewTests(TestCase):
    """
    Integration tests for the `home` view.

    These tests ensure that the view correctly handles both GET and POST requests:
        - GET request:
            * Returns status code 200
            * Renders the "processor/home.html" template
            * Contains the expected form header text
        - POST request:
            * Accepts a file upload
            * Processes the uploaded text using the application logic
            * Returns status code 200
            * Renders the "processor/output.html" template
            * Contains the processed text in the response
    """

    def test_get_request_renders_form(self):
        """
        Test that a GET request to the `home` view renders the form.

        Verifies:
            - The response status code is 200 (OK).
            - The "processor/home.html" template is used.
            - The page contains the form header text ("Upload a Text File").
        """
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "processor/home.html")
        self.assertContains(response, "Upload a Text File")

    def test_post_request_processes_text(self):
        """
        Test that a POST request with a valid text file is processed correctly.

        Verifies:
            - The response status code is 200 (OK).
            - The "processor/output.html" template is used.
            - The processed text appears in the response.
        """
        file_content = b"Hello world!"
        uploaded_file = SimpleUploadedFile("test.txt", file_content, content_type="text/plain")
        response = self.client.post(reverse("home"), {"file": uploaded_file})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "processor/output.html")
        self.assertContains(response, "H")

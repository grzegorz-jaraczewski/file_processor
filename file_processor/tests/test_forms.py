from django.test import SimpleTestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from django.utils.datastructures import MultiValueDict

from processor.forms import UploadFileForm


class UploadFilesFormTest(SimpleTestCase):
    """
    Unit tests for the UploadFileForm.

    These tests verify that the form behaves correctly when handling
    file uploads:
        - Accepts a valid uploaded text file.
        - Rejects submissions without a file.
    """

    def test_valid_form(self):
        """
        Test that UploadFileForm validates successfully when a valid
        text file is provided.

        Simulates a file upload by creating a SimpleUploadedFile and
        wrapping it in a MultiValueDict to mimic request.FILES.
        """
        file_content = b"Hello World"
        uploaded_file = SimpleUploadedFile("test.txt", file_content, content_type="text/plain")
        files = MultiValueDict({"file": [uploaded_file]})
        form = UploadFileForm(files=files)
        self.assertTrue(form.is_valid())

    def test_invalid_form_no_file(self):
        """
        Test that UploadFileForm is invalid when no file is submitted.

        Ensures the required 'file' field validation works as expected.
        """
        form = UploadFileForm(data={})
        self.assertFalse(form.is_valid())

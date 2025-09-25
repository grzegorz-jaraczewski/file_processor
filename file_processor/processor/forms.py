from django import forms


class UploadFileForm(forms.Form):
    """
    Form used for uploading a text file.

    This form contains a single file field that expects
    a plain text file (.txt). The uploaded file will be
    processed by the application, which shuffles the
    letters inside each word while keeping the first and
    last letters in place.
    """

    file = forms.FileField(
        label="Choose the text file: ",
        help_text="Upload a .txt file that you want to process."
    )

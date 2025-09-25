from django.shortcuts import render
from .forms import UploadFileForm
from .utils import process_text


def home(request):
    """
    Handle file upload and text processing for the application.

    - On GET request:
        Renders the home page with an empty upload form.
    - On POST request:
        Validates the uploaded file, reads its contents,
        processes the text by shuffling the inner letters of
        each word, and renders the result page.

    Args:
        request (HttpRequest): The HTTP request object. May contain
                               form data and uploaded files.

    Returns:
        HttpResponse: A rendered template response. Either:
            * "processor/home.html" with the upload form, or
            * "processor/result.html" with the processed text.
    """
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = request.FILES["file"]
            text = uploaded_file.read().decode("utf-8")
            processed = process_text(text)
            return render(
                request=request,
                template_name="processor/output.html",
                context={"output": processed}
            )
    else:
        form = UploadFileForm()
    return render(
        request=request,
        template_name="processor/home.html",
        context={"form": form}
    )

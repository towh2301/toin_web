from django.shortcuts import render
from django.http import FileResponse, HttpResponse
from pdf2docx import Converter
import os, tempfile, uuid

app_name = 'converter'

def index(request):
    return render(request, 'base.html')

def convert_pdf(request):
    if request.method == 'POST' and request.FILES.get('pdf_file'):
        pdf_file = request.FILES['pdf_file']

        if not pdf_file.name.lower().endswith('.pdf'):
            return HttpResponse("Please upload a valid PDF file.", status=400)

        # Temporary paths
        tmp_dir = tempfile.mkdtemp(prefix='pdf2docx_')
        pdf_path = os.path.join(tmp_dir, f"{uuid.uuid4().hex}.pdf")
        docx_path = os.path.join(tmp_dir, f"{uuid.uuid4().hex}.docx")

        # Save PDF temporarily
        with open(pdf_path, 'wb') as f:
            for chunk in pdf_file.chunks():
                f.write(chunk)

        try:
            # Convert PDF → DOCX
            cv = Converter(pdf_path)
            cv.convert(docx_path)
            cv.close()

            response = FileResponse(open(docx_path, 'rb'),
                                    as_attachment=True,
                                    filename=pdf_file.name.replace('.pdf', '.docx'))
            return response
        except Exception as e:
            return HttpResponse(f"Conversion failed: {e}", status=500)
        finally:
            pass  # (optionally cleanup)
    return HttpResponse("No file uploaded.", status=400)

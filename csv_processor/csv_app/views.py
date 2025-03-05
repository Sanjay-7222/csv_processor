from django.shortcuts import render
from django.http import JsonResponse
import os
from django.conf import settings
from .models import CSVFile, ProcessedData
from .forms import CSVUploadForm
from .tasks import process_csv

def upload_csv(request):
    if request.method == "POST":
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = form.save()
            file_path = os.path.join(settings.MEDIA_ROOT, str(csv_file.file))
            process_csv.delay(file_path)  

            return JsonResponse({"message": "File uploaded successfully! Processing in the background."}, status=200)
        
        
        return JsonResponse({"error": form.errors['file'][0]}, status=400)

    return render(request, "csv_app/upload.html", {"form": CSVUploadForm()})


def results(request):
    query = request.GET.get("q", "")
    if query:
        data = ProcessedData.objects.filter(column_name__icontains=query)
    else:
        data = ProcessedData.objects.all()
    
    return render(request, "csv_app/results.html", {"data": data})

from django.db import models

# Create your models here.

class CSVFile(models.Model):
    file = models.FileField(upload_to="csv_files/")
    uploaded_at = models.DateTimeField(auto_now_add=True)

class ProcessedData(models.Model):
    column_name = models.CharField(max_length=255)
    sum_value = models.FloatField()
    avg_value = models.FloatField()
    count_value = models.IntegerField()

import pandas as pd
from celery import shared_task
from .models import ProcessedData

@shared_task
def process_csv(file_path):
    df = pd.read_csv(file_path)

    numeric_cols = df.select_dtypes(include=['number']).columns

    for col in numeric_cols:
        ProcessedData.objects.create(
            column_name=col,
            sum_value=df[col].sum(),
            avg_value=df[col].mean(),
            count_value=df[col].count()
        )

    return f"Processed {len(numeric_cols)} columns!"

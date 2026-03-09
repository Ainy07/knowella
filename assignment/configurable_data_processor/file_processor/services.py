import pandas as pd
import json
from django.conf import settings
from .models import ProcessedData
def process_file(file_path):

    df = pd.read_csv(file_path)

    with open("config/rules.json") as f:
        config = json.load(f)

    operations = config.get("operations", [])

    for op in operations:

        column = op["column"]
        action = op["action"]
        value = op["value"]

        if action == "multiply":
            df[column] = df[column] * value

        elif action == "add":
            df[column] = df[column] + value
        
        elif action == "filter":
            df = df[df[column] > value]

        elif action == "drop_column":
            df = df.drop(columns=[column])

    return df


def save_to_db(df):
    
    for _, row in df.iterrows():
        ProcessedData.objects.create(
            name=row["name"],
            age=row["age"],
            salary=row["salary"]
        )
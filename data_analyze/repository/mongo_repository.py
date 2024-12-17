import pandas as pd
from mongo_consumer_app.db.database import student_collection



def get_average_of_gpa():
    life_style = list(student_collection.find({}, {'life_style': 1, '_id': 0}))
    df = pd.DataFrame(map(lambda x: x['life_style'], life_style))
    df['GPA'] = pd.to_numeric(df['GPA'], errors='coerce')

    return df['GPA'].mean()

def get_average_of_sleep_hours_per_day():
    life_style = list(student_collection.find({}, {'life_style': 1, '_id': 0}))
    df = pd.DataFrame(map(lambda x: x['life_style'], life_style))
    df['Sleep_Hours_Per_Day'] = pd.to_numeric(df['Sleep_Hours_Per_Day'], errors='coerce')

    return df['Sleep_Hours_Per_Day'].mean()


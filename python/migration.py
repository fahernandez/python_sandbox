import pandas as pd
from sqlalchemy import create_engine
import os
def migration():

    conn = os.getenv("DATABASE_URL")
    engine = create_engine(conn, echo=False)
    df = pd.read_csv("../data/candidates.csv", sep=";")
    print(df.head())
    df = df.astype({
        'first_name': 'string',
        'Last_name': 'string',
        'email': 'string',
        'application_date': 'string',
        'country': 'string',
        'yoe': 'string',
        'seniority': 'string',
        'technology': 'string',
        'code_challenge_score': 'int',
        'technical_interview_score': 'int'
    })

    df.to_sql('candidates', con=engine, if_exists="append", index=False)
    print("values inserted")


if __name__ == '__main__':
    migration()


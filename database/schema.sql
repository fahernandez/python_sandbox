CREATE TABLE IF NOT EXISTS candidates (
    ID int NOT NULL PRIMARY KEY AUTO_INCREMENT,
    first_name varchar(255),
    Last_name varchar(255),
    email varchar(255),
    application_date date,
    country varchar(255),
    yoe varchar(255),
    seniority varchar(255),
    technology varchar(255),
    code_challenge_score int,
    technical_interview_score int
)

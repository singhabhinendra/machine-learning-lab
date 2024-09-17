# import necessary packages
import pandas
import psycopg2
from sqlalchemy import create_engine

# establish connection with the database
engine = create_engine(
	"jdbc:postgresql://localhost:5432/postgres")

# read the pandas dataframe
data = pandas.read_csv("path to dataset")

# connect the pandas dataframe with postgresql table
data.to_sql('loan_data', engine, if_exists='replace')

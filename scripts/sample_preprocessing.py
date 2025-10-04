
# sample_preprocessing.py
# Simple example script to load CSV and show basic stats
import pandas as pd
df = pd.read_csv('data/survey_sample.csv')
print(df.describe())

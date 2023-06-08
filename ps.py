from ydata_profiling import ProfileReport
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
path=r"C:\Users\SAQIB\Downloads\heart dataset.xlsx"
df=pd.read_csv(path)
# it will generate a report of dataset
profile=ProfileReport(df)
profile.to_file(output_file='anus.html')
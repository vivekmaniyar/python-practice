import pandas as pd

# reading csv file
# fd = pd.read_csv('sample4.csv',index_col=0)

# reading excel file
fd = pd.read_excel('sample2.xlsx',index_col=0)

print(fd.head())
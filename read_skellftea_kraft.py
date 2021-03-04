import pandas as pd
import xlrd

df = pd.read_excel('volymer-1.xlsx',engine='openpyxl')
print(df.head())

# xlrd.open_workbook_xls('volymer (5).xls')
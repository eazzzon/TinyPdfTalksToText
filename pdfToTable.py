from tabula import read_pdf
from tabulate import tabulate
import pandas as pd
import io, os
os.chdir(os.getcwd())

target_page = 12

file = read_pdf('yourpdfname.pdf',pages = target_page,
                         multiple_tables = True, stream = True)
table = tabulate(file)

df_table = pd.read_fwf(io.StringIO(table))

for col in df_table.columns:
    split_col = df_table[col].str.split(" ", n = 1, expand = True)[1]
    df_table[col] = split_col
    
df_table.to_excel("table.xlsx")

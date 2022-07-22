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

df_table.to_excel("table.xlsx")

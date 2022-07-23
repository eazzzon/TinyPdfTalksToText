from tabula import read_pdf
from tabulate import tabulate
import pandas as pd
import io, os
os.chdir(os.getcwd())

def colTofloat(df_col):
    """
    convert dataframe from string to float and escape TypeError from type like float
    """
    col_array = []
    for idx, ele in enumerate(df_col):
    
        try: 
            col_array.append(float(ele))
        except:
            col_array.append(ele)

    return col_array

# read your desire page of the table
target_page = 12

file = read_pdf('yourpdfname.pdf',pages = target_page,
                         multiple_tables = True, stream = True)
table = tabulate(file)

df_table = pd.read_fwf(io.StringIO(table))

# seperate dataframe by multi whitespace, convert string to float for data
for col in df_table.columns:
    split_col = df_table[col].str.split(" +", n = 1, expand = True)[1]
    df_table[col] = colTofloat(split_col)

df_table.to_excel("table.xlsx")

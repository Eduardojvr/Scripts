import csv
import pandas as pd
import string

print("Inicio")

df = pd.read_csv('../Boleto2023.csv')

data = df.to_dict(orient='records')

columns = df.columns.tolist()

i = 0
with open('arquivo.txt', 'w') as arquivo:
    for row in data:
        print(row)
        values = [str(value).replace("'", "") for value in row.values()]
        if(i == 0):
            sql = f"INSERT INTO BOLETO VALUES ({', '.join(['`'+(val)+'`' for val in values])}),\n"
            sql = sql.replace('`', "'")
        else:
            sql = f"({', '.join(['`'+(val)+'`' for val in values])}),\n"
            sql = sql.replace('`', "'")
    
        i+=1
        arquivo.write(sql)



print("Fim")


import pandas as pd #pip instal pandas
import os

data_file_folder = "C:\\Users\\evanh\\Documents\\EcelSheets"

df = []
for file in os.listdir(data_file_folder):
    if file.endswith('.xlsx'):
        print('Loading File {0}...'.format(file))
        df.append(pd.read_excel(os.path.join(data_file_folder,file), sheet_name='Sheet1'))


df_master = pd.concat(df,axis=0)
df_master.to_excel('C:\\Users\\evanh\\Documents\\EcelSheets\\masterfile.xlsx', index=False)
import pandas as pd

data_file_folder = "C:\\Users\\evanh\\Documents\\EcelSheets"
dataframe1 = pd.read_excel(data_file_folder + '\\' + 'Workbook1' + '.xlsx')
dataframe2 = pd.read_excel(data_file_folder + '\\' + 'Workbook2' + '.xlsx')
master_file_name = 'masterfile'

df_master = pd.merge_ordered(dataframe1,dataframe2,on='Product',fill_method='ffill').fillna(0)

df_master.to_excel('C:\\Users\\evanh\\Documents\\EcelSheets\\'+ master_file_name +'.xlsx', index=False)
print(dataframe1)
print(dataframe2)
print(df_master)
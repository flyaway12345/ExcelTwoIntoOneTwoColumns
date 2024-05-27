import pandas as pd
#paste your path here, make sure to have double backslashes
#EX: data_file_folder = "C:\\Users\\evanh\\Documents\\EcelSheets"
data_file_folder = "C:\\Users\\evanh\\Documents\\EcelSheets"
#Paste THe Name Of Your First Workbook without the .xlsx extesnion 
workbook_one_name = "Workbook1"
#Paste THe Name Of Your Second Workbook without the .xlsx extesnion 
workbook_two_name = "Workbook2"

#Output File Name
master_file_name = 'masterfile'

#Gets Data From Workbooks
dataframe1 = pd.read_excel(data_file_folder + '\\' + workbook_one_name + '.xlsx')
dataframe2 = pd.read_excel(data_file_folder + '\\' + workbook_two_name + '.xlsx')

#Gets Column Names
column_one_name = dataframe1.columns.array[0]
column_two_name = dataframe1.columns.array[1]

#Merges Workbooks
df_master = pd.merge_ordered(dataframe1,dataframe2,on=column_one_name,fill_method='ffill').fillna(0) #fillna(0) replaces NaN Values With Zero

#Deletes Old Column Data
del df_master[column_two_name + '_x']

#Formats Column B Name To Match Original
column_two_name_temp = column_two_name + "_y"
df_master.rename(columns={column_two_name_temp: column_two_name},inplace=True)

#Create New Workbook Using Compiled Data
df_master.to_excel('C:\\Users\\evanh\\Documents\\EcelSheets\\'+ master_file_name +'.xlsx', index=False)

#Comapres Changes In console
# print(dataframe1)
# print(dataframe2)
print(df_master)
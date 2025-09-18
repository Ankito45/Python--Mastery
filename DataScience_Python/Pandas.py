# PANDAS -> Stands for Python Data Analysis used for data manipulation and Analysis
# PANDAS -> Mainly resolve around two primary data Structure - Series(1D) & DataFrame(2D)
# methods like .dropna() and .fillna() to handle missing values seamlessly
# Helps in Data removal of duplicates and fix inconsistences , Filter, sort and Modify data along with representing in Graphically

# Pandas DataFrame is 2D table-like structure where data in arranged in rows and columns
# Data -> Actual values in the table.
# Rows -> Labels that identify each row.
# Columns -> Labels that define each data category.
import pandas as pd
import numpy as np
lst = ['Geek','For','Geeks','is','Portal','For','Geeks'] # Created using a list 
df = pd.DataFrame(lst)
print(df)
data = {'Name':['Tom', 'nick', 'krish', 'jack'],
        'Age':[20, 21, 19, 18]} # created using a dictionary 
print(data)
da = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) # Creating a dataframe of the numpy array
dp = pd.DataFrame(da, columns=['A', 'B', 'C'])
print(dp)

# This is called as Column selection
data1 = {'Name':['Jai', 'Prince', 'Gaurav', 'Anuj'],
        'Age':[27, 24, 22, 32],
        'Address':['Delhi', 'Kanpur', 'Allahabad', 'Kanu'],
        'Qualification':['Msc', 'MA', 'MCA', 'Phd']}
df = pd.DataFrame(data1)
print(df[['Name', 'Qualification']])
# Row selection pandas provide a unique method DataFrame.loc[] which is used for label-based selection
import os
os.chdir(r"D:\PYTHON\DataScience_Python") # Command to change the current working directory 
data2 = pd.read_csv("nba.csv",index_col="Name")
# Also this method allows to Indexing a DataFrame using .loc[]
first = data2.loc["Avery Bradley"]
second = data2.loc["R.J. Hunter"]
print(first,"\n\n\n", second)

# drop() method. Columns is deleted by dropping columns with column names.
data3 = pd.read_csv("nba.csv", index_col ="Name")
# data3.drop(["Team", "Weight"], axis = 1, inplace = True) # dropping passed columns
print(data3)

# Indexing and Selecting Data in Pandas DataFrame also -> Subset Selection in Pandas
# Indexing in pandas means simply selecting particular rows and columns of data from a DataFrame.
# Selecting all rows and some columns.
# Selecting some rows and all columns.
# Selecting a specific subset of rows and columns.
data4 = pd.read_csv("nba.csv", index_col ="Name")
print(data4["Age"]) # Indexing a Dataframe using indexing operator [] 
# Indexing through iloc() method ->allows us to select data based on integer position. Unlike .loc[] (which uses labels) 
data5 = pd.read_csv("nba.csv",index_col = "Name")
print(data5.iloc[3])  # .iloc[] requires us to specify row and column positions as integers (0-based indexing).


# Pandas one of the major feature is to help handle/work with missing values
# isnull() -> It returns True for NaN (missing) values and False otherwise.
# notnull() -> It returns the opposite, True for non-missing values and False for NaN values.
dict = {'First Score':[100, 90, np.nan, 95],
        'Second Score': [30, 45, 56, np.nan],
        'Third Score':[np.nan, 40, 80, 98]}
df1 = pd.DataFrame(dict)
print(df1.isnull())
# To full these missing/null values using  fillna(), replace() and interpolate()
# fillna() -> Specifically designed to fill missing values (NaN) in a Series or DataFrame.
# replace() -> Replaces specific values in a Series or DataFrame with new values. This can be any value, not just NaN
# interpolate() ->  Fills missing values (NaN) by estimating them based on surrounding valid data points. Primarily used for numerical data.
dict1 = {'First Score':[100, 90, np.nan, 95],
        'Second Score': [30, 45, 56, np.nan],
        'Third Score':[np.nan, 40, 80, 98]}
df2 = pd.DataFrame(dict1)
print(df2.fillna(0))
# dropna() -> is flexible which allows us to drop rows or columns depending on the configuration.
print(df2.dropna()) # drop rows with at least one Nan value (Null value). and prints the rows which has all the values


# ------------Accessing and modifying Index-----------------
data6 = {'Name': ['John', 'Alice', 'Bob', 'Eve', 'Charlie'],
        'Age': [25, 30, 22, 35, 28],
        'Gender': ['Male', 'Female', 'Male', 'Female', 'Male'],
        'Salary': [50000, 55000, 40000, 70000, 48000]}
dF = pd.DataFrame(data6)
print(dF.index) # Accessing the index
df_with_index = dF.set_index('Name')
print(df_with_index) # Setting a custom index such as 'Name'
df_reset = dF.reset_index() # Reset the index back to the default integer index
print(df_reset)
row = dF.loc[1]
print(row)
subset = dF.loc[0:2, ['Name', 'Age']] # Accessing the multiple rows and columns
print(subset)
filtered_data = dF[dF['Age'] > 25] # Accessing the rows on the basis of conditions
print(filtered_data)
salary_at_index_2 = dF.at[2, 'Salary'] # Access the 'Salary' of the row with label 2
print(salary_at_index_2)
data7 = pd.read_csv("nba.csv", index_col="Name") # Selecting a Single Column
print("Dataset")
print(data7.head(5))
first = data7["Age"]
print("\nSingle Column selected from Dataset")
print(first.head(5))
first1 = data7[["Age", "College", "Salary"]] # Selecting Multiple Columns
print("\nMultiple Columns selected from Dataset")
print(first1.head(5))
all_rows_specific_columns = data7.loc[:, ["Team", "Position", "Salary"]] # Selecting All Rows and Specific Columns
print(all_rows_specific_columns)
rows = data7.iloc[[3, 5, 7]] # We can select multiple rows by passing a list of integer positions using iloc[]
print(rows)
player_list = [['M.S.Dhoni', 36, 75, 5428000],['A.B.D Villers', 38, 74, 3428000],
               ['V.Kohli', 31, 70, 8428000],
               ['S.Smith', 34, 80, 4428000],
               ['C.Gayle', 40, 100, 4528000],
               ['J.Root', 33, 72, 7028000],
               ['K.Peterson', 42, 85, 2528000]]
Df = pd.DataFrame(player_list, columns=['Name', 'Age', 'Weight', 'Salary'])
# df.set_index('Name', inplace=True) # Slicing the rows using the iloc[]
# custom = df.loc['A.B.D Villers':'S.Smith']
df1 = Df.iloc[0:4] # Slicing Rows in dataframe
print(df1)
df2 = Df.iloc[:, 0:2] # Slicing columns in dataframe
print(df2)
data8 = Df[Df['Age'] > 35].iloc[:, :] # using boolean Conditions in Data Frame
print("\nFiltered Data based on Age > 35:\n", data8) 


# -----------------Filter Pandas Dataframe with multiple conditions-----------------
dataFrame = pd.DataFrame({'Name': [' RACHEL ', ' MONICA ', ' PHOEBE ','  ROSS  ', 'CHANDLER', ' JOEY '],               
'Age': [30, 35, 37, 33, 34, 30],'Salary': [100000, 93000, 88000, 120000, 94000, 95000],
'JOB': ['DESIGNER', 'CHEF', 'MASUS', 'PALENTOLOGY','IT', 'ARTIST']})
# Filtering the Pandas DataFrame with the multiple conditions using the loc[] function which works for columns and indexes
print(dataFrame.loc[(dataFrame['Salary']>=100000) & (dataFrame['Age']< 40) & (dataFrame['JOB'].str.startswith('D')),['Name','JOB']])
# Filtering the data using the numpy
filtered_values = np.where((dataFrame['Salary']>=100000) & (dataFrame['Age']< 40) & (dataFrame['JOB'].str.startswith('D')))
print(filtered_values)
print(dataFrame.loc[filtered_values])
# Filtering the dataFrame using the query 
print(dataFrame.query('Salary <= 100000 & Age < 40 & JOB.str.startswith("C").values'))
# "eval" & "query" works only with columns
print(dataFrame[dataFrame.eval("Salary <=100000 & (Age <40) & JOB.str.startswith('A').values")])


# ----------------Pandas ,Merging, Joining and Concatenating-----------------
# Concatenating the dataFrame using the .concat() function 
# Main Purpose of concat() ->  Stacking/appending along an axis
dataF = {'Name':['Jai','Prince','Gaurav','Anuj'],
         'Age':[27, 24, 22, 32],'Address':['Nagpur','Kanpur','Allahabad','Kannuaj'],
         'Qualification':['Msc','MA','Mtech','Phd'],'Mobile No': [97, 91, 58, 76]}
dataF1 = {'Name': ['Gaurav', 'Anuj', 'Dhiraj', 'Hitesh'],
         'Age': [22, 14, 12, 52],'Address': [ 'Allahabad', 'Nagpur', 'Kanpur', 'Kannuaj'],
         'Qualification': ['Mtech', 'B.A', 'Bcom', 'B.hons'],'Salary': [1000, 2000, 3000, 4000]}
dF1 = pd.DataFrame(dataF, index=[0, 1, 2, 3])
dF2 = pd.DataFrame(dataF1, index=[4, 5, 6, 7])
print(pd.concat([dF1, dF2]))
# Concatenating DataFrames by Setting Logic on Axes which has all the common values
res2 = pd.concat([dF1, dF2], axis=1, join='inner')
# Concatenating DataFrame with group keys
res = pd.concat(([dF1,dF2]), keys=['x', 'y'])
# Concatenating dataframes and series with the help of columns
data9 = {'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'],
        'Age':[27, 24, 22, 32],
        'Address':['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj'],
        'Qualification':['Msc', 'MA', 'MCA', 'Phd']}
dF3 = pd.DataFrame(data9,index=[0, 1, 2, 3])
s1 = pd.Series([1000, 2000, 3000, 4000], name='Salary')
print(pd.concat([dF3, s1], axis=1))

#----- Merging in DataFrame is like merging in SQL only which includes inner, full outer, left outer, right outer----
# Main Purpose of merge() -> Combining based on common values in columns/indices and also using the Keys
data11 = {'key': ['K0', 'K1', 'K2', 'K3'], 'key1': ['K0', 'K1', 'K0', 'K1'],
        'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'],'Age':[27, 24, 22, 32],}
data10 = {'key': ['K0', 'K1', 'K2', 'K3'],'key1': ['K0', 'K0', 'K0', 'K0'],
        'Address':['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj'],'Qualification':['Btech', 'B.A', 'Bcom', 'B.hons']}
DF = pd.DataFrame(data11)
DF1 = pd.DataFrame(data10)
print(pd.merge(DF, DF1, on='key')) # Merging DataFrames Using One Key
print(pd.merge(DF,DF1, on=['key','key1'])) # Now we merge dataframe using multiple keys.
# 'left' in order to use keys from left frame only -> left outer join
print(pd.merge(DF, DF1, how='left', on=['key', 'key1']))
# 'right' in order to use keys from right frame only -> right outer join
print(pd.merge(DF,DF1, how='right', on=['key', 'key1']))
# 'inner' in order to use keys intersection from both frames -> inner join
print(pd.merge(DF, DF1, how='inner', on=['key', 'key1']))
# 'outer' in order to use keys union of both the frames -> full outer join
print(pd.merge(DF, DF1, how ='outer', on=['key', 'key1']))

# ---- Main Purpose of join() -> for combining data on a key column or an index
data12 = {'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'],'Age':[27, 24, 22, 32], 'key':['K0', 'K1', 'K2', 'K3']}
data13 = {'Address':['Allahabad', 'Kannuaj', 'Allahabad', 'Kannuaj'],
          'Qualification':['MCA', 'Phd', 'Bcom', 'B.hons']}
dataf = pd.DataFrame(data12)
dataf1 = pd.DataFrame(data13, index=['K0', 'K1', 'K2', 'K3'])
# print(dataf.join(dataf1, how='outer')) # the joining of the pandas dataframe using the how operator
# print(dataf.join(dataf1, on='key')) # joined using the on operator 
# Joining DataFrames with Different Index Levels (Multi-Index) like X0,X1,X2 and Y0,Y1,Y2
data14 = {'Name':['Jai', 'Princi', 'Gaurav'],
        'Age':[27, 24, 22]}
data15 = {'Address':['Allahabad', 'Kannuaj', 'Allahabad', 'Kanpur'],
        'Qualification':['MCA', 'Phd', 'Bcom', 'B.hons']}
dataf2 = pd.DataFrame(data14, index=pd.Index(['K0', 'K1', 'K2'], name='key'))
index = pd.MultiIndex.from_tuples([('K0', 'Y0'), ('K1', 'Y1'),('K2', 'Y2'), ('K2', 'Y3')],names=['key', 'Y'])
dataf3 = pd.DataFrame(data15, index= index)
print(dataf2.join(dataf3, how='inner'))


# ---- Sorting the values in Pandas DataFrame -------
# In Pandas we have -> .sort_values() the function that help in sorting the values using the column 
# by: Specifies the column to sort by.
# ascending: A boolean (True for ascending, False for descending).
# inplace: If True, the original DataFrame is modified otherwise a new sorted DataFrame is returned.
# na_position: Use 'first' to put NaNs at the top or 'last' (default) to place them at the end.
# ignore_index: If True, resets the index after sorting.
d = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],'Age': [25, 30, 35, 40],'Score': [85, 90, 95, 80]}
DF2 = pd.DataFrame(d)
print(DF2.sort_values(by=['Age','Score'], ascending=False, na_position="first"))
# sort_index() method in Pandas on the basis of indexes
print(DF2.sort_index())
# quicksort -  It selects a "pivot" element and partitions the dataset into two halves: 
# one with elements smaller than the pivot and the other with elements greater than the pivot.
print(DF2.sort_values(by='Age', kind='quicksort'))
# MergeSort - Divides the dataset into smaller subarrays, sorts them and then merges them back together in sorted order.
print(DF2.sort_values(by='Age',kind='mergesort'))
# Heapsort - sorting algorithm that builds a heap data structure to systematically extract the largest or smallest element and reorder the dataset.
print(DF2.sort_values(by='Age',kind='heapsort'))


# ---- Pivot Tables using Pandas in Python -------
df3 = pd.DataFrame({'Product': ['Carrots', 'Broccoli', 'Banana', 'Banana','Beans', 'Orange', 'Broccoli', 'Banana'],
                    'Category': ['Vegetable', 'Vegetable', 'Fruit', 'Fruit','Vegetable', 'Fruit', 'Vegetable', 'Fruit'],
                    'Quantity': [8, 5, 3, 4, 5, 9, 11, 8],
                    'Amount': [270,239,617,384,626,610,62,90]})
# here according to the question given the value is like the total sales,mean,median,minimum sale
pivot = df3.pivot_table(index=['Product','Category'],values=['Amount'],aggfunc='sum')
print(pivot)
# Now calculating the next pivot table as mean,median and minimum sales by category
# here using the aggfunc = mean,sum,min,max,median
pivot1 = df3.pivot_table(index=['Category'],values=['Amount'],aggfunc={'mean','median','min','max'})
print(pivot1)
# Now calculating the next pivot table as mean,median and minimum sales by Product
pivot2 = df3.pivot_table(index=['Product'],values=['Amount'],aggfunc={'mean','min','max','median'})
print(pivot2)

# SERIES in Python means a 1D ARRAY that can hold any type of data
df4 = np.array(['g', 'e', 'e', 'k', 's'])
print(pd.Series(df4)) # Created a series from a list
data_dict = {'Geeks': 10, 'for': 20, 'geeks': 30} # Created a series from a Dictionary
# Created a Series from list Comprehension
ser = pd.Series(range(1,20,3), index=[x for x in 'abcdefg'])
print(ser.head(5)) # Retrieving the first 5 elements of the series
print(ser.iloc[:3]) # Retrieving the first three character by using the iloc[] method but we can't access the values like we do in array or list in python


# ----------- Binary Operation in Pandas Like Addition,Subtraction, Multiplication and Division -----------
s1 = pd.Series([10, 20, 30], index=['a', 'b', 'c'])
s2 = pd.Series([1, 2, 3], index=['a', 'b', 'c'])
print(s1+s2) # Addition of the the two series
print(s1 == s2) # Comparing the two series using the equals operator
print(s1*s2) # Multiplication of series
print(s1-s2) # Subtraction of the two series
print(s1>s2) # Checking whether the values in series1 is greater than the values in the series2
s3 = pd.Series([True,False,True],index=['a','b','c'])
s4 = pd.Series([False,True,True],index=['a','b','c'])
print(s3 & s4)
print(s3 | s4)
print(s3 ^ s4)

# ---- called as Modifying Index in pandas series -----
# If the SERIES doesn't have any kin dof index then the default index count starts from 0 
series = pd.Series(['New York', 'Chicago', 'Toronto', 'Lisbon'])
series.index = ['City 1', 'City 1', 'City 3', 'City 3'] 
print(series)


# --------- Data Cleaning in Pandas ---------
# Means handling the missing data,values, duplicates
# Handling the missing values by isnull() -. return 'True' if the value is not there and 'False' when value is there 
d = pd.DataFrame({'First Score': [100, 90, np.nan, 95],'Second Score': [30, 45, 56, np.nan],
                  'Third Score': [np.nan, 40, 80, 98]},index=[1,2,3,4])
print(d.isnull())
# isna() -> is almost similar to the isnull() function which handles the missing values
# notnull() -> returns a DataFrame with Boolean values where True indicates non-missing (valid) data and False fro missing values
# This function is useful when we want to focus only on the rows that have valid, non-missing values.
# Now filtering the same data based of missing values on a large dataset 
d1 = pd.read_csv("employees.csv")
bool_series = pd.isnull(d1["Gender"])
print(d1[bool_series])
non_bool = pd.notnull(d1["Gender"])
print(d1[non_bool])

# Handling or filling or replacing the missing values
# fillna() -> used to replace only missing values (NaN) with a given value. Lets see various example for this.
# the fillna() function sub isna() Returns True for NaN, False for non-NaN
print(d.fillna(0))
#  pad method is used to fill missing values with the previous value. -> also called forward filling
print(d.fillna(method='pad'))
# bfill method is used to fill it with the next value.
print(d.fillna(method='bfill'))
# fill all null values in Gender column with "No Gender"
d1["Gender"].fillna("No Gender",inplace=True)
print(d1[10:25])
# replace() function -> to replace NaN values with a specific value.
# replace() -> works on any value (including strings, numbers, regex)
dat = pd.read_csv("employees.csv")
# dat.replace(to_replace=np.nan, value=-99) # this is not working reason blank != blank
dat.replace({np.nan: -99}, inplace=True) # this command will change every missing value to the value assigned to 
# df.replace({"Age": {np.nan: 99},"Salary": {np.nan: -1}}, inplace=True)  # change the value for specific column
print(dat[10:25])   
# interpolate() -> in Pandas is used to fill missing values (NaN) with estimated values, based on different mathematical methods.    
# dropna() -> removes rows that contain at least one missing value.
# drop rows where all values are missing using dropna(how='all').
# remove columns that contain at least one missing value we use dropna(axis=1).
dict2 = pd.DataFrame({'First Score': [100, 90, np.nan, 95],'Second Score': [30, np.nan, 45, 56],
        'Third Score': [52, 40, 80, 98],'Fourth Score': [np.nan, np.nan, np.nan, 65]})
print(dict2.dropna())
print(dict2.dropna(axis=1))
nd = d1.dropna(axis=0, how='any')
print("Old data frame length:", len(d1))
print("New data frame length:", len(nd))
print("Rows with at least one missing value:", (len(d1) - len(nd)))
# difference is 101 which clearly states that the these rows which had at least 1 Null value in any column
import pandas as pd

file = r'D:\Yash\Documents\Coding\CSV File\students.csv'
df = pd.read_csv(file)

# to chack the row and column of the data frame
df.shape

# to chech the column names of the data frame
df.columns

# to check the data types of each column in the data frame
df.info()

# to check the summary statistics of the numerical columns in the data frame
df.describe()

# to check the number of duplicate rows in the data frame
df.duplicated().sum()

# Average marks of students
df['exam_score'].mean()

# Highest marks of students
df['exam_score'].max()

# Lowest marks of students
df['exam_score'].min()

# Average attendence
df['attendance_percent'].mean()

# Lowest attendence
df['attendance_percent'].min()

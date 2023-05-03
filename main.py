import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
print('setup complete')

#load the dataset and check the first five rows
# df = pd.read_csv(r'https://raw.githubusercontent.com/GauravGurv/Practice_Dataset/f0defb1b1ec97b4948e12c1ba16d8f1780842261/ds_salaries.csv?token=GHSAT0AAAAAACB5ZS7K2NC3BE6NRF454R7WZCRBW2Q')
df = pd.read_csv("D:\Data Science\DS_Project\salaries\dataset\ds_salaries.csv")
print(df.head(5))

#Total Numbers of raw and columns
print(df.shape)

# We can remove the salary_currency and company location columns and salary_usd in enough for EDA
df.drop(['salary_currency','company_location'],axis=1,inplace=True)
print(df.head(3))

# we have to remove duplicate from
print(df.drop_duplicates())

# for finding duplicates in book
print(df.duplicated().sum())

# in previous command we have removed a duplicate and in this shape command column and rows  are same
print(df.shape)
df.drop_duplicates(inplace=True)
print(df.shape)

#-------------------Descriptives of data------------------------------
# using skimpy library
print(df.info())
print(df.describe())
print(df.dtypes)
print(df.isnull().sum())


#-------------------EDA AND DATA VISUALIZATION------------------------------
print(df['experience_level'].unique())
'''
Some details
SE : SENIOR_LEVEL           MI : MEDIUM_LEVEL           EN : ENTRY_LEVEL            EX : EXECUTIVE_LEVEL
FT : FULL_TIME              CT : CONTRACT               FL : FREE_LANCE             PT : PART_TIME
'''

#number of jobs based on experience level
print(df['experience_level'].value_counts())

jobs=df['job_title'].value_counts()
print(jobs)

print(df.nunique())

#-----------<AxesSubplot: title={'center': 'Salary for experience'}, xlabel='experience_level', ylabel='count'>---------------
plt.title("Salary for experience")
plt.xlabel('Experiance_level')
plt.ylabel('Salary')
sns.countplot(data=df,x="experience_level")
plt.show()

#---------------------boxplot (showing salary)----------------------------
#This box plot is saying that minimum salary in data_scinece field is 5132_dollars and maximum salary is 450k_dollars
fig=px.box(df['salary_in_usd'])
fig.show()


#-------------------Lines plot---------------------------------
#people who are hired for full time get more salary then other peole working and the below graph is showing us
# that in 2023 companies are hiring mostly for full time
plt.title("Salary for time")
sns.lineplot(x='employment_type', y='salary_in_usd', data=df, err_style='bars',ci=68)
plt.show()

#-------------------Point plot---------------------------------
sns.pointplot(x='employment_type', y='work_year', data=df, ci='sd')
plt.show()


#-------------------understand with violin plot---------------------------------
fig=px.violin(df,x='employment_type',y='salary_in_usd',box=True)
fig.show()

'''
The default value of numeric_only in DataFrame.corr is deprecated. In a future version, it will default to False. 
Select only valid columns or specify the value of numeric_only to silence this warning.
'''
# df_corr=df.corr()
# print(df_corr)

'''
There is a positive correlation (0.24) between work_year and salary_in_usd, 
which suggests that people with more years of work experience tend to have higher salaries.

There is a negative correlation (-0.22) between work_year and remote_ratio, 
which suggests that people with more years of work experience tend to work less remotely.

There is a weak negative correlation (-0.08) between salary_in_usd and remote_ratio, 
which suggests that people who work remotely do not necessarily have lower salaries.
'''
# print(sns.heatmap(df_corr, annot=True))


fig=px.sunburst(df,path=['job_title','employment_type','experience_level'],values='salary_in_usd')
fig.show()


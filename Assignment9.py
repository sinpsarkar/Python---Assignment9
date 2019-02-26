# =============================================================================
# Read the dataset from the below link:
# 
# https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/06_Stats/US_Baby_Names/US_Baby_Names_right.csv
# =============================================================================

import pandas as pd
import numpy as np

File_Link='https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/06_Stats/US_Baby_Names/US_Baby_Names_right.csv'
df_US_Baby_Namesdata=pd.read_csv(File_Link)

df_US_Baby_Namesdata.head(2)

# =============================================================================
# Question 1: Delete unnamed columns
# =============================================================================
df_US_Baby_Namesdata.drop(['Unnamed: 0'],axis=1, inplace=True)


print("New Data: \n")
df_US_Baby_Namesdata


# =============================================================================
# Question 2: Show the distribution of male and female
# =============================================================================


print("Distribution of Male & Female: \n")
round(df_US_Baby_Namesdata['Gender'].value_counts(normalize=True)*100,2)

# =============================================================================
# Question 3: Show the top 5 most preferred names
# =============================================================================

print("Top 5 preferred names: \n",
      df_US_Baby_Namesdata[["Name","Count"]].groupby('Name').sum().sort_values("Count",ascending=0).head(5))



# =============================================================================
# Question 4: What is the median name occurence in the dataset
# =============================================================================

df_US_Baby_Namesdata_median_Name=df_US_Baby_Namesdata[["Name","Count"]].groupby('Name').sum()

print("The median name occurence in the dataset: \n",
      df_US_Baby_Namesdata_median_Name[df_US_Baby_Namesdata_median_Name['Count'] == df_US_Baby_Namesdata_median_Name['Count'].median()])

# =============================================================================
# Question 5: Distribution of male and female born count by states
# =============================================================================


df_US_Baby_Namesdata_Gender_Distribution=df_US_Baby_Namesdata[['State','Gender','Count']].set_index(['State','Gender'])

print("Distribution of male and female born count by state: \n",
      df_US_Baby_Namesdata_Gender_Distribution.groupby(['State','Gender']).sum())
# 15.Analyse various school outcomes in Tennessee using pandas. Suppose you are a public school administrator. Some
# schools in your state of Tennessee are performing below average academically. Your superintendent, under pressure
# from frustrated parents and voters, approached you with the task of understanding why these schools are
# under-performing. To improve school performance, you need to learn more about these schools and their students,
# just as a business needs to understand its own strengths and weaknesses and its customers. Though you is eager to
# build an impressive explanatory model, you know the importance of conducting preliminary research to prevent
# possible pitfalls or blind spots. Thus, you engages in a thorough exploratory analysis, which includes: a lit
# review, data collection, descriptive and inferential statistics, and data visualization. Phase 1 - Data Collection
# Here is a data of every public school in middle Tennessee. The data also includes various demographic,
# school faculty, and income variables. You need to convert the data into useful information. • Read the data in
# pandas data frame • Describe the data to find more details

import pandas as pd

# df=pd.read_csv('/Users/MspDx/IdeaProjects/EdurekaAssignment/NumPy and Pandas/CSV/middle_tn_schools.csv')
df=pd.read_csv('C:\\Users\\pmani\\IdeaProjects\\EdurekaAssignments\\NumPy and Pandas\\CSV\\middle_tn_schools.csv')
print(df.describe())


# Phase 2 - Group data by school ratings
# Chooses indicators that describe the student body (for example, reduced_lunch) or
# school administration (stu_teach_ratio) hoping they will
# explain school_rating. reduced_lunch is a variable measuring the average percentage
# of students per school enrolled in a federal program that provides lunches for students
#     from lower-income households. In short, reduced_lunch is a good proxy for household
#     income.

# © B r a i n 4 c e E d u c a t i o n S o l u t i o n s P v t . L t d Page 3
# Isolates ‘reduced_lunch’ and groups the data by ‘school_rating’ using pandas groupby
# method and then uses describe on the re-shaped data

a=df.groupby(['school_rating','reduced_lunch'])
b=df.groupby('school_rating')['reduced_lunch'].count()
print(a.describe())
print(b)
print(b.describe())
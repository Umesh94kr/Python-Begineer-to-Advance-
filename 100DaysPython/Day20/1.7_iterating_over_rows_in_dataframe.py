import pandas as pd 

student_dict = {
    "student" : ['Andela', 'James', 'Lilly'],
    "marks" : [56, 78, 98]
}

student_dataframe = pd.DataFrame(student_dict)

# Loop through rows in dataframe 
for (index, row) in student_dataframe.iterrows():
    print(row.student) 
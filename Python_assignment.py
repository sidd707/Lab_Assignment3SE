import pandas as pd
df = pd.DataFrame({'Employee ID': ['161E90', '161F91', '161F99','171E20','171G30'],
                   'Name':['Raman','himadri','jaya','Tejas','Ajay'],
                   'Age': [41, 38, 51,30,45],
                   'Salary(PM)':[56000,67500,82100,55000,44000]})
print(df)
while True:
    print('''Enter the choice
    1. Employee ID
    2. Name
    3. Age
    4. Salary
    5. Exit''')
    choice = int(input())
    if choice==1:
        query = input("Enter the query to be Employee ID ")
        print(df[df["Employee ID"]==query])
    elif choice==2:
        query = input("Enter the query to be Employee ID ")
        print(df[df["Name"]==query])
    elif choice==3:
        query = input("Enter the query to be Employee ID ")
        print(df[df["Age"]==query])
    elif choice==4:
        query = input("Enter the query to be Employee ID ")
        print(df[df["Salary(PM)"]==query])
    else:
        break

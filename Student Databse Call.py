from Student_Databse_Call import *

print("Enter 1 for to execute database operations")
x = int(input())
while (x>0):
    print("Enter 1 for Insert")
    print("Enter 2 for Update")
    print("Enter 3 for Delete")
    print("Enter 4 for SelectAll")
    print("Enter 5 for SelectAllByOrder")
    print("Enter 6 for SelectById")
    x = int(input())
    if x == 1:
        print("------------------ Enter the values to insert ----------------------")
        print("Enter Id, Name, Stream, Address"))
        id = input()
        name = input()
        stream = input()
        address = input()
        t=(id,name,stream,address)
        insertData(t)
    elif x == 4:
        print("----------------------------------------")
        for i in selectAllData():
            print(i)
        print("----------------------------------------")
        

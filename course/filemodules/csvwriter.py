import csv

list1 = list()
"""
def adder(user,course,score,start,end):
    list2 = [user,course,score,start,end]
    list1.append(list2)
"""

def csvwriter(user,course,grade,start_time,end_time):
    with open("./course/csvfiles/students.csv","a") as f:
        writer = csv.writer(f)
        list2 = [user,course,grade,start_time,end_time]
        list1.append(list2)
        writer.writerows(list1)
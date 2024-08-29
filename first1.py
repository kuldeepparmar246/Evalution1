
def pmark_present(arr,student,day):
    if day not in arr:
        arr[day]=list()
    arr[day].append(student)
    print(arr[day])
    return arr

def remove_student(arr,student,day):
    if day not in arr:
        return arr
    if student in arr[day]:
        arr[day].remove(student)
    return arr

def is_present(arr,student,day):
    if day not in arr:
        arr[day]=list()
    if student in arr[day]:
        return True
    return False


def display_atendance(arr,day):
    print("Student Present")
    print('\n')
    print(arr[day])



arr = dict()
while True:
    print("1 for add student")
    print("2 for remove student")
    print("3 for check student presence")
    print("4 for display attendance ")
    print("5 for restart")
    print("6 for exit")
    x=int(input("Enter Number : "))
    if x==5:
        continue
    elif x==6:
        break
    elif x==1:
        day=str(input("day of Attendence : "))
        student=str(input("Student Name : "))
        arr=pmark_present(arr,student,day)
    elif x==2:
        day=str(input("day of Attendance : "))
        student=str(input("student name : "))
        arr=remove_student(arr,student,day)
    elif x==3:
        day=str(input("day of Attendance : "))
        student=str(input("Student name : "))
        print(is_present(arr,student,day))
    elif x==4:
        day=str(input("day of Attendance : "))
        display_atendance(arr,day)
                          
    

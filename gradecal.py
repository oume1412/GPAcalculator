import pandas as pd
import math
from tabulate import tabulate

# Grade table.
gradeTable = {'A': 4,
              'B+': 3.5,
              'B': 3,
              'C+': 2.5,
              'C': 2,
              'D+': 1.5,
              'D': 1,
              'F': 0}

def calculate():
    # This method do Insert, Edit, Saving, Calculate GPA.

    df = pd.read_csv('GPA.csv')

    todo = input(''' | Insert(I) | Edit(E) | Save(S) | Calculate GPA(C) |
    Enter what do you want to do : ''')

    while True:
        if todo.upper() == 'C':  # Calculating GPA.
            credit = sum(df['หน่วยกิต'])
            each_credit = sum((df['คำนวณค่าเกรด'] * df['หน่วยกิต']) / credit)
            total_gpa = (math.floor(each_credit * 100) / 100)

            choice = input('''| Semester(S) | GPAX(G) |
Which grade you want to know? : ''')

            if choice.upper() == 'G':  # Calculating Accumulated grade point average.
                print('Your GPAX is : ', total_gpa)

            elif choice.upper() == 'S':  # Calculating Grade point average each semester.
                year = input('Enter a year : ')
                semester = input('Enter a semester : ')
                c = sum(df[df['ภาคการศึกษา'] == year + '/' + semester])
                semester = sum(c['หน่วยกิต'])
                semester_d = sum((c['คำนวณค่าเกรด'] * c['หน่วยกิต']) / semester)
                semester_gpa = (math.floor(semester_d * 100) / 100)
                print('Your grade for ', year, '/', semester, 'is : ', semester_gpa)

            else:
                print('Wrong input! Please try again!')

        elif todo.upper() == 'I':  # Insert data to table.
            subject_id = input('Enter your subject ID : ')
            subject_name = input('Enter your subject name : ').upper()
            year_semester = input('Enter Year/Semester : ')
            credits_i = int(input('Enter your credits : '))
            section = int(input('Enter your section : '))
            grade_letter = input('Enter your grade : ').upper()
            grade_num = gradeTable[grade_letter]
            subject = subject_id + ' ' + subject_name
            info = {'ชื่อวิชา': subject,
                    'ภาคการศึกษา': year_semester,
                    'หน่วยกิต': credits_i,
                    'ตอนเรียน': section,
                    'เกรด': grade_letter,
                    'คำนวณค่าเกรด': grade_num}
            df = df.append(info, ignore_index = True)
            print(df)

        elif todo.upper() == 'S':  # Saving data.
            df.to_csv('GPA.csv', encoding='utf-8', index=False)

        elif todo.upper() == 'E':  # Editing data.
            print(tabulate(df, headers='keys', tablefmt='psql'))
            while True:
                index = int(input("Enter row index : "))
                if index > len(df.index)-1:
                    print('Wrong index please insert again :')

                else:
                    column = input("Which column you want to update? : ")

                    if column == 'ชื่อวิชา':
                        subjectId = input('Enter your subject ID : ')
                        subjectName = input('Enter your subject name : ').upper()
                        df.loc[index, column] = subjectId + ' ' + subjectName

                    elif column == 'ภาคการศึกษา':
                        yearSemester = input('Enter Year/Semester : ')
                        df.loc[index, column] = yearSemester

                    elif column == 'หน่วยกิต':
                        credits = int(input('Enter your credits : '))
                        df.loc[index, column] = credits

                    elif column == 'ตอนเรียน':
                        section = int(input('Enter your section : '))
                        df.loc[index, column] = section

                    elif column == 'เกรด':
                        gradeLetter = input('Enter your grade : ').upper()
                        grade_num = gradeTable[gradeLetter]
                        df.loc[index, column] = gradeLetter
                        df.loc[index, 'คำนวณค่าเกรด'] = grade_num

                    else:
                        print('There is no column name', column, 'please try again')

                    option = input('Update more data? [y/n] : ')
                    if option == 'y':
                        pass
                    elif option == 'n':
                        break
                    else:
                        print('Wrong input!')

            print(tabulate(df, headers='keys', tablefmt='psql'))

        else:
            print('Wrong input! Please try again!')


        todo = input(''' | Insert(I) | Edit(E) | Save(S) | Calculate GPA(C) |
    Enter what do you want to do : ''')

calculate()

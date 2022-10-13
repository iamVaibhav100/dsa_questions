def gradingStudents(grades):
    for i in range(len(grades)):
        if grades[i] >= 38 and grades[i] % 5 > 2:
            grades[i] = -(-grades[i]//5)*5
    print('\n'.join(map(str, grades)))

if __name__ == '__main__':
    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)



def calculateGrade(students_marks):
    for ls in students_marks:
        total = sum(ls)
        tlen = len(ls) 
        avg = total/tlen
        if avg>=90:
            yield "A+"
        elif avg>=80 and avg<90:
            yield "A"
        elif avg>=70 and avg<80:
             yield "B"
        elif avg>=60 and avg<70:
             yield "C"
        elif avg>=50 and avg<60:
             yield "D"
        else:
             yield "F"

if __name__ == '__main__':
    students_marks_rows = int(input().strip())
    students_marks_columns = int(input().strip())

    students_marks = []

    for _ in range(students_marks_rows):
        students_marks.append(list(map(int, input().rstrip().split())))

    result = calculateGrade(students_marks)
    for i in result:
        print(i)
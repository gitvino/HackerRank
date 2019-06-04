
'''

Problem: Given a list of grades, roundup the grades,
> If the difference between the grade and the next multiple of 5 is less than 3, round  up grade to the next multiple of 5.
> If the value of grade is less than 38, no rounding occurs as the result will still be a failing grade.

URL: https://www.hackerrank.com/challenges/grading/problem

'''


'''
gradingStudents: 
    Input: List of grades
    Output: List of rounded grades. 

'''
def gradingStudents(grades):
    results = []
    for grade in grades:
        if grade >= 38:
            remainder = grade % 5
            if remainder > 2:
                rounded_grade = grade + (5 - remainder)
                if rounded_grade >= 40:
                    results.append(rounded_grade)
                else:
                    results.append(grade)
            else:
                results.append(grade)
        else:
            results.append(grade)
    return results

if __name__ == '__main__':
    n = int(input())
    grades = []
    for _ in range(n):
        grades.append(int(input()))
    results = gradingStudents(grades)
    for value in results:
        print(value)

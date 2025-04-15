score={
    "harry":81,
    "ron":78,
    "hermione":99,
    "draco":74,
    "neville":62
}

grades={}
for student in score:
    student_score=score[student]
    if student_score>90:
        grades[student]="Outstandding"
    elif(student_score>80):
        grades[student]="exceedds expectaions"
    elif(student_score>70):
        grades[student]="acceptable"
    else:
        grades[student]="fail"

print(grades)
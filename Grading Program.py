student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

student_grades={}

for keys in student_scores:
    k=student_scores[keys]
    if k>=91 and k<=100:
        student_grades[keys]="Outstanding"
    elif k>=81 and k<=90:
        student_grades[keys]="Exceeds Expectations"
    elif k>=71 and k<=80:
        student_grades[keys]="Acceptable" 
    else:
        student_grades[keys]="Fail"       

print(student_grades)

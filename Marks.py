marks = [55,64,75,80,65]

sum_of_marks=sum(marks)
number_of_subjects=len(marks)
average_mark=sum_of_marks / number_of_subjects

print "Your average mark is", average_mark

if average_mark >= 80:
    print"Grade A"
elif average_mark >= 60 and 80:
    print "Grade B"
elif average_mark >= 50 and 60:
    print "Grade C"
else:
    print "Grade F"




prelim = eval(input("Input Prelim Grade: "))
midterm = eval(input("Input Midterm Grade: "))
semi_final = eval(input("Input SemiFinal Grade: "))
final = eval(input("Input Final Grade: "))
quiz = eval(input("Input Quiz Grade: "))
project = eval(input("Input Project Grade: "))


prelim_g = prelim * .15
midterm_g = midterm * .15
semi_final_g = semi_final * .15
final_g = final * .15
quiz_g = quiz * .15
project_g = project * .15


final_grade = prelim_g + midterm_g + semi_final_g + final_g + quiz_g + project_g

if final_grade < 0 :
	print("Invalid grade")
elif final_grade > 100 :
	print("Invalid grade")
elif final_grade >= 75 : 
	print(f"Your prelim grade is {final_grade}.")
	print("Congrats! You passeed the course.")
else:
	print(f"Your prelim grade is {final_grade}.")
	print("Sorry, you failed the course.")






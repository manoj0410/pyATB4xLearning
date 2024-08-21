#Grade calculator
# Write a program that calcualtes and displays the letter grade
# for a given number score (e.g A,B,C,D or F)
#based on the following grading scale:
# A: 90-100
# B: 80-89
# C: 70-79
# D: 60-69
# F: 0-59

#Building Logic:
# input: Take input from user ---Score or Marks----int
# o/p: return string as per conditions.

score=int(input("Enter the score\n"))
if 100 >= score >= 90:
    print("Your grade is:", "A" )
elif 89 >= score >= 80:
    print("Your grade is",'B')
elif score <= 79 and score >= 70:
    print("Your grade is", 'C')
elif score <= 69 and score >= 60:
    print("Your grade is", 'D')
elif score > 100:
    print("You are superman!")
else:
    print("Your grade is", 'F')

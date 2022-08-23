
scores = []
number_of_students = int(input("Enter number of students: "))
the_score = 0
for list in range(0, number_of_students):
    student_scores = int(input(f"Input student for student {list + 1}: "))
    scores.append(student_scores)

highscore = 0

for score in range(0, number_of_students):
    if scores[score] > highscore:
        highscore = scores[score]

print(f"The high score is {highscore}")



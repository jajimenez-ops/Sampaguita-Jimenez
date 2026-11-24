#Johann Dominic Jimenez
#8 - Sampaguita

quizzes = []
for i in range(1,6):

    quiz_score = int(input("Enter a grade: "))
    quizzes.append(quiz_score)


print("QUIZ SCORE REPORT")
print(f"Number of quizzes: {len(quizzes)}")
print(f"Total score: {sum(quizzes)}")
print(f"Average score: {sum(quizzes)/len(quizzes)}")
print(f"Highest score: {max(quizzes)}")
print(f"Lowest score: {min(quizzes)}")
print(f"Ascending: {sorted(quizzes)}")
print(f"Descending:{sorted(quizzes, reverse = True) }")
print(f"Original: {quizzes}")


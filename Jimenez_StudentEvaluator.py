# Global Variables
student_name = ""
score1 = 0
score2 = 0
score3 = 0
average = 0
perf_level = ""

def display_header():
    #First local Variable
    print(f"STUDENT PERFORMANCE EVALUATOR")

def get_student_info():

    #The global keyword is to turn the local variables in the functions into global variables
    global student_name, score1, score2, score3
    student_name = input("Please enter your student name: ")
    score1 = int(input("Please enter your score 1: "))
    score2 = int(input("Please enter your score 2: "))
    score3 = int(input("Please enter your score 3: "))
def evaluate_performance():
    global average, perf_level

    #The 2nd Local Variable
    total_score = score1 + score2 + score3
    average = total_score / 3


    #Selection Structure to determine performance level

    if 90 <= average <= 100:
        perf_level = "Outstanding"
    elif 85 <= average < 90:
        perf_level = "Very Satisfactory"
    elif 80 <= average < 85:
        perf_level = "Satisfactory"
    elif 75 <= average < 80:
        perf_level = "Fairly Satisfactory"
    else:
        perf_level = "Needs Improvement"



def display_report():
    print(f"STUDENT PERFORMANCE REPORT")
    print(f"Student Name: {student_name}")
    print(f"Assessment Scores: {score1} , {score2} , {score3}")
    print(f"Average Score: {average}")
    print(f"Performance Level: {perf_level}")

#Execute the Main Program
display_header()
get_student_info()
evaluate_performance()
display_report()
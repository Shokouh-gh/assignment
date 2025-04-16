def save_grades():
    with open("grades.txt", "w") as file:
        for i in range(5): 
            grade = input(f"grade {i+1}: ")
            file.write(grade + "\n")  
save_grades()
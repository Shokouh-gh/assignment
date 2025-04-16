def calculate_average(filename):
    with open(filename, "r") as file:
        total = 0
        count = 0
        for line in file:
            grade = float(line.strip())
            total += grade
            count += 1
        if count > 0:
            average = total / count
            print("moadel:", average)
        else:
            print("nothing.")
calculate_average("grades.txt")
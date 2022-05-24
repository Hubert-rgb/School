import random

arr = []
for i in range(5):
    firstname = input()
    lastName = input()
    gradeArr = [random.randint(1,6) for j in range(10)]
    arr.append([firstname, lastName, gradeArr])
file1 = open("zad2Wyniki1.txt", "a")
for i in range(5):
    file1.write(arr[i][0] + " ")
    file1.write(arr[i][1] + " ")
    for j in range(10):
        file1.write(str(arr[i][2][j])+ " ")
    file1.write("\n")
file1.close()
file2 = open("zad2Wyniki2.txt", "a")
for i in range(5):
    sumGrade = 0
    avGrade = 0
    for j in range(10):
        sumGrade += arr[i][2][j]
    avGrade = sumGrade/10
    print(avGrade)
    file2.write(arr[i][0] + " " + arr[i][1] + " " + str(avGrade) + "\n")
file2.close()

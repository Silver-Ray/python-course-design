
import csv

matrix=list()

with open('random_numbers.csv','r',encoding='utf-8')as file:
    reader=csv.reader(file)
    for line in reader:
        matrix.append(line)

print(matrix)
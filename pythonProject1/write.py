import csv

matrix=list()

with open('random_numbers.csv','r',encoding='utf-8')as file:
    reader=csv.reader(file)
    for line in reader:
        matrix.append(line)



with open('new_file.csv',mode= 'w', newline='',encoding='utf-8') as file:
    writer=csv.writer(file)
    #写入标题行
    writer.writerow(['Column1', 'Column2', 'Column3', 'Column4', 'Column5'])

    #写入随机数矩阵的数据
    for row in matrix:
        writer.writerow(row)

print(f"CSV文件 已生成。")
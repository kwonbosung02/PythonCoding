
get_num = int(input())

array = []
Matrix = [[0]*19 for i in range(19)]
cnt = 0
for i in range(get_num):
    array.extend(input().replace("[","").replace("]","").split(','))

    array = [int (i) for i in array]
print(array)

for i in range(get_num):
    Matrix[array[2*i]][array[2*i + 1]] = 1
    
for i in range(19):
    print(str(Matrix[i]).replace("[","").replace("]",""))

        
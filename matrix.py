def add(m1, m2):
    if len(m1) == len(m2) and len(m1[0]) == len(m2[0]):
        res = []
        for x in range(len(m1)):
            row = []
            for y in range(len(m1[0])):
                row.append(m1[x][y] + m2[x][y])
            res.append(row)
        print("Addition Result:")
        for row in res:
            print(row)
    else:
        print("Matrix dimensions do not match for addition")

def mul(m1, m2):
    if len(m1[0]) == len(m2):
        res = []
        for i in range(len(m1)):
            row = []
            for j in range(len(m2[0])):
                row.append(0)  
            res.append(row) 

        for i in range(len(m1)):
            for j in range(len(m2[0])):
                for k in range(len(m2)):
                    res[i][j] += m1[i][k] * m2[k][j]
        print("Multiplication Result:")
        for row in res:
            print(row)
    else:
        print("Matrix dimensions do not match for multiplication")

def transpose(m):
    res = []
    for i in range(len(m[0])):
        row = []
        for j in range(len(m)):
            row.append(m[j][i])
        res.append(row)
    print("Transpose Result:")
    for row in res:
        print(row)
    
m1 = []
m2 = []

r1 = int(input("Enter total no. of rows of 1st matrix: "))
c1 = int(input("Enter total no. of columns of 1st matrix: "))
print("Enter the elements of 1st matrix: ")
for i in range(r1):
    row = []
    for j in range(c1):
        val = int(input(f"[{i}][{j}] -> "))
        row.append(val)
    m1.append(row)

r2 = int(input("Enter total no. of rows of 2nd matrix: "))
c2 = int(input("Enter total no. of columns of 2nd matrix: "))
print("Enter the elements of 2nd matrix: ")
for i in range(r2):
    row = []
    for j in range(c2):
        val = int(input(f"[{i}][{j}] -> "))
        row.append(val)
    m2.append(row)

add(m1, m2)

mul(m1, m2)

print("Transpose of 1st Matrix:")
transpose(m1)

print("Transpose of 2nd Matrix:")
transpose(m2)

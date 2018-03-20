width = 9
height = 7
column = []
for column_index in range(height):
    row = []
    for row_index in range(width):
        print(width/3 % (row_index+1))
        # row.append('#')
    column.append('#')
    # print(row)
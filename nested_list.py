list=[10,34,90,[45,78,-3],89]
print(len(list))
print(list[3])
print(list[4])
print(list[3][2])
print(list[-2])
print(list[len(list)-1])
print(list[3][:]) # slicing
print(list[3][0:2])
print(list[3][::2])

# CODING EXERCISE

row1=['4','5',"6"]
row2=['7','8','9']
row3=['10','11','12']
matrix=[row1,row2,row3]
print(f"{row1}\n{row2}\n{row3}\n")
position=input("Enter the position where you want to hide money:")
row_number=int(position[0])
column_number=int(position[1])
row_selected=matrix[row_number-1]
row_selected[column_number-1]="x"
print(f"{row1}\n{row2}\n32{row3}\n")




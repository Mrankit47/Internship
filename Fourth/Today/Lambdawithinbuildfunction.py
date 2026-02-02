number = [3,5,7,5,3,7]

double= list(map(lambda a:a*2,number))

print(double)


#exampl 2

num = [6,9,44,66,22,34,56]

odd = list(filter(lambda a : a%2 != 0,num))
even = list(filter(lambda a : a%2 == 0,num))

print("odd no : ", odd)
print("even no : ",even)
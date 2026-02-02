# Add 10 to each number in a list using lambda.

num = [3,6,4,1,7,9,7,90]

add = list(map(lambda a: a%2!=0,num))

print(add)
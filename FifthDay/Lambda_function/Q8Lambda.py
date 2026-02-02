#Find the length of each string in a list using lambda.

name = ['Ankit','anshita','ansh','tanvi','shikah','nandita']

length = list(map(lambda a : len(a),name))
print(length)
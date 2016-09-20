name='./ceshi.txt'
file= open(name, "a+")
line = file.readline()
file.write('\n abc')
file.close()

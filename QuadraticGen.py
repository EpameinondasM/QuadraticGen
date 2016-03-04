
from math import sqrt
from random import randint

number_of_equations = int(input("How many equations do you need?\n"))

file1 = open("Two.txt",'w+')
file2 = open("Double.txt",'w+')
file3 = open("NoRoots.txt",'w+')


def Deuterovathmia(a,b,c):
		global number_of_equations
		D = (b ** 2) - 4 * (a * c)
	
		if D > 0 and a != 0:
				x1 = (- b + sqrt(D)) / (2 * a)
				x2 = (- b - sqrt(D)) / (2 * a)
				valuex = 'x1 = {0} x2 = {1}'.format(x1,x2)
				write_to_file(a,b,c,file1,valuex)
				number_of_equations -= 1
		elif D == 0 and a != 0:
		
				x = - b / (2 * a)
				valuex = 'x = {0}'.format(x)
				write_to_file(a,b,c,file2,valuex)
				number_of_equations -= 1
		else:
				valuex = 0
				write_to_file(a,b,c,file3,valuex)
				number_of_equations -= 1
		

def write_to_file(a,b,c,file,valuex):
		valuea = 'a = {0} '.format(a)
		valueb = 'b = {0} '.format(b)
		valuec = 'c = {0}'.format(c)
		valuex = str(valuex)
		sa = str(valuea)
		sb = str(valueb)
		sc = str(valuec)
		file.write(sa)
		file.write(sb)
		file.write(sc)
		file.write('\n')
		file.write(valuex)
		file.write('\n')



def main():
	global number_of_equations
	for a in range(-10,10):
		for b in range(-10,10):
			for c in range (-10,10):
				Deuterovathmia(a,b,c)
				print (number_of_equations)
				if number_of_equations < 1:
					return 


main()					
file1.close()
file2.close()
file3.close()
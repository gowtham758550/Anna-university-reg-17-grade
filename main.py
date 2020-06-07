#author = <gowtham758550@gmail.com>
#Anna university regulation 2017 
#Minimum Internal Mark And External Mark To 
#Pass The Semester Regulation 2017
#Python code for give the minimum required 
#minimum external mark with the internal marks 

import math

#function to check that we can get a grade or not
def check(n):
	if n>=45 and n<=100:
		return n
	else:
		return 'na'

#function to find required external mark
def external_mark(internal_mark):
	o= math.ceil((100*(91 - internal_mark))/80)
	o = check(o)
	aplus = math.ceil((100*(81 - internal_mark))/80)
	aplus = check(aplus)
	a = math.ceil((100*(71 - internal_mark))/80)
	a = check(a)
	bplus = math.ceil((100*(61 - internal_mark))/80)
	bplus = check(bplus)
	if internal_mark >= 14:
		b = 45
	else:
		b = math.ceil((100*(50 - internal_mark))/80)
		b = check(b)
		
	print("\n\nInternal mark : ",internal_mark)
	print("____________________________________________")
	print("|     GRADE     |   Minimum mark required  |")
	print("____________________________________________")
	print("|       O       |            {}            |".format(o))
	print("____________________________________________")
	print("|       A+      |            {}            |".format(aplus))
	print("____________________________________________")
	print("|       A       |            {}            |".format(a))
	print("____________________________________________")
	print("|       B+      |            {}            |".format(bplus))
	print("____________________________________________")
	print("|       B       |            {}            |".format(b))
	print("____________________________________________")
	print("\n\nna - Not Applicable \n If you got n/a for any grade then you can't get that grade withyour current internal mark")

print("______             __   ______")
print("| ___ \           /  | |___  /")
print("| |_/ /___  __ _  `| |    / / ")
print("|    // _ \/ _` |  | |   / /  ")
print("| |\ \  __/ (_| | _| |_./ /   ")
print("\_| \_\___|\__, | \___/\_/    ")
print("            __/ |             ")
print("           |___/              ")
print("\n\nGive ur internal mark and find ur required external marks out of 100 for all\n\n")                              
print(" _____               _        ")
print("|  __ \             | |       ")
print("| |  \/_ __ __ _  __| | ___   ")
print("| | __| '__/ _` |/ _` |/ _ \  ")
print("| |_\ \ | | (_| | (_| |  __/  ")
print(" \____/_|  \__,_|\__,_|\___|  ")

while(True):
	while(True):
		try:
			internal_mark = int(input("\n\nEnter your internal mark : "))
			while(True):
				if internal_mark > 20:
					raise Exception("\n\nInternal mark must be less than 21")
				else:
					break
			break
		except ValueError:
			print("\n\nEnter a integer value eg.1,12,19 no decimal values or text")
		except Exception as a:
			print(a)
			
	external_mark(internal_mark)
			
	print("\n\nWant to check another(y/n) : ",end = "")
	if input().lower() == 'y':
		pass
	else:
		break
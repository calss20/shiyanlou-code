
for i in range(1,100):
	if (i%7 == 0):
		continue
	elif(i%10 == 7):
		continue
	elif(i//10 == 7):
		continue
	print(i)

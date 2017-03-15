sum = 0

x = 1
y = 2
z = 0

while (z < 1000000):
	if y % 2 == 0:
		sum += y

	z = x + y
	x = y
	y = z

print("The sum is: " + str(sum))

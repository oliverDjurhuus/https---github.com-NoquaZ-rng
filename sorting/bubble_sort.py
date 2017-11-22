import random

elements = random.sample(range(0, 200), 10)
print elements

no_elements = len(elements)

for i in xrange(no_elements-1,0,-1):
	swapped = False
	for j in range(i):
		if elements[j+1] < elements[j]:
			elements[j+1], elements[j] = elements[j], elements[j+1]
			swapped = True
	if not swapped:
		break;

print elements


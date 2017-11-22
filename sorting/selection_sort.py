import random 

elements = random.sample(range(0, 200), 10)
print elements

no_elements = len(elements)

for i in range(no_elements):
	i_min = i;
	
	sorting_scope = range(i+1, no_elements)
	for j in sorting_scope :
		if elements[j] < elements[i_min]:
			i_min = j

	if i != i_min :
		elements[i], elements[i_min] = elements[i_min], elements[i]

print elements


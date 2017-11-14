

items = [26,18,45,38,59,49,44,12,11,1,55,50,3,7,35,41,14,43,39,57]

length_items = len(items)


for i in xrange(length_items-1,0,-1):
	swapped = False
	for j in range(i):
		if items[j+1] < items[j]:
			items[j+1], items[j] = items[j], items[j+1]
			swapped = True
	if not swapped:
		break;

print items
	















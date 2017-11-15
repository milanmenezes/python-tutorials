l1=[eval(i) for i in raw_input("Enter the list\n").split()]
s=set(l1)
for key in s:
	indices = [i for i, x in enumerate(l1) if x == key]
	print key, ":",indices
l1=[eval(i) for i in raw_input("Enter the list\n").split()]
key=eval(raw_input("Enter the key\n"))
indices = [i for i, x in enumerate(l1) if x == key]
print indices
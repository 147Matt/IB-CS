collection=[7,2,3]
Current_index=0
min_index=0
while Current_index< len(collection):
	i= Current_index+1
	while i< len(collection):
		if collection[min_index]>collection[i]:
			min_index=i
		
		i+=1

	
	temp= collection[Current_index]
	collection[Current_index]=collection[min_index]
	collection[min_index]=temp

	Current_index += 1


print(collection)
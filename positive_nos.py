def pos_nos(l):
	ans = []
	for i in l:
		if i>0:
			ans.append(i)
	return ans

list1 = [12, -7, 5, 64, -14]
list2 = [12, 14, -95, 3]
print("The positive nos in list 1 are : ",pos_nos(list1))
print("The positive nos in list 2 are : ",pos_nos(list2))
		
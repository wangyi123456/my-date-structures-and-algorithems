def paritition (arr,begin,end):
	privot_index = begin
	privot = arr[privot_index]
	left = privot_index + 1
	right = end - 1
	while True:
		while left <= right and arr[left] <= privot: # 注意是否包含等于号
			left += 1
		while right >= left and arr[right] >= privot:
			right -= 1
		if left > right:   #结束时要让左右岔开位置
			break
		else:			
			arr[left],arr[right] = arr[right],arr[left]
	arr[right],arr[privot_index] = arr[privot_index],arr[right]  # 这里必须用right交换，因为循环结束right指向的才是小于 privot 的值,注意缩进，用数组别用privet
	return right

	
def QuickSort(arr,begin,end):
	
	if begin < end:
		privot = paritition(arr,begin,end)
		QuickSort(arr,begin,privot)
		QuickSort(arr,privot+1,end)
test = [0,1,3,5,3,6,8,0,12,12]
QuickSort(test,0,len(test))
print(test)

#归并排序'Mukta Mahee'
def merge_sort(arr):
	if len(arr) == 1:
		return arr
	else :
		n = int(len(arr)/2)
		left_half  = merge_sort(arr[:n])
		right_half = merge_sort(arr[n:])
		newseq = merge(left_half,right_half)
		return newseq

def merge(l_arr,R_arr):
	la = len(l_arr) 
	lb = len(R_arr)
	newarr = list() 
	a,b = 0,0
	while a<la and b<lb:
		if l_arr[a] < R_arr[b]:
			newarr.append(l_arr[a])
			a += 1
		else:
			newarr.append(R_arr[b])
			b += 1
	if a < la:
		newarr.extend(l_arr[a:])
	if b < lb:
		newarr.extend(R_arr[b:])
	return newarr
test = [1,3,5,3,6,8,0,12,12]
print(merge_sort(test))

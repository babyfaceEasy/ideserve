#YOUTUBE LINK: https://www.youtube.com/watch?v=a7D77DdhlFc&index=1&list=PLamzFoFxwoNjw4EpaVZzP-8lqWA9hOmnD
#this is to find any peak in a list of integers
#PEAK: is any element greater than its neigbours

#ALGO1 : this is a linear method, where we check each elenment to see if its greater thn it neigbours
#space complexity 0(1)
#time complexity 0(n)

def peak_algo1(ls):
 	for x in range(1, len(ls)):
 		if ls[0] >= ls[1]:
 			return ls[0]
 		elif ls[len(ls) - 1 ] >= ls[len(ls) - 2 ]:
 			return ls[len(ls) - 1]
 		else:
 			if ls[x] >= ls[x + 1] and ls[x] >= ls[x - 1]:
 				return ls[x]


#ALGO2: this is using binary search to get our answer.
#get a random number if its not a peak element if the left elt is bigger then our peak is on the left else if the right elt is higer
#then the peak element is on the right.
#space complexity 0(1)
#time complexity 0(log n)

def peak_algo2(ls):
 	print(ls)
 	start = 0
 	end = len(ls) - 1
 	while start <= end:
 	 	mid = (start + end)//2
 	 	if ls[mid] >= ls[mid + 1] and ls[mid] >= ls[mid - 1]:
 	 		return ls[mid]
 	 	else:
 	 		if ls[mid + 1] > ls[mid]:
 	 			end = mid - 1
 	 		else:
 	 			start = mid + 1
 	else:
 		return 'null';

if __name__ == '__main__':
	#ls = [10, 40, 20, 5, 45, 50, 65, 90, 35, 25]
	#ls = [10, 50, 4, 5, 90, 56, 5]
	ls = []
	#print(ls)
	print(peak_algo2(ls))
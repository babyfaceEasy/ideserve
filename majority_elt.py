#YOUTUBE LINK:https://www.youtube.com/watch?v=zOyOwDEF1Rc&list=PLamzFoFxwoNjw4EpaVZzP-8lqWA9hOmnD&index=2
#this is to find the majority element.
#MAJORITY ELEMENT is the element that occurs more than n/2 times. NB: at most, we would find one
#else we return false not found

#Algo1: we use two loops, inner loop counts element and outer loop check if number of element is greater than n /2 
#else we return null
#Time complexity : 0(n^2)

def majorityElt(ls):
	for x in range(0, len(ls)):
		currElt =  ls[x]
		times = len(ls) // 2
		count = 0
		for i in range(x,len(ls)):
			if ls[i] == currElt:
				count = count + 1

		if count > times:
			return currElt

	return None

#ALGO 2: wwe sort the array then apply the algo methodology. NB: out sorting algo should take O(nlogn)
#then the algo 1 uses O(n)
#Time Complexity :  n * O(nlogn)


#ALGO3: Boyer-Moore Vote Algorithm
#find a candidate for majority element, then check if this candidate is a majority element
#TIME COMPLEXITY: 0(n) 
#SPACE COMPLEXITY: 0(1)

def majorityElt3(ls):
	#this is to find the max element
	candidate = None
	count = 0

	for x in range(0, len(ls)):
		if count == 0:
			candidate = ls[x]
			count = 1
			continue
		else:
			if candidate == ls[x]:
				count = count + 1
			else:
				count = count - 1

	if count == 0:
		return None
	#check if element is majority element
	count = 0
	for x in range(0, len(ls)):
		if candidate == ls[x]:
			count = count + 1

	return candidate if count > len(ls) // 2 else None



if __name__ == '__main__':
	#ls = [10, 40, 20, 5, 45, 50, 65, 90, 35, 25]
	ls = [2, 6, 2, 2, 6, 2, 2, 8, 2, 1]
	#ls = [1, 7, 8, 2, 6, 8, 1, 3, 2, 8]
	ls =  [2, 1, 2, 4, 7]
	print(majorityElt(ls))

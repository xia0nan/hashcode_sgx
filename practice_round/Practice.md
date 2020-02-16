# More pizza

## Requirement
- The pizzeria has types of pizza, you can only order at most one pizza of each type
- Each type of pizza has a specified size: the size is the number of slices in a pizza of this type.
- You estimated the maximum number of pizza slices that you want to order for your hub based on the number of registered participants

### Goal
Order as many pizza slices as possible, but not more than the maximum number

### Input format
- *ASCII*
- lines terminated with a *single '\n'*
- When a single line contains multiple elements, they are separated by *single spaces*.
- First line
	- an integer M: 1 <= M <= 10e9
		- maximum number of pizza slices to order
	- an integer N: 1 <= N <= 10e5
		- the number of different types of pizza
- Second line
	- N integers: the number of slices in each type of pizza, in **non-decreasing order**
	- 1 <= S0 <= S1 <= ... <= Sn-1 <= M

## Example
- a_example.in
- 17 slices maximum, 4 different types of pizza
- type0 has 2 slices, type1 has 5, type2 has 6, and type3 has 8 slices

## Submission
- The first line should contain a single integer K (0 ≤ K ≤ N) – the number of different types of pizza to order.
- The second line should contain K numbers – the types of pizza to order (the types of pizza are numbered from 0 to N-1 in the order they are listed in the input).
- The total number of slices in the ordered pizzas must be less than or equal to M.

## Colab Exploration
https://colab.research.google.com/drive/1bVHi-ztCphGWmqVkh81MAvV-VIiWq9Rz
#https://www.codewars.com/kata/5715eaedb436cf5606000381/train/python

# Original
def positive_sum(arr):
    sum = 0
    for e in arr:
        if e > 0:
            sum = sum + e
    return sum

#Refactor
def positive_sum(arr):
    return sum(x for x in arr if x > 0)


#https://www.codewars.com/kata/60cc93db4ab0ae0026761232/train/python

#Original
def arrange(s):
    left = 0
    right = -1
    t = []
    while len(t) < len(s):
        t.append(s[left])
        t.append(s[right])
        if left > right:
            left, right = right -1, left +1
        else:
            left, right = right + 1, left - 1     
    if len(t) > len(s):
        t.pop() 
    return t
            
# Refactor
from collections import deque

def arrange(s):
    queue = deque(s)
    return [queue.pop() if 0<i%4<3 else queue.popleft() for i in range(len(s))]

"""
This above one was hard and I used the top solution and did research to figure out why it was the best solution. Hopefully that's ok.

Explanation:

If the remainder of an index 'i' / 4 == 1 or 2, or every 4th index excluding those divisbile by 4 (i.e. 4/4 has no remainder),
the pop is used on the last index

If the remainder lies outside of that condition, the pop is used on the first index. 

By using this method, the reverse for s is simulated by the correct popping of indices, thus improving the time complexity.

"""


#https://www.codewars.com/kata/5784c89be5553370e000061b/train/python

# Original
def max_product(a):
    max1 = 0
    max2 = 0

    for num in a:
        if num > max1:
            max2 = max1
            max1 = num
        elif num > max2:
            max2 = num

    return max1 * max2

# Refactor
def max_product(a):
    max1 = max(a)
    a.remove(max1)
    max2 = max(a)
    return max1 * max2
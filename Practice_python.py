# 1. Student Attendance Analysis
# A college maintains the daily attendance details of its students in the form of a list containing student IDs.
#  Some students may have attended multiple sessions on the same day. 
# The administration wants to identify the longest continuous sequence of sessions in which no student ID is repeated. 4
# Develop a solution that determines the maximum length of such a sequence.

arr=list(map(int,input().split()))
left=0
seen=set ()
max_length=0
for right in range(len(arr)):
    while arr[right] in seen:
        seen.remove(arr[left])
        left += 1
    seen.add(arr[right])
    length=max(max_length,right-left+1)
print(length)


# 2. Online Shopping Price Analysis
# An online shopping application stores the prices of products viewed by a customer during a browsing session.
# The customer wants to identify a continuous range of products that provides the maximum possible total discount value. 
# Given the discount values, determine the maximum value that can be obtained from any continuous range.

arr=list(map(int,input().split()))
curr=arr[0]
maximum=arr[0]
for i in range(1,len(arr)):
    curr=max(arr[i],curr+arr[i])
    maximum=max(maximum,curr)   
print(maximum)


# 3. Rainwater Collection System
# A city installs buildings of different heights along a straight road. During rainfall, water gets collected between taller buildings.
# The engineering team needs to calculate the total amount of water that can remain trapped after heavy rainfall based on the heights of the buildings.

arr = list(map(int, input().split()))
water = 0
for i in range(len(arr)):
    left_max = max(arr[:i+1])
    right_max = max(arr[i:])
    level = min(left_max, right_max)
    water += level - arr[i]
print(water)

# 5. Product Sales Analysis
# A retail company stores the daily sales quantity of a product for several consecutive days. 
# Due to seasonal changes, some days may have negative adjustments. The company wants to identify the period that produced the highest multiplication of sales-related values. 
# Develop a solution to determine this maximum product.

arr = list(map(int, input().split()))
current_max = arr[0]
current_min = arr[0]
maximum = arr[0]
for i in range(1, len(arr)):
    x = arr[i]
    old_max = current_max
    old_min = current_min
    current_max = max(x, old_max * x, old_min * x)
    current_min = min(x, old_max * x, old_min * x)
    maximum = max(maximum, current_max)
print(maximum)



# 6. Customer Purchase History.An e-commerce application stores the product IDs purchased by a customer in chronological order. 
# The same product may appear multiple times. The system needs to determine the longest sequence of consecutive purchases in which every product ID is unique.

arr = list(map(int, input().split()))
seen = set()
left = 0
maximum = 0
for right in range(len(arr)):
    while arr[right] in seen:
        seen.remove(arr[left])
        left += 1
    seen.add(arr[right])
    maximum = max(maximum, right - left + 1)
print(maximum)

# 7. Bank Transaction Analysis
# A bank stores transaction amounts for a customer's account. A continuous group of transactions may add up to a specific target amount. 
# The auditing system needs to determine how many different continuous transaction groups produce exactly the specified amount.

arr = list(map(int, input().split()))
target = int(input())
prefix_sum = 0
count = 0
seen = {0: 1}
for x in arr:
    prefix_sum += x
    needed = prefix_sum - target
    if needed in seen:
        count += seen[needed]
    if prefix_sum in seen:
        seen[prefix_sum] += 1
    else:
        seen[prefix_sum] = 1
print(count)


# 8. Employee Skill Grouping
# A company receives a list of employee skill codes represented as strings. Employees having the same set of characters in their skill codes belong to the same skill category, even if the characters appear in a different order. 
# The HR system needs to organize employees into appropriate skill groups.

arr = input().split()
groups = {}
for word in arr:
    key = ''.join(sorted(word))
    if key not in groups:
        groups[key] = []
    groups[key].append(word)
for group in groups.values():
    print(group)

# 9. Network Packet Analysis
# A network monitoring system receives packet identifiers in chronological order. The system must determine the longest sequence of consecutive packets whose identifiers form a continuous numerical sequence,
# regardless of their original order in the incoming data.

arr = list(map(int, input().split()))
nums = set(arr)
maximum = 0
for x in nums:
    if x - 1 not in nums:
        current = x
        length = 1
        while current + 1 in nums:
            current += 1
            length += 1
        maximum = max(maximum, length)
print(maximum)


# 10. Hospital Appointment Scheduling
# A hospital receives appointment requests represented by starting and ending times. Some appointments overlap with each other. The scheduling system needs to combine overlapping 
# appointment periods so that the final schedule contains only non-overlapping time ranges.


n = int(input())
arr = []
for i in range(n):
    start, end = map(int, input().split())
    arr.append([start, end])
arr.sort()
result = []
for start, end in arr:
    if len(result) == 0 or start > result[-1][1]:
        result.append([start, end])
    else:
        result[-1][1] = max(result[-1][1], end)
print(result)
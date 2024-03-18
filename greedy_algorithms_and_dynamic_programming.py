import numpy as np


# Implement a dyanamic programming algorithm to solve the Rod Cutting Problem.
# Input: 
# price_table: market prices of rod of different lengths
# rod_length: length of given rod
# Output:
# A series of rod lengths after cut that provide the maximum profit
# The sum of all lengths should equal to rod_length. 
# Lengths in vector can be in any order.
# Example: 
# Given price_table = [1, 2, 8, 9] and rod_length = 4. 
# The algorithm should return a set of length including [2, 2]

import numpy as np

def rod_cutting_problem(price_table, rod_length):
    #revenue array 
    rev = np.zeros(len(price_table)+1)
    #position
    #cut_position = np.zeros(len(price_table))
    cut_position = 0
    price_table = np.insert(price_table, 0, 0)

    for i in range (1,rod_length+1):
        max_revenue = -10000
        if i == 1:
            rev[i] = price_table[i]
            max_revenue = rev[i]
        else:
            for j in range (1,i+1):
                if max_revenue < price_table[j] + rev[i-j]:
                    max_revenue = price_table[j] + rev[i-j]
                    cut_position = j
            rev[i] = max_revenue
        #print(cut_position, max_revenue)
  
    result = [cut_position, rod_length - cut_position]
    return result # should be replaced with your result


# Implement a dyanamic programming algorithm to solve the Maximum Subarray Problem.
# Input: 
# A: input array containing a series of integers
# Output:
# Array of intergers containing two intergers representing the start and end index of the maximum subarray
# Index starts from 0.
# Example: 
# Given array A = [-23, 18, 20, -7, 12]
# The algorithm should return two indices [1, 4]

def maximum_subarray(A):

    # Initialize max values
    max_now = A[0]
    max_overall = A[0]


    for i in range(1, len(A)):

        # Re-calculate max_now
        max_now = max(A[i], A[i] + max_now)

        # Compare max_now with max_overall
        if (max_now > max_overall):
            max_overall = max_now
            end_i = i
	
    start_i = end_i

	# Looking for the best start index of subarray
    while (start_i >= 0):
        max_overall -= A[start_i]

        if (max_overall == 0):
            break

        # Decrement the start index
        start_i -= 1

	# Printing the max total
    max_total = 0
    for i in range(start_i, end_i + 1):
        max_total += A[i]
    #print(max_total)
    return [start_i, end_i] # should be replaced with your result


# Implement a dyanamic programming algorithm to solve the Matrix Chain Product Problem.
# Input: 
# A: input array containing a series of matrix dimensions
# For N matrices, the total number of dimensions is N+1 and the total number of multiplications is N-1
# Output:
# Array of intergers containing N-1 intergers representing the order of the multiplications (order starts from 1)
# e.g., 1 presents the first multiplication and N-1, represents the last multiplication.
# Example:
# Given 3 matrics, the dimension array = [100, 2, 50, 6] representing matrix A1(100*2), A2(2*50), A3(50*6).
# The algorithm should return two intergers for the 2 matrix multiplications [2, 1] i.e., A1*(A2*A3)

def matrix_multiplication(matrix_dimensions):
    n = len(matrix_dimensions)-1
    mat_sum = [[0 for _ in range(n+1)] for _ in range(n+1)]
    mat_start = [[0 for _ in range(n+1)] for _ in range(n+1)]
    # for i in range(1,n):
    #     mat_sum[i,i] = 0
    for L in range(2,n+1):
        for start in range(1, n-L+2):
            end = start + L - 1
            #print(start)
            #print(end)
            mat_sum[start][end] = np.inf
            for k in range(start,end):
                cost = mat_sum[start][k] +mat_sum[k+1][end] + matrix_dimensions[start-1]*matrix_dimensions[start]*matrix_dimensions[end]
                if cost < mat_sum[start][end]:
                    mat_sum[start][end] =  cost
                    mat_start[start][end] = k
    return mat_sum, mat_start

def get_matrix_multiplication_positions(s, i, j, pos=None):
    if pos is None:
        pos = []

    if i == j:
        return pos
    else:
        k = s[i][j]
        pos.append(k)
        get_matrix_multiplication_positions(s, i, k, pos)
        get_matrix_multiplication_positions(s, k + 1, j, pos)
        return pos

def matrix_chain_product(matrix_dimensions):
    m, s = matrix_multiplication(matrix_dimensions)
    optimal_order = get_matrix_multiplication_positions(s, 1, len(matrix_dimensions) - 1)
    order = optimal_order[::-1] 
    return order # should be replaced with your result
  

# Implement a dyanamic programming algorithm to solve the 0/1 Knapsack Problem.
# Input: 
# Two input arrays containing a series of weights and profits
# An integer K representing the knapsack capacity.
# Output:
# 0/1 Array of indicating which items are selected (0: not selected; 1: selected)
# Example:
# Given 4 items with weight = [5, 4, 6, 3] and profit = [10, 40, 30, 50]
# The algorithm should return array = [0, 1, 0, 1] represeting the second and the last item are selected.

def zero_one_knapsack(weight, profit, K):
    n = len(weight)
    M_table = [[0 for _ in range(K+1)] for _ in range(n+1)]

    #Find the max weight possible
    for i in range(1,n+1):
        for j in range(K+1):
            if weight[i-1] > j:
                M_table[i][j] = M_table[i-1][j]
            else:
                M_table[i][j] = max(M_table[i-1][j], M_table[i-1][j - weight[i - 1]] + profit[i - 1])
    max_value = M_table[n][K]  
    #print(max_value)

    #Find the list of items included in the knapsack
    List_of_items = []
    a = K
    for i in range(n, 0, -1):
        if M_table[i][a] != M_table[i - 1][a]:
            List_of_items.append(i - 1)
            a -= weight[i - 1]    
    #print(List_of_items)

    #Identify items included as 1 at the appropriate index
    items = [0 for _ in range(n)]
    for i in range(len(List_of_items)):
        items[List_of_items[i]] = 1
    #print(items)
    return items


# Implement the Radix sort algorithm. For sorting each digit you should use counting sort.
# Input: 
# An input arrays containing a series of integers. Each interger has maximum K digits. The range of each digit is from 0 to 9.
# Note that some integers may have less than K digits.
# Output:
# sorted array
# Example:
# Given array = [15, 24, 26, 3] and K = 2
# The algorithm should return sorted array [3, 15, 24, 26].

def radix_sort(A, K):
# Implement your algorithm here...
    return A # should be replaced with your result


# Implement the activity selection algorithm using greedy appraoch.
# Input: 
# Two input arrays containing a series of start time and finish time
# Output:
# 0/1 indicating which activities are selected (0: not selected; 1: selected)
# Example:
# Given N=4 items with start time = [1, 3, 0, 5, 8, 5] and finish time = [2, 4, 6, 7, 9, 9]
# The algorithm should return array =  [1, 1, 0, 1, 1, 0] represeting the 4 activites: (1, 2), (3, 4), (5, 7), (8, 9) are selected.

def check_sort(start_time, finish_time):
    #re-order array by fastest finish time
    finish_time_sorted = []
    start_time_sorted = []
    for i in range(len(finish_time)):
        min_index = np.argmin(finish_time)
        finish_time_sorted.append(finish_time[min_index])
        start_time_sorted.append(start_time[min_index])
        finish_time = np.delete(finish_time, min_index)
        start_time = np.delete(start_time, min_index)
    #print(start_time_sorted)
    #print(finish_time_sorted)
    return start_time_sorted, finish_time_sorted

def activity_selection(start_time, finish_time):
    start_time_new, finish_time_new = check_sort(start_time, finish_time)
    #all activities are sorted by their finish time
    list = [1]
    list1 = []
    k = 0
    n = len(start_time)
    for m in range(1,n):
        if start_time_new[m]>=finish_time_new[k]:
            list.append(1)
            k = m
        else:
            list.append(0)
    for m in range(n):
        for x in range(n):
            if finish_time[m] == finish_time_new[x] and start_time[m] == start_time_new[x]:
                list1.append(list[x])
    print(list1) 
    return list1 # should be replaced with your result



########### DO NOT MODIFY CODE BELOW THIS LINE #############

def verify_rod_cutting(price_table, result, true_result):
    total_price = sum(price_table[i-1] for i in result)
    return true_result == total_price

def verify_max_subarray(A, result, true_result):
    total_sum = sum(A[i] for i in range(result[0], result[1] + 1))
    return true_result == total_sum

def verify_matrix_chain(result, true_result):
    for i in range(len(true_result)):
        if result[i] != true_result[i]:
            return False
    return True

def verify_zero_one_knapsack(weight, profit, result, true_result, K):
    total_weight = 0
    total_profit = 0

    for i in range(len(result)):
        if result[i]:
            total_weight += weight[i]
            total_profit += profit[i]

    return total_weight <= K and total_profit == true_result

def verify_radix_sort(result, true_result):
    for i in range(len(true_result)):
        if result[i] != true_result[i]:
            return False
    return True

def verify_activity_selection(result, true_result):
    for i in range(len(true_result)):
        if result[i] != true_result[i]:
            return False
    return True

print("Name: {} blazer_id: {}".format(name, blazer_id))

print("---------- Rod Cutting Problem ---------")
price_table_1 = [1, 5, 8, 9]
result1 = rod_cutting_problem(price_table_1, len(price_table_1))
pass1 = verify_rod_cutting(price_table_1, result1, 10)
print("Case 1: Correct:", "Yes" if pass1 else "No")

price_table_2 = [2, 3, 6, 9, 10, 17, 17]
result2 = rod_cutting_problem(price_table_2, len(price_table_2))
pass2 = verify_rod_cutting(price_table_2, result2, 19)
print("Case 2: Correct:", "Yes" if pass2 else "No")

print("------ Maximum Subarray Problem ------")
array_1 = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
result1 = maximum_subarray(array_1)
pass1 = verify_max_subarray(array_1, result1, 43)
print("Case 1: Correct:", "Yes" if pass1 else "No")

array_2 = [-2, -3, 4, -1, -2, 1, 5, -3]
result2 = maximum_subarray(array_2)
pass2 = verify_max_subarray(array_2, result2, 7)
print("Case 2: Correct:", "Yes" if pass2 else "No")


print("------ Matrix Chain Product ------")
matrix_dimensions_1 = [100, 2, 50, 6]
result1 = matrix_chain_product(matrix_dimensions_1)
pass1 = verify_matrix_chain(result1, [2, 1])
print("Case 1:", "Correct: " + ("Yes" if pass1 else "No"))

matrix_dimensions_2 = [100, 60, 70, 30, 100]
result2 = matrix_chain_product(matrix_dimensions_2)
pass2 = verify_matrix_chain(result2, [2, 1, 3])
print("Case 2:", "Correct: " + ("Yes" if pass2 else "No"))

print("------ 0/1 Knapsack Problem ------")
weight_1 = [10, 20, 30]
profit_1 = [60, 100, 120]
result1 = zero_one_knapsack(weight_1, profit_1, 50)
pass1 = verify_zero_one_knapsack(weight_1, profit_1, result1, 220, 50)
print(f"Case 1: Correct: {'Yes' if pass1 else 'No'}")

weight_2 = [5, 4, 6, 3]
profit_2 = [10, 40, 30, 50]
result2 = zero_one_knapsack(weight_2, profit_2, 10)
pass2 = verify_zero_one_knapsack(weight_2, profit_2, result2, 90, 10)
print(f"Case 2: Correct: {'Yes' if pass2 else 'No'}")

print("------ Radix Sort ------")
array_1 = [23, 12, 65, 89, 62, 38, 48]
result1 = radix_sort(array_1, 2)
pass1 = verify_radix_sort(result1, [12, 23, 38, 48, 62, 65, 89])
print(f"Case 1: Correct: {'Yes' if pass1 else 'No'}")

array_2 = [1047, 2992, 9473, 7362, 1938, 4845, 3838, 5693, 9128]
result2 = radix_sort(array_2, 4)
pass2 = verify_radix_sort(result2, [1047, 1938, 2992, 3838, 4845, 5693, 7362, 9128, 9473])
print(f"Case 2: Correct: {'Yes' if pass2 else 'No'}")

print("------ Activity Selection Problem ------")
start_1 = [1, 3, 0, 5, 8, 5]
finish_1 = [2, 4, 6, 7, 9, 9]
result1 = activity_selection(start_1, finish_1)
pass1 = verify_activity_selection(result1, [1, 1, 0, 1, 1, 0])
print(f"Case 1: Correct: {'Yes' if pass1 else 'No'}")

start_2 = [4, 3, 2, 5, 1, 3, 6, 1, 7, 4]
finish_2 = [6, 6, 4, 7, 2, 5, 7, 3, 9, 7]
result2 = activity_selection(start_2, finish_2)
pass2 = verify_activity_selection(result2, [1, 0, 1, 0, 1, 0, 1, 0, 1, 0])
print(f"Case 2: Correct: {'Yes' if pass2 else 'No'}")


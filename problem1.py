""" Problem Statement:
We are given an array of integers representing the scores a faculty gives to students. We need to find the index where the sum of points on the left side becomes greater than the sum on the right side.

Approach:
We can use prefix sums to efficiently compute the sum of elements on both sides of any index. We loop through the array, calculate the sum of elements to the left, and compare it to the sum of elements on the right.
    """
    
def find_weird_faculty_index(scores):
    total_sum = sum(scores)
    left_sum = 0
    
    for i in range(len(scores)):
        total_sum -= scores[i]  # total_sum now represents the sum of elements on the right
        if left_sum > total_sum:
            return i  # index where left_sum becomes greater than right_sum
        left_sum += scores[i]
    
    return -1  # in case no such index is found

# Example input
scores = [4, -1, -2, 3, 4]
print(find_weird_faculty_index(scores))  # Output: 3
        
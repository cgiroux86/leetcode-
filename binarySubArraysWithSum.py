
def countSubarrays(arr, n, k):

    start = 0
    end = 0
    count = 0
    sum = arr[0]

    while (start < n):

        # If sum is less than k, move end
        # by one position. Update count and
        # sum accordingly.
        if (sum == k):
            count += 1
            sum += arr[end]
            end += 1

        elif sum < k:
            end += 1
            # For last element, end may become
            sum += arr[end]

        # If sum is greater than or equal to k,
        # subtract arr[start] from sum and
        # decrease sliding window by moving
        # start by one position

        else:
            sum -= arr[start]
            start += 1

    return count


# Driver Code
array = [1, 0, 1, 0, 1]
k = 2
size = len(array)
count = countSubarrays(array, size, k)
print(count)
# def numSubarraysWithSum(A, S):
#     curr_max = A[0]
#     total_max = 0
#     res = 0

#     for i in range(len(A)):
#         if curr_max == S:
#             res += 1
#         curr_max = max(curr_max, curr_max + A[i])
#     print(res)
# res = 0
# sub = 0
# for i in range(len(A)):
#     sub = A[i]
#     if sub == S:
#         res += 1
#     for j in range(i + 1, len(A)):
#         sub = sub + A[j]
#         if sub == S:
#             res += 1
#         if sub > S:
#             break
# return res


# numSubarraysWithSum([0, 0, 0, 0, 0], 0)

def avg_subarray_of_k(nums, k):
    result = []          # To store averages
    window_sum = 0       # Sum of current window
    left = 0             # Left pointer

    # Iterate through array using right pointer
    for right in range(len(nums)):
        window_sum += nums[right]   # Add current element

        # When window size becomes k
        if right >= k - 1:
            # Calculate average and store
            result.append(window_sum / k)

            # Remove leftmost element (slide window)
            window_sum -= nums[left]

            # Move left pointer
            left += 1

    return result


print(avg_subarray_of_k([1, 2, 3, 4, 5], 2))
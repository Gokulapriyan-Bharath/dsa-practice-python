# Problem: Contains Duplicate


# Approach 1: Using set
def contains_duplicate_set(array):
    return len(array) != len(set(array))

# Approach 2: Brute force
def contains_duplicate_bruteforce(array):
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            if array[i] == array[j]:
                return True
    return False


# Approach 3: Hashing
def contains_duplicate_hashing(array):
    seen = set()

    for num in array:
        if num in seen:
            return True
        seen.add(num)

    return False


print(contains_duplicate_set(array=[1,2,3,4]))
print(contains_duplicate_bruteforce(array=[1,2,3,4]))
print(contains_duplicate_hashing(array=[1,2,3,4]))

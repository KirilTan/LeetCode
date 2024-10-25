## Two Sum

This code solves the classic "two-sum" problem using a **hash map (dictionary)** to efficiently find pairs of numbers that add up to a given target. Below is a detailed step-by-step explanation of how the code works.

### Code Explanation:

```python
def two_sum(nums, target):
    # Create a dictionary to store the index of each number
    num_to_index = {}
    
    # Loop through each number in the array
    for i, num in enumerate(nums):
        # Calculate the complement that we need to find
        complement = target - num
        
        # Check if the complement is already in the dictionary
        if complement in num_to_index:
            return [num_to_index[complement], i]
        
        # Store the number and its index in the dictionary
        num_to_index[num] = i
```

### Let's break it down:

1. **Defining the function:**
   ```python
   def two_sum(nums, target):
   ```
    - We define a function called `two_sum` that accepts two parameters:
        - `nums`: a list of integers.
        - `target`: an integer representing the sum we are trying to find by adding two numbers from `nums`.

2. **Creating the dictionary:**
   ```python
   num_to_index = {}
   ```
    - We initialize an empty dictionary called `num_to_index`.
    - This dictionary will store the numbers from the list as keys and their corresponding indices as values.
    - The goal is to use the dictionary to quickly check if a number (specifically the complement of the current number) exists in the array.

3. **Looping through the list `nums`:**
   ```python
   for i, num in enumerate(nums):
   ```
    - We loop through the list `nums` using `enumerate`. This allows us to access both:
        - `i`: the index of the current element.
        - `num`: the value of the current element at index `i`.
    - We are essentially iterating over each element to see if we can find its complement (another number in the list that, when added to `num`, equals the `target`).

4. **Calculating the complement:**
   ```python
   complement = target - num
   ```
    - For each element `num`, we calculate its complement by subtracting `num` from the `target`.
    - The complement is the value we are looking for in the dictionary (i.e., the number that, when added to `num`, will equal `target`).

   **Example**:  
   If `target = 9` and the current `num = 7`, then the `complement = 9 - 7 = 2`.  
   We want to check if `2` exists in the dictionary as we loop through the list.

5. **Checking if the complement exists in the dictionary:**
   ```python
   if complement in num_to_index:
   ```
    - We check if the `complement` already exists as a key in the `num_to_index` dictionary.
    - If the complement is found, it means we have already encountered the number that, when added to the current `num`, equals the `target`.

6. **Returning the indices:**
   ```python
   return [num_to_index[complement], i]
   ```
    - If the complement exists in the dictionary, we return the indices of the complement (which was stored earlier in the dictionary) and the current number `num` (i.e., `i`).
    - This gives us the two indices of the numbers that add up to the target.

   **Example**:  
   If `complement = 2` and we find it in the dictionary at index `0`, and the current `num = 7` is at index `1`, we return `[0, 1]`.

7. **Storing the current number and its index:**
   ```python
   num_to_index[num] = i
   ```
    - If the complement is **not** found in the dictionary, we store the current number (`num`) and its index (`i`) in the `num_to_index` dictionary.
    - This way, the next time we encounter a number whose complement is `num`, we can easily look it up.

   **Example**:  
   If `num = 7` and `i = 1`, then `num_to_index[7] = 1` is stored in the dictionary.

---

### Example Walkthrough:

Let’s walk through an example using the array `nums = [2, 7, 11, 15]` and `target = 9`.

#### Initial Setup:
- We have `num_to_index = {}` (an empty dictionary).

#### Iteration 1:
- `i = 0`, `num = 2`
- Compute the complement: `complement = 9 - 2 = 7`.
- Check if `7` is in `num_to_index`: No, it's not.
- Add `num = 2` to the dictionary: `num_to_index = {2: 0}`.

#### Iteration 2:
- `i = 1`, `num = 7`
- Compute the complement: `complement = 9 - 7 = 2`.
- Check if `2` is in `num_to_index`: Yes, it is (with index `0`).
- Return the indices: `[0, 1]`.

The function stops as soon as it finds the solution, so it returns `[0, 1]`.

---

### Time and Space Complexity:

- **Time Complexity**:  
  The time complexity is **O(n)**, where `n` is the number of elements in the array. This is because we are looping through the array once, and dictionary lookups and insertions are done in constant time, **O(1)**.

- **Space Complexity**:  
  The space complexity is **O(n)** because, in the worst case, we store all `n` elements of the array in the dictionary.

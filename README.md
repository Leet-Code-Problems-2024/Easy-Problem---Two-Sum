# Easy-Problem---Two-Sum
This problem demonstrates the solutions to the leet code problem two sum with the explanation of how it works

This code defines a class called Solution with a method twoSum that takes in a list of numbers (nums) and a target sum (target). The goal of the method is to find and return the indices of two numbers in the list that add up to the target sum.

Here's a step-by-step explanation of the code:

1. index = list(): This line initializes an empty list called index, which will be used to store the indices of the two numbers whose sum equals the target.

2. The code uses nested loops:

  - The outer loop (for j in range(0, len(nums)-1)) iterates over each element in the list, except for the last one. It uses the variable j to represent the index of the first number in the pair.
  - The inner loop (for i in range(j + 1, len(nums))) iterates over the remaining elements in the list, starting from the element following the one selected by the outer loop. It uses the variable i to represent the index of the second number in the pair.

3. Inside the inner loop, there is an if statement that checks whether the sum of the numbers at indices i and j equals the target:

''' if(nums[i] + nums[j] == target): '''

4. If the condition is true, the code sets the variable index1 to the value of j. 


If the condition is true, the code sets the variable index1 to the value of j and index2 to the value of i. These variables represent the indices of the two numbers in the list that add up to the target.
python

            index1 = j
            index2 = i

The code then appends index1 and index2 to the index list. This is done to store the indices of the two numbers forming a pair that meets the target sum condition.
python

            index.append(index1)
            index.append(index2)

The loops continue iterating until all possible pairs of numbers have been checked.

Finally, the method returns the index list containing the indices of the two numbers whose sum equals the target.

python

            return index

The provided block enclosed in triple double-quotes below the method signature serves as type hints, indicating the expected types for the method parameters (nums and target) and the return type (List[int]). These type hints can be useful for developers and tools that support type checking in Python. The overall goal of the twoSum method is to efficiently find and return the indices of a pair of numbers in the input list nums that add up to the specified target sum.

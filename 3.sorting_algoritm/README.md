# 🔢 Sorting Algorithms

A collection of notes on five fundamental sorting algorithms in Data Structures and Algorithms (DSA). This README focuses on how each algorithm works, its time complexity, and its space complexity.

## 📚 Table of Contents

1. Bubble Sort
2. Selection Sort
3. Insertion Sort
4. Merge Sort
5. Quick Sort
6. Complexity Comparison

## 1. 🫧 Bubble Sort

**Definition:** Bubble Sort is a simple sorting algorithm that repeatedly compares adjacent elements and swaps them if they are in the wrong order.

**How It Works:**
- Compare two adjacent elements.
- Swap them if the left element is greater than the right element.
- Repeat the process until the array is sorted.
- After each pass, the largest unsorted element reaches its correct position.

**Time Complexity (TC):**
- Best Case: O(n) — when the array is already sorted and an optimization detects no swaps.
- Average Case: O(n²)
- Worst Case: O(n²)

**Space Complexity (SC):** O(1) — uses constant extra space.

**Key Point:** Easy to understand and implement, but inefficient for large datasets.

## 2. 🎯 Selection Sort

**Definition:** Selection Sort repeatedly finds the smallest element from the unsorted portion and places it at the beginning of that portion.

**How It Works:**
- Start from the first element.
- Find the minimum element in the unsorted portion.
- Swap it with the first unsorted element.
- Move the boundary of the sorted portion one position forward.
- Repeat until the entire array is sorted.

**Time Complexity (TC):**
- Best Case: O(n²)
- Average Case: O(n²)
- Worst Case: O(n²)

**Space Complexity (SC):** O(1) — sorts the array in place.

**Key Point:** Performs relatively few swaps, but always makes a quadratic number of comparisons.

## 3. 📥 Insertion Sort

**Definition:** Insertion Sort builds a sorted portion of the array one element at a time by inserting each new element into its correct position.

**How It Works:**
- Consider the first element as sorted.
- Select the next element as the key.
- Compare the key with elements in the sorted portion.
- Shift larger elements one position to the right.
- Insert the key into its correct position.
- Repeat until all elements are sorted.

**Time Complexity (TC):**
- Best Case: O(n) — when the array is already sorted.
- Average Case: O(n²)
- Worst Case: O(n²)

**Space Complexity (SC):** O(1) — uses constant extra space.

**Key Point:** Works well for small or nearly sorted arrays.

## 4. 🔀 Merge Sort

**Definition:** Merge Sort is a divide-and-conquer algorithm that divides an array into smaller parts, sorts them recursively, and merges the sorted parts.

**How It Works:**
- Divide the array into two halves.
- Recursively sort each half.
- Compare elements from both sorted halves.
- Merge them into a single sorted array.
- Continue until the entire array is sorted.

**Time Complexity (TC):**
- Best Case: O(n log n)
- Average Case: O(n log n)
- Worst Case: O(n log n)

**Space Complexity (SC):** O(n) — the standard array-based implementation requires additional space for merging.

**Key Point:** Provides predictable performance and is suitable for large datasets. It is also stable when implemented by choosing the left element first when elements are equal.

## 5. ⚡ Quick Sort

**Definition:** Quick Sort is a divide-and-conquer algorithm that selects a pivot and partitions the array around it, then recursively sorts the resulting sections.

**How It Works:**
- Select a pivot element.
- Partition the array so that smaller elements appear before the pivot and larger elements appear after it.
- Place the pivot in its correct position.
- Recursively sort the left and right partitions.
- Stop when a partition contains zero or one element.

**Time Complexity (TC):**
- Best Case: O(n log n)
- Average Case: O(n log n)
- Worst Case: O(n²) — can occur when partitions are highly unbalanced.

**Space Complexity (SC):**
- Average Case: O(log n) auxiliary space for recursion.
- Worst Case: O(n) auxiliary space for recursion.

**Key Point:** Often fast in practice and usually sorts in place, but performance depends on pivot selection and partition balance.

## 📊 Complexity Comparison

| Algorithm | Best TC | Average TC | Worst TC | Auxiliary SC |
|---|---|---|---|---|
| Bubble Sort | O(n) | O(n²) | O(n²) | O(1) |
| Selection Sort | O(n²) | O(n²) | O(n²) | O(1) |
| Insertion Sort | O(n) | O(n²) | O(n²) | O(1) |
| Merge Sort | O(n log n) | O(n log n) | O(n log n) | O(n) |
| Quick Sort | O(n log n) | O(n log n) | O(n²) | O(log n) average; O(n) worst |

*Note: Complexity assumes standard implementations. Bubble Sort's best case requires an early-stop optimization. Quick Sort's space complexity includes recursion-stack space.*

## 🧠 Important Notes

- **TC (Time Complexity):** Describes how an algorithm's running time grows with input size.
- **SC (Space Complexity):** Describes how much memory an algorithm needs. Here, auxiliary space means extra memory beyond the input array.
- **Stable Sorting:** Equal elements retain their original relative order.
- **In-place Sorting:** Uses little additional memory to rearrange elements.

## 🎓 Learning Goals

- Understand the working principles of sorting algorithms.
- Compare best, average, and worst-case complexities.
- Understand the difference between time and space complexity.
- Choose an appropriate sorting algorithm for different situations.

---

**Learn the logic. Analyze the complexity. Master DSA.** 🚀


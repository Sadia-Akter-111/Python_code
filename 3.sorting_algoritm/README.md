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

**Definition:** Insertion Sort builds a sorted portion of the

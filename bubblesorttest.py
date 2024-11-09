import unittest

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

class TestBubbleSort(unittest.TestCase):

    def test_positive_case(self):
        # Typical case: an unsorted array with distinct values
        arr = [64, 34, 25, 12, 22, 11, 90]
        sorted_arr = bubble_sort(arr[:])  # Pass a copy of arr to avoid modifying the original
        self.assertEqual(sorted_arr, [11, 12, 22, 25, 34, 64, 90])

    def test_negative_case(self):
        # Negative case: array with mixed data types should raise a TypeError
        arr = [64, "text", 25, 12]
        with self.assertRaises(TypeError):
            bubble_sort(arr)

    def test_performance_case(self):
        # Performance test: large array with numbers from 10000 down to 1
        large_arr = list(range(10000, 0, -1))  # Reverse sorted array
        sorted_arr = bubble_sort(large_arr[:])  # Pass a copy to avoid modifying the original
        self.assertEqual(sorted_arr, list(range(1, 10001)))

    def test_boundary_case(self):
        # Boundary cases: empty array, single element, duplicate values, already sorted, reverse sorted
        self.assertEqual(bubble_sort([]), [])  # Empty array
        self.assertEqual(bubble_sort([1]), [1])  # Single element
        self.assertEqual(bubble_sort([5, 5, 5, 5]), [5, 5, 5, 5])  # Duplicates
        self.assertEqual(bubble_sort([1, 2, 3, 4]), [1, 2, 3, 4])  # Already sorted
        self.assertEqual(bubble_sort([4, 3, 2, 1]), [1, 2, 3, 4])  # Reverse sorted

    def test_idempotency_case(self):
        # Idempotency: sorting an already sorted array multiple times should yield the same result
        arr = [2, 3, 7, 9, 14]
        sorted_once = bubble_sort(arr[:])  # First sort
        sorted_twice = bubble_sort(sorted_once[:])  # Second sort
        self.assertEqual(sorted_once, sorted_twice)

if __name__ == "__main__":
    unittest.main()
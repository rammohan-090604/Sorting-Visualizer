import random
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np

class SortingAlgorithms:
    def __init__(self):
        self.array = []

    def generate_random_array(self, size):
        self.array = random.sample(range(1, size + 1), size)

    def bubble_sort(self):
        n = len(self.array)
        for i in range(n - 1):
            for j in range(n - i - 1):
                if self.array[j] > self.array[j + 1]:
                    self.array[j], self.array[j + 1] = self.array[j + 1], self.array[j]
                    self.visualize()

    def insertion_sort(self):
        n = len(self.array)
        for i in range(1, n):
            key = self.array[i]
            j = i - 1
            while j >= 0 and self.array[j] > key:
                self.array[j + 1] = self.array[j]
                j -= 1
            self.array[j + 1] = key
            self.visualize()

    def selection_sort(self):
        n = len(self.array)
        for i in range(n):
            min_idx = i
            for j in range(i + 1, n):
                if self.array[j] < self.array[min_idx]:
                    min_idx = j
            self.array[i], self.array[min_idx] = self.array[min_idx], self.array[i]
            self.visualize()

    def quick_sort(self, low, high):
        if low < high:
            pivot = self.partition(low, high)
            self.quick_sort(low, pivot - 1)
            self.quick_sort(pivot + 1, high)

    def partition(self, low, high):
        pivot = self.array[high]
        i = low - 1
        for j in range(low, high):
            if self.array[j] < pivot:
                i += 1
                self.array[i], self.array[j] = self.array[j], self.array[i]
                self.visualize()
        self.array[i + 1], self.array[high] = self.array[high], self.array[i + 1]
        self.visualize()
        return i + 1

    def merge_sort(self, arr, l=0):
        if len(arr) > 1:
            mid = len(arr) // 2
            left_half = arr[:mid]
            right_half = arr[mid:]

            self.merge_sort(left_half, l)
            self.merge_sort(right_half, l + mid)

            i = j = k = 0

            while i < len(left_half) and j < len(right_half):
                if left_half[i] < right_half[j]:
                    arr[k] = left_half[i]
                    i += 1
                else:
                    arr[k] = right_half[j]
                    j += 1
                k += 1
                self.array[l + k - 1] = arr[k - 1]
                self.visualize()

            while i < len(left_half):
                arr[k] = left_half[i]
                i += 1
                k += 1
                self.array[l + k - 1] = arr[k - 1]
                self.visualize()

            while j < len(right_half):
                arr[k] = right_half[j]
                j += 1
                k += 1
                self.array[l + k - 1] = arr[k - 1]
                self.visualize()

    def visualize(self):
        plt.clf()
        norm = plt.Normalize(min(self.array), max(self.array))
        colors = cm.viridis(norm(self.array))
        plt.bar(range(len(self.array)), self.array, color=colors)
        plt.pause(0.5)

sorting = SortingAlgorithms()

while True:
    print("1. Bubble Sort, 2. Insertion Sort, 3. Selection Sort, 4. Quick Sort, 5. Merge Sort")
    print("Enter q to quit")

    raw_choice = input("Enter your choice: ")

    if raw_choice == 'q':
        break

    choice = int(raw_choice)
    array_size = int(input("Enter the size of the array: "))

    sorting.generate_random_array(array_size)

    if choice == 1:
        sorting.bubble_sort()
    elif choice == 2:
        sorting.insertion_sort()
    elif choice == 3:
        sorting.selection_sort()
    elif choice == 4:
        sorting.quick_sort(0, len(sorting.array) - 1)
    elif choice == 5:
        sorting.merge_sort(sorting.array)
    else:
        print("Invalid choice. Please try again.")
    
    plt.show(block=False)

# Sorting-Visualizer
Built an Sorting Visualizer using simple python script and gui (PyQt5).

This project is a Sorting Visualizer designed to help students understand various sorting algorithms through visualization. The visualizer provides an interactive and colorful way to observe how different sorting algorithms work step-by-step. This tool can be especially useful for teaching and learning sorting algorithms.

## Features

- Visualizes Bubble Sort, Insertion Sort, Selection Sort, Quick Sort, and Merge Sort.
- Assigns colors to bars based on their values for better visualization.
- Step-by-step visualization of each comparison and swap.
- Interactive interface to choose different sorting algorithms and array sizes.

## Usage

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/sorting-visualizer.git
    ```
2. Navigate to the project directory:
    ```bash
    cd sorting-visualizer
    ```
3. Install the required dependencies:
    ```bash
    pip install matplotlib numpy
    ```
4. Run the `sorting_visualizer.py` script:
    ```bash
    python sorting_visualizer.py
    ```

## How to Use

1. After running the script, you will be prompted to choose a sorting algorithm:
    ```
    1. Bubble Sort
    2. Insertion Sort
    3. Selection Sort
    4. Quick Sort
    5. Merge Sort
    Enter 'q' to quit
    ```
2. Enter the number corresponding to the sorting algorithm you want to visualize.
3. Enter the size of the array when prompted.
4. Watch the sorting algorithm in action as it sorts the array step-by-step with a visual representation.

## Code Overview

### SortingAlgorithms Class

This class contains the implementation of the sorting algorithms and the visualization logic.

- `generate_random_array(size)`: Generates a random array of the specified size.
- `bubble_sort()`: Implements Bubble Sort and visualizes each swap.
- `insertion_sort()`: Implements Insertion Sort and visualizes each insertion.
- `selection_sort()`: Implements Selection Sort and visualizes each selection.
- `quick_sort(low, high)`: Implements Quick Sort and visualizes each partitioning step.
- `partition(low, high)`: Helper method for Quick Sort to partition the array.
- `merge_sort(arr, l=0)`: Implements Merge Sort and visualizes each merge step.
- `visualize()`: Visualizes the current state of the array with colored bars.

### Main Loop

The main loop prompts the user to select a sorting algorithm and array size, then runs the chosen sorting algorithm on a randomly generated array of the specified size.

## Contributing

Contributions are welcome! If you have suggestions for improvements or new features, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

This project was created to help students learn sorting algorithms more effectively and to make the learning process more engaging and visually appealing.


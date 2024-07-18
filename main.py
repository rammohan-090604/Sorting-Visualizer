import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QComboBox, QPushButton, QWidget, QSpinBox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import random

class SortingVisualizer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sorting Visualizer")
        self.setGeometry(100, 100, 800, 600)
        
        self.main_widget = QWidget(self)
        self.setCentralWidget(self.main_widget)
        layout = QVBoxLayout(self.main_widget)

        # Dropdown for selecting the sorting algorithm
        self.algorithm_combo = QComboBox(self)
        self.algorithm_combo.addItem("Bubble Sort")
        self.algorithm_combo.addItem("Selection Sort")
        self.algorithm_combo.addItem("Insertion Sort")
        self.algorithm_combo.addItem("Merge Sort")
        self.algorithm_combo.addItem("Quick Sort")
        self.algorithm_combo.setStyleSheet("QComboBox { padding: 5px; }")
        layout.addWidget(self.algorithm_combo)

        self.input_box = QSpinBox(self)
        self.input_box.setMinimum(1)
        self.input_box.setMaximum(100)
        self.input_box.setValue(15)
        self.input_box.setStyleSheet("QSpinBox { padding: 5px; }")
        layout.addWidget(self.input_box)

        # Button for randomizing the array
        self.randomize_button = QPushButton("Randomize Array", self)
        self.randomize_button.clicked.connect(self.randomize_data)
        self.randomize_button.setStyleSheet("QPushButton { padding: 10px; background-color: #4CAF50; color: white; border: none; }"
                             "QPushButton:hover { background-color: #45a049; }")
        layout.addWidget(self.randomize_button)

        # Submit button
        self.submit_button = QPushButton("Sort", self)
        self.submit_button.clicked.connect(self.start_sorting)
        self.submit_button.setStyleSheet("QPushButton { padding: 10px; background-color: #f44336; color: white; border: none; }"
                         "QPushButton:hover { background-color: #d32f2f; }")
        layout.addWidget(self.submit_button)
        
        # Matplotlib canvas
        self.fig, self.ax = plt.subplots()
        self.canvas = FigureCanvas(self.fig)
        layout.addWidget(self.canvas)
        
        self.num_elements = self.input_box.value()
        self.data = self.generate_random_data(self.num_elements)
        self.plot_data()
        
    def generate_random_data(self, num_elements):
        return [random.randint(1, 100) for _ in range(num_elements)]
    
    def plot_data(self):
        self.ax.clear()
        self.ax.bar(range(len(self.data)), self.data, color='blue')
        for i, value in enumerate(self.data):
            self.ax.text(i, value, str(value), ha='center', va='bottom')
        self.canvas.draw()
        
    def randomize_data(self):
        self.num_elements = self.input_box.value()
        self.data = self.generate_random_data(self.num_elements)
        self.plot_data()
        
    def start_sorting(self):
        algorithm = self.algorithm_combo.currentText()
        if algorithm == "Bubble Sort":
            self.bubble_sort()
        elif algorithm == "Selection Sort":
            self.selection_sort()
        elif algorithm == "Insertion Sort":
            self.insertion_sort()
        elif algorithm == "Merge Sort":
            self.merge_sort()
        elif algorithm == "Quick Sort":
            self.quick_sort()
            
    def bubble_sort(self):
        data = self.data.copy()  # Create a copy to avoid modifying original data
        n = len(data)
        for i in range(n):
            for j in range(0, n-i-1):
                if data[j] > data[j+1]:
                    data[j], data[j+1] = data[j+1], data[j]
                    self.update_plot(data)
        
    def selection_sort(self):
        data = self.data.copy()
        n = len(data)
        for i in range(n):
            min_idx = i
            for j in range(i+1, n):
                if data[j] < data[min_idx]:
                    min_idx = j
            data[i], data[min_idx] = data[min_idx], data[i]
            self.update_plot(data)
            
    def insertion_sort(self):
        data = self.data.copy()
        n = len(data)
        for i in range(1, n):
            key = data[i]
            j = i - 1
            while j >= 0 and data[j] > key:
                data[j + 1] = data[j]
                j -= 1
            data[j + 1] = key
            self.update_plot(data)
            
    def merge_sort(self):
        data = self.data.copy()
        self._merge_sort(data, 0, len(data) - 1)
        self.update_plot(data)
    
    def _merge_sort(self, data, low, high):
        if low < high:
            mid = (low + high) // 2
            self._merge_sort(data, low, mid)
            self._merge_sort(data, mid + 1, high)
            self._merge(data, low, mid, high)
    
    def _merge(self, data, low, mid, high):
        left = data[low:mid+1]
        right = data[mid+1:high+1]
        i = j = 0
        k = low
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                data[k] = left[i]
                i += 1
            else:
                data[k] = right[j]
                j += 1
            k += 1
        
        # Copy the remaining elements of left and right subarrays
        while i < len(left):
            data[k] = left[i]
            i += 1
            k += 1
        
        while j < len(right):
            data[k] = right[j]
            j += 1
            k += 1
        
        # Update plot once after merging
        self.update_plot(data)
    
    def quick_sort(self):
        data = self.data.copy()
        self._quick_sort(data, 0, len(data) - 1)
        self.update_plot(data)
    
    def _quick_sort(self, data, low, high):
        while low < high:
            pivot = self._partition(data, low, high)
            self._quick_sort(data, low, pivot - 1)
            low = pivot + 1
        # Update plot after each partition step
        self.update_plot(data)
    
    def _partition(self, data, low, high):
        pivot = data[low]
        i = low + 1
        j = high
        while True:
            while i <= j and data[i] <= pivot:
                i += 1
            while i <= j and data[j] >= pivot:
                j -= 1
            if i <= j:
                data[i], data[j] = data[j], data[i]
            else:
                break
        data[low], data[j] = data[j], data[low]
        return j
        
    def update_plot(self, data):
        self.data = data
        self.plot_data()
        QApplication.processEvents()
        
if __name__ == "__main__":
    # Check if QApplication instance exists
    if not QApplication.instance():
        app = QApplication(sys.argv)
    else:
        app = QApplication.instance()
    window = SortingVisualizer()
    window.show()
    sys.exit(app.exec_())

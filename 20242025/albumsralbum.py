import random

class Sorter:
    def __init__(self):
        self.array = [random.randint(1, 20) for _ in range(10)]

    def insertion_sort(self):
        for i in range(1, len(self.array)):
            key = self.array[i]
            j = i - 1
            while j >= 0 and key < self.array[j]:
                self.array[j + 1] = self.array[j]
                j -= 1
            self.array[j + 1] = key

    def display_array(self):
        for number in self.array:
            print(number, end=' ')
        print()

if __name__ == "__main__":
    sorter = Sorter()
    print("Unsorted array:")
    sorter.display_array()
    
    sorter.insertion_sort()
    
    print("Sorted array:")
    sorter.display_array()

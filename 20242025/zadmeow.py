class ArraySorter:
    def __init__(self, input_array):
        self.input_array = input_array

    def find_min_index(self, end_index):
        min_index = 0
        for index in range(1, end_index + 1):
            if self.input_array[index] < self.input_array[min_index]:
                min_index = index
        return min_index

    def sort_array(self):
        for index in range(len(self.input_array) - 1, -1, -1):
            min_index = self.find_min_index(index)
            self.input_array[index], self.input_array[min_index] = self.input_array[min_index], self.input_array[index]

    def display_array(self):
        for element in self.input_array:
            print(element, end=' ')
        print()

def main():
    input_array = [int(input("Enter an element: ")) for _ in range(10)]
    array_sorter = ArraySorter(input_array)
    array_sorter.sort_array()
    array_sorter.display_array()

if __name__ == "__main__":
    main()
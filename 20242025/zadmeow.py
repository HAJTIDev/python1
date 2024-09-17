class ArraySorter:
    def __init__(self, array):
        self.array = array

    def getmaxindex(self, end):
        max_index = 0
        for i in range(1, end + 1):
            if self.array[i] > self.array[max_index]:
                max_index = i
        return max_index

    def sort(self):
        for i in range(len(self.array) - 1, -1, -1):
            max_index = self.getmaxindex(i)
            self.array[i], self.array[max_index] = self.array[max_index], self.array[i]

    def display(self):
        for element in self.array:
            print(element, end=' ')
        print()

def main():
    array = [int(input("Enter an element: ")) for _ in range(10)]
    sorter = ArraySorter(array)
    sorter.sort()
    sorter.display()

if __name__ == "__main__":
    main()

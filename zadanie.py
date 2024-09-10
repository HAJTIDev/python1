import random

def generate_array():
    return [random.randint(1, 100) for _ in range(50)]

def search_array(array, x):
    array.append(x)
    for i, element in enumerate(array):
        if element == x:
            if i == len(array) - 1:
                return "Element not found in the array."
            else:
                return f"Element found at index {i}."
    return "Element not found in the array."

def main():
    x = int(input("Enter the number to search: "))
    array = generate_array()
    result = search_array(array, x)
    print(f"Array: {', '.join(map(str, array[:-1]))}")
    print(result)

if __name__ == "__main__":
    main()
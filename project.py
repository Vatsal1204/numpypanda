import numpy as np

def create_array():
    print("Select the type of array to create:")
    print("1. 1D Array")
    print("2. 2D Array")
    print("3. 3D Array")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        elements = list(map(int, input("Enter elements for 1D array: ").split()))
        array = np.array(elements)
    elif choice == 2:
        rows = int(input("Enter number of rows: "))
        cols = int(input("Enter number of columns: "))
        elements = list(map(int, input(f"Enter {rows * cols} elements: ").split()))
        array = np.array(elements).reshape(rows, cols)
    elif choice == 3:
        depth = int(input("Enter depth: "))
        rows = int(input("Enter number of rows: "))
        cols = int(input("Enter number of columns: "))
        elements = list(map(int, input(f"Enter {depth * rows * cols} elements: ").split()))
        array = np.array(elements).reshape(depth, rows, cols)
    else:
        print("Invalid choice.")
        return None

    print("Array created successfully:")
    print(array)
    return array

def slicing(array):
    try:
        if array.ndim == 1:
            start, end = map(int, input("Enter range (start end): ").split())
            sliced_array = array[start:end]
        elif array.ndim == 2:
            start_row, end_row = map(int, input("Enter row range (start end): ").split())
            start_col, end_col = map(int, input("Enter column range (start end): ").split())
            sliced_array = array[start_row:end_row, start_col:end_col]
        elif array.ndim == 3:
            start_depth, end_depth = map(int, input("Enter depth range (start end): ").split())
            start_row, end_row = map(int, input("Enter row range (start end): ").split())
            start_col, end_col = map(int, input("Enter column range (start end): ").split())
            sliced_array = array[start_depth:end_depth, start_row:end_row, start_col:end_col]
        print("Sliced Array:")
        print(sliced_array)
    except:
        print("Invalid slicing input.")

def mathematical_operations(array):
    print("Choose a mathematical operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    choice = int(input("Enter your choice: "))

    elements = list(map(int, input(f"Enter {array.size} elements for the second array: ").split()))
    second_array = np.array(elements).reshape(array.shape)

    if choice == 1:
        result = array + second_array
    elif choice == 2:
        result = array - second_array
    elif choice == 3:
        result = array * second_array
    elif choice == 4:
        result = array / second_array
    else:
        print("Invalid choice")
        return

    print("Result:")
    print(result)

def combine_arrays(array):
    elements = list(map(int, input(f"Enter {array.size} elements for another array: ").split()))
    second_array = np.array(elements).reshape(array.shape)
    if array.ndim == 1:
        combined_array = np.hstack((array, second_array))
    else:
        combined_array = np.vstack((array, second_array))
    print("Combined Array:")
    print(combined_array)

def search_sort_filter(array):
    print("Choose an option:")
    print("1. Search a value")
    print("2. Sort the array")
    print("3. Filter values")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        value = int(input("Enter value to search: "))
        result = np.where(array == value)
        print(f"Value found at indices: {result}")
    elif choice == 2:
        sorted_array = np.sort(array, axis=None)
        print("Sorted Array:")
        print(sorted_array)
    elif choice == 3:
        threshold = int(input("Enter threshold value for filtering: "))
        filtered_array = array[array > threshold]
        print("Filtered values:")
        print(filtered_array)
    else:
        print("Invalid choice.")

def aggregate_statistics(array):
    print("Choose an aggregate/statistical operation:")
    print("1. Sum")
    print("2. Mean")
    print("3. Median")
    print("4. Standard Deviation")
    print("5. Variance")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Sum:", np.sum(array))
    elif choice == 2:
        print("Mean:", np.mean(array))
    elif choice == 3:
        print("Median:", np.median(array))
    elif choice == 4:
        print("Standard Deviation:", np.std(array))
    elif choice == 5:
        print("Variance:", np.var(array))
    else:
        print("Invalid choice")

def main():
    array = None 

    while True:
        print("\nChoose an option:")
        print("1. Create a Numpy Array")
        print("2. Perform Mathematical Operations")
        print("3. Combine or Split Arrays")
        print("4. Search, Sort, or Filter Arrays")
        print("5. Compute Aggregates and Statistics")
        print("6. Slice the Array")
        print("7. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            array = create_array()
        elif choice == 2 and array is not None:
            mathematical_operations(array)
        elif choice == 3 and array is not None:
            combine_arrays(array)
        elif choice == 4 and array is not None:
            search_sort_filter(array)
        elif choice == 5 and array is not None:
            aggregate_statistics(array)
        elif choice == 6 and array is not None:
            slicing(array)
        elif choice == 7:
            print("Exiting...")
            break
        else:
            print("Invalid choice or array not created yet.")

if __name__ == "__main__":
    main()
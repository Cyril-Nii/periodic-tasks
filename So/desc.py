entered_list = input("Enter your numbers separated by commas (e.g., 3,4,5,6,7):\n")
entered_list = [int(num) for num in entered_list.split(",")]  # Convert to integers

def sort_descending(arr):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] < arr[j]:  # Swap if next element is larger
                arr[i], arr[j] = arr[j], arr[i]

sort_descending(entered_list)

print("Descending order:", entered_list)
    


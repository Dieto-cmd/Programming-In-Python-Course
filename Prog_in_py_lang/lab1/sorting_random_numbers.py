import random 

def Bubble_sort(numbers):
    numbers = numbers.copy()
    n = len(numbers)
    for i in range(n):
        for j in range(n-i-1):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
    return numbers
def insertion_sort(numbers):
    numbers = numbers.copy()
    for i in range(1, len(numbers)):
        key = numbers[i]
        j = i - 1
        while j >= 0 and numbers[j] > key:
            numbers[j+1] = numbers[j]
            j -= 1
        numbers[j+1] = key
    return numbers

N = 19
numbers = [random.randint(1,100) for _ in range(N)]
print("Randomly generated numbers: ", numbers)
result = Bubble_sort(numbers)
print("Bubble Sorted numbers: ", result)
result = insertion_sort(numbers)
print("Insertion Sorted numbers: ", result)

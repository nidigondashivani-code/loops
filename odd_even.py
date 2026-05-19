nested_list = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

even_count = 0
odd_count = 0

for sublist in nested_list:      
    for num in sublist:          
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

print("Even numbers:", even_count)
print("Odd numbers:", odd_count)
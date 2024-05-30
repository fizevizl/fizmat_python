def sum_of_non_negative_elements(arr):
    total_sum = 0
    
    for num in arr:

        if num >= 0:
            
            total_sum += num
    
   
    return total_sum

array = [1, -2, 3, 4, -5, 6, 7, -8, 9]
result = sum_of_non_negative_elements(array)
print("Сума невід'ємних елементів масиву:", result)

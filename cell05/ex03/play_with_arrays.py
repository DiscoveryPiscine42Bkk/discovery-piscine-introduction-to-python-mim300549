

original_array = [2, 8, 8, 48, 8, 22, -12, 2]


new_array = list({num + 2 for num in original_array if num + 2 > 5})



print( original_array)
print( new_array)

initial_motorcycles = 1 
weeks = 2 
final_motorcycles = initial_motorcycles * (2 ** weeks)

left_without_motorcycles = final_motorcycles - initial_motorcycles

print("Кількість онуків без мотоциклів через", weeks, "тижні:", left_without_motorcycles)

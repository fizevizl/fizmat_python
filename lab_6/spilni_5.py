def count_children(girls, fence_height):
    girls_count = 0
    boys_count = 0

    for girl in girls:
        if girl + 10 <= fence_height:
            girls_count += 1
        else:
            boys_count += 1

    return girls_count, boys_count


fence_height = int(input("Введіть висоту паркану у сантиметрах: "))
children_heights = list(map(int, input("Введіть зріст дітей через пробіл: ").split()))

girls_count, boys_count = count_children(children_heights, fence_height)

print("Кількість дівчаток:", girls_count)
print("Кількість хлопчиків:", boys_count)

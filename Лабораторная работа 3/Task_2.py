# TODO Напишите функцию find_common_participants
def find_common_participants(first, second, div =","):
    first_set = set(first.split(div))
    second_set = set(second.split(div))
    result = list(first_set.intersection(second_set))
    result.sort()
    return result

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
print(find_common_participants(participants_first_group, participants_second_group, "|"))
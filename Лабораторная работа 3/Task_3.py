# TODO  Напишите функцию count_letters
def count_letters(text):
    text = text.lower()
    result = {}
    result["length"] = 0
    for let in text:
        if let.isalpha():
            if let in result:
                result[let] += 1
                result["length"] += 1
            else:
                result[let] = 1
                result["length"] += 1
    return result

# TODO Напишите функцию calculate_frequency
def count_frequency(letdict):
    num = letdict["length"]
    letdict.pop("length")
    for let in letdict:
        letdict[let] = round(letdict[let] / num, 2)
    return letdict

main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""

# TODO Распечатайте в столбик букву и её частоту в тексте
dictionary = count_frequency(count_letters(main_str))
for let in dictionary:
    if dictionary[let] == 0:
        print(let+":", "0.00")
    else:
        print(let + ":", dictionary[let])
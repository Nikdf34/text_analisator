def string_to_list(a):
    a = a.lower()
    punctuation = [',', ':', ';', '.', '!', '?']
    for i in punctuation:
        a = a.replace(i, '')
    words = a.split()
    return words
def longest_word(words):
    v = len(words[0])
    m = []
    b = words[0]
    for i in words:
        if len(i) >= v:
            v = len(i)
            b = i
    m.append(b)
    for i in words:
        if len(i) == v:
            m.append(i)
    m = list(set(m))
    return 'Самое/ые длинное/ые слово/а:', m
def shorts_word(words):
    vi = len(words[0])
    mi = []
    bi = words[0]
    for i in words:
        if len(i) <= vi:
            vi = len(i)
            bi = i
    mi.append(bi)
    for i in words:
        if len(i) == vi:
            mi.append(i)
    mi = list(set(mi))
    return 'Самое/ые короткое/ые слово/а:', mi
def unique_words(words):
    a = {}
    for i in words:
        if i not in a:
            a[i] = 1
        else:
            a[i] += 1
    return a
def unique_symbols(a):
    my_dict = {}
    for i in a:
        if i not in my_dict:
            my_dict[i] = 1
        else:
            my_dict[i] += 1
    return my_dict
# my_words = (string_to_list('моя логика решила,,? погул?ять ИлИ Пок,!УРить или или'))
# my_wordsen = ('моя логика решила,,? погул?ять ИлИ Пок,!УРить или или')
# print(unique_symbols(my_wordsen))
# print(unique_words(my_words))
# longest_word(my_words)
# shorts_word(my_words)
while True:
    a = input('Введите текст, который хотите обработать: ')
    if a == '':
        print('введите текст! Совсем забыли про это?!')
    else:
       break
с = (string_to_list(a))
while True:
    b = input('выберите действие: \n1 - самое длинное слово текста , 2 - самое короткое слово текста, 3 - посчитать количество каждого слова в тексте, 4 - посчитать количество каждого символа в тексте: ')
    if b == '1':

        print(longest_word(с))
        break
    elif b == '2':
        print(shorts_word(с))
        break
    elif b == '3':
        print(unique_words(с))
        break
    elif b == '4':
        print(unique_symbols(a))
        break
    else:
        print('А вы точно ввели правильную цифру?')
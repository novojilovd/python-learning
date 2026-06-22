import string

with open('text.txt', 'r') as text:
    try:
        a: object = text.read()
    except UnicodeDecodeError:
        print('UnicodeDecodeError')
    except:
        print('Something is wrong')
    else:
        symbol_count: int = 0 # Количество символов
        word: dict = {} # Словарь для сбора слов и их количества в тексте
        sentance_count: int = 0 # Количество предложений

        start_index: list = [False, 0] # Список для сохранения метки о начале обработки слова
                                       # и стартовой позиции слова

        for x in range(len(a)):
            match a[x]:
                case _ if (a[x] in string.punctuation or a[x] in string.whitespace):

                    if (a[x] in ['.', '!', '?'] or x == len(a) - 1) and start_index[0]:
                        # Если встречаем символ разделения предложения и до этого были печатные символы,
                        #  то +1 предложение
                        sentance_count += 1

                    if start_index[0]:
                        # Если встречаем знак пунктуации или пробел и до этого были печатные символы,
                        #  то добавляем слово в словарь, либо прибавляем 1 к количеству, если оно уже
                        #  есть в словаре
                        # Метку о начала слова меняем на False
                        if a[start_index[1]:x] not in word.keys():
                            word[a[start_index[1]:x]] = 1
                            start_index[0] = False
                        else:
                            word[a[start_index[1]:x]] += 1
                            start_index[0] = False


                case _ if a[x] not in string.punctuation:

                    symbol_count += 1
                    if not start_index[0]:
                        # Если до этого не встречались печатные символы, то ставим метку о начале слова
                        #  и сохраняем позицию первого символа в слове
                        start_index[0] = True
                        start_index[1] = x

                    if x == len(a) - 1:
                        #Также обрабатываем пограничный случай, если печатный символ стоит в конце строки
                        sentance_count += 1
                        if start_index[0]:
                            if a[start_index[1]:x + 1] not in word.keys():
                                word[a[start_index[1]:x + 1]] = 1
                                start_index[0] = False
                            else:
                                word[a[start_index[1]:x + 1]] += 1
                                start_index[0] = False


        if len(word.keys()) != 0:
            # Если в файле были данные, то продолжаем обработку
            word_count = 0
            position = 0
            for a in sorted(word.items(), key=lambda item: item[1], reverse=True):
                if a[1] != word_count:
                    word_count = a[1]
                    position += 1
                elif a[1] == word_count and position == 6:
                    continue

                if position == 6:
                    break
                print(f'Слово "{a[0]}" встречается {word_count} раз(а)')

            print(f'Количество символов: {symbol_count}')
            print(f'Количество предложений: {sentance_count}')

        else:
            # Иначе выводим сообщение об ошибке
            print('Файл пуст')
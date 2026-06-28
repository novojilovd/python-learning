import string

with open('text.txt', 'r') as text:
    try:
        checking_text: object = text.read()
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

        for symbol_index in range(len(checking_text)):
            match checking_text[symbol_index]:
                case _ if (checking_text[symbol_index] in string.punctuation or checking_text[symbol_index] in string.whitespace or checking_text[symbol_index] in string.digits):

                    if (checking_text[symbol_index] in ['.', '!', '?'] or symbol_index == len(checking_text) - 1) and start_index[0]:
                        # Если встречаем символ разделения предложения и до этого были печатные символы,
                        #  то +1 предложение
                        sentance_count += 1

                    if start_index[0]:
                        # Если встречаем знак пунктуации или пробел и до этого были печатные символы,
                        #  то добавляем слово в словарь, либо прибавляем 1 к количеству, если оно уже
                        #  есть в словаре
                        # Метку о начала слова меняем на False
                        if checking_text[start_index[1]:symbol_index] not in word.keys():
                            word[checking_text[start_index[1]:symbol_index]] = 1
                            start_index[0] = False
                        else:
                            word[checking_text[start_index[1]:symbol_index]] += 1
                            start_index[0] = False


                case _ if checking_text[symbol_index] not in string.punctuation:

                    symbol_count += 1
                    if not start_index[0]:
                        # Если до этого не встречались печатные символы, то ставим метку о начале слова
                        #  и сохраняем позицию первого символа в слове
                        start_index[0] = True
                        start_index[1] = symbol_index

                    if symbol_index == len(checking_text) - 1:
                        #Также обрабатываем пограничный случай, если печатный символ стоит в конце строки
                        sentance_count += 1
                        if start_index[0]:
                            if checking_text[start_index[1]:symbol_index + 1] not in word.keys():
                                word[checking_text[start_index[1]:symbol_index + 1]] = 1
                                start_index[0] = False
                            else:
                                word[checking_text[start_index[1]:symbol_index + 1]] += 1
                                start_index[0] = False


        if len(word.keys()) != 0:
            # Если в файле были данные, то продолжаем обработку
            word_count = 0
            position = 0
            for checking_text in sorted(word.items(), key=lambda item: item[1], reverse=True):
                if checking_text[1] != word_count:
                    word_count = checking_text[1]
                    position += 1
                elif checking_text[1] == word_count and position == 6:
                    continue

                if position == 6:
                    break
                print(f'Слово "{checking_text[0]}" встречается {word_count} раз(а)')

            print(f'Количество символов: {symbol_count}')
            print(f'Количество предложений: {sentance_count}')

        else:
            # Иначе выводим сообщение об ошибке
            print('Файл пуст')
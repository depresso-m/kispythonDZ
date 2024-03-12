def add_dots(text, phrase_length=3):
    # Разбиваем текст на предложения
    sentences = text.split('. ')

    # Создаем список для хранения фрагментов предложений с точками
    fragmented_sentences = []

    # Добавляем точки после каждой фразы в предложениях
    for sentence in sentences:
        phrases = sentence.split(' ')
        fragmented_phrases = []
        current_phrase = []
        for word in phrases:
            current_phrase.append(word)
            if len(current_phrase) == phrase_length:
                fragmented_phrases.append(' '.join(current_phrase))
                current_phrase = []
        if current_phrase:
            phrase = ' '.join(current_phrase)
            if '.' in phrase:
                fragmented_phrases.append(phrase)
            else:
                fragmented_phrases.append(phrase + '.')
        fragmented_sentences.extend(fragmented_phrases)

    # Объединяем фрагментированные предложения
    transformed_text = '. '.join(fragmented_sentences)

    transformed_text = transformed_text.replace(', ', '. ')

    transformed_text = transformed_text.replace(',.', '.')

    # Заменяем двойные точки на одиночные
    transformed_text = transformed_text.replace('..', ',')

    # Сводит к одинаковому количеству фрагментов в предложении (в моем случае к 5)
    dot_count = 0
    for index, char in enumerate(transformed_text):
        if char == ".":
            dot_count += 1
        elif char == ",":
            dot_count = 0

        if dot_count >= 5:
            transformed_text = transformed_text[:index] + ' ' + transformed_text[index + 1:]
            dot_count = 0
    return transformed_text

def create_table(text):
    # Разбиваем текст на предложения
    sentences = text.split(',')

    # Создаем список для групп предложений
    groups = [[] for _ in range(max(len(sentence.split('.')) for sentence in sentences))]

    # Добавляем предложения в соответствующие группы
    for sentence in sentences:
        parts = sentence.strip().split('.')
        for i, part in enumerate(parts):
            groups[i].append(part.strip())

    # Выводим таблицу
    print("Таблица:")
    for i, group in enumerate(groups, start=1):
        print(f"{i}")
        print('\n'.join(group))
        print()

original_text1 = """
Следовательно, ускорение блокчейн-транзакций расширяет горизонты универсальной коммодитизации знаний и компетенций. 
Вместе с тем, прагматичный подход к цифровым платформам не оставляет шанса для нормативного регулирования непроверенных гипотез. 
Следовательно, прагматичный подход к цифровым платформам повышает вероятность бюджетного финансирования волатильных активов.
"""

original_text2 = """
Тем не менее, парадигма цифровой экономики открывает новые возможности практического применения цифровых следов граждан. 
Соответственно, совокупность сквозных технологий открывает новые возможности универсальной коммодитизации волатильных активов. 
Следовательно, программа прорывных исследований несёт в себе риски практического применения государственно-частных партнёрств.
"""

original_text3 = """
Коллеги, совокупность сквозных технологий повышает вероятность нормативного регулирования опасных экспериментов. 
С другой стороны, совокупность сквозных технологий несёт в себе риски нормативного регулирования внезапных открытий. 
Тем не менее, совокупность сквозных технологий открывает новые возможности несанкционированной кастомизации опасных экспериментов. 
"""
transformed_text = add_dots(original_text1)
print(transformed_text)

create_table(transformed_text)
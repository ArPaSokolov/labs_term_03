import pymorphy2

sentence1, noun = "Если б не было {noun}, не видали б снега мы.", "зима"
sentence2, adjective = "{adjective} человека Кузиком не назовут!", "хороший"
sentence3, verb = "{verb} дальше, у вас неплохо получается.", "пить"

morph = pymorphy2.MorphAnalyzer()
noun_form = morph.parse(noun)[0].inflect({'gent'}).word # меняем форму слова
verb_form = morph.parse(verb)[0].inflect({'impr', 'plur'}).word.title()
adjective_form = morph.parse(adjective)[0].inflect({'accs'}).word.title() # меняем форму слова + с прописной

# Подставляем слово в предложение
print(sentence1.format(noun=noun_form))
print(sentence2.format(adjective=adjective_form))
print(sentence3.format(verb=verb_form))

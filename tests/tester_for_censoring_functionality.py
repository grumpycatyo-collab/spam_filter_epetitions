from utils.similarity import is_it_similar
route = 'data\modified_words.txt'
with open(route, 'r', encoding='utf-8') as file:
    words = file.read().splitlines()

errors = []
for word in range(100000):
    if is_it_similar(words[word]):
        errors.append(words[word])

with open('data\sewarradawoedds.txt', 'w', encoding='utf-8') as file:
    for err in errors:
        file.write(err + '\n')
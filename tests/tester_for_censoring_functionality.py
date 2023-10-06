from utils.similarity import is_it_similar
# route = r'C:\Users\Max\spam_filter_epetitions\data\modified_words.txt'
# with open(route, 'r', encoding='utf-8') as file:
#     words = file.read().splitlines()
#
# errors = []
# for word in words:
#     if is_it_similar(word):
#         errors.append(word)
str = "пизд"
print(is_it_similar(str))

#
# with open(r'C:\Users\Max\spam_filter_epetitions\data\sewarradawoedds.txt', 'w', encoding='utf-8') as file:
#     for err in errors:
#         file.write(err + '\n')
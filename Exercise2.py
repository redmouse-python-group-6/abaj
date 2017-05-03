# Написать программу для поиска самого длинного слова в строке, разделенной пробелами.


str = "Введите любую строку, чтобы найти самое длинное слово"
words = str.split()
len_max = 0
max_len_word=""
for word in words:
    if len_max < len(word):
        len_max = len(word)
        max_len_word = word
print ("Самое длинное слово'%s' длина %d символов" % (max_len_word, len_max))


# Написать программу поиска самого длинного слова в строке,разделенной точкой запятой.


str="Написать,программу,чтобы,найти,самое,длинное,слово,в,строке"
words=str.split(',')
len_max=0
max_len_word=""
for word in words:
	if len_max < len_(word):
		len_max = len(word)
		max_len_word=word
print("Самое длинное слово '%s' длина %d символов " % (max_len_word, len_max))


# Написать программу самого короткого слова который выделяется знаком который пользователь вводит


str_in = input("Введите строку:\n")
word_in = input("Введите слов которое нужно найти:\n")
words = str_in.split()
is_word = false
for word in words:
	if word == word_in:
		is_word= true
if is_word:
	print("Введенное вами слово '%s' существует в строке" % word_in)
else:
	print("Введеное вами слово '%s' не найдено" % word_in)


#Посчитать кол-во слов в предложении которое вводит пользователь

str_in = input ("Введите строку")
words = str_in.split('')
count_Words = 0
for word in words:
	count_words +=1
print("Количество слов в строке равна %d"% count_words)
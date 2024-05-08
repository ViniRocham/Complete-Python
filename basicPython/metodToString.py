
mensage = 'I Love to play soccer'
mensageSpace = '          I Love to play soccer'


#lower case
print(mensage.lower())

#upper case
print(mensage.upper())

#only first upper string
print(mensage.capitalize())

#find the string in the sentence
print(mensage.find('a'))

#find the initial string of the word in the sentence
print(mensage.find('play'))

#change string/word to another string/word
print(mensage.replace('o', 'e'))
print(mensage.replace('Love', "don't love"))

#exclude white spaces at the beginning of the sentence
print(mensageSpace.strip())
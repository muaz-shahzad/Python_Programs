import random
import string

word = input("Type any sentence: ")
words_list = word.split(" ")
coded_word = []
decoded_word_list = []

def generate_random_letters(length):
    random_letters = random.choices(string.ascii_letters, k=length)
    return ''.join(random_letters)


def encodingWord(words_list):
    for word in words_list:
        if len(word) >= 3:
            random_char1 = generate_random_letters(3)
            random_char2 = generate_random_letters(3)
            final = word[1:] + word[0]
            new_text = random_char1.swapcase() + final + random_char2.swapcase()
            final_text = new_text.swapcase()
            coded_word.append(final_text)
        else:
            coded_word.append(word[::-1])

    return " ".join(coded_word)


result = encodingWord(words_list)
print(f"\nEncoding Message: {result}")

def decodingWord(result):
    d = result.split(" ")
    for value in d:
        if len(value) >= 3:
            d_word = value[3:-3]
            decoding_word = d_word[-1] + d_word[0:-1]
            decode_Final = decoding_word.swapcase()
            decoded_word_list.append(decode_Final)
        else:
            decoded_word_list.append(value[::-1])
    return " ".join(decoded_word_list)



opt = input("\nFor Decode Sentence Press 1: ")
if opt == "1":
    decode = decodingWord(result)
    print(f"\nDecoded Message: {decode}")
else:
    print("Good Bye")



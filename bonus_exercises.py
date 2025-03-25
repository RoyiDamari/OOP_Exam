# question 1

numbers = [1, 1, 10, 10, 9, 9, 5, 5, 6, 8, 8]

for i in range(0, len(numbers) - 1, 2):

    if numbers[i] != numbers[i + 1]:
        print("The number without a pair is:", numbers[i])
        break

else:
    print("The number without a pair is:", numbers[-1])


# question 2

words = ["java", "jjava", "vaj", "aavj", "j", "vjaa", "dan", "and", "ddan"]
words_count = {}

for word in words:
    sorted_word_list = sorted(word)
    sorted_word_str = " ".join(sorted_word_list)

    if sorted_word_str not in words_count:
        words_count[sorted_word_str] = 0
    words_count[sorted_word_str] += 1

print(words_count)












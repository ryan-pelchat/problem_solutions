"""
https://open.kattis.com/problems/meanwords

Little Timmy got caught by his teacher using some mean words. After getting sent to the principal, little Timmy learned his lesson - he should do his best to not get caught next time!

What Timmy decided to do is to take all the mean words that he wants to say, and combine them all together into a single "mean" word by getting the average of all the characters in the same position across all the words that have a character in that position, and then rounding this average down to get the character in that position.

Note: The value of a character is its ASCII value, so the value of a is 
, the value of b is 
 and so on up to z, which has value 
. So when we average characters, we are averaging their ASCII values, rounding this down to the nearest integer, and then using the corresponding character as the result of this averaging.

Help Timmy create his mean mean words!

"""

numWords = int(input())

words = []
for i in range(numWords):
    word = input()  # get word
    while len(words) < len(
        word
    ):  # make sure that there are enough lists in words to accomodate the values in word
        words.append([])
    for j in range(len(word)):  # add the characters to the correct list in words
        words[j].append(ord(word[j]))  # append the ACII value to correct list in words

newMeanWord = ""
for word in words:  # compute the average of each list in words
    newMeanWord += chr(sum(word) // len(word))  # append the character to newMeanWord

print(newMeanWord)  # output the new mean word

sentence = input("Please enter a sentence: ").strip(" ").strip(",").strip("-").upper()  # enter the sentence and erase the blanks and commas
count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
index = 0
for ch in sentence:             # for loop to find the frequency of letters
    index = abc.find(ch)
    if index >= 1:
        count[index] += 1
maximum = 0         # finding in the list abc which letter is most frequent
for i, value in enumerate(count):
    if value > maximum:
        maximum = value
        index_1 = i
print("The most common letter is", abc[index_1])        # printing the most common

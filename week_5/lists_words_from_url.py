from urllib.request import urlopen

url = "https://www.mit.edu/~ecprice/wordlist.10000"
word_list = urlopen(url).read().splitlines()  #get the list

total_words = len(word_list) #count how many words
total_length = 0 # unknown total length
counters = [0] * 23 #counter for word length from 1-22

for word in word_list:
    word_length = len(word) #counts the length of per word (index) in the list of words
    total_length += word_length # count full length by going through the whole list
    counters[word_length] += 1 #increases the count for this length word in the counters list

average_length = total_length / total_words #divide the whole length of the words of the list with the total word count

print(f"{total_words} words") #total words

print(f"The average word length is {average_length}") #average length throughout the words

print(f"Length Count")  #how many words of this length
for i in range(1, 23):
   if counters[i] >= 0:
    print(f"{i:6d}{counters[i]:6d}")




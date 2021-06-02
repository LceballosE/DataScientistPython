# ---------- WEEK 3
#rainfall_mi is a string that contains the average number of inches of rainfall in Michigan for every month (in inches) with every month separated by a comma. Write code to compute the number of months that have more than 3 inches of rainfall. Store the result in the variable num_rainy_months. In other words, count the number of items with values > 3.0. Hard-coded answers will receive no credit.

rainfall_mi = "1.65, 1.46, 2.05, 3.03, 3.35, 3.46, 2.83, 3.23, 3.5, 2.52, 2.8, 1.85"
num_rainy_months = 0

rainfall_list = rainfall_mi.split(", ")

for item in rainfall_list:
    if float(item)>3:
        num_rainy_months = num_rainy_months +1


# The variable sentence stores a string. Write code to determine how many words in sentence start and end with the same letter, including one-letter words. Store the result in the variable same_letter_count. Hard-coded answers will receive no credit.

sentence = "students flock to the arb for a variety of outdoor activities such as jogging and picnicking"
same_letter_count =0
sentence_list = sentence.split(" ")
count_words = 0

for item in sentence_list:
    word = list()
    for char in item:
        word.append(char)
    print(word)    
    word_end = word[-1]
    word_start = word[0]
    if word_start ==word_end:
        same_letter_count =same_letter_count + 1

# Write code to count the number of strings in list items that have the character w in it. Assign that number to the variable acc_num. 
# HINT 1: Use the accumulation pattern!
# HINT 2: the in operator checks whether a substring is present in a string.
# Hard-coded answers will receive no credit.
	
items = ["whirring", "wow!", "calendar", "wry", "glass", "", "llama","tumultuous","owing"]
acc_num=0
for item in items:
    if "w" in item:
        acc_num=acc_num+1
	        


#Write code that counts the number of words in sentence that contain either an “a” or an “e”. Store the result in the variable num_a_or_e.
#Note 1: be sure to not double-count words that contain both an a and an e.
#HINT 1: Use the in operator.
#HINT 2: You can either use or or elif.
#Hard-coded answers will receive no credit.


sentence = "python is a high level general purpose programming language that can be applied to many different classes of problems."
num_a_or_e = 0

sentence_list = sentence.split(" ")   # puedo separarlo y manejar una lista o directamente en el for recorrer la cadena  - ejemplo siguiente. 

for item in sentence_list:
    if "a" in item:
        num_a_or_e =num_a_or_e+1
    elif "e" in item:
        num_a_or_e =num_a_or_e+1


#Write code that will count the number of vowels in the sentence s and assign the result to the variable num_vowels. For this problem, vowels are only a, e, i, o, and u. Hint: use the in operator with vowels.

s = "singing in the rain and playing in the rain are two entirely different situations but both can be fun"
vowels = ['a','e','i','o','u']
num_vowels =0
# Write your code here.
for item in s:
    if item in vowels:
        num_vowels=num_vowels+1


# ----------   Week 4

#Write code to add ‘horseback riding’ to the third position (i.e., right before volleyball) in the list sports.

sports = ['cricket', 'football', 'volleyball', 'baseball', 'softball', 'track and field', 'curling', 'ping pong', 'hockey']

sports.insert(2,"horseback riding")

print(sports)


#Write code to take ‘London’ out of the list trav_dest.

trav_dest = ['Beirut', 'Milan', 'Pittsburgh', 'Buenos Aires', 'Nairobi', 'Kathmandu', 'Osaka', 'London', 'Melbourne']
trav_dest.pop(-2)

#Write code to add ‘Guadalajara’ to the end of the list trav_dest using a list method.

trav_dest = ['Beirut', 'Milan', 'Pittsburgh', 'Buenos Aires', 'Nairobi', 'Kathmandu', 'Osaka', 'Melbourne']
trav_dest.append("Guadalajara")


#Write code to rearrange the strings in the list winners so that they are in alphabetical order from A to Z.

winners = ['Kazuo Ishiguro', 'Rainer Weiss', 'Youyou Tu', 'Malala Yousafzai', 'Alice Munro', 'Alvin E. Roth']
winners.sort()


#Write code to switch the order of the winners list so that it is now Z to A. Assign this list to the variable z_winners.

winners = ['Alice Munro', 'Alvin E. Roth', 'Kazuo Ishiguro', 'Malala Yousafzai', 'Rainer Weiss', 'Youyou Tu']
z_winners = list()
winners.sort(reverse=True)
z_winners = winners

#Currently there is a string called str1. Write code to create a list called chars which should contain the characters from str1. Each character in str1 should be its own element in the list chars.

str1 = "I love python"
# HINT: what's the accumulator? That should go here.
chars =list()
for item in str1:
    chars.append(item)

#For each character in the string saved in ael, append that character to a list that should be saved in a variable app.
	
ael = "python!"

app=list()

for item in ael:
    app.append(item)

#For each string in wrds, add ‘ed’ to the end of the word (to make the word past tense). Save these past tense words to a list called past_wrds.
	
wrds = ["end", 'work', "play", "start", "walk", "look", "open", "rain", "learn", "clean"]

past_wrds =list()

for item in wrds:
    past_wrds.append(item+"ed")

#Below are a set of scores that students have received in the past semester. Write code to determine how many are 90 or above and assign that result to the value a_scores.

scores = "67 80 90 78 93 20 79 89 96 97 92 88 79 68 58 90 98 100 79 74 83 88 80 86 85 70 90 100"
score_list= scores.split(" ")
a_scores=0
for score in score_list:
    if int(score)>=90:
        a_scores=a_scores+1

#Write code that uses the string stored in org and creates an acronym which is assigned to the variable acro. Only the first letter of each word should be used, each letter in the acronym should be a capital letter, and there should be nothing to separate the letters of the acronym. Words that should not be included in the acronym are stored in the list stopwords. For example, if org was assigned the string “hello to world” then the resulting acronym should be “HW”.

stopwords = ['to', 'a', 'for', 'by', 'an', 'am', 'the', 'so', 'it', 'and', "The"]
org = "The organization for health, safety, and education"
acro=""
org_list = org.split(" ")

for word in stopwords:
    if word in org_list:
        org_list.pop(org_list.index(word))
        # print(org_list)

for item in org_list:
    char=item[0]    
    acro=acro+char.upper()
	
	
#Write code that uses the string stored in sent and creates an acronym which is assigned to the variable acro. The first two letters of each word should be used, each letter in the acronym should be a capital letter, and each element of the acronym should be separated by a “. ” (dot and space). Words that should not be included in the acronym are stored in the list stopwords. For example, if sent was assigned the string “height and ewok wonder” then the resulting acronym should be “HE. EW. WO”.
	
stopwords = ['to', 'a', 'for', 'by', 'an', 'am', 'the', 'so', 'it', 'and', 'The']
sent = "The water earth and air are vital"

acro=""
sent_list = sent.split(" ")

for word in stopwords:
    if word in sent_list:
        sent_list.pop(sent_list.index(word))
        print(sent_list)

for item in sent_list:
    char=item[0:2] 
    if sent_list.index(item) < len(sent_list)-1:         
        acro=acro+char.upper()+ ". "
    else:
        acro=acro+char.upper()


#A palindrome is a phrase that, if reversed, would read the exact same. Write code that checks if p_phrase is a palindrome by reversing it and then checking if the reversed version is equal to the original. Assign the reversed version of p_phrase to the variable r_phrase so that we can check your work.
	
p_phrase = "was it a car or a cat I saw"
r_phrase= p_phrase[::-1] # todo el texto empezando por el final

if p_phrase == r_phrase:
    print("it is palindrome")
else:
    print("it is not palindrome")
	
	
#Provided is a list of data about a store’s inventory where each item in the list represents the name of an item, how much is in stock, and how much it costs. Print out each item in the list with the same formatting, using the .format method (not string concatenation). For example, the first print statment should read The store has 12 shoes, each for 29.99 USD.

inventory = ["shoes, 12, 29.99", "shirts, 20, 9.99", "sweatpants, 25, 15.00", "scarves, 13, 7.75"]

text=list()
for item in inventory:
    text=item.split(", ")
    print("The store has {} {}, each for {} USD.".format(text[1],text[0],text[2]))


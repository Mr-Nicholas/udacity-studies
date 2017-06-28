import urllib

''' This simple program reads a .txt file and removes common profanities'''

# save a list of profane words

# take input from a user

# convert the input to a string

# if the input contains one of the profane words, remove it

# print the sanitised input to the screen


def read_txt():
    quotes = open("/Users/Heath/apps/udacity-studies/python-intro/profanity-editor/quotes.txt")
    file_contents = quotes.read()
    print(file_contents)
    quotes.close()
    test_profanity(file_contents)

def test_profanity(text_to_check):
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q="+text_to_check)
    output = connection.read()
   # print(output)
    connection.close()

    if "true" in output:
        print("Profanity has been detected.")
    elif "false" in output:
        print("No profanity has been found.")
    else:
        print("Error in scanning file provided.")
    
read_txt()

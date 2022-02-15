"""
Copyright 2022

Licensed under the GNU General Public License, Version 3.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

https://www.gnu.org/licenses/gpl-3.0.en.html

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

# Import


# Constants

LETTER = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

STOP_WORDS = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 
'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 
'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', 
"she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 
'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 
'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 
'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 
'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 
'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 
'about', 'against', 'between', 'into', 'through', 'during', 'before', 
'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 
'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 
'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 
'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 
'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 
'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 
'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', 
"couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 
'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', 
"mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 
'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', 
"won't", 'wouldn', "wouldn't"]
#the most common words gathered from a variety of dictionaries

# Functions

def Contain(file_name):
    """
    -------------------------------------------------------
    
    Use: list_of_words = Contain(file_name)
    -------------------------------------------------------
    Parameters:
       x
    Returns:
       x
    ------------------------------------------------------
    """
    handle_file = open(file_name, "r", encoding="utf8")
    
    list_of_words = extractText(handle_file)

    clean_list = Not_for_use(list_of_words)

    handle_file.close() # Close File handle

    return clean_list



def extractText(handle_file):
    """
    -------------------------------------------------------
    
    Use: words = extractText(handle_file)
    -------------------------------------------------------
    Parameters:
       x
    Returns:
       x
    ------------------------------------------------------
    """

    a = handle_file.read() # Reading File Content
    string = "" # Intializing String
    i = 0

    a = remove(a) # Remove Scripts from HTML File
    a = removecss(a)

    while i < len(a):
        # Skip HTML tags so that they are not concatenated to string
        if a[i] == '<':
            while a[i] != '>':
                i += 1
            
            i += 1

        # Only execute if it is an alphabet or space
        elif i < len(a)  and (a[i] in LETTER or a[i].isspace() == True):     
            string += a[i].lower() # Concatenate characters from string 'a' to string 'string'
            # print(a[i], end="") # Printing string (Testing only)
            i += 1
            
        # Move to next character
        else:
            i += 1

    string = removebin(string) # Removing Garbage and Punctuations

    list_of_words = string.split(" ") # Converting string to a Word List
    list_of_words = ' '.join(list_of_words).split() # Removing empty List Objects
    
    return list_of_words



def removebin(string):
    """
    -------------------------------------------------------
    
    Use: removebin(string)
    -------------------------------------------------------
    Parameters:
       x
    Returns:
       x
    ------------------------------------------------------
    """
    string = string.strip()

    # Removing all the symbols
    string = string.replace("`", "").replace("~", "").replace("!", "").replace("@", "").replace("#", "").replace("$", "").replace("%", "")
    string = string.replace("^", "").replace("&", "").replace("*", "").replace("(", "").replace(")", "").replace("-", "").replace("_", "")
    string = string.replace("+", "").replace("=", "").replace("[", "").replace("]", "").replace("{", "").replace("}", "").replace(".", "")
    string = string.replace(";", "").replace(":", "").replace("|", "").replace("?", "").replace(",", "").replace("<", "").replace(">", "")
    string = string.replace("\n", " ")
    string = string.replace("\t", " ")

    return string



def remove(string):
    """
    -------------------------------------------------------
    Remove HTML Scripts from given string
    Use: string = remove(string)
    -------------------------------------------------------
    Parameters:
       x
    Returns:
       x
    ------------------------------------------------------
    """

    x = len(string) // 30

    # Loop till all script tags are removed
    for _ in range(x):
        if "<script" in string:
            starting_index = string.find("<script") 
            ending_index = string.find("</script>")
            string = string[:starting_index] + string[ending_index+9:]

    return string



def Not_for_use(list_of_words):
    """
    -------------------------------------------------------
    Remove Stop Words from given list_of_words
    Use: list_of_words = Not_for_use(list_of_words)
    -------------------------------------------------------
    Parameters:
       x
    Returns:
       x
    ------------------------------------------------------
    """
    new_list = []

    for i in list_of_words:
        if i not in STOP_WORDS:
            new_list.append(i) # Adding to new_list

    return new_list



def removecss(string):
    """
    -------------------------------------------------------
    Remove HTML Styles from given string
    Use: string = removecss(string)
    -------------------------------------------------------
    Parameters:
       x
    Returns:
       x
    ------------------------------------------------------
    """

    x = len(string) // 30

    for _ in range(x):
        if "<style" in string:
            starting_index = string.find("<style")
            ending_index = string.find("</style>")
            string = string[:starting_index] + string[ending_index+8:]

    return string
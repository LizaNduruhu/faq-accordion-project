# We first define this function that will capitalize words in a string.
def capitalize_words(input_string):
    # The string method .split() breaks the string into a list of words.
    words = input_string.split()
    
    # capitalize() method capitalizes the first letter of a word and lowers the rest.
    capitalized_words = [word.capitalize() for word in words]
    
    # The string method .join() combines the words back into a single string.
    result = " ".join(capitalized_words)
    
    return result

# Prompt the user to input their own sentence.
user_input = input("Enter a sentence: ")

# Here we call the function and display the result of what the user has inputed.
result = capitalize_words(user_input)
print("Capitalized sentence:", result)

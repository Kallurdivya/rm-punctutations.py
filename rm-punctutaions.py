import string 
test_str = input("Enter your string: \n") 
test_str = test_str.translate(str.maketrans('', '', string.punctuation)) 
print(test_str)
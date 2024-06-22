
import string
import random

def GenerateRandom_Password(length, nums, special_symbols) :
    pwd = ""
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation
    
    characters = letters
    if nums == True :
        characters += digits
    if special_symbols == True :
        characters += special
        
    meets_requirements = False
    has_number = False 
    has_special = False
    
    while (meets_requirements == False) or (len(pwd) <= length) :
        new_char = random.choice(characters)
        pwd += new_char
        
        if new_char in digits :
            has_number = True
        elif new_char in special :
            has_special = True
        
        meets_requirements = True
        if nums == True :
            meets_requirements = has_number
        if special_symbols == True :
            meets_requirements = meets_requirements and has_special
        
    return pwd
if __name__ == "__main__" :
    length = int(input("Enter The Length of Your Password \n(Should be Greater than 6): "))
    pwd = ""
    while length > 5 and length <=15 :
        choice = int(input("Select your Choice:\n  1.EASY\n  2.MEDIUM\n  3.HARD\n"))
        if choice == 1 :
            pwd = GenerateRandom_Password(length, False, False)
            break
        elif choice == 2 :
            pwd = GenerateRandom_Password(length, True, False)
            break
        elif choice == 3 :
            pwd = GenerateRandom_Password(length, True, True)
            break
        else :
            print("Choice Correct Difficulty Level....")
            continue
    if length <= 5 or length > 15 :
        print("Length Didnt reached the Requirements")
    print(pwd)
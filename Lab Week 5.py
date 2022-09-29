########################################################################
##
## CS 101 Lab
## Program 5
## Name Jason Nguyen
## Email jqn2mn@umsystem.edu
##
## PROBLEM : Linda Hall Library Card System
##
## ALGORITHM : 
##      1. Write out the algorithm
## 
## ERROR HANDLING:
##      Any Special Error handling to be noted.  Wager not less than 0. etc
##
## OTHER COMMENTS:
##      Any special comments
##
########################################################################

import string

def get_school(card):
    value6 = int(card[5])
    if value6 == 1:
        return "School of Computing and Engineering SCE"
    elif value6 == 2:
        return "School of Law"
    elif value6 == 3:
        return "College of Arts and Sciences"
    else:
        return "Invalid School"

    
def get_grade(card):
    value7 = int(card[6])
    if value7 == 1:
        return "Freshman"
    elif value7 == 2:
        return "Sophomore"
    elif value7 == 3:
        return "Junior"
    elif value7 == 4:
        return "Senior"
    else:
        return "Invalid Grade"
    
def verify_check_digit(card):
    if len(card) != 10:
        print("Library card is invalid.")
        print("The length of the number given must be 10")
        return False
    if len(card) == 10:
        return True

    char1 = card[0]
    char2 = card[1]
    char3 = card[2]
    char4 = card[3]
    char5 = card[4]
    char6 = card[5]
    char7 = card[6]
    char8 = card[7]
    char9 = card[8]
    char10 = card[9]
    a1 = char1.isalpha()
    a2 = char2.isalpha()
    a3 = char3.isalpha()
    a4 = char4.isalpha()
    a5 = char5.isalpha()
    num3 = char8.isnumeric()
    num4 = char9.isnumeric()
    num5 = char10.isnumeric()
    
    if a1 or a2 or a3 or a4 or a5 == False:
        if a1 == False:
            index = 0
            char = char1
            print(f"The first 5 characters must be A-Z, the invalid character is at {index} is {char}")
            return False
        elif a2 == False:
            index = 1
            char = char2
            print(f"The first 5 characters must be A-Z, the invalid character is at {index} is {char}")
            return False
        elif a3 == False:
            index = 2
            char = char3
            print(f"The first 5 characters must be A-Z, the invalid character is at {index} is {char}")
            return False
        elif a4 == False:
            index = 3
            char = char4
            print(f"The first 5 characters must be A-Z, the invalid character is at {index} is {char}")
            return False
        elif a5 == False:
            index = 4
            char = char5
            return False
        else:
            if num3 or num4 or num5 == False:
                if num3 == False:
                    index = 7
                    num = char8
                    print(f"The last 3 characters must be 0-9, the invalid character is at {index} is {num}")
                elif num4 == False:
                    index = 8
                    num = char9
                    print(f"The last 3 characters must be 0-9, the invalid character is at {index} is {num}")
                elif num5 == False:
                    index = 9
                    num = char10
                    print(f"The last 3 characters must be 0-9, the invalid character is at {index} is {num}")
                else:
                    if int(char6) != 1 or 2 or 3:
                        print("The sixth character must be 1 2 or 3")
                        return False
                    elif int(char7) != 1 or 2 or 3 or 4:
                        print("The sixth character must be 1 2 3 or 4")
                        return False
                    else:
                        return True


if __name__ == "__main__":

    print(f"{'Linda Hall':^80}")
    print(f"{'Library Card Check':^80}")
    print(f"{'===========================================================':^80}")

    
    card = input("\nEnter Library Card. Hit Enter to Exit ==> ")

    check = verify_check_digit(card)
    while check == False:
        card = input("\nEnter Library Card. Hit Enter to Exit ==> ")
        print("Library card is invalid.")
        check = verify_check_digit(card)

    school = get_school(card)
    grade = get_grade(card)

    if check == True:
        print("Library card is valid.")
        print(f"This card belong to a student in {school}")
        print(f"The card belongs to a {grade}")
        

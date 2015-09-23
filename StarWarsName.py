# Author - Joshua Schoonmaker
# StarWarsName.py
# CIS 125 IWU
# Week 3 Star Wars Name Assignment

# 

def main():
    
    # Initial input requests
    
    strFirstName = input("Please enter your first name: ")
    strLastName = input("Please enter your last name: ")
    strMaidenName = input("Please enter your mother's maiden name: ")
    strBirthCity = input("Please enter the name of the city in which you were born: ")
    print()
    
    # Setting chopped inputs to new variables
    
    a = strFirstName[0:2]
    b = strLastName[0:3]
    c = strMaidenName[0:2]
    d = strBirthCity[0:3]
    
    # Adding together new variables
    
    print(b + a, c + d)
    
main()
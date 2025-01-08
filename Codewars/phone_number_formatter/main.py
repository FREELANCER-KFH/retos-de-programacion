'''
In this project, I developed a solution that returns a number but in a phone number format.
This project is part of the kata chanllenges in CodeWars for Python beginners.
Att: Kevin Feliz Henríquez.
'''
def create_phone_number(n):
    phone_number = '('
    counter = 0
    
    for i in n[0:3]:
        phone_number += str(i)
    
    phone_number += ') '
        
    for j in n[3::]:
        if counter == 3:
            phone_number += '-'
        phone_number += str(j)
        counter +=1
        
    return phone_number

#Test cases
print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) == "(123) 456-7890")
print(create_phone_number([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == "(111) 111-1111")
print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) == "(123) 456-7890")
print(create_phone_number([0, 2, 3, 0, 5, 6, 0, 8, 9, 0]) == "(023) 056-0890")
print(create_phone_number([0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == "(000) 000-0000")
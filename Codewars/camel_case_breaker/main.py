'''
In this project, I developed a solution that add an espace between two letters,
if and only if the second of that two letters is upper.
This project is part of the kata chanllenges in CodeWars for Python beginners.
Att: Kevin Feliz Henríquez.
'''
def camer_case_breaker(s):
    camel_case_s = ''
    
    lst_s = list(s)
    
    for i in range(len(lst_s)):
        if lst_s[i].isupper():
            camel_case_s += ' '
        camel_case_s += lst_s[i]
    
    return camel_case_s

camel_case = 'kevinFelizHenriquez'
print(camer_case_breaker(camel_case))
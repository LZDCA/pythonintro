# HOMEWORK : LESSON 3 : TYPES


# a: float(4.6) and int(4.6) ARE DIFFERENT. FORMER IS A DECIMAL TYPE AND LATER ONE IS AN INTEGER
print(float(4.6))
print(int(4.6))


#b: int(3.7) RETRUNS 3
print(int(3.7))


#c: YES, int("4.5") WORKS, IT COVERT A STRING TO A INTEGER WHICH IS 4.
#        OOPS, I WAS WRONG. STRING "4.5" NEEDS TO BE CONVERTED TO A FLOAT FIRST THEN CAN BE CONVERTED TO A INTEGER
#c: NO, int("4 and 5") DOES NOT WORK, IT IS A STRING WHICH CANNOT COVERT TO NUMBERS
print(int(float("4.5")))
#print(int(float("4 and 5")))
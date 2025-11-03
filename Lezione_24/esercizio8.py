'''
Scrivere in Python dei cicli che stampino le seguenti sequenze di valori:
a) 1, 2, 3, 4, 5, 6, 7
b) 3, 8, 13, 18, 23
c) 20, 14, 8, 2, -4, -10
d) 19, 27, 35, 43, 51

For example:
Test 	        Result A        Result B        Result C        Result D

print_seq()     1               3               20              19
                2               8               14              27
                3               13              8               35
                4               18              2               43
                5               23              -4              51
                6                               -10
                7
'''

def print_seq(): 
    
    print("Sequenza a):")
    for n in range(1, 8):
        print(n)
    print()

    print("Sequenza b):")
    for n in range(3, 25, 5):
        print(n)
    print()

    print("Sequenza c):")
    for n in range(20, -11, -6):
        print(n)
    print()

    print("Sequenza d):")
    for n in range(19, 55, 8):
        print(n)
    print()
    
    return

if __name__ == "__main__":
    print_seq()
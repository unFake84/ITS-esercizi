'''
Anagram Checker:

    Create a function that checks whether two given strings are anagrams of each other.
    Convert both strings to lowercase and remove any non-alphabetic characters.
    Sort the characters of each string and compare the sorted strings for equality.
    Indicate whether the strings are anagrams or not.

'''

from string import ascii_lowercase

def anagramChecker(s1: str, s2: str) -> bool:

    cleaner_s1: str = ''.join([w_s1 for w_s1 in s1.lower() if w_s1 in ascii_lowercase])
    cleaner_s2: str = ''.join([w_s2 for w_s2 in s2.lower() if w_s2 in ascii_lowercase])

    if len(cleaner_s1) != len(cleaner_s2):
        return False

    check_len: dict[str, int] = {}
    check_len2: dict[str, int] = {}

    for word1, word2 in zip(cleaner_s1, cleaner_s2):

        if word1 not in check_len:
            check_len[word1] = 1
        else:
            check_len[word1] += 1

        if word2 not in check_len2:
            check_len2[word2] = 1
        else:
            check_len2[word2] += 1

    for key1, value1 in check_len.items():

        for key2, value2 in check_len2.items():

            if key1 == key2:
                if value1 != value2:

                    return False

    return True

if __name__ == "__main__":

    print(anagramChecker("Biblio ,tecario!", "Beato coi libri."))
    print(anagramChecker("amor", "ramo "))
    print(anagramChecker("ciccio", "ciocco"))
    print(anagramChecker("", ""))
    print(anagramChecker("T2r56ilussa", "Salustr#.    //i"))










    # for word in cleaner_s1:

    #     if word not in check_len:
    #         check_len[word] = 1
        
    #     else:
    #         check_len[word] += 1

    # for word in cleaner_s2:

    #     if word not in check_len2:
    #         check_len2[word] = 1
        
    #     else:
    #         check_len2[word] += 1
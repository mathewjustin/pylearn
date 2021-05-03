def is_anagram(s1, s2):

    if(len(s1)!=len(s2)):
            return False

    str1=sorted(s1)
    str2=sorted(s2)
    for x in range(len(str1)):
        if(str1[x]!=str2[x]):
            return False

    return True





if __name__ == '__main__':

    s1=['f','l','u','s','t','e','r']
    s2=['r','e','s','t','f','u','l']

    print(is_anagram(s1,s2))
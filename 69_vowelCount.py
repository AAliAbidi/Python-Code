def countVowels(string):
    num = 0
    for char in string:
        if char in "aeiouAEIOU":
            num +=1
    print(num)
countVowels("AliAmirkinza")

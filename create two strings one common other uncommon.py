def String(str1):
    sec1=[]
    sec2=[]

    for letter in str1:
        if str1.count(letter) > 1:
            sec1.append(letter)
        else:
            sec2.append(letter)
    print("Same= ","".join(sec1))
    print("Not same= ","".join(sec2))

str1=input("Enter string= ")
String(str1)

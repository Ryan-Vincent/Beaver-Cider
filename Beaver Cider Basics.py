import math
x = 0
while x == 0:
    n = 0
    newword = []
    print "Welcome to BEAVER CIDER!"
    ecordc = raw_input("Would you like to:\na) ENCRYPT\nb) DECRYPT? ").lower()
    word = str(raw_input("Would you like to", ecordc,"\na) TEXT FILE\nb) CSV FILE\nc) Words, sentences or phrases"))
    shift = raw_input("Would you like to shift by:\na) PI \nb) YOUR OWN CHOICE ").lower()
   
    if shift == "a":
        shift = math.pi
    else:
        None
    word= list(word)

    if ecordc == "a":
        ecordc = "encrypt"
        if shift == "b":
            shift_num = int(raw_input("How many digits to shift by... "))
            for i in range(len(word)):
                if word[i] == " ":
                    n = " "
                else:
                    n = ord(word[i])
                    n = n + shift_num
                    n = chr(n)
                newword.append(n)
            print(''.join(str(i) for i in newword))
       
    if ecordc == "b":
        ecordc = "decrypt"
        if shift == "b":
            shift_num = int(raw_input("How many digits to shift by... "))
            for i in range(len(word)):
                if word[i] == " ":
                    n = " "
                else:
                    n = ord(word[i])
                    n = n - shift_num
                    n = chr(n)
                newword.append(n)
            print(''.join(str(i) for i in newword))



                    file_ = raw_input("Enter .txt file name.N:\.txt")
        f1 =open(file_, 'r')
        filedata = f1.read()
        f1.close()
        word = filedata
        word = list(word)

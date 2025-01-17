upperCaseLetters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
lowerCaseLetters = [letter.lower() for letter in upperCaseLetters] + [" "]
# Add spaces to lowerCase letters to still shift them

def LetterChange (letter, up = True):
    if letter in upperCaseLetters:
        if up:
            return upperCaseLetters[(upperCaseLetters.index(letter)+shift)%26]
        return upperCaseLetters[(upperCaseLetters.index(letter)-shift)%26]
    elif letter in lowerCaseLetters:
        if up:
            return lowerCaseLetters[(lowerCaseLetters.index(letter)+shift)%27]
        return lowerCaseLetters[(lowerCaseLetters.index(letter)-shift)%27]
    else:
        return(letter) # Allows punctuation to exist but does not shift it

while True:
    options = input("1) Make a code\n2) Decode a Message\n3) Exit\n")
    if options == "1":
        message = input("Enter a message to encode: ")
        shift = int(input("Enter a shift value: "))
        word = ""
        for letter in message:
            word += LetterChange(letter)
        print(word)
        break
    elif options == "2":
        while True:
            try:
                message = input("Enter a message to decode: ")
                shift = int(input("Enter a shift value: "))
                word = ""
                for letter in message:
                    word += LetterChange(letter, False)
                print(word)
                break
            except ValueError:
                print("Invalid shift value")
    elif options == "3":
        break
    else:
        print("Invalid option")
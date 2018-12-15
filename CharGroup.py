#
 #This class will hold the category english character
 #and relevant singhala characters of that group


class CharGroup:
    patternchar = ''
    characters = ()

    def __init__(self,patternchar,characters):
        self.patternchar = patternchar
        self.characters = characters

    def to_string(self):
        str_to_print = "Pattern : "+ self.patternchar
        str_to_print += " | Chars :"
        chars = ""
        for a in self.characters:
            chars += " "+a
        chars = chars.encode('utf-8')
        str_to_print += chars
        return str_to_print+"\n"

    def __str__(self):
        return self.to_string()

    def __repr__(self):
        return self.to_string()

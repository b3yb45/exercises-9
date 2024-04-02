class MorseMsg():
    __ru_alph = {
        '/': ' ',
        '.-': 'А', 
        '-...': 'Б', 
        '.--': 'В', 
        '--.': 'Г', 
        '-..': 'Д', 
        '.': 'Е', 
        '...-': 'Ж', 
        '--..': 'З', 
        '..': 'И', 
        '-.-': 'К', 
        '.-..': 'Л', 
        '--': 'М', 
        '-.': 'Н',
        '.--.': 'П', 
        '---': 'О', 
        '.-.': 'Р', 
        '...': 'С', 
        '-': 'Т', 
        '..-': 'У', 
        '..-.': 'Ф', 
        '....': 'Х', 
        '-.-.': 'Ц', 
        '---.': 'Ч', 
        '----': 'Ш', 
        '--.-': 'Щ', 
        '-.--': 'Ъ', 
        '-..-': 'Ь', 
        '..-..': 'Э', 
        '.--.': 'Ю', 
        '.-.-': 'Я'
    }
    
    __en_alph = {
        '/': ' ',
        '.-': 'A', 
        '-...': 'B', 
        '-.-.': 'C', 
        '-..': 'D', 
        '.': 'E', 
        '..-.': 'F', 
        '--.': 'G', 
        '....': 'H', 
        '..': 'I', 
        '.---': 'J', 
        '-.-': 'K', 
        '.-..': 'L', 
        '--': 'M', 
        '-.': 'N', 
        '---': 'O', 
        '.--.': 'P', 
        '--.-': 'Q', 
        '.-.': 'R', 
        '...': 'S', 
        '-': 'T', 
        '..-': 'U', 
        '...-': 'V', 
        '.--': 'W', 
        '-..-': 'X', 
        '-.--': 'Y', 
        '--..': 'Z'
    }
    
    __eng_vowels = ['A', 'E', 'I', 'O', 'U', 'Y']

    __ru_vowels = ['А', 'Е', 'И', 'О', 'У', 'Ы', 'Э', 'Ю', 'Я']

    def __init__(self, message=None):
        self.__message = message

    def eng_decode(self):
        self.__msg_eng = ''
        for i in self.__message.split():
            self.__msg_eng += self.__en_alph[i]
        return self.__msg_eng
    
    def ru_decode(self):
        self.__msg_ru = ''
        for i in self.__message.split():
            self.__msg_ru += self.__ru_alph[i]
        return self.__msg_ru

    def get_vowels(self, lang):
        if lang == 'eng':
            msg_en_vow = ''
            for i in self.eng_decode():
                if i in self.__eng_vowels:
                    msg_en_vow += i

            return msg_en_vow
    
        msg_ru_vow = ''
        for i in self.ru_decode():
            if i in self.__ru_vowels:
                msg_ru_vow += i

        return msg_ru_vow

    def get_consonants(self, lang):
        if lang == 'eng':
            msg_en_cons = ''
            for i in self.eng_decode():
                if i not in self.__eng_vowels:
                    msg_en_cons += i

            return msg_en_cons
    
        msg_ru_cons = ''
        for i in self.ru_decode():
            if i not in self.__ru_vowels:
                msg_ru_cons += i

        return msg_ru_cons
            

    def __str__(self):
        return self.__message

    def __repr__(self):
        return self.__str__()
    

msg_ru = MorseMsg('.. --. --- .-. -..- / .- -. -.. .-. . . .--')
print(msg_ru.ru_decode())
print(msg_ru.get_consonants('ru'))
print(msg_ru.get_vowels('ru'))

msg_eng = MorseMsg('.. --. --- .-. / .- -. -.. .-. . . ...-')
print(msg_eng.eng_decode())
print(msg_eng.get_consonants('eng'))
print(msg_eng.get_vowels('eng'))
class Sol:
    def detect_capital(self, word):
        for i, char in enumerate(word):
            if not word[0].isupper():
                if char.isupper():
                    return False
            else:
                if word[1].isupper():
                    if not char.isupper():
                        return False
                else:
                    if i != 0:
                        if char.isupper():
                            return False
        return True

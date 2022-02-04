class Language:
    def __init__(self, language:str, mode:str, name:str):
        self.language = language
        self.name = name
        self.mode = mode
        
        # Languages
        self.tr:str = "tr"
        self.en:str = "en"

        # Modes
        self._save:str = "SAVE"
        self._del:str = "DEL"
    def success(self):
        if (self.language == self.tr):
            if (self.mode == self._save):
                return f"--> ({self.name}) TODO basariyla olusturuldu."
            elif (self.mode == self._del):
                return f"--> ({self.name}) TODO basariyla kaldirildi."
        elif (self.language == self.en):
            if (self.mode == self._save):
                return f"--> ({self.name}) TODO is successfuly created."
            elif (self.mode == self._del):
                return f"--> ({self.name}) TODO is successfuly removed."
            
    def unsuccess(self):
        if (self.language == self.tr):
            if (self.mode == self._save):
                return f"--> ({self.name}) TODO zaten olusturulmus."
            elif (self.mode == self._del):
                return f"--> ({self.name}) TODO dosyasi bulunamadi."
        elif (self.language == self.en):
            if (self.mode == self._save):
                return f"--> ({self.name}) TODO is already created."
            elif (self.mode == self._del):
                return f"--> ({self.name}) TODO is can't finded."
import pandas

class NatoPhoneticTranslator:
    def __init__(self) -> None:
        self.sourceData = pandas.read_csv("nato_phonetic_alphabet.csv")
        self.phonetics = {row["letter"]:row["code"] for (index,row) in self.sourceData.iterrows() }

    def Translate(self) -> None:
        original = input("Enter a word: ").upper()
        translation = [self.phonetics[n] for n in original]
        print(translation)

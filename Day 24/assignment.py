import re

class LetterGenerator:
    inputLetterPath = "Input/Letters/starting_letter.txt"
    inputNamesPath = "Input/Names/invited_names.txt"
    outputPath = "Output/ReadyToSend/letter_for_{name}.txt"

    def __init__(self) -> None:
        self.Generate()

    def Generate(self) -> None:
        with open(LetterGenerator.inputLetterPath) as inputLetter:
            letter = inputLetter.read()

        with open(LetterGenerator.inputNamesPath) as inputNames:
            names = inputNames.readlines()

        for name in names:
            name = name.strip()
            outputLetter = letter.replace("[name]", name)
            with open(LetterGenerator.outputPath.format(name = name), mode="w") as output:
                output.write(outputLetter)

Suits = {
    "hearts": '♥',
    "diamonds": '♦',
    "clubs": '♣',
    "spades": '♠'
}

TopOfCard       = " _________ "
TopValueLine    = "|{shortString}       |"
SingleSuitLine  = "|    {suit}    |"
DoubleSuitLine  = "|  {suit}   {suit}  |"
EmptyCardLine   = "|         |"
BottomValueLine = "|       {shortString}|"
BottomOfCard    = "|_________|"

CardTypes = {
    "Ace" : { 
        "value": 11, 
        "shortString": " A", 
        "renderStrings" : [ 
            TopOfCard,
            TopValueLine,
            EmptyCardLine,
            EmptyCardLine,
            SingleSuitLine,
            EmptyCardLine,
            EmptyCardLine,
            BottomValueLine,
            BottomOfCard,
        ]
    },
    "2" : { 
        "value": 2, 
        "shortString" : " 2", 
        "renderStrings" : [ 
            TopOfCard,
            TopValueLine,
            SingleSuitLine,
            EmptyCardLine,
            EmptyCardLine,
            EmptyCardLine,
            SingleSuitLine,
            BottomValueLine,
            BottomOfCard,
        ]
    },
    "3" : { 
        "value": 3, 
        "shortString" : " 3", 
        "renderStrings" : [
            TopOfCard,
            TopValueLine,
            SingleSuitLine,
            EmptyCardLine,
            SingleSuitLine,
            EmptyCardLine,
            SingleSuitLine,
            BottomValueLine,
            BottomOfCard,
        ]
    },
    "4" : { 
        "value": 4, 
        "shortString" : " 4", 
        "renderStrings" : [ 
            TopOfCard,
            TopValueLine,
            DoubleSuitLine,
            EmptyCardLine,
            EmptyCardLine,
            EmptyCardLine,
            DoubleSuitLine,
            BottomValueLine,
            BottomOfCard,
        ]
    },
    "5" : { 
        "value": 5, 
        "shortString" : " 5", 
        "renderStrings" : [
            TopOfCard,
            TopValueLine,
            DoubleSuitLine,
            EmptyCardLine,
            SingleSuitLine,
            EmptyCardLine,
            DoubleSuitLine,
            BottomValueLine,
            BottomOfCard,
        ]
    },
    "6" : { 
        "value": 6, 
        "shortString" : " 6", 
        "renderStrings" : [
            TopOfCard,
            TopValueLine,
            DoubleSuitLine,
            EmptyCardLine,
            DoubleSuitLine,
            EmptyCardLine,
            DoubleSuitLine,
            BottomValueLine,
            BottomOfCard,
        ]
    },
    "7" : { 
        "value": 7, 
        "shortString" : " 7", 
        "renderStrings" : [
            TopOfCard,
            TopValueLine,
            DoubleSuitLine,
            SingleSuitLine,
            SingleSuitLine,
            SingleSuitLine,
            DoubleSuitLine,
            BottomValueLine,
            BottomOfCard,
        ]
    },
    "8" : { 
        "value": 8, 
        "shortString" : " 8", 
        "renderStrings" : [
            TopOfCard,
            TopValueLine,
            DoubleSuitLine,
            DoubleSuitLine,
            EmptyCardLine,
            DoubleSuitLine,
            DoubleSuitLine,
            BottomValueLine,
            BottomOfCard,
        ]
    },
    "9" : { 
        "value": 9, 
        "shortString" : " 9", 
        "renderStrings" : [
            TopOfCard,
            TopValueLine,
            DoubleSuitLine,
            DoubleSuitLine,
            SingleSuitLine,
            DoubleSuitLine,
            DoubleSuitLine,
            BottomValueLine,
            BottomOfCard,
        ]
    },
    "10": { 
        "value": 10, 
        "shortString" : "10",
        "renderStrings" : [
            TopOfCard,
            TopValueLine,
            DoubleSuitLine,
            DoubleSuitLine,
            DoubleSuitLine,
            DoubleSuitLine,
            DoubleSuitLine,
            BottomValueLine,
            BottomOfCard,
        ]
    },
    "Jack": { 
        "value": 10, 
        "shortString": " J", 
        "renderStrings" : [
            TopOfCard,
            TopValueLine,
            DoubleSuitLine,
            DoubleSuitLine,
            DoubleSuitLine,
            DoubleSuitLine,
            DoubleSuitLine,
            BottomValueLine,
            BottomOfCard,
        ]
    },
    "Queen": { 
        "value": 10, 
        "shortString": " Q", 
        "renderStrings" : [
            TopOfCard,
            TopValueLine,
            DoubleSuitLine,
            DoubleSuitLine,
            DoubleSuitLine,
            DoubleSuitLine,
            DoubleSuitLine,
            BottomValueLine,
            BottomOfCard,
        ]
    },
    "King": { 
        "value": 10, 
        "shortString": " K", 
        "renderStrings" : [
            TopOfCard,
            TopValueLine,
            DoubleSuitLine,
            DoubleSuitLine,
            DoubleSuitLine,
            DoubleSuitLine,
            DoubleSuitLine,
            BottomValueLine,
            BottomOfCard,
        ]
    }
}

EmptyCard = {
    "renderStrings": [
        TopOfCard,
        EmptyCardLine,
        EmptyCardLine,
        EmptyCardLine,
        EmptyCardLine,
        EmptyCardLine,
        EmptyCardLine,
        EmptyCardLine,
        BottomOfCard,
    ]
}

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
import random as r
import os as bigdawg
import time as tdawg


class fuckingHiraganaQuiz():

    def __init__(self):

        self.hiragana = {
            "あ": "a",   "い": "i",   "う": "u",   "え": "e",   "お": "o",
            "か": "ka",  "き": "ki",  "く": "ku",  "け": "ke",  "こ": "ko",
            "さ": "sa",  "し": "shi", "す": "su",  "せ": "se",  "そ": "so",
            "た": "ta",  "ち": "chi", "つ": "tsu", "て": "te",  "と": "to",
            "な": "na",  "に": "ni",  "ぬ": "nu",  "ね": "ne",  "の": "no",
            "は": "ha",  "ひ": "hi",  "ふ": "fu",  "へ": "he",  "ほ": "ho",
            "ま": "ma",  "み": "mi",  "む": "mu",  "め": "me",  "も": "mo",
            "や": "ya",  "ゆ": "yu",  "よ": "yo",
            "ら": "ra",  "り": "ri",  "る": "ru",  "れ": "re",  "ろ": "ro",
            "わ": "wa",  "を": "wo",  "ん": "n"
            }
        
        self.bigdawg = bigdawg
        #################---- colors nd shiii---#########
        self.BLINKERINO = "\033[5m" ################## fuck this shit ive been trying for a bit and idc to fix it might be my term idfk im going to sleep 
        ####basic ass colors shit fuck im so sleepy rn 
        self.GREEN = "\033[92m"  # correct
        self.RED   = "\033[91m"  # incorrect
        self.RESET = "\033[0m"   # default


    def WIPE_THE_TERMINAL_ITS_EVIL_AS_FUCK(self): ###### if u dont the terminal can gain sentience and kill u in ur sleep

        self.bigdawg.system('cls')


    def looperino(self): #### heart of everything fr fr folknemskirino
        while True:
            self.WIPE_THE_TERMINAL_ITS_EVIL_AS_FUCK() #### windows superiority everything else inferiority (said no one ever)

            randomLetterBullshit = r.choice(list(self.hiragana.keys()))

            guess = input(f"hey fuck u nerd whats this shit in romaji {randomLetterBullshit} nerd \n")

            correcterino = self.hiragana[randomLetterBullshit]

            if guess == correcterino:
                print (f"{self.BLINKERINO}{self.GREEN}WELL DONE IDIOTTTT fuckin otaku nerd {self.RESET} \n") ####### RESET OR UR TERMINAL BLOWS UP
            else:
                print (f"{self.RED}fucking dumbass im gnna beat ur ass {self.RESET} \nthe answer was actually {self.GREEN} {correcterino} {self.RESET} dumbasssssss") ####### RESET OR UR TERMINAL BLOWS UP 
            while True:
                replay =  input("\nagain? y/n ").lower().strip()
                if replay == "y":
                    print ("ye ur a fuckn nerdddd")
                    tdawg.sleep(2)
                    break
                elif replay == "n":
                    print ("hey fuck u buddy eat my ass")
                    return

            input
G = fuckingHiraganaQuiz()
G.looperino()

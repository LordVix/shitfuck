import random as r
import os as bigdawg
import time as tdawg


class fuckingHiraganaQuiz:

    def __init__(balls):

        balls.hiragana = {
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
        
        #################---- colors nd shiii---#########
        balls.BLINKERINO = "\033[5m" ################## fuck this shit ive been trying for a bit and idc to fix it might be my term idfk im going to sleep 
        ####basic ass colors shit fuck im so sleepy rn 
        balls.GREEN = "\033[92m"  # correct
        balls.RED   = "\033[91m"  # incorrect
        balls.RESET = "\033[0m"   # default


    def WIPE_THE_TERMINAL_ITS_EVIL_AS_FUCK(balls): ###### if u dont the terminal can gain sentience and kill u in ur sleep

        bigdawg.system('cls') ######## im not making it usable for linux and mac idc if its 2 lines fuck them


    def looperino(balls): #### heart of everything fr fr folknemskirino
        while True:
            balls.WIPE_THE_TERMINAL_ITS_EVIL_AS_FUCK() #### windows superiority everything else inferiority (said no one ever)

            randomLetterBullshit = r.choice(list(balls.hiragana))

            guess = input(f"hey fuck u nerd whats this shit in romaji {randomLetterBullshit} nerd \n").lower().strip()

            correcterino = balls.hiragana[randomLetterBullshit]

            if guess == correcterino:
                print (f"{balls.BLINKERINO}{balls.GREEN}WELL DONE IDIOTTTT fuckin otaku nerd {balls.RESET} \n") ####### RESET OR UR TERMINAL BLOWS UP
            else:
                print (f"{balls.RED}fucking dumbass im gnna beat ur ass {balls.RESET} \nthe answer was actually {balls.GREEN} {correcterino} {balls.RESET} dumbasssssss") ####### RESET OR UR TERMINAL BLOWS UP 
            while True:
                replay =  input("\nagain? y/n ").lower().strip()
                if replay == "y":
                    print ("ye ur a fuckn nerdddd")
                    tdawg.sleep(2)
                    break
                elif replay == "n":
                    print ("hey fuck u buddy eat my ass")
                    return

        
startBullshit = fuckingHiraganaQuiz()
startBullshit.looperino()

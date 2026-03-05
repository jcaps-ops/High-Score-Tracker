import random
import time

def game():
    def pathgen(currentpath,islost):
        
        islost = False
        pathrand = random.randint(1,6)
        global branchpath1
        if pathrand == 1:
            branchpath1 = "dice--------"
        if pathrand == 2:
            branchpath1 = "slot machine"
        if pathrand == 3:
            branchpath1 = "blackjack---" 
        if pathrand == 4:
            branchpath1 = "wheel-------"
        if pathrand == 5:
            branchpath1 = "store-------"
        if pathrand == 6:
            branchpath1 = "Lottery-----"
        pathrand = random.randint(1,6)
        global branchpath2
        if pathrand == 1:
            branchpath2 = "dice--------"
        if pathrand == 2:
            branchpath2 = "slot machine"
        if pathrand == 3:
            branchpath2 = "blackjack---" 
        if pathrand == 4:
            branchpath2 = "wheel-------"
        if pathrand == 5:
            branchpath2 = "store-------"
        if pathrand == 6:
            branchpath2 = "Lottery-----"
        

        print(f"---------------{branchpath1}----")
        print(f"--{currentpath}-------------------------")
        print(f"---------------{branchpath2}----")

        

        p_choice = input("Which path do you want to take (W or S):")

        if p_choice == "w":
            currentpath = branchpath1
        
        elif p_choice == "s":
            currentpath = branchpath2
            
        else:
            print("Wrong pathway")

    def pathchoice(currentpath):
        
        if currentpath == "dice--------":
            dicegame(money,boonbet,islost)
        if currentpath == "slot machine":
            slotmachinegame(money,boonbet,islost)
        if currentpath == "blackjack---":
            blackjackgame(money,boonbet,islost)
        if currentpath == "wheel-------":
            wheelgame(money,boonbet,islost)
        if currentpath == "store-------":
            store(money,potentailboonname,potentailbooncost,luckstat)
        if currentpath == "Lottery-----":
            lotterygame(boonbet,money,islost)


    def dicegame(money,boonbet,islost):
        boonbet = 0
        p_roll = 0
        D_roll = 0


        #You Draw the card

        print(f"Your current money is {money}")

        bet_value = bet(money,boonbet)
        money = bet_value[0]
        boons = bet_value[1]
        all_in = bet_value[2]

        p_roll = random.randint(1,6)
        D_roll = random.randint(1,6)
        D_roll = str(D_roll)
        p_roll = str(p_roll)

        print(f"You rolled a {p_roll}")
        print(f"The Dealer rolled a {D_roll}")

        if p_roll > D_roll:
            claculated_boon = calcboon(luckstat,money,boonbet,boons,all_in)
            money = claculated_boon[0]
            has_lost = claculated_boon[1]
            money += boonbet * 2
        if p_roll < D_roll:
            islost = True
            claculated_boon = calcboon(luckstat,money,boonbet,boons,all_in)
            money = claculated_boon[0]
            has_lost = claculated_boon[1]
            money -= boonbet
        if p_roll == D_roll:
            claculated_boon = calcboon(luckstat,money,boonbet,boons,all_in)
            money = claculated_boon[0]
            has_lost = claculated_boon[1]

    def slotmachinegame(money,boonbet,islost):
        bet_value = bet(money,boonbet)
        money = bet_value[0]
        boons = bet_value[1]
        all_in = bet_value[2]
        boonbet = 0

        slot1 = ""
        slot2 = ""
        slot3 = ""

        randomvalue = random.randint(1,5)
        if randomvalue == 1:
            slot1 = "X"
        if randomvalue == 2:
            slot1 = "O"
        if randomvalue == 3:
            slot1 = "V"
        if randomvalue == 4:
            slot1 = "Z"
        if randomvalue == 5:
            slot1 = "W"
 
        randomvalue = random.randint(1,5)
        if randomvalue == 1:
                slot2 = "X"
        if randomvalue == 2:
                slot2 = "O"
        if randomvalue == 3:
                slot2 = "V"
        if randomvalue == 4:
                slot2 = "Z"
        if randomvalue == 5:
                slot2 = "W"

        randomvalue = random.randint(1,5)
        if randomvalue == 1:
                slot3 = "X"
        if randomvalue == 2:
                slot3 = "O"
        if randomvalue == 3:
                slot3 = "V"
        if randomvalue == 4:
                slot3 = "Z"
        if randomvalue == 5:
                slot3 = "W"
        print(f"You have {money} dollars")
        bet(money,boonbet)
        print(f"---{slot1}---{slot2}---{slot3}---")

        if slot1 == slot2 and slot2 == slot3:
                    claculated_boon = calcboon(luckstat,money,boonbet,boons,all_in)
                    money = claculated_boon[0]
                    has_lost = claculated_boon[1]
                    money += boonbet * 3
        elif slot1 == slot2 or slot2 == slot3:
                    claculated_boon = calcboon(luckstat,money,boonbet,boons,all_in)
                    money = claculated_boon[0]
                    has_lost = claculated_boon[1]
                    money += boonbet
        else:
                    islost = True
                    claculated_boon = calcboon(luckstat,money,boonbet,boons,all_in)
                    money = claculated_boon[0]
                    has_lost = claculated_boon[1]
                    money -= boonbet
            
    def blackjackgame(money,boonbet,islost):
        
        boonbet = 0
        total = 0
        is_playing = True
        d_total = 0

        
        print(f"the anount of money you have is {money}")
        bet_value = bet(money,boonbet)
        money = bet_value[0]
        boons = bet_value[1]
        all_in = bet_value[2]

        total = 0

        total +=  random.randint(1,10)
        total +=  random.randint(1,10)

        print(f"Your total is {total}")

        is_playing = True

        while is_playing == True:
            p_action = input("Would you like to hit or stand:")

            if p_action == "hit":
                total +=  random.randint(1,10)
                print(total)

                if total > 21:
                    total = 0
                    print("You busted")
                    is_playing = False

            elif p_action == "stand":
                    is_playing = False
            else:
                    print("That is not an acceptible option")

        d_total = 0

        while d_total < 17:
            d_total += random.randint(1,10)

            if d_total > 21:

                d_total = 0

        print(f"The dealers total is {d_total}")

        if total > d_total:
            claculated_boon = calcboon(luckstat,money,boonbet,boons,all_in)
            money = claculated_boon[0]
            has_lost = claculated_boon[1]
            money += boonbet
            print("You won")
        if total == d_total:
            claculated_boon = calcboon(luckstat,money,boonbet,boons,all_in)
            money = claculated_boon[0]
            has_lost = claculated_boon[1]
            print("You both tied")
        if total < d_total:
            print("You lost")
            islost = True
            claculated_boon = calcboon(luckstat,money,boonbet,boons,all_in)
            money = claculated_boon[0]
            has_lost = claculated_boon[1]
            money -= boonbet

    def wheelgame(money,boonbet,islost):

        boonbet = 0
        bet_location = "white"

        print(f"You have {money} dollars")
        bet_value = bet(money,boonbet)
        money = bet_value[0]
        boons = bet_value[1]
        all_in = bet_value[2]
        bet_location = input("What color do you want to bet on (red black green)")

        wheelspin = random.randint(1,101)
        wheelcolor = ""
        if wheelspin < 51:
                wheelcolor = "black"
        if wheelspin > 50 and wheelspin < 101:
                wheelcolor = "red"
        if wheelspin == 101:
                wheelcolor = "green"
            
        print(f"The wheel landed on a {wheelcolor}")

        if wheelcolor == bet_location:
                claculated_boon = calcboon(luckstat,money,boonbet,boons,all_in)
                money = claculated_boon[0]
                has_lost = claculated_boon[1]
                money += boonbet * 2
                print("You won")
                if wheelcolor == "green":
                    claculated_boon = calcboon(luckstat,money,boonbet,boons,all_in)
                    money = claculated_boon[0]
                    has_lost = claculated_boon[1]
                    money += boonbet * 2
        else:
                claculated_boon = calcboon(luckstat,money,boonbet,boons,all_in)
                money = claculated_boon[0]
                has_lost = claculated_boon[1]
                islost = True
                money -= boonbet
                print("You lost")

    def store(money,potentailboonname,potentailbooncost,luckstat):
        newboon = ""

        boonrand1 = random.randint(0,len(potentailbooncost) - 1)
        storeoption1name = potentailboonname[boonrand1]
        storeoption1cost = potentailbooncost[boonrand1]

        boonrand2 = random.randint(0,(len(potentailbooncost) - 1))
        storeoption2name = potentailboonname[boonrand2]
        storeoption2cost = potentailbooncost[boonrand2]
        global boons
        while True:
                print(f"You have {money} dollars")
                print("The options at the store")
                print(f"The first option is {storeoption1name} it costs {storeoption1cost} dollars")
                print(f"the second option is {storeoption2name} it costs {storeoption2cost} dollars")
                plyerinput = input("If you want to buy an option please input the number.If you do not want to buy one type n:")
                if plyerinput == "1":
                    if money >= storeoption1cost:
                        boons.append(storeoption1name)
                        newboon = (storeoption1name)
                        money -= storeoption1cost
                        potentailboonname.pop(boonrand1)
                        potentailbooncost.pop(boonrand1)
                        break
                elif plyerinput == "2":
                    if money >= storeoption2cost:
                        boons.append(storeoption2name)
                        newboon = (storeoption2name)
                        money -= storeoption2cost
                        potentailboonname.pop(boonrand2)
                        potentailbooncost.pop(boonrand2)
                        break
                elif plyerinput == "n":
                    break
                else:
                    print("not excepted input skill issue")

        if newboon == "Lucky coin":
            luckstat += 3
        if newboon == "Budlight":
            luckstat += 5
        if newboon == "Sober":
            luckstat -= 3
        if newboon == "Too lucky":
            luckstat += 7
        print(f"You have these boons {boons}")
                
        
        
    def calcboon(luckstat,money,boonbet,boons,all_in):
        
        has_lost = False

        income = 0
        if "Basic inssurance" in boons:
            
            if islost == True:
                bi = boonbet/4
                bi = int(bi)
                money += bi
                print(f"Your Basic insurance kicked in saving you {bi} dollars")
        
        if "diamond inssurance" in boons:
            
            if islost == True:
                bi = boonbet/2
                bi = int(bi)
                income += bi
                print(f"Your Diamond insurance kicked in saving you {bi} dollars")
        
        if money <= 1:
            loser()
            print("You ran out of money loser so get back in there loser or are you to weak")
            ttime = input("Do you want to play again(Y/N)")
            if ttime == "N" or ttime == "n":
                 print("Well good luck loser")
            else:
                 game()

        if "All in frenzy" in boons:
            if islost == False:
                if all_in == True:
                    income += boonbet

        if "Stolen tokens" in boons:
            bi = boonbet/4
            bi = int(bi)
            income += bi
            print(f"Your Stolen tokens kicked in saving you {bi} dollars")

        if "double trouble" in boons:
            boonbet * 2
            
        if "bonus check" in boons:
            income += 5
            
        if "money laundering" in boons:
            
            monbet = random.randint(1,round(5 - (luckstat/5)))
            print(monbet)
            if monbet == 1:
                income += 30
                print(f"money laundering sucsess you now have{money}")
        
        if "Daily Double" in boons:
            chance = random.randint(1,20 - luckstat)
            if chance == 1:
                print(f"You stared with {money}")
                income += money 
                print("Your daily double kicked in")
        if "Daily Triple" in boons:
            chance = random.randint(1, 20 - luckstat)
            if chance == 1:
                print(f"You stared with {money}")
                income += money * 3
                print("Your daily Triple kicked in")
        if "Budlight" in boons:
            money -= 2
        if "Sober" in boons:
            income += 10
        if "Money printer" in boons:
            income += 15
        if "basic Money maker" in boons:
            print(f"Income before basic Money maker {income}")
            income += 2
            income = income * 2
            print(f"Income after basic Money maker {income}")
        if "Extreme money maker" in boons:
            print(f"Income before extreme Money maker {income}")
            income += 2
            income = income * 3
            print(f"Income after extreme Money maker {income}")
        if "Grand money maker" in boons:
            print(f"Income before Grand Money maker {income}")
            income += 1
            income = income * 4
            print(f"Income after Grand Money maker {income}")
        if "Little for me" in boons:
            if islost == False:
                bi = boonbet/4
                bi = int(bi)
                money += bi
                print(f"Your little for me kicked in earning you {bi} dollars")
        if "A lot for me" in boons:
            if islost == False:
                bi = boonbet/2
                bi = int(bi)
                money += bi
                print(f"Your a lot for me kicked in earning you {bi} dollars")
        

        money += income

        return(money,has_lost)
        

    def jackblack():
        #this is baccarate 
        global money
        global boonbet
        curentmoney = money
        global islost
        global levelCounter
        global has_won
        print("*********************************##%%%%%%%%%%%#######%#########%%###########*#######%%%#########%%%%%%%%%%%%%%#################################*****##***************")
        time.sleep(0.1)
        print("*++++++************###############%%%#%%%%##########################%###############%%%%%#######%%%%%%%%%%%%###################################*****##***************")
        time.sleep(0.1)
        print("+++++*++********###########################%##############%%###############*####**===-==+++####*##%%%%%%%%%%%%%%%%%##########################***********************+")
        time.sleep(0.1)
        print("+++++++++*******###########################%##########%###%################*+====+**+--:.::::::=*##%#%%%%%%%%%%%%#%%########################****#**************++++++")
        time.sleep(0.1)
        print("+++++++++++*******#####**###############################################*+=-=+#%%@@%%#*--+++-::..:+=*##%%%%%%%%####%#####################********************++++++++")
        time.sleep(0.1)
        print("++++++++++++*********##################%##############################*===+*#%%%%#**###***##*+-....:+#*%%%%########################*#####******************++++++++++")
        time.sleep(0.1)
        print("++++++++++++************#*#############################%###########**==++*##%%%*++=========++++-:....:-*##%##%%###########################*************++++++++++++++")
        time.sleep(0.1)
        print("==+++++++++***++**********###*#############**#*###################*+=+**##%%%#*++============+++*::::...-#%%%%%%%#########################*************++++++++++++++")
        time.sleep(0.1)
        print("===+*+=+++++*+++***************########*###**####################+=+**##%%%##+++============++++*+--:....=##%%%%###################******************++++++++++++++++")
        time.sleep(0.1)
        print("***=-=====++++++********************##**######################*#+++**##%%###*++===============+++**+=:...:-##%%#############***##********************++++++++++++++++")
        time.sleep(0.1)
        print("*=++=+***--=++++++*++****************#*******##*****##########*+-=***#%%##***#***++++++++++++**++***=-::::=################*****#*******************+++++++++++++++++")
        time.sleep(0.1)
        print("*==+*****=-==*******+==+******************************#######++===**##%%%****+++****++++*###*****+*##*:::::=###############****##*********++*********++++++++++++++++")
        time.sleep(0.1)
        print("+++*********+=-==+**===+************************+**+****##**+====++*#%%%#***###%##**+=+*####***++++#%#+-:...+*#############***###******##**+******+*+++++++++++++++++")
        time.sleep(0.1)
        print("**********+**+-=-+*+==+++++*******************++*******##*#*======+##%%#*+++++++++++==++***##***+++*%%+-:.....-############********###******++***++++++++++++++++++++")
        time.sleep(0.1)
        print("**********=-+=-==++*++++++++==*******************++*****+**=====+**#%%%%*+++=====+++=++++++++++==++*%%+-::..::-*############**********+******++*+++++++++++++++++++++")
        time.sleep(0.1)
        print("+*********=----+++++++++++++++=++=+*++++***********+******+=-===+*##%%#**++++++++*##+****+====+++++###*-::..:.-+###*#######*****####**++*****++++++++++++++++++++++++")
        time.sleep(0.1)
        print("+++++++++==++**+-=+++++*******++=++*++++-==-++++=********+=====++*###**+***++++*++**##**+*+++++++++*###*--:..::=+*#########**#########*+***++*+++++++++++++++++++++++")
        time.sleep(0.1)
        print("=-+==+++=+*****+-===+++++********++*****+++=-=+*=++**+=+++++++=+++**+++++**++*****###**+++*+++++++++**#**-.....:-*#####****#########*****+++**+++++++++***++++++++++=")
        time.sleep(0.1)
        print("--+++++==**+*++***+==-===++*****+++++******+==:+********+-=++=+*++++++++******##########**+*+**++++++=+**:::::.::*#######################*++****+++++++**++++++++++++")
        time.sleep(0.1)
        print("+==+++***************===-=-=+*****************--+*******+++==++++**+++++********++**+**##***++*++++====++=.:.:::-***###################***+++***++*++++++++++++++++++")
        time.sleep(0.1)
        print("+++***********************+--++***************=:-********+**++++*#*+++++***#*++++++*+*****#*++++++========-::::--+++**#################*****++****+++++++++++++++++++")
        time.sleep(0.1)
        print("****++********************+==+***************+-:=***##*****+=++***++++++**##*++++++++**++****++++========-::::::**+*##*+*##############*****++++*++++++===+++++++++++")
        time.sleep(0.1)
        print("**********************++++***************+++=+*--==##**+=======+*++++++**###**+++++++*****###*++++===-===-:...:-+++*###################******+++++++++++====++++=====")
        time.sleep(0.1)
        print("+*********************+++==+****************--*:-==***#####+=-=+++***+**##*#**+=+++++**##%%%##*++++====++-::::::*****###############*********++++++++++++++==========")
        time.sleep(0.1)
        print("*******++++++++*****+*****-=****************==***++++++******+==+*###*#***+**+=+++++***#%%#%%##*++=====+=-::::=*=******############*************+++++++++++++=====+==")
        time.sleep(0.1)
        print("******+++++++++++*********++***********************#****####*+==+*#######**+++++=+++****##%%%%##*+++=-=---:--=-=+++==+****#*********************++----:::::::::::::-:")
        time.sleep(0.1)
        print("++++++*********++++**+++++****++++++++++++*********#****##**+:-+*####%%##***++++++++**#*#%%%%%%##%####*=-:::.:::::::::::::::-+******************+*********+=--::::::-")
        time.sleep(0.1)
        print("++*+++++=---------------------------::-----=----=--=*+-:-=******##########***++********##%%%%%%%%%######*=::.::::::::-:::::::::::::---+**************#****####*******")
        time.sleep(0.1)
        print("*******++-----=----==---=----=---=--------=---=----=+************#############%%#########%%%%%%%%#########*+--::::::=********###*****************###*##*######*****#*")
        time.sleep(0.1)
        print("*****+++*+------==--=--=----=+++++===-=+=+=++=+++=****************#*#######%%%%%%%%%%%%%%%%%%%%#############***+----:::+**##*#*#***********+++++*********####****##*#")
        time.sleep(0.1)
        print("***+++**+********+*+++++++++++++++++++++**++++++*********************########%%%%%%%%%%%%%%%%#################****+++---::+#####****#***+++********#*####***********#")
        time.sleep(0.1)
        print("+++++***++**+++++++++++++++++++++++++*++++++++*********************#*##########%%%%%%%%%%%%#################************+-::*#***#*###**++++++++*##**#######*********")
        time.sleep(0.1)
        print("****++**++**+++++++++++++++++++++++++++++++++**********************##*#######################################*************+-::+**#####********++*####################")
        time.sleep(0.1)
        print("*+++****+++*++++++++++++++++++++++++++++++++***********************########################################****#******###****=:-######***********##**################")
        time.sleep(0.1)
        print("************++++++++++++++++++**++***++++++********************##**#########################################*##*#***##########*--#*###**********######**#############")
        time.sleep(0.1)
        print("********++**+++++++++++++++++++*******+***+*********************#***###########################################################+:+####**********#####################")
        time.sleep(0.1)
        print("***##*******++++*******+++***************************************#*############################################################*-:*##***********#####################")
        time.sleep(0.1)
        print("***###**++**++***++******************************##************#*###############################################################*-:*##************###################")
        time.sleep(0.1)
        print("***##***************************************#**###************#*#################################################################=:-#***********################%%%%%")
        time.sleep(0.1)
        print("***###**************************************#####**************##################################################################*-:+#**********#################%%%%")
        time.sleep(0.1)
        print("#######**********************************#######***********#*#####################################################################*--#*******#*####################%%")
        time.sleep(0.1)
        print("########***#***********************#****########*********##########################################################################+:+*******################%%%#%%%%")
        time.sleep(0.1)
        print("*****###***#********************#******############**#############################################################%%####%##########*--*********##############%%%%%%%%")
        time.sleep(0.1)
        print("***********#**************************##########**#################################################################%%##%%###########+---------=***##########%%%%%%%%%")
        time.sleep(0.1)
        print("###*++*#***#************************##########%#*##################################################################%%%#%%%############=-----=***********###%%%%%%%%%%")
        time.sleep(0.1)
        print("########***#***********************###########%#*############################################################%%%%%#%%%%%%%###########*--==+*******###########%%%%%%%%")
        time.sleep(0.1)
        print("**#*###****##********#*************###########%#################################################################%%%%%%%%%%%###########+-=******##########%%%%#####%%%")
        time.sleep(0.1)
        print("+**######**##*#*****##***********############%%##################################################################%%%%%%%%%%%%#########*+-+###############%%%%%%%%%%%%")
        time.sleep(0.1)
        print("+======+***##*#******###*********###########%%%###################################################################%%@%%%%%%%%%%#########*+###%%%%%%%%%%%%%%%@@@%%%%%%")
        time.sleep(0.1)
        print("==++*******##*#*****#************##%#####%%%%%%###################################################################%%%%%%%%%%%%%##########+#%%%%%%%%%%%%%%%@%@@%%%%%%%")
        time.sleep(0.1)
        print("A challanger approches!\nHe challenges you to a game of baccarate!")
        time.sleep(0.2)
        print("It is time to face your first boss; jack black. you must get twice your current amount of money in order to beat him.")
        time.sleep(0.2)
        while money < curentmoney * 2:   
                print(f"you have {money} dollars")
                bet_value = bet(money,boonbet)
                money = bet_value[0]
                boons = bet_value[1]
                all_in = bet_value[2]
                total = 0
                total += random.randint(1,9)
                total += random.randint(1,9)

                if total >= 10:
                    total -= 9

                print(total)

                p_action = input("would you like to stand or hit")
                if p_action == "hit":
                    total += random.randint(1,9)
                    if total >= 10:
                        total -= 9
                pdist = 9 - total
                dealertotal = random.randint(5,9)
                ddist = 9 - dealertotal

                print(f"You got a {total}")
                print(f"Jack black got a {dealertotal}")

                ddist = abs(ddist)
                pdist = abs(pdist)
                
                boonbet = int(boonbet)
                if pdist < ddist:
                    print("you won")
                    claculated_boon = calcboon(luckstat,money,boonbet,boons,all_in)
                    money = claculated_boon[0]
                    has_lost = claculated_boon[1]
                    
                    money += boonbet
                elif pdist == ddist:
                    claculated_boon = calcboon(luckstat,money,boonbet,boons,all_in)
                    money = claculated_boon[0]
                    has_lost = claculated_boon[1]
                else:
                    print("You lose")
                    claculated_boon = calcboon(luckstat,money,boonbet,boons,all_in)
                    money = claculated_boon[0]
                    has_lost = claculated_boon[1]
                    money -= boonbet
        levelCounter = 10
        has_won = True



    def leveldesign1():
        print("...@*..:   ..::........*@@@@*@@:.+  .-.#@@@#:::::.......:.....=.%.@@--+-.*:.*@##@@@@........:==###-====*@@@@@@@@@@@")
        time.sleep(0.1)
        print(":*+-*@:.@@@#-..*.=%@@@*.#@@@@*@@-#@+@@+*@@@#:#++@=++=*#+##@@@@+-@%@@-@*  %=+@%@@@@@..+-+++=*#=%. =-:..@@.:...:===%.")
        time.sleep(0.1)
        print("@@@@@@@@%@@@@%%*@.:+@%@@=%@@@%#@%+@@%@#-@@@@@@*@####*#@##**#=@#@=@@#-#@@@#:@@%@@@@.#@@@@=:=*:=@ .%=-%@:--+*+%@#=@  ")
        time.sleep(0.1)
        print("@@@@@@@@@@@@@@@@@@.....:..@@@@*@@:.@@%@-%@@@===:+++#@-*=*#+==+=@=@@:@@@@@@@@*%@@@:=++==--%@**%%@@*#%@++#%%###.::=@#")
        time.sleep(0.1)
        print("...............=-@@@ .+.-:.@@@@#@@.#  .%:@@@*-%@@@%+--+-+**#*#-@#@%.*  =-=@#%@@@--::=...@@@@@@@@@@@@@@@@@@@@@@@@@@@")
        time.sleep(0.1)
        print(".*++**+=+#+=++*+  @@@.@@@@# @@@@#@%=@@@@:%@@@%@-#+*%%%@#*=#@@+@@@@:%@@@@-@@@@@@=.:#%+.-@@@-.........::--====..#@@@#")
        time.sleep(0.1)
        print(".=-::--=++=.-%@+..%@  .+-:.@@@@@@+-%-::.@@@*-+-#*+-:**%#*.+:@#@@.@@@@*@@@#@@+.#@@%*:@@.  %==-=+#+#=.+:....:@@@+    ")
        time.sleep(0.1)
        print("@@. .-=-:...=:.=-=-..@@*.:=+:.@@@@@@:.=+@.%@@%:%@@=.=##:.-%@%.@@@- @  -:@@@@@#.:-:...@@:=%%#++*%+#-..... .+@@@%.*#.")
        time.sleep(0.1)
        print("@@@...::--::-=.......@@=   :..@@@@@@*#=-:-@@@-..-+**-=:=..+%@@@@-.#%@%@@@@@#..*@..@@@... ::............-@@@..... # ")
        time.sleep(0.1)
        print("@@.@@@..:..            +@@@@@:. @@@@@#.@@@.@@@-@@##*=*=#@@@*.*%@=.@@@.#@@@@@--+:. @@%.:==-::-=.....:..:@@@..:. :@@@")
        time.sleep(0.1)
        print("...:+@@@ -@@@@@@@@@@@@@*.@%...*:.@@@@@:.:..-@@@=.#:@==*....-=@@@++@%-.@@%@@..-@@@@@.           . :-.%@@@@@-..@@@*..")
        time.sleep(0.1)
        print("@.    .@@%. ..: :...   @@.@@..:...@@@@%.@@+.@@@.*@..==*-***+:%@*:. *.%@@@@..:...@@.@@@@@@@@@@@@@@.@@@@:.-..%@@..@@#")
        time.sleep(0.1)
        print("-+@*..  .+.   . .       ...-@..**..@@@@*.-:.#@@.*+@@%:+-*#+:@@@::@@##@#@@. ....@..@            ..@@+..  -@@@*.@@@..")
        time.sleep(0.1)
        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  -- .@@@@=:+=.@@@=*%#==%+*#*:@@%.+...@@@@:....=@@+@--:.:.. .....:@.  ..:@%..:@@=-+*.")
        time.sleep(0.1)
        print("   .. ..    .   .   .   ..  @@@. .. :@@@@+...%@@.=-=.:=:++#*@@-- +-@@@@=.:..#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#:=+--.")
        time.sleep(0.1)
        print(".@.  -#@@@+.... ... .. ...-  @@@+ .. *@@@%*@@.@@:@+#*#**#+:%@@:@@#%@@@* ...%@@+              ..  ....:+  .=..=#*#+ ")
        time.sleep(0.1)
        print(".#%@@   :@*..+=:::  -..#=.-#   @@#.#. #@@@=...@@%:*@--+.--=%@+..=-@@@# .  @@@  =#-.-..*:-......#@@@+   =@@#*+=:.   ")
        time.sleep(0.1)
        print(" .=*#%@@   . .. .++..: -:.-+.#  @@@+...%@@@*.:.@@++..*#@@##%@=*@-@@@% .=@@@@  -+-* :. -.:   .:.#%   .@@%#==.    .=#")
        time.sleep(0.1)
        print("    .:*#@@%:.=::...... =+:.=.=#  @@@....@@@@#:.@@.#@#=*:-++@@:.-@-@@... @@: :*.=-- :- *:--...-.   @@%%*-..   .#@@@@")
        time.sleep(0.1)
        print("@@+    .:##=.:=.-*#*.-##:....-:+#  @@=. .@@@#.:=@%=+#-#*#*-@@.-@#@@ ..+@@  .=+...-.+.. ..-=::..@@@##..    -@@@@@@@@")
        time.sleep(0.1)
        print("@@@@@@.   .+#+         +#=:. .::*.  @@@...@@@++:@@=@.**-=+@@=-.@@@ ..%@@  *.*. . :##=*--:..   ##=.     %@@@@@@@@@@.")
        time.sleep(0.1)
        print("#@@@@@@@@+   .###.   ....+#*....#.#+ -@@. -@@%.:@@@*@%@@@#@@.:@@@.#+@@. :#:.:.:--#..       =#%.    +@@@@@@@@@#.....")
        time.sleep(0.1)
        print("   .@@@@@@@@@.   =#*.      :##- =.+@@  @@@@@@@@@@@+@@#%*#@@@@@@@@@#@@  @#.. :=+*   ..   #%%.   .@@@@@@@@@-.  :@@@@@")
        time.sleep(0.1)
        print(".@@*:  .%@.*@@@@=.....=...    #==...%@+ * .... ....=##%%%+=-:....:.@ @@#...:##      :###.   %@@@@@#@%.  :@@@@@@@@@*")
        time.sleep(0.1)
        print("   --+*   ..@@.@@@@@#....       =+.                 .......              =##      ..  . .@@@@..@@  .-*%@*.         ")
        time.sleep(0.1)
        print("@@@@@@@@@@@@@=  .-@@@@@@@@@@%%%=*##@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#       @@@@@@@@@@@@*:-#- @*@@@@@@@@@@@@@@@")
        time.sleep(0.1)
        print("** *+*****=  :@@@@@@-        @@@@@@@      ...                   ..  .. :@@@@@@@%-...+-:.     -+%@@@@@@@@@@@@@@@@@@@")
        time.sleep(0.1)
        print(" ..@+..*.%@@@@@@@@.+@@@*=+@@@@@   ..#@@==-+#+@#.@@@@@*@@@@@@@+@*:@ @-@@%#..  .@@@@@+-#@#@@@@%-@#@-@.@    ..     *%*")
        time.sleep(0.1)
        print("@@@@   ..   .*@+ @.+ .**=+::  .@@@=  . .@@=#=%@@ *==....+++.@@#*-*@@@..   %@@%  *@@+++@@@% %@@@@*#%:#@@@@@@@@@@....")
        time.sleep(0.1)
        print("#@#* .   -@@@@@@.%- :-@@@@@@@@@@*=-@@@@@@.    . .@@@@@@@@%@         ..%@%=..@@@@. @-: @@@%...       ...      .@@@#*")
        time.sleep(0.1)
        print("  @@@@@@@@*   @+.-  --+.#@@@:. =%*@@@  :@@@-  .@@. .... : +@@.  .%@@@=@@@@@@@@@@= @--.@@@+.  #@@@@@@-    @@@%@@@@- ")
        time.sleep(0.1)
        print("*#*=@%##@@@@@@@.@@@@@@@@@@@@@@@@@@@# #@@@@@@@@@@@#.:-.-=#+=*@@@@@@@@@#@@ -. @@@:  @*-%@@@..@@@@@-@@@@@@@@%...#@@@*@")
        time.sleep(0.1)
        print(" @  +      +%%@ .@#. %@*.@@@@== .---@@:   -%%%:  @%@@@@@--@@@@@@@ -.: @@.%@ %@@@+#%@=@# @..@@#. ..@@@@@ @@@-.=@@@**")
        time.sleep(0.1)
        print("@@@@@@@@@@@@-.@ .@@. @*+@@@@- =-+ % @#@%#@*:@*+@*   @  @*@@+-=@@-**#+@# .-: *@@@*@ @ @: @...@#-+@@#.+= * .  @@@@@**")
        time.sleep(0.1)
        print("    %::+@@@@ .@ .@@+ @..@@@@  @#@ @:@#@@@@@**#**%@@%*@%###-:-=*@+*+@.++.+@@+@@@@:@ @*@* @  @@.  @-=.@# + =  @@@@+@@")
        time.sleep(0.1)
        print("@@@##+% #%+%@@@#...@ *@@#=@@+@@@@@@@@@:.@#.#@@@@@@@%@@@%-@@@@@@@-@@-=@@@@@@@@@@*+@@ %=.@@%%%@#@@@@@@@%@#@@-%@#%@+@@")
        time.sleep(0.1)
        print("@-#+#@@@@@@@@@@@@%@@@@@@@@%-   .-@@...=#@@@@@@@@+:-:#.*+*=*@@@@@@@%%@@*. ....=+*@@@@@@@@%@@@@@@@*@#*...@@@@@@@@@@##")
        time.sleep(0.1)
        print("@@@@@@@@@@@@@@@@@@@@@. =. #@@@@%%..:=@@@@@@@@#:@.@-@%%@-@=%%%#@@@@@%@##-@@@@@@:....@@@@@@@@@@@@@@@@@@@@@%@@@@@@@@@@")
        time.sleep(0.1)
        print("@%@@@@@@@@@###*@@   .:=-+@@@@@#@@@@@@@@@@@@=.@.:+..@.##.@-.*..#+%@@@@@@*@.  =@%@@@@ ---====@@@@@@@@@@@#@@@@@@@@@@@@")
        time.sleep(0.1)
        print("@@@@@-+:.@@@@@@@@#*+==##@@@@@@@@@@@@@@-%%..@@.@@:.@+.@@.-@%.@@..@%.@#@@@@@@@@@@@@@@..............@@@@@#+%@@@@@@%%@@")
        time.sleep(0.1)
        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#...@@-%@@=.@@..@@%.@@--@@=.@@.@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#@@@@@")
        time.sleep(0.1)
        print("@@@:. ..-@@@@@@@@@@@@@@@@@@@@@@@@@@@@..@@@..@@ @@@@@..@..@@@#.=@. #@.@@@@@@@@@@@@@@@@@@@@@@#.:@%#=-=..%@@@@@@@@#@@@")
        time.sleep(0.1)
        print("@@@@@@-@@@@@@@@@@@@@@@@@@@@@@@@##@.*@@@@..+#@%.=@@. @.@#..#@@.:*#+. .@*%#@@@@@@@@@@@@@@@@@@#=*=*@. .@+@@@@@@@@@@@@@")
        time.sleep(0.1)
        print("@@@@@@@@.+@@@@@@@@@@@@@@@@@@@@@@@.+#@...@@@@@..#@..=@%@@@...@. .@@@@@@%@@@@@@@@@@@#@@@@@@@@*..@@: @@@@=..@@@*-@@@@@")
        time.sleep(0.1)
        print("@#@.==@@%@.-@@@@@@@@@@@#@@@@@=.#@@@@@@..@@- .@@@@@@ -:@%..@@@@@@ .@%%..+@@#@@@@@@@@@@#@@@@@-%@. .@@@@@=.-@@=..:%@@@")
        time.sleep(0.1)
        print("=.@:@..@%@@@@@@@@@@@@@@@@@@@@@@@@*#. .+@@@..-#@%-:..@#@@=..#-*@% .@@@@@@%@@@@@@@@@@@@@@@@@@@:.@@@@.....-+@@@@@@@@@@")
        time.sleep(0.1)
        print("%@@@@@@@@@#%@@@@@@@@@@@%##:.-......@@@@@@@:..... :=@@*@@@@+.. .....@@@@@@@-+=#%%@@@@@@@@@@@@@@@@..#@@@@@@@@.....*@@")
        time.sleep(0.1)
        print(".@@@@@@@@@@@@@@@@@.@@@@@@@@@@@@@@.. +*:...@@@@@@@@...=@:..=@@@@@@@+...#%...@@@@@@@@*...+....-@@@@@@=....@@=-@@@@@@#")
        time.sleep(0.1)
        print("@@...#@@@@@@=...*.@#+..:%@@@@@@. :@@@@@ *@@@@@@@@=.%@@@@@..@@@@@@@@@.:@@@@*..#%@@--@@@=%@@@%...--@@@@@@..@@@@*+-#@#")
        time.sleep(0.1)
        print("...@@@#.....%@@@@%@@...@@@@=...@@@%@%@@%..*@@@=...@@@#@@@@#..:@%@@...@@@@@@@@%...*@+@...:@@@@@@@*....@@@....@@@@@@#")
        time.sleep(0.1)
        print(".%@@:...@@@@@@@@@@...=#@#.-:#@@@@%@@@@%=:.-@##.@:@@@%#@@@@@@--.+#@#.::%@@@@@@@@@.-.=@%*-...@@@@@@@@@:..-@@@=...-@@@")
        time.sleep(0.1)
        print("#@#.-.=@@@@@#*+...%@@@@@@....@@@@@@%=..-#@@@@@@.:.#@#%@@@*:..=@@%@@@%=..-#@@@@+=.=.*@@@@@@@:...+-+#:%.-..@@@@@@@*..")
        time.sleep(0.1)
        print("@@##-=........+%@@@@@@@@@#+*-......:.@@@@@@%@%@@@.#-....-+**@@@@@#@@@@@@*=#--:*#*@#@@@@@@#@@@@@%=+-=+*%@@###@@@@@@@")
        time.sleep(0.1)                                                                                                                                                 
        print("                                                                                                                                                                   ")
        time.sleep(0.1)
        print("                                                                                                                                                                   ")
        time.sleep(0.1)
        print("     .                                   @=          .                                                                                                             ")
        time.sleep(0.1)
        print("    +@@                                 :@@       =@@@@                                                                                                            ")
        time.sleep(0.1)
        print("    +@@       -@@@   =#     *.  .@@@-   :@@       #  @@                                                                                                            ")
        time.sleep(0.1)
        print("    +@@     *@@  :@@ =@@   @@= @@:  @@- :@@          @@        @@@@@@.@                                                  @#    @@  @-                              ")
        time.sleep(0.1)
        print("    +@@     @@@@@@@@+ @@# +@@ @@@@@@@@% :@@          @@          @%   @@@@@  @@#@#    @@#@@ @@@* @@@@@ %@  +@ @@@@@: %@@@@#   +@@%.@- @@@@@. @@@@@ -@@@:           ")
        time.sleep(0.1)
        print("    +@@     @@         @@-@@  @@#       :@@          @@          @%   @  :@ %@@@@@   .@: @@ @@  @@   @:@@  *@ @@  @@.@=  @#    @@  @--@.  @@%@   @@=@              ")
        time.sleep(0.1)
        print("    +@@===- #@@: .-:   =@@@    @@+  :-  :@@       :-+@@--        @%   @  :@ *@       -@%#.  @@  @@  +@ %@  @@ @@  @@ @% .@#    @@  @-:@+  @%-@:  @+=@              ")
        time.sleep(0.1)
        print("     @@@@@%   #@@@@:    =@:     -@@@@=   @:       %@@@@@@        %.   @   %  -@@@-   -@+=@@:+*   =@@%   *@@-= :*  *=  %@#+.    =+  #  .%@@-   @@@   #              ")
        time.sleep(0.1)
        print("                                                                                      @@@@=                                                                        ")
        time.sleep(0.1)


    def startingui():
        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
        time.sleep(0.1)
        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
        time.sleep(0.1)
        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
        time.sleep(0.1)
        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
        time.sleep(0.1)
        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
        time.sleep(0.1)
        print("@@@@@@#-------*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@--=@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@-----------@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@--=@@@@@@@@@")
        time.sleep(0.1)
        print("@@@@@---+@@@*---%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@---@@@@@%=--*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@--=@@@@@@@@@")
        time.sleep(0.1)
        print("@@@@+--@@@@@@@---@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@---@@@@@@@=-=@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@--=@@@@@@@@@")
        time.sleep(0.1)
        print("@@@@=-=@@@@@@@@@@@@@@--------#@@@@@---------#@@@--=@@@%--+------%@@@@@#-------+@@@@@@@@@@@@---@@@@@@@--=@@@@*-------=@@@+--@@@@@#--#@@+-------=@@@@@--=@@@@@@@@@")
        time.sleep(0.1)
        print("@@@@=-=@@@@@@@@@@@@@@@%@@@@*--#@@@=--@@@@@*#@@@@--=@@@%--=@@@@=--@@@@*--*@@@#--+@@@@@@@@@@@---+++++=---@@@@+--*@@@#--=@@@--=@@@@--+@@@@%@@@@@--=@@@@--=@@@@@@@@@")
        time.sleep(0.1)
        print("@@@@=-=@@@@@@@@@@@@@@@@@@@@@--+@@@=--*%@@@@@@@@@--=@@@%--#@@@@%--#@@@---@@@@@=--@@@@@@@@@@@---------=%@@@@@=-=@@@@@*--@@@%--%@@+--@@@@@@@@@@@*--@@@@--=@@@@@@@@@")
        time.sleep(0.1)
        print("@@@@=-=@@@@@@@@@@@@@%---------+@@@@+--------%@@@--=@@@%--#@@@@%--#@@@---@@@@@+--@@@@@@@@@@@---@@@@=--%@@@@@--=@@@@@*--@@@@+--@%--%@@@@----------@@@@--=@@@@@@@@@")
        time.sleep(0.1)
        print("@@@@+--@@@@@@@---@@@--*@@@@@--+@@@@@@@@@@@--=@@@--=@@@%--#@@@@%--#@@@---@@@@@=--@@@@@@@@@@@---@@@@@=--%@@@@=-=@@@@@+--@@@@@--+=-=@@@@+--@@@@@*--@@@@--=@@@@@@@@@")
        time.sleep(0.1)
        print("@@@@@---+@@@*---%@@@--+@@@@@--+@@@=-*@@@@%--+@@@--=@@@%--#@@@@%--#@@@#--=@@@+--+@@@@@@@@@@@---@@@@@@---%@@@*--=@@@+--+@@@@@%----@@@@@*--%@@@@+--@@@@---@@@@@@@@@")
        time.sleep(0.1)
        print("@@@@@@#-------*@@@@@@---------+@@@*--------+@@@@--=@@@%--#@@@@%--#@@@@%-------#@@@@@@@@@@@@---@@@@@@@---@@@@%-------#@@@@@@@+--*@@@@@@=---------@@@@#---=@@@@@@@")
        time.sleep(0.1)
        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@+-=@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
        time.sleep(0.1)
        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@+--%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
        time.sleep(0.1)
        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@#--------------------------------------------------------------------------------------------------------------=@@@@@@@@@@@@@@@@@@@@@")
        time.sleep(0.1)
        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@#--------------------------------------------------------------------------------------------------------------=@@@@@@@@@@@@@@@@@@@@@")
        time.sleep(0.1)
        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@#--------------------------------------------------------------------------------------------------------------=@@@@@@@@@@@@@@@@@@@@@")
        time.sleep(0.1)
        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@#--------------------------------------------------------------------------------------------------------------=@@@@@@@@@@@@@@@@@@@@@")
        time.sleep(0.1)
        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@#--------------------------------------------------------------------------------------------------------------=@@@@@@@@@@@@@@@@@@@@@")
        time.sleep(0.1)
        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@#--------------------------------------------------------------------------------------------------------------=@@@@@@@@@@@@@@@@@@@@@")
        time.sleep(0.1)
        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@#--------------------------------------------------------------------------------------------------------------=@@@@@@@@@@@@@@@@@@@@@")
        time.sleep(0.1)
        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@#--------------------------------------------------------------------------------------------------------------=@@@@@@@@@@@@@@@@@@@@@")
        time.sleep(0.1)
        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@#--------------------------------------------------------------------------------------------------------------=@@@@@@@@@@@@@@@@@@@@@")
        time.sleep(0.1)
        print("@@@@@@@@@@=-------------------------------------------------------------------------------------------------------------------------------------------@@@@@@@@@@")
        time.sleep(0.1)
        print("@@@@@@@@@@=-------------------------------------------------------------------------------------------------------------------------------------------@@@@@@@@@@")
        time.sleep(0.1)
        print("@@@@@@@@@@=-------------------------------------------------------------------------------------------------------------------------------------------@@@@@@@@@@")
        time.sleep(0.1)
        print("@@@@@@@@@@=-------------------------------------------------------------------------------------------------------------------------------------------@@@@@@@@@@")
        time.sleep(0.1)
        print("@@@@@@@@@@=-------------------------------------------------------------------------------------------------------------------------------------------@@@@@@@@@@")
        time.sleep(0.1)
        print("@@@@@@@@@@=-------------------------------------------------------------------------------------------------------------------------------------------@@@@@@@@@@")
        time.sleep(0.1)
        print("@@@@@@@@@@=-------------------------------------------------------------------------------------------------------------------------------------------@@@@@@@@@@")
        time.sleep(0.1)
        print("@@@@@@@@@@=-------------------------------------------------------------------------------------------------------------------------------------------@@@@@@@@@@")
        time.sleep(0.1)
        print("@@@@@@@@@@=-------------------------------------------------------------------------------------------------------------------------------------------@@@@@@@@@@")
        time.sleep(0.1)
        print("@@@@@@@@@@=-------------------------------------------------------------------------------------------------------------------------------------------@@@@@@@@@@")
        time.sleep(0.1)
        print("@@@@@@@@@@=-------------------------------------------------------------------------------------------------------------------------------------------@@@@@@@@@@")
        time.sleep(0.1)
        print("@@@@@@@@@@=-------------------------------------------------------------------------------------------------------------------------------------------@@@@@@@@@@")
        time.sleep(0.1)
        print("@@@@@@@@@@=-------------------------------------------------------------------------------------------------------------------------------------------@@@@@@@@@@")
        time.sleep(0.1)
        print("@@@@@@@@@@=-------------------------------------------------------------------------------------------------------------------------------------------@@@@@@@@@@")
        time.sleep(0.1)
        print("@@@@@@@@@@=-------------------------------------------------------------------------------------------------------------------------------------------@@@@@@@@@@")
        time.sleep(0.1)
        print("@@@@@@@@@@=-------------------------------------------------------------------------------------------------------------------------------------------@@@@@@@@@@")
        time.sleep(0.1)
        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
        time.sleep(0.1)
        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
        time.sleep(0.1)
        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
        time.sleep(0.1)
        print("Here is how to play")
        time.sleep(0.1)
        print("First you will see a menu like this")
        time.sleep(0.1)
        print(f"---------------option 1----")
        time.sleep(0.1)
        print(f"--start-------------------------")
        time.sleep(0.1)
        print(f"---------------option 2----")
        time.sleep(0.1)
        print("Now what do you do at this stage")
        time.sleep(0.1)
        print("well you will recive two choices ")
        time.sleep(0.1)
        print("Where would you like to go(w or S)")
        time.sleep(0.1)
        print("This is the choice on which option with W being the first one and S being the second one")
        time.sleep(0.1)
        startint = input("Would you like to start:")
        global playing
        playing = True
        leveldesign1()
        

    def bet(money,boonbet): 
        all_in = False
        while True:
            while True:
                boonbet = input("How much do you want")
                if boonbet.isnumeric() == True:
                    break
            boonbet = int(boonbet)
            if boonbet == money:
                print("You went all in")
                all_in = True

            if boonbet > money:
                print("To much money please input a accepted amount")
            else:
                break

        return(money,boonbet,all_in)

    def lotterygame(boonbet,money,islost):

        print(f"You have {money} dollars")
        paction = input("What size lottey do you want to play (L:50 M:25 S:5)")
        if paction == "l" or paction == "L":
            boonbet = 50
            all_in = False
            chance = random.randint(1,10)
            if chance == 1:
                claculated_boon = calcboon(luckstat,money,boonbet,boons,all_in)
                money = claculated_boon[0]
                has_lost = claculated_boon[1]
                money += boonbet * 2
                print("You won")
            else:
                islost = True
                claculated_boon = calcboon(luckstat,money,boonbet,boons,all_in)
                money = claculated_boon[0]
                has_lost = claculated_boon[1]
                money -= boonbet
                print("Sorry you lost")
        if paction == "m" or paction == "M":
            boonbet = 25
            all_in = False
            chance = random.randint(1,10)
            if chance == 1:
                claculated_boon = calcboon(luckstat,money,boonbet,boons,all_in)
                money = claculated_boon[0]
                has_lost = claculated_boon[1]
                money += boonbet * 2
                print("You won")
            else:
                islost = True
                claculated_boon = calcboon(luckstat,money,boonbet,boons,all_in)
                money = claculated_boon[0]
                has_lost = claculated_boon[1]
                money -= boonbet
                print("Sorry you lost")
        if paction == "s" or paction == "S":
            boonbet = 5
            all_in = False
            chance = random.randint(1,10)
            if chance == 1:
                claculated_boon = calcboon(luckstat,money,boonbet,boons,all_in)
                money = claculated_boon[0]
                has_lost = claculated_boon[1]
                money += boonbet * 2
                print("You won")
            else:
                islost = True
                claculated_boon = calcboon(luckstat,money,boonbet,boons,all_in)
                money = claculated_boon[0]
                has_lost = claculated_boon[1]
                money -= boonbet
                print("Sorry you lost")
    def loser():
        print(".+##############################################*-      ")
        time.sleep(0.1)
        print("+#=------------------------------------------------=*#  ")  
        time.sleep(0.1)
        print("*#----------------------------------------------------+@")
        time.sleep(0.1)
        print("@+----------------------------------------------------=@")
        time.sleep(0.1)
        print("@+----------------------------------====-----==-------=@") 
        time.sleep(0.1)
        print("@+----+%=------+%%%%@*=----@%%@+---+@%%#+--=#@%%%=----=@")
        time.sleep(0.1)
        print("@+----+%=----=#*-----*%=--#@--=%---+#------=*+--#*=---=@")
        time.sleep(0.1)
        print("@+----+%=----+%=------#+---#@@%----+@@@@*--=#@@@#=----=@")
        time.sleep(0.1)
        print("@+----+%=----=#+-----+%=--*#--=@---+#------=*+-=#+----=@")
        time.sleep(0.1)
        print("@+----+@%%%*--=+%%%%@#=---=@%%@+---+@%%%+--=#+--**=---=@")
        time.sleep(0.1)
        print("@+-----=====-----===--------==------====--------------=@")
        time.sleep(0.1)
        print("@+----------------------------------------------------=@")
        time.sleep(0.1)
        print("##----------------------------------------------------+@")
        time.sleep(0.1)
        print("*#=------------------------------------------------=*%   ")
        time.sleep(0.1)
        print(".%#*****************=-----=********************#%-       ")
        time.sleep(0.1)
        print("                    *=---+@-                             ")  
        time.sleep(0.1)   
        print("                    #=-+@:                               ")     
        time.sleep(0.1)
        print("                    ###-                                 ")     
        time.sleep(0.1)
        print("                    =                                    ")   
        time.sleep(0.1)
        print("                                                         ")  
        time.sleep(0.1)
        print("                                    %*.  .*@%-=%:        ")    
        time.sleep(0.1)
        print("                                    %=:%+.  .*+..-%.     ")     
        time.sleep(0.1)
        print("                                @@@+..:%=.  ..  .=%      ")   
        time.sleep(0.1)
        print("                                -#..:%=..:%-.      =*    ")  
        time.sleep(0.1)
        print("                            -%:-%=..-%-.         .%      ")  
        time.sleep(0.1)
        print("                            %*  .-%-....          .+#    ")
        time.sleep(0.1)
        print("                                .%-  .::               +%")
        time.sleep(0.1)
        print("                                :#:                :#-   ")
        time.sleep(0.1)
        print("                                    -*:            .#-   ")  
        time.sleep(0.1)
        print("                                    =#+:..     .*=       ")    
        time.sleep(0.1)
        print("                                        -*:. .++         ")     
        time.sleep(0.1) 
        print("                                            :**+         ")        
            

    bosslevel = 0
    global currentpath
    currentpath = "Start"
    global branchpath1
    global branchpath2
    branchpath1 = ""
    branchpath2 = ""
    global pathrand
    pathrand = 0
    global money
    money = 500
    global boonbet
    boonbet = 0
    global boons
    boons = []
    global potentailboonname
    global potentailbooncost
    potentailboonname = ["double trouble","money laundering","bonus check","Basic inssurance","diamond inssurance","Daily Double", "Daily Triple","Lucky coin","Budlight","Sober","basic Money maker","Extreme money maker","Money printer","Little for me","A lot for me","Stolen tokens","Too lucky","Grand money maker","All in frenzy"]
    potentailbooncost = [60, 120, 70, 100, 180, 50, 100, 60, 75, 136, 120, 180,200,40,80,140,220,500,10]
    global islost
    islost = False
    global levelCounter
    levelCounter = 20
    global luckstat
    luckstat = 0

    playing = True
    has_won = False
    startingui()
    luckstat = 0
    while playing == True:
            print(f"You are {levelCounter} levels from the boss")
            pathgen(currentpath,islost)
            pathchoice(currentpath)
            levelCounter -= 1
            print(f"You are {levelCounter} levels from the boss")
            if levelCounter <= 0:
                input("Are you ready to countinue:")
                jackblack()


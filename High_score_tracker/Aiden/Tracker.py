#AS 2nd High score tracker
import csv

def score_tracking(username, score):
    all = []
    with open("Documents/A_Highscores.csv", mode= 'r') as sample:
        reader = csv.reader(sample)
        for line in reader:
            if line[0] == 'Username':
                pass
            else:
                all.append({'Username':line[0] ,'Highscore':line[1] ,'Latest Score':line[2]})
        for line in all:
            if line["Username"] == username:
                newline = line
                all.remove(line)
                newline['Latest Score'] = score
                if score > int(newline['Highscore']):
                    newline['Highscore'] = score
                else:
                    pass
                print(newline)
            else:
                pass
        try:
            all.append(newline)
        except:
            all.append({'Username':username ,'Highscore':score ,'Latest Score':score})
    with open("Documents/A_Highscores.csv", mode= 'w', newline= '') as sample:
        fieldnames = ['Username','Highscore','Latest Score']
        writer = csv.DictWriter(sample, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(all)

def highscores():
    all = []
    current = {'Highscore':0}
    with open("Documents/A_Highscores.csv", mode= 'r') as sample:
        reader = csv.reader(sample)
        for line in reader:
            if line[0] == 'Username':
                pass
            else:
                all.append({'Username':line[0] ,'Highscore':line[1]})
        print(all)
        if len(all) >= 10:
            for i in range(1, 10):
                for user in all:
                    if int(user['Highscore']) > int(current['Highscore']):
                        current = user
                    elif int(user['Highscore']) == int(current['Highscore']):
                        current = user
                    else:
                        pass
                print(f'{i}: {current["Username"]}: {current["Highscore"]}')
                all.remove(current)
                current = {'Highscore':0}
        else:
            for i in range(1, len(all)):
                for user in all:
                    if int(user['Highscore']) > int(current['Highscore']):
                        current = user
                    elif int(user['Highscore']) == int(current['Highscore']):
                        current = user
                    else:
                        pass
                print(f'{i}: {current["Username"]}: {current["Highscore"]}')
                all.remove(current)
                current = {'Highscore':0}


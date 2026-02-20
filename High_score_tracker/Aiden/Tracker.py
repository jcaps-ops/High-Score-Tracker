#AS 2nd High score tracker
import csv

def score_tracking(username, score):
    all = []
    with open("High_score_tracker/Aiden/highscores.csv", mode= 'r') as sample:
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
    with open("High_score_tracker/Aiden/highscores.csv", mode= 'w', newline= '') as sample:
        fieldnames = ['Username','Highscore','Latest Score']
        writer = csv.DictWriter(sample, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(all)

score_tracking('Steve', 100)
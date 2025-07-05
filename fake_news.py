#MINI PROJECT ON :- fake news genrator 
import random
print("'WLECOME TO FAKE NEWS GENRATOR'")

#Creating subjects
bollywood = ['Sharukh khan','Salman khan','Tiger shroff']
politics = ['Rahul Gandhi', 'Amit Shah', 'Arvind Kejriwal', 'Yogi Adityanath']
comedy = ['Kapil Sharma', 'Johnny Lever', 'Bhuvan Bam', 'Samay Raina']

#creating action
b = ['was seen selling popcorn', 'danced on road during traffic', 'got lost in Film City']
p = ['was seen eating golgappe', 'gave speech in rap style', 'fell asleep in Lok Sabha', 'announced free wifi for cows']
c = ['started crying after joke failed', 'got stuck in a laughing loop', 'mistook sanitizer for hair oil']

#creating place
bp = ['outside Mannat', 'in Bandra', 'on a film set', 'near RedFort', 'near India Gate']
pp = ['in Parliament', 'outside BJP office', 'at Delhi Metro station', 'in front of Rashtrapati Bhavan']
cp = ['on live stage', 'in a comedy show', 'at Mumbai airport', 'in shopping mall']

while True: #this loop will go on until user say N/n to stop
    a = input("you want to create a fake new's headline Y/N:-")
    if a.upper() == 'Y':

        print("on what topic you want to create a fake new's:-   1) poltics  2)comedy  3)bollywood") 
        
        d = input("tell your response:- ")
        
        if d.lower() == 'politics' or d == '1' :
            subject = random.choice(politics)
            action = random.choice(p)
            place = random.choice(pp)
            print(f"Fake new's headline on Poltics is :- {subject} {action} {place} ")

        elif d.lower() == 'comedy' or d == '2' :
            subject = random.choice(comedy)
            action = random.choice(c)
            place = random.choice(cp)
            print(f"Fake new's headline on comedy is :- {subject} {action} {place} ")

        elif d.lower() == 'bollywood' or d == '3' :
            subject = random.choice(bollywood)
            action = random.choice(b)
            place = random.choice(bp)
            print(f"Fake new's headline on Bollywood is :- {subject} {action} {place} ")

        elif d.lower() == 'politics' or d == '4':
            subject = random.choice(politics)
            action = random.choice(p)
            place = random.choice(pp)
            print(f"Fake new's headline on Poltic's is :- {subject} {action} {place} ")
        
        else:
            print("Choose Correctly, TRY again")
            break 
        
    elif a.upper() =='N':
        print("Exiting Fake New's Genrator")
        break
    
    else:
        print("Please enter y/Y for YES and n/N for NO")

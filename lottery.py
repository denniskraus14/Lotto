#lottery simulation (test)

#key:
#A 5 $2 tickets ($10/week)
#B 2 $2 tickets and 2 $2 tickets ($10/week)
#C 3 $3 tickets($9/week)
#D 4 $3 tickets ($12 week)
import random

#source: https://www.palottery.state.pa.us/draw-games/powerball/prizes-chances.aspx
def calculate_winnings(tickets, winners, name, multiplier_value):
    winnings = 0
    index = 0
    multiply=True
    million = False
    for ticket in tickets:
        whites = 0
        red = 0
        temp_winnings = 0
        for num in ticket[:-1]: #loop for the 5 whites
            if num in winners[:-1]:
                whites+=1
        if ticket[-1]==winners[-1]: #if you got the powerball
            red+=1
        #check to see how much you won
        if whites==5 and red==1: #jackpot - let's assume last jackpot of 111,000,000
            temp_winnings += 111000000
            multiply=False
            print(name,"jackpot in the year", years, "multiplier =", multiplier_value, winners)
            break
        elif whites==5 and red==0:
            temp_winnings += 1000000
            million=True
            print(name,"1000000 in the year",years,"multiplier =", multiplier_value, winners)
            break
        elif whites==4 and red==1:
            temp_winnings += 50000
            print(name,"50000 in the year", years,"multiplier =", multiplier_value, winners)
            break
        elif whites==4 and red==0:
            temp_winnings+=100
        elif whites==3 and red==1:
            temp_winnings+=100
        elif whites==3 and red==0:
            temp_winnings+=7
        elif whites==2 and red==1:
            temp_winnings+=7
        elif whites==1 and red==1:
            temp_winnings+=4
        elif whites==0 and red==1:
            temp_winnings+=4

        if name=="B" and (index==0 or index==1) and multiply:
            #if multiplier and is B's first or second ticket
            winnings += temp_winnings*multiplier_value
        elif ((name=="B" and (index==0 or index==1) and million) or ((name=="C" or name=="D") and million)):
            winnings+=2000000
        elif (name=="C" or name=="D") and multiply:
            winnings+= temp_winnings*multiplier_value
        else:
            winnings+=temp_winnings
        index+=1 #next ticket
    if name=="C":
        return winnings-9 #B 3 $3 tickets
    elif name=="D":
        return winnings-12
    else:
        return winnings-10 #subtract cost of all the tickets

#source: https://lottery-pa.custhelp.com/app/answers/detail/a_id/3340/~/how-is-the-power-play-multiplier-chosen-for-the-powerball-game%3F
def choose_megaplier():
    twos = [2]*24
    threes = [3] * 13
    fours = [4] * 3
    fives = [5] * 2
    tens = [10]
    total = twos+threes+fours+fives+tens
    random.shuffle(total)
    return random.choice(total)

#powerball rules
#this is a function that randomly chooses the 5 (1-69 balls) and 1 powerball(1-26)  
def drawing():
    nums = []
    while len(nums)<5: #first 5
        num = random.randint(1,69)
        if num in nums:
            pass
        else:
            nums.append(num)
    nums.append(random.randint(1,26)) #6th ball
    return nums

#main loop simulating 'winning' lifetimes (a prize over 50000)
years = 2021
A_total=0
B_total = 0
C_total=0
D_total = 0
deaths=0
lifetimes=0
#winning_lifetime = 0
while lifetimes<1:
    while years<2075:
        trial = 0
        A=[]
        B=[]
        C=[]
        D = []
        while trial<52: #lets say we play for a full year
            winners = drawing()
            #let's assume 4 tickets are the same nums and A gets an extra ticket
            #let's also choose B's first two tickets as the multiplier tickets
            #likewise, C's 3 tickets are the first 3 and D's 4 are the first 4
            ticket1 = drawing()
            ticket2 = drawing()
            ticket3 = drawing()
            ticket4 = drawing()
            ticket5 = drawing()
            megaplier_value = choose_megaplier()
            A.append(calculate_winnings([ticket1,ticket2,ticket3,ticket4,ticket5], winners, "A",1)) #your megaplier is 1
            B.append(calculate_winnings([ticket1,ticket2,ticket3,ticket4], winners, "B", megaplier_value))
            C.append(calculate_winnings([ticket1,ticket2,ticket3], winners, "C", megaplier_value))
            D.append(calculate_winnings([ticket1,ticket2,ticket3, ticket4], winners, "D", megaplier_value))
            trial+=1
        A_total+=sum(A)
        B_total+=sum(B)
        C_total+=sum(C)
        D_total+=sum(D)
        #if max(D)>=49985 or max(B)>=49985 or max(A)>=49985  or max(C)>=49985:
            #winning_lifetime+=1
        #else:
            #deaths+=1
        years+=1
    lifetimes+=1
    years = 2021
    
    

print("Over",lifetimes,"lifetimes:")
print("A lifetime:", A_total)
print("B lifetime:", B_total)
print("C lifetime:", C_total)
print("D lifetime:", D_total)

#print("Winning lifetimes",winning_lifetime)
#print("Winless deaths:",deaths)


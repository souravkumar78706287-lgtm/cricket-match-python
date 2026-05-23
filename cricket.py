# cricket match full ipl by sourav kumar
print("..THE MATCH IS STARTED..")
team1 = input("Enter team1 name: ")
team2 = input("Enter team2 name ")
print(f"{team1} vs {team2}")

print("\nTOSS TIME")
toss = int(input("Enter 1 for Head and 0 for Tail: "))
if toss == 1:
    batting = team1
    bowling = team2
    print(f"{team1} won toss and elected to bat")
else:
    batting = team2
    bowling = team1
    print(f"{team2} will bat first and they won")
total_runs = 0
wicket = 0
batsman1_runs = 0
batsman2_runs = 0
overs = int(input("\nEnter total overs: "))
players = ["harsh","arnav","sourav","ankit","aadi","siddharth","farzan","krishna","apurva","nishita","nikhill"]
bowlers = ["harsh","arnav","sourav","apurva","raj"]
batsman1 = players[0]
batsman2 = players[1]
batsmanindex = 1
bowlerindex = 0
for over in range(overs):
    print(f"\nOVER {over+1}")
    bowler = bowlers[bowlerindex]
    bowlerindex += 1
    if bowlerindex == len(bowlers):
        bowlerindex = 0
    for ball in range(6):
        ball_input = input("Enter run/W/WD/NB: ")
        if ball_input.upper() == "W":
            wicket += 1
            print("WICKET")
            print(f"{batsman1}: out")
            batsmanindex += 1
            if batsmanindex < len(players):
                batsman1 = players[batsmanindex]
                print(f"new batsman is {batsman1}")
            if wicket == 10:
                print("ALL OUT")
                break
        elif ball_input.upper() == "WD":
            total_runs += 1
            print("Wide Ball")
        elif ball_input.upper() == "NB":
            total_runs += 1
            print("No Ball")

        else:
            run = int(ball_input)
            total_runs += run
            batsman1_runs += run
            if run == 4:
                print("FOUR")

            elif run == 6:
                print("SIX")

            elif run == 0:
                print("DOT BALL")

            if run % 2 == 1:
                batsman1, batsman2 = batsman2, batsman1
                batsman1_runs, batsman2_runs = batsman2_runs, batsman1_runs
        print(f"Score: {total_runs}/{wicket}")
    batsman1, batsman2 = batsman2, batsman1
    batsman1_runs, batsman2_runs = batsman2_runs, batsman1_runs
    print("\n========== SCOREBOARD ==========")
    print(f"Score: {total_runs}/{wicket}")
    print(f"Overs: {over+1}")
    print(f"\nStriker: {batsman1} - {batsman1_runs}")
    print(f"Non-Striker: {batsman2} - {batsman2_runs}")
    print(f"Bowler: {bowler}")
    print(f"the match is now over..")

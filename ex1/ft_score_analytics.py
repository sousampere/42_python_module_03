#!/usr/bin/python3

import sys

av = sys.argv

if (len(av) == 1):
    print("=== Player Score Analytics ===")
    print(f"No score provided. Usage : python3 {av[0]} <score1> <score2> ...")
else:
    lst = []
    for arg in av[1:]:
        try:
            lst.append(int(arg))
        except ValueError:
            print("You typed a wrong argument. Please try "
                  f"with digits only. ({arg})")
            exit()
    players = len(lst)
    print("====================== Leaderboard ======================")
    print("")
    print(f"   /////////////\\\\      Total players : {len(lst)}")
    print(f"  (((((((((((((( \\\\     Total score   : {sum(lst)}")
    print(f"))) ~~      ~~  (((     Average Score : {sum(lst) / len(lst)}")
    print(f"((( (*)     (*) )))     High score    : {max(lst)}")
    print(f")))     <       (((     Lowest score  : {min(lst)}")
    print(f"((( '\\______/`  )))     Score range   : {max(lst) - min(lst)}")
    print(f")))\\___________/(((     Score processed : {lst}")
    print("      _) (_")
    print("     / \\_/ \\")
    print("    /(     )\\")
    print("   // )___( \\")
    print("    \\(     )//")
    print("    (       )")
    print("     |  |  |")
    print("      | | |")
    print("      | | |")
    print("     _|_|_|_")
    print("=========================================================")

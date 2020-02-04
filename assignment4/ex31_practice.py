print("""Prisoner's dilemma: A and B committed the same crime.
They can choose to 'confess' or 'not confess'.
A and B are not informed of the other person's decision.""")

print("A chooses to: ")
A_decision = str(input('> '))

if A_decision == 'confess':
    print("Should B 'confess' or 'not confess'?")

    B_decision = str(input('> '))
    if B_decision == 'confess':
        print("Both A and B are imprisoned for 4 years.")
    elif B_decision == 'not confess':
        print("A is imprisoned for 1 years. B is imprisoned for 8 years.")
    else:
        print("Not sure what will happen!")

elif A_decision == 'not confess':
    print(" Should B 'confess' or 'not confess'?")

    B_decision = str(input('> '))
    if B_decision == 'confess':
        print("A is imprisoned for 8 years. B is imprisoned for 1 years.")
    elif B_decision == 'not confess':
        print("Both A and B are imprisoned for 1 year.")

else:
    print("There is no game to play!")

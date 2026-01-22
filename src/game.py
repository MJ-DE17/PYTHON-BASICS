out = True
not_out = False
score = 0

action = input("What's the score? ")

if action.isnumeric() and int(action) <= 6:
    score += int(action)
    print("Score:", score)

elif action.lower() == "out":
    print("Next player")

else:
    print(not_out)
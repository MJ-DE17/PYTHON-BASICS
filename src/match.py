day = int(input("Enter the day"))
match day:
    case 1 | 7:
        print("Yeah its weekend")
    # case 7:
    #     print("Yeah its weekend")
    case _:
        print("Noo, its weekday")
        
day = 4
match day:
  case 1 | 2 | 3 | 4 | 5:
    print("Today is a weekday")
  case 6 | 7:
    print("I love weekends!")
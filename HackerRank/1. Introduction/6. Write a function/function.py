def is_leap(year):
    Leap = True

    if year % 400 == 0:
        Leap = True
    elif year % 100 == 0:
        Leap = False
    elif year % 4 == 0:
        Leap = True
    else:
        Leap = False
    return Leap

year = int(input())
print(is_leap(year))

from datetime import timedelta, date, datetime

inp = input("\nPress any key to start...\n")

if inp:
    start = datetime.today()

inp2 = input("\n\nNow press any key to stop\n")

if inp2:
    end = datetime.today()

print(str((end-start)))

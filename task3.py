sleep = int(input())
hours = int(input())
minutes = int(input())
sleepH = sleep // 60
sleepM = sleep % 60
sleepM += minutes
if (sleepM > 59):
    sleepM -= 60
    sleepH += 1
print(sleepH + hours)
print(sleepM)




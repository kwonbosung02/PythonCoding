from operator import eq
participant = input()
success = input()
participant = participant.replace("[","").replace("]","").replace('"',"").split(",")
success = success.replace("[","").replace("]","").replace('"',"").split(",")
answer = ''
Flag = True
participant.sort()
success.append('zzz')
success.sort()
print(participant)
print(success)

for i in range(len(success)):
    if not eq(participant[i],success[i]):
        answer = participant[i]
        break
    else:
        continue
print(answer)

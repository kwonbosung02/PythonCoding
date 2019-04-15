
import collections

participant = input()
success = input()
participant = participant.replace("[","").replace("]","").replace('"',"").split(",")
success = success.replace("[","").replace("]","").replace('"',"").split(",")    

print(list((collections.Counter(participant) -collections.Counter(success)).keys())[0])

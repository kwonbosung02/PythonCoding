
import collections

participant = input()
success = input()
participant = participant[1:-1].replace('"',"").split(",")

success = success[1:-1].replace('"',"").split(",")

print(list((collections.Counter(participant) -collections.Counter(success)).keys())[0])

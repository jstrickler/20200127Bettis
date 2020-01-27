#!/usr/bin/env python

actor = "Chris Hemsworth"
print(actor)
print(actor.upper())
print(actor)
print(len(actor))

actor_upper = actor.upper()
print(actor.lower())
print(actor.count('i'))
print(actor.count("wo"))
print(actor.count('h'))
print(actor.lower().count('h'))

print(actor.startswith("Chris"))
print(actor.startswith("Liam"))
print("is" in actor)
print("ris" in actor)
print("iam" in actor)

print(actor.replace("Chris", "Liam"))
print()

s = "      Guido Van Rossum      "
print("|" + s.lstrip() + "|")
print("|" + s.rstrip() + "|")
print("|" + s.strip() + "|")
print()

g = "dododoooooGuido Van Rossumoooddooodoodod"
print("|" + g.lstrip("do") + "|")
print("|" + g.rstrip("do") + "|")
print("|" + g.strip("do") + "|")
print()
print(g.replace('do', ''))

data = "10/20/2019"

fields = data.split('/')
print(fields)
month, day, year = data.split('/')
print(int(month), int(day), int(year))

print(data.split(':'))


x = 0
score = x

from colorama import Fore

#Question 1
print("whats the most common thing found on the staue's head?")
answer_1 = input("a) cones b) bird poop c) napkins")

if answer_1.lower() == "a" or answer_1.lower() == "cones":
    print(Fore.GREEN + "Correct") 
    x = x + 1   
else:
  print(Fore.RED + "incorrect, the answer was cones")
print("                              ")
print(Fore.WHITE)

#Question 2
print("what language is primarily used to build websites?")
answer_1 = input("a) javascript b) html c) c#")
if answer_1.lower() == "b" or answer_1.lower() == "html":
    print(Fore.GREEN + "Correct")
    x = x + 1   
else:
  print(Fore.RED + "incorrect, the answer was html")
print("                              ")
print(Fore.WHITE)

#Question 3
print("how many floors does the tower building have?")
answer_1 = input("a) 2 b) 6 c) 9")
if answer_1.lower() == "c" or answer_1.lower() == "9" or answer_1.lower() == "nine":
    print(Fore.GREEN + "Correct")
    x = x + 1   
else:
  print(Fore.RED + "incorrect, the answer was html")
print("                              ")
print(Fore.WHITE)

#Question 4
print("if 9 is 5 what year did USA get to the moon?")
answer_1 = input("a) 1969 b) 1965 c) 1970")
if answer_1.lower() == "b" or answer_1.lower() == "1965":
    print(Fore.GREEN + "Correct")
    x = x + 1   
else:
  print(Fore.RED + "incorrect, the answer was 1965, because 9 is 5")
print("                              ")
print(Fore.WHITE)

#Question 5
print("who is the first president of the united states?")
answer_1 = input("a) george washington b) elon musk              c) george washingmachine")
if answer_1.lower() == "a" or answer_1.lower() == "c" or answer_1.lower() == "george washington" or answer_1.lower() == "george washingmachine":
    print(Fore.GREEN + "Correct")
    x = x + 1   
else:
  print(Fore.RED + "incorrect, the answer was html")
print("                              ")
print(Fore.WHITE)

score = float(x / 5) * 100
print(x,"out of 5, that's",score, "%")
if x == 2 or x == 1 or x == 3 :
  print(Fore.RED + "you suck")
else:
  print(Fore.GREEN + "good job")

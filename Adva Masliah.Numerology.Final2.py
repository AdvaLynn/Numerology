#Numerology
#Adva Masliah
#Python 3
#To Get the Numerology of a First and Last Name
print("This program will give you the numerology of your name")
print("Please input your first and last name")
name = input()
r = 0
s = " "
name = name + s
number= ""
number2 = ""
add = 0
add1 = 0
s1 = 0
def capital(x):
    if ord(x)> 90:
        x = ord(x)
        x = x- 32
        return chr(x)
    else:
        return x
def lowercase(x):
    if ord(x)< 97:
      x = ord(x)
      x = x +32
      return chr(x)
    else:
      return x

def Numerology(N):
    if N == "a" or N =="A"or N == "j"or N == "J"or N == "S"or N == "s":
        n1 = 1
    if N == "b" or N =="B"or N == "k"or N == "K"or N == "t"or N == "T":
        n1 = 2
    if N == "c" or N =="C"or N == "l"or N == "L"or N == "u"or N == "U":
        n1 = 3
    if N == "D" or N =="d"or N == "M"or N == "m"or N == "V"or N == "v":
        n1 = 4
    if N == "e" or N =="E"or N == "n"or N == "N"or N == "W"or N == "w":
        n1 = 5
    if N == "f" or N =="F"or N == "o"or N == "O"or N == "X"or N == "x":
        n1 = 6
    if N == "g" or N =="G"or N == "p"or N == "P"or N == "y"or N == "Y":
        n1 = 7
    if N == "H" or N =="h"or N == "Q"or N == "q"or N == "Z"or N == "z":
        n1 = 8
    if N == "I" or N =="i"or N == "R"or N == "r":
        n1 = 9
    return n1
def middle(mylist):
    nl = []
    for i in range (len(mylist)):
       each = mylist[i]
       f = len(each)
       nl.append(f)
       m = max(nl)
    for i in range(len(mylist)):
          if len(mylist[i]) != m:
             x = (m - len(mylist[i]))/ 2
             if type(x) is float:
                x = int(x - 1)
                spaces = x * " "
             print(spaces + mylist[i] + spaces)
          else:
             print(mylist[i])
def keywords(x):
   if x == 1:
      mylist=["Initiating action", "Pioneering", "Leading", "Independent", "Attaining", "Individual"]
   if x == 2:
      mylist=["Cooperation", "Adaptability", "Consideration of others", "Partnering", "Mediating"]
   if x == 3:
      mylist=["Expression", "Verbalization", "Vocialization", "The arts", "The joy of living"]
   if x == 4:
      mylist=["A foundation", "Order", "Service", "Struggle against limits", "Steady growth"]
   if x == 5:
      mylist=["Expansiveness", "Visionary", "Adventure", "The constructive use of freedom"]
   if x == 6:
      mylist=["Responsibility", "Protection", "Nurturing", "Community, Balance", "Sympathy"]
   if x == 7:
      mylist=["Analysis", "Understanding", "Knowledge", "Awareness", "Studious", "Meditating"]
   if x == 8:
      mylist= ["Practical endeavors", "Status oriented", "Power-seeking", "High-material goals"]
   if x == 9:
      mylist= ["Humanitarian", "Giving nature", "Selflessness", "Obligations", "Creative expression"]
   return middle(mylist)

for L in range(len(name)):
  if name[L] == s:
        r = r + 1
        if r == 1:
            first= name[0:L]
            capital1 = capital(name[0])
            end = ""
            for c in range(1,len(first)):
              x = lowercase(name[c])
              end = end + x
            first = capital1 + end
            f = L
            for N in range(len(first)):
                s1 = first[N]
                s1 = Numerology(s1)
                number = number + str(s1)
                add = add + s1
                    
        if r == 2:
            second= name[f:L]
            capital2 = capital(second[1])
            end2 = ""
            for c in range(2,len(second)):
              y = lowercase(second[c])
              end2 = end2 + y
            second = capital2 + end2
            for N in range(len(second)):
                s2 = second[N]
                s2 = Numerology(s2)
                number2 = number2 + str(s2)
                add1 = add1 + s2
total = add + add1
stotal = str(total)
t = 0
y = "no"
for u in range(len(stotal)):
   t = t + int(stotal[u])
   if t > 9:
      t = str(t)
      t2 = 0
      for u2 in range(len(t)):
         t2 = t2 + int(t[u2])
         y = "yes"
   
                
print(first, second)
print(number, number2)
if y == "yes":
   print(t2)
   keyword = keywords(t2)
   
else:
   print(t)
   keyword = keywords(t)

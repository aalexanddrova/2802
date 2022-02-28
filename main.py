listeven=[ ]
listtodd=[ ]
listpos=[ ]
listneg=[ ]
listtens=[ ]
listhundrets=[ ]

N = int(input("cik veselu skaitlu: " ))
for x in range(N):
  x = int(input("ievadi tos: "))
  if x%2==0:
    listeven.append(x)
  if x%2!=0:
    listtodd.append(x)
  if x>0:
    listpos.append(x)
  if x<0:
    listneg.append(x)
  if 10<=x<100:
    listtens.append(x)
  if x>=100:
    listhundrets.append(x)
if len(listeven)>len(listtodd):
   print("vairak ie para skaitlu")
else:
  print("vairak ir para skaitlu")
if len(listpos)>len(listneg):
  print("vairak ir pozitivo skaitlu")
else:
  print("vairak ir negativo skaitlu")
if len(listtens)>len(listhundrets):
  print("vairak ir divciparu skaitlu")
else:
  print("vairak ir trisciparu skaitlu")
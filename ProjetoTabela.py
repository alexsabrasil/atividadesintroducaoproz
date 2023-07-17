#1
nota = 10
if (nota<=10) :
  #É menor ou igual a 10!
  print("Verdadeiro")
else:
  print()
Verdadeiro

#2
nota = 6
faltas = 4
if ((nota<=6) and (faltas<=3)) :
  #(faltas<=3) é falso
  # V && F = F
  print()
else:
  print("Falso")
  Falso

  #4
dia = "qua"
if ((dia == "sab") or (dia == "dom")) :
  # as duas setenças são falsas
  # F || F = F
  print()
else:
  print("Falso")
  Falso

  #5
feriado = True
if (not(feriado == False)) :
  # não (false) = true
  # !(false) = true
  print("Verdadeiro")
else:
  print()
  Verdadeiro

  #6
dia = "qua"
feriado = False
if ((dia == "seg") or not(feriado == False)) :
  # (!(false) = true) != (feriado = false)
  # as duas setenças são falsas
  # F || F = F
  print()
else:
  print("Falso")
  falso
  

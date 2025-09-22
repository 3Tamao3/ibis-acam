print("***********************")
print("*    Özbay, Rene      *")
print("*  Aufgabenstellung   *")
print("*       1usa          *")
print("***********************")

choice = int(input("write 1 for Rechteck or 2 for Kreis: "))

if choice == 1:
 choice2 = input("write Ur for Umfang or Ar for Fläche: ")
 if choice2 == 'Ur':
  a = float(input("Zahl für a: "))
  b = float (input("Zahl für b: "))
  uResult = 2 * a + 2 * b
  print("Der Umfang ist: ", uResult)
 elif choice2 == 'Ar':
  a = float(input("Zahl für a: "))
  b = float (input("Zahl für b: ")) 
  aResult = a * b
  print("Die Fläche beträgt: ", aResult)
 else:
  print("Invalid Choice")
 choice3 = input("write Uk for Umfang or Ak for Fläche: ")
 if choice3 == 'Uk':
  r = float(input("Zahl für r: "))
  rResult = 2 * 3.14 * r
  print("Der Umfang vom Kreis ist: ", rResult)
 elif choice3 == 'Ak':
  r = float(input("Zahl für r: "))
  arResult = 3.14 * pow(r, 2)
  print("Die Fläche vom Kreis ist: ", arResult)
 else:
  print("Invalid Choice")
else:
 print("Invalid Choice")

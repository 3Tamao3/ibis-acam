print ("***********************")
print ("*     Özbay Rene      *")
print ("*   Fibonacci-Folge   *")
print ("*       app17b        *")
print ("***********************")


def fibonacci(n, a=0, b=1):
    if n > 0:
        print(a)
        fibonacci(n - 1, b, a + b)

def berechne_exp(x, n):
   
    ist = 1
    fak = 1
    for i in range(1, 50):
        fak *= i
        ist += x**i / fak
   
    taylor = 0
    fak = 1
    for i in range(n + 1):
        if i > 0:
            fak *= i
        taylor += x**i / fak

    def absF(ist, taylor):
        return ist - taylor

    def relF(ist, taylor):
        return absF(ist, taylor) / ist * 100  # 

    print("IST-Wert:", ist)
    print("Taylor-Wert:", taylor)
    print("Absoluter Fehler:", absF(ist, taylor))
    print("Relativer Fehler:", round(relF(ist, taylor), 4), "%")

n_fib = int(input("Gib die Anzahl der Fibonacci-Zahlen ein: "))
print("Die Fibonacci-Zahlen bis", n_fib, "sind:")
fibonacci(n_fib)

x = float(input("\nGib den Wert für x ein: "))
n_exp = int(input("Gib die Anzahl der Taylor-Glieder n ein: "))
berechne_exp(x, n_exp)
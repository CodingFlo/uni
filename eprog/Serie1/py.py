# Übung 2
print("Hello, World! ", end="")
print("I am Florian Kainrath and I study technical mathematics at TU Wien")

# Übung 3
# "" weglassen => Programm kann nicht aufgeführt werden, da der Text so als Befehle gehandhabt werden, anstelle eines Strings/Textes

# Übung 4
grades = range(0, 101)  # 101 it only goes from 0 to n-1

for grade in grades:
    # gewollte Ausgabe
    print("Your final grade is: ", grade)
    # schönere Ausgabe mit Einheit
    print("Your final grade is: " + grade + "%")

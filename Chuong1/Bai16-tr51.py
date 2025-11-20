print("Các số chẵn chia hết cho 3 và bé hơn 50 là:")

for i in range(1, 50):
    if i % 2 == 0 and i % 3 == 0:
        print(i, end=" ")
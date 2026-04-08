import time

SIZE = 1_000_000
STEP = SIZE // 10

# Temps pour append
liste = []
s = time.time()
for i in range(SIZE):
    if i % STEP == 0:
        print(f"Empilement en cours: {i} éléments")
    liste.append(i)
e = time.time()
print(f"Taille de la liste après append: {len(liste)}")
print(f"Temps d'empilement pour une liste: {e - s:.4f} secondes")

# Temps pour pop()
liste = list(range(SIZE))
s = time.time()
for i in range(SIZE):
    if i % STEP == 0:
        print(f"Dépilement pop() en cours: {i} éléments")
    liste.pop()
e = time.time()
print(f"Temps de dépilement pour une liste: {e - s:.4f} secondes")

# Temps pour pop(0)
liste = list(range(SIZE))
s = time.time()
for i in range(SIZE):
    if i % STEP == 0:
        print(f"Dépilement pop(0) en cours: {i} éléments")
    liste.pop(0)
e = time.time()
print(f"Temps de dépilement pour une liste: {e - s:.4f} secondes")


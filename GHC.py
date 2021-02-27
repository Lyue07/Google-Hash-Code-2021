# RIBEIRO Luis
# AKADIRI Maessarath
# BOUHARICHA Basma
# RESTES Célia

file = open("a.txt", "r")
first_line = file.readline()
first_split = first_line.split()

simulation_time = int(first_split[0])
nb_intersection =int(first_split[1])
nb_streets = int(first_split[2])
nb_cars = int(first_split[3])
nb_points = int(first_split[4])

Streets = []
Streets_start_end = {}
street_time = {}

for i in range(nb_streets):
    street = file.readline().split()
    Streets_start_end[street[2]] = (int(street[0]), int(street[1]))
    street_time[street[2]] = int(street[3])

D = {}
for i in range(nb_cars):
    car = file.readline().split()
    for j in range(1, int(car[0])):
        if car[j] in D:
            D[car[j]] += 1
        else:
            D[car[j]] = 1
# D c'est les rues traversées par les voitures sauf la dernière
file.close()


# Croiser avec les noeud "end" pour identifier les intersections concernées
ff = list(D)
histo = [0] * nb_intersection
for e in ff:
    histo[Streets_start_end[e][1]] += 1

# print("D : ", D)
# print("Streets_start_end : ", Streets_start_end)
# print("histo : ", histo)


# On calcul le nbr de noeud concernés
nb_noeud = 0
for i in histo:
    if (i != 0):
        nb_noeud += 1

f = open("result_a.txt", "w")
f.write(str(nb_noeud) + '\n')

# On écris dans le fichier et on met le temps à 1sec pour chaque feu (méthode naive)

for i in range(len(histo)):
    if histo[i] != 0:
        f.write(str(i) + '\n')
        f.write(str(histo[i]) + '\n')
        for e in ff:
            if Streets_start_end[e][1] == i:
                f.write(str(e) + ' ' + str(1) + '\n')
f.close()



# for i in range(len(histo)):
#     if histo[i] != 0:
#         f.write(str(i) + '\n')
#         f.write(str(histo[i]) + '\n')
#         R = []
#         for e in ff:
#             if Streets_start_end[e][1] == i:
#                 R.append((e, D[e]))
#         R.sort(key=lambda tup: tup[1])
#         for i in range(len(R)):
#             time = R[i][1] // R[0][1]
#             f.write(str(R[i][0]) + ' ' + str(time) + '\n')                
# f.close()
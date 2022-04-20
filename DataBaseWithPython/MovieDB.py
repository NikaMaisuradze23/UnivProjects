import sqlite3
import matplotlib.pyplot as plt
import numpy as np

conn = sqlite3.connect('movies_ranking.sqlite')
cursor = conn.cursor()
baza = cursor.execute("SELECT * FROM movies")

filmi = str(input("ჩაწერეთ ფილმი: "))
studio = str(input("ჩაწერეთ სტუდია: "))  #ბაზაში დაამატებს რასაც მომხარებელი ჩაწერს
janri = str(input("ჩაწერეთ ჟანრი: "))
cursor.executemany("INSERT INTO movies (Film, Genre, LeadStudio) VALUES (?,?,?)", (filmi, studio, janri))

cursor.execute("UPDATE movies SET Genre=Horor WHERE id=1")


for elementi in baza: #წამოიღებს ყველაფერს ბაზიდან
    print(elementi)
    print("\n")


fetchch = cursor.fetchone() #წამოიღებს ბაზაში მერე სვეტის პირველ ელემენტს
print(fetchch[2])
print("\n")

fetchal = cursor.fetchall() #წამოიღებს თითოეული სვეტის პირველე ელემენტს სანამ არ გავა ბოლოში
for row in fetchal:
        print("Movie: ", row[1])
        print("janri: ", row[2])
        print("Studio: ", row[3])
        print("\n")




record = cursor.fetchmany(4) #წამოიღებს პირველ 4 ელემენტს ბაზიდან
for rec in record:
    print(rec)
    print("\n")




plt.style.use('_mpl-gallery')

# make data:
np.random.seed(76)
films = 0.5 + np.arange(8)
leadStudio = np.random.uniform(2, 7, len(films))

# plot
fig, ax = plt.subplots()

ax.bar(films, leadStudio, width=1, edgecolor="white", linewidth=0.7)

ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
       ylim=(0, 8), yticks=np.arange(1, 8))

plt.show()


conn.close()
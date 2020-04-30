import numpy as np
import matplotlib.pyplot as plt
scores = {"Day 1": 100, "Day 2": 108, "Day 3":112, "Day 4":115, "Day 5":150,
          "Day 6":178, "Day 7": 143, "Day 8": 132, "Day 9":190, "Day 10": 235,
          "Day 11":253, "Day 12": 298, "Day 13": 328, "Day 14":390, "Day 15": 257,
          "Day 16":288, "Day 17": 393, "Day 18": 425, "Day 19":458, "Day 20": 450,
          "Day 21":473, "Day 22": 333, "Day 23": 452, "Day 24":490, "Day 25": 495,
          "Day 26":488, "Day 27": 543, "Day 28": 532, "Day 29":590, "Day 30": 605}


Days = np.arange(1,31,1)
scorelist = [k for k in scores.values()]

fig= plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.plot(scorelist,Days,'b')
ax.set_ylabel('Days')
ax.set_xlabel('Score')
ax.set_ylim(1,30)
ax.set_xlim(0,1000)
plt.show()

sc1=np.mean(scorelist)
sc2=np.median(scorelist)
sc3=np.amax(scorelist)
sc4=np.amin(scorelist)

print("Your score statistics are:")
print("Average score:",sc1)
print("Median among score:",sc2)
print("Highest score:",sc3)
print("Lowest score:",sc4)

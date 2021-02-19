import json

data = json.load(open("payload_yul1927424da.json"))

import pprint
pprint.pprint(data)

sky = []
velocities = []
for row in data:
    sky.append([row["position"]["x"], row["position"]["y"]])
    velocities.append([row["velocity"]["dx"], row["velocity"]["dy"]])

def stars_aligned(sky):
    xpos = {}
    ypos = {}
    for pos in sky:
        xpos[pos[0]] = 1
        ypos[pos[1]] = 1
    return len(xpos) + len(ypos)

alignment = stars_aligned(sky)
print("Initial alignment:", alignment)
while True:
    for i in range(len(sky)):
        sky[i][0] += velocities[i][0]
        sky[i][1] += velocities[i][1]
    new_alignment = stars_aligned(sky)
    if new_alignment < alignment:
        alignment = new_alignment
        print("The stars align:", alignment)
        pprint.pprint(sky)




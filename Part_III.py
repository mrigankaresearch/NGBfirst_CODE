#@title copy verts
################# copy verts into new set ################
import numpy as np
NEW_Verts=np.zeros((len(verts)+1,3))
print(len(NEW_Verts))
for x in range(1,len(NEW_Verts)):

  verts[x-1][0]=verts[x-1][0]   # +Tx if needed to translate all coordinators into positive quadrant
  verts[x-1][1]=verts[x-1][1]
  verts[x-1][2]=verts[x-1][2]

  NEW_Verts[x][0]=verts[x-1][0]  #This is a copy where updated vertices are recorded
  NEW_Verts[x][1]=verts[x-1][1]
  NEW_Verts[x][2]=verts[x-1][2]

#@title format input
import numpy as np
import scipy.ndimage as nd
import matplotlib.pyplot as plt
import cv2
import math
import os
import PIL
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
import glob
#################### v and   f allignment ##############

f_CP=open('/content/sample_data/FandiskNoisy.obj','r')
verts=[]
faces=[]

Lines = f_CP.readlines()
count = 0
# Strips the newline character
for line in Lines:


  str1=line.split()
  if (len(str1)>0):
    if  str1[0]=='v':
      count +=1
      #print(count)
      str_3=str1[3].split('\n')
      verts.append([   str1[1],str1[2],str_3[0]  ])
    elif  str1[0]=='f':

      data=line.split()
      #print(data)
      count_V = len(data)

      Vert_Arr=[0,0,0,0]
      for FC in range(1, count_V):
        Vertex_id=data[FC].split('/')
        Vert_Arr[FC-1]=Vertex_id[0]

      if count_V== 4 :    # index + 3 vertices =4
        # FOR 3 PT FACES
        faces.append([        Vert_Arr[0],Vert_Arr[1],Vert_Arr[2]  ])
      elif count_V==5 :
        faces.append([        Vert_Arr[0],Vert_Arr[1],Vert_Arr[2]  ])
        faces.append([        Vert_Arr[0],Vert_Arr[2],Vert_Arr[3]  ])


print('vertex detected:',count)
#Write to
verts_align=np.zeros((len(verts),3))

for x in range(len(verts)):
  verts_align[x][0]=verts[x][0]
  verts_align[x][1]=verts[x][1]
  verts_align[x][2]=verts[x][2]

faces_align=np.zeros((len(faces),3))

for x in range(len(faces)):

  faces_align[x][0]=faces[x][0]
  faces_align[x][1]=faces[x][1]
  faces_align[x][2]=faces[x][2]


for i in range(faces_align.shape[0]):
  for j in range(3):
    faces_align[i][j] = int(faces_align[i][j])


f_CP=open('/content/sample_data/Vert_align.obj','w')

for data in range(0,verts_align.shape[0],1):
  f_CP.write('v'+' '+f'{ verts_align[data][0]}'+' '+f'{verts_align[data][1]}'+' '+f'{verts_align[data][2]}'+'\n')

for data in range(0,len(faces),1):
  f_CP.write('f'+' '+f'{faces_align[data][0]}'+' '+f'{faces_align[data][1]}'+' '+f'{faces_align[data][2]}'+'\n')

f_CP.close()

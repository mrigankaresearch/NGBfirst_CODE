#@title Adjacency List
######################## Adjacency List #################
### This code creates Adjacency List for each vertex###############
import numpy as np

Vert_Cords_Final=np.zeros((len(verts),3))

Total_Verts=len(NEW_Verts)             # minnus 1 is the actual
Adjacency_List=np.zeros((Total_Verts,205),dtype=int) ########### Assume each node has max 205 neighbours, index 0 is no. of times the vertex id found after search


# Search the faces
for this_face in range(len(faces)):

  N_V= len(faces[this_face])
  if N_V==3:
    first_index=faces[this_face][0]+1
    second_index=faces[this_face][1]+1
    third_index=faces[this_face][2]+1

    pos= int(Adjacency_List[first_index][0] + 1)
    Adjacency_List[first_index][pos]=second_index
    Adjacency_List[first_index][0]= int(Adjacency_List[first_index][0] + 1)

    pos= int(Adjacency_List[first_index][0] + 1)
    Adjacency_List[first_index][pos]=third_index
    Adjacency_List[first_index][0]= int(Adjacency_List[first_index][0] + 1)



first_index=0
second_index=0
third_index=0

for this_face in range(len(faces)):
  N_V= len(faces[this_face])
  if N_V==3:
    first_index=faces[this_face][1]+1
    second_index=faces[this_face][0]+1
    third_index=faces[this_face][2]+1
    #print(this_face,first_index)
    pos= int(Adjacency_List[first_index][0] + 1)
    Adjacency_List[first_index][pos]=second_index
    Adjacency_List[first_index][0]= int(Adjacency_List[first_index][0] + 1)

    pos= int(Adjacency_List[first_index][0] + 1)
    Adjacency_List[first_index][pos]=third_index
    Adjacency_List[first_index][0]= int(Adjacency_List[first_index][0] + 1)


first_index=0
second_index=0
third_index=0

for this_face in range(len(faces)):
  N_V= len(faces[this_face])
  if N_V==3:
    first_index=faces[this_face][2]+1
    second_index=faces[this_face][0]+1
    third_index=faces[this_face][1]+1

    pos= int(Adjacency_List[first_index][0] + 1)
    Adjacency_List[first_index][pos]=second_index
    Adjacency_List[first_index][0]= int(Adjacency_List[first_index][0] + 1)

    pos= int(Adjacency_List[first_index][0] + 1)
    Adjacency_List[first_index][pos]=third_index
    Adjacency_List[first_index][0]= int(Adjacency_List[first_index][0] + 1)

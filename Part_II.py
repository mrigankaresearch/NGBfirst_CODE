#@title align
f_CP=open('/content/sample_data/Vert_align.obj','r')
verts=[]
faces=[]

FACE_IDS=[]
FACE_IDS_unique=[]
print('Verts :',len(verts))
Lines = f_CP.readlines()
count = 0
# Strips the newline character
for line in Lines:
  count +=1
  str1=line.split()

  if  str1[0]=='v':

    #print(count)
    str_3=str1[3].split('\n')
    verts.append([float(str1[1]),float(str1[2]),float(str_3[0])])
  elif  str1[0]=='f':

    #print(data)
    str_3=str1[3].split('\n')
    Vert_Arr=[0,0,0]
    Vert_Arr[0]=int(float(str1[1]))
    Vert_Arr[1]=int(float(str1[2]))
    Vert_Arr[2]=int(float(str_3[0]))

    faces.append([        Vert_Arr[0]-1,Vert_Arr[1]-1,Vert_Arr[2]-1  ])
    FACE_IDS.append(Vert_Arr[0]-1)
    FACE_IDS.append(Vert_Arr[1]-1)
    FACE_IDS.append(Vert_Arr[2]-1)

FACE_IDS_unique = np.unique(FACE_IDS)
print('No of lines read:',count)

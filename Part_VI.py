#Write to File
f_CP=open('/content/sample_data/TVCG__OPT_fd_2.obj','w')

for data in range(0,Vert_Cords_Final.shape[0],1):
  f_CP.write('v'+' '+f'{ Vert_Cords_Final[data][0]}'+' '+f'{Vert_Cords_Final[data][1]}'+' '+f'{Vert_Cords_Final[data][2]}'+'\n')

for data in range(0,len(faces),1):
  f_CP.write('f'+' '+f'{faces[data][0]+1}'+' '+f'{faces[data][1]+1}'+' '+f'{faces[data][2]+1}'+'\n')

f_CP.close()

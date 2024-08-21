import random
import pulp
from pulp import LpMaximize, LpProblem, LpStatus, lpSum, LpVariable,LpMinimize

#@title OPTIMZED CODE NOSPEED UP
def function_OPT_NOSPEEDUP(Vi,NBList,MP):
  tmp=[]
  opt_val=0

  model = LpProblem("impl4-problem",LpMaximize)
  THIS_s=[]
  for N_val in range(len(NBList)):
    THIS_s.append(NBList[N_val])

  mi=np.min(THIS_s)
  ma=np.max(THIS_s)
  # Initialize the decision variables
  cpx=LpVariable(name="cpx", lowBound=MP-0.3*MP)
  diff=ma-mi
  model += cpx>=MP-0.3*MP
  model += cpx<=MP
  for N_val in range(len(NBList)):
    model += cpx-NBList[N_val]-0.5*(diff/2)  # Solve the problem for one face at a time

  Nf=len(NBList)
    
  status = model.solve()
  for var in model.variables():
    #print(var.value())
    tmp.append(var.value())
  model=None
  opt_val=tmp[0]
  #print('Optimium found is:',opt_val,'GT is',MP)
  return opt_val

#@title OPTIMIZER  CALLER FUNCTION
######################   Optimized center point ######################################
def optimizedCenter(Vi,ALLNeighbors,MP):
  optimized_x=0
  optimized_y=0
  optimized_z=0
  #print(Vi,ALLNeighbors)
  Vix=ALLNeighbors[0][0]
  Viy=ALLNeighbors[0][1]
  Viz=ALLNeighbors[0][2]
  P_x=[]
  P_y=[]
  P_z=[]
  for i in range(1,len(ALLNeighbors)):
    P_x.append(ALLNeighbors[i][0])
    P_y.append(ALLNeighbors[i][1])
    P_z.append(ALLNeighbors[i][2])
  optimized_x=function_OPT(Vix,P_x,MP[0])
  optimized_y=function_OPT(Viy,P_y,MP[1])
  optimized_z=function_OPT(Viz,P_z,MP[2])
  #input()
  return [optimized_x,optimized_y,optimized_z]


#@title TVC Github Upload _ ALL_NGB_using OPTIMIZATION(August2024)
########################### MAIN ALGORITHM ######################

Central_incenter=[]
Candidate_incenters=[]


import numpy as np
NEW_Verts=np.zeros((len(verts)+1,3))
print(len(NEW_Verts))
for x in range(1,len(NEW_Verts)):
  NEW_Verts[x][0]=verts[x-1][0]
  NEW_Verts[x][1]=verts[x-1][1]
  NEW_Verts[x][2]=verts[x-1][2]

# Calculate the Path Length
#for all_points in range(100000,100001):



#function
def common_member(a, b):
    a_set = set(a)
    b_set = set(b)

    # check length
    if len(a_set.intersection(b_set)) > 0:
        return(a_set.intersection(b_set))
    else:
      return []
      print('No Common')

Longest=[]
AllCurrentNeighbors=[]


for no_of_iter in range(4):
  Longest=[]
  lengthcount=0
  print('iter',no_of_iter)
  for all_points in range(1,Adjacency_List.shape[0]):

    Total_Ngb_of_current_Point=Adjacency_List[all_points][0]
    if Total_Ngb_of_current_Point==0:
      #print(all_points,Total_Ngb_of_current_Point)
      continue
    Arr_Path_length=np.zeros((Total_Ngb_of_current_Point,3)) #### Assume 100 neighbours index 0 is curr_node , colum 0,1,2 is x,y,z cords

    curr_point=all_points
    #print(no_of_iter,curr_point)

    THISPT=[NEW_Verts[curr_point][0],NEW_Verts[curr_point][1],NEW_Verts[curr_point][2]]
    AllCurrentNeighbors.append(THISPT)

    uniq_list=[]
    for _ngb in range(1,Total_Ngb_of_current_Point+1):
      uniq_list.append(Adjacency_List[all_points][_ngb])

    uniq_list=np.unique(uniq_list)

    n=len(uniq_list)

    cnt=0
    for _ngb in uniq_list:
      if _ngb !=0 :
        curr_x=NEW_Verts[curr_point][0]
        curr_y=NEW_Verts[curr_point][1]
        curr_z=NEW_Verts[curr_point][2]

        Arr_Path_length[0][0]=curr_x
        Arr_Path_length[0][1]=curr_y
        Arr_Path_length[0][2]=curr_z
        curr_ngb=_ngb

        ngb_x=NEW_Verts[_ngb][0]
        ngb_y=NEW_Verts[_ngb][1]
        ngb_z=NEW_Verts[_ngb][2]

        Arr_Path_length[cnt][0]=ngb_x
        Arr_Path_length[cnt][1]=ngb_y
        Arr_Path_length[cnt][2]=ngb_z

        cnt +=1

    #print(Arr_Path_length)

    ####################################### Formula for Smoothing The Edges (Laplacian )#######################
    if(n>2):
      edgea=edgeb=edgec=0


      sum_x=sum_y=sum_z=0
      #print('len unique list',len(uniq_list))
      for Pts in range(1,len(uniq_list)):
        edgea=Arr_Path_length[Pts][0]-curr_x
        edgeb=Arr_Path_length[Pts][1]-curr_y
        edgec=Arr_Path_length[Pts][2]-curr_z

        sum_x += edgea
        sum_y += edgeb
        sum_z += edgec




      Set_Lambda=0.00491
      New_Cords_x = curr_x + Set_Lambda * (sum_x / len(uniq_list))
      New_Cords_y = curr_y+ Set_Lambda * (sum_y / len(uniq_list))
      New_Cords_z = curr_z + Set_Lambda * (sum_z / len(uniq_list))

      ########################### Proposed IETE Model Begin ###########################################
      Total_Ngb_of_current_Point=Adjacency_List[all_points][0]
      curr_point=all_points
      #print('curr_point',curr_point)
      curr_x=NEW_Verts[curr_point][0]
      curr_y=NEW_Verts[curr_point][1]
      curr_z=NEW_Verts[curr_point][2]


      Normal_done=[]
      Incentre_of_faces_x=[]
      Incentre_of_faces_y=[]
      Incentre_of_faces_z=[]
      All_incentres=[]
      ngbcounter=-1
      num_faces=0
      for _ngb in uniq_list:                          #_ngb is unique neighbor for central vertex
        ngbcounter+=1
        Neighbour_of_ngb=Adjacency_List[_ngb][0]
        uniq_list_ngb=[]
        for cnt_ngb in range(1,Neighbour_of_ngb+1):
          uniq_list_ngb.append(Adjacency_List[_ngb][cnt_ngb])    #every neighbor _ngb has unique neighbors uniq_list_ngb
                                                                 # Edge is shared by two faces, thus same vertex sets are redundant
        uniq_list_ngb=np.unique(uniq_list_ngb)

        #find the opposite alpha,beta angle

        curr_i_x=curr_x
        curr_i_y=curr_y
        curr_i_z=curr_z

        curr_j_x=NEW_Verts[_ngb][0]
        curr_j_y=NEW_Verts[_ngb][1]
        curr_j_z=NEW_Verts[_ngb][2]

        THISPT=[NEW_Verts[_ngb][0],NEW_Verts[_ngb][1],NEW_Verts[_ngb][2]]
        AllCurrentNeighbors.append(THISPT)

        opposite=list(common_member(uniq_list,uniq_list_ngb))
        if len(opposite) > 0:
          for o in opposite:
            o_x=NEW_Verts[o][0]
            o_y=NEW_Verts[o][1]
            o_z=NEW_Verts[o][2]

            #print('curr_y,curr_z,curr_j_y,curr_j_z',curr_y,curr_z,curr_j_y,curr_j_z)
            vector_oi=[curr_i_x-o_x,curr_i_y-o_y,curr_i_z-o_z]
            vector_oj=[-curr_j_x+o_x,-curr_j_y+o_y,-curr_j_z+o_z]
            vector_ij=[curr_j_x-curr_i_x,curr_j_y-curr_i_y,curr_j_z-curr_i_z]


            curr_face_triangle=[all_points,_ngb,o]

            if curr_face_triangle in Normal_done:
              pass
            else:
              num_faces +=1
              Area=0
              s=0
              a =  pow( pow(vector_oi[0],2) + pow(vector_oi[1],2) + pow(vector_oi[2],2) , 0.5)
              b =  pow( pow(vector_oj[0],2) + pow(vector_oj[1],2) + pow(vector_oj[2],2) , 0.5)
              c =  pow( pow(vector_ij[0],2) + pow(vector_ij[1],2) + pow(vector_ij[2],2) , 0.5)

              sumabc=a+b+c
              if (a+b+c)==0.0 or (a+b+c)==-0.0:
                print('yes')
                sumabc=0.0000001

              inc_x=(a*curr_i_x + b*curr_j_x+ c*o_x)/sumabc
              inc_y=(a*curr_i_y + b*curr_j_y+ c*o_y)/sumabc
              inc_z=(a*curr_i_z + b*curr_j_z+ c*o_z)/sumabc

              Incentre_of_faces_x.append(inc_x)
              Incentre_of_faces_y.append(inc_y)
              Incentre_of_faces_z.append(inc_z)
              All_incentres.append([inc_x,inc_y,inc_z])
              # incentre Ends


              Normal_done.append([all_points,_ngb,o])
              Normal_done.append([all_points,o,_ngb])
      #all_incentres calculated for current central vertex i

      avg_of_all_incentre_x= np.sum(Incentre_of_faces_x) / num_faces
      avg_of_all_incentre_y= np.sum(Incentre_of_faces_y) / num_faces
      avg_of_all_incentre_z= np.sum(Incentre_of_faces_z) / num_faces

      longest_pt_1=None
      longest_pt_2=None

      for id1 in range(len(All_incentres)):
        first_pt=All_incentres[id1]
        longest=0
        for id2 in range(len(All_incentres)):
          second_pt=All_incentres[id2]
          dis= pow( pow(first_pt[0]-second_pt[0],2)+pow(first_pt[1]-second_pt[1],2)+pow(first_pt[2]-second_pt[2],2),0.5)

          if dis > longest:
            longest=dis
            longest_pt_1=All_incentres[id1]
            longest_pt_2=All_incentres[id2]
      if longest_pt_1==None or longest_pt_2==None:
        print(dis,longest_pt_1,longest_pt_2,All_incentres)
      #longest edge
      longest_mid_point_x=avg_of_all_incentre_x
      longest_mid_point_y=avg_of_all_incentre_y
      longest_mid_point_z=avg_of_all_incentre_z
      # midpoint of longest edge
      longest_mid_point_x=(longest_pt_1[0]+longest_pt_2[0])/2
      longest_mid_point_y=(longest_pt_1[1]+longest_pt_2[1])/2
      longest_mid_point_z=(longest_pt_1[2]+longest_pt_2[2])/2
      Longest.append([longest,longest_mid_point_x,longest_mid_point_y,longest_mid_point_z])
      ########################### Bounds Selection Ends ###########################################


      optimized_val=optimizedCenter(curr_point,AllCurrentNeighbors,[longest_mid_point_x,longest_mid_point_y,longest_mid_point_z])



      ###################### UPDATE NEIGHBORS #######################
      uniq_list_ngb_2=[]
      for _ngb in uniq_list:
        Neighbour_of_ngb=Adjacency_List[_ngb][0]
        for cnt_ngb in range(1,Neighbour_of_ngb+1):
          uniq_list_ngb_2.append(Adjacency_List[_ngb][cnt_ngb])

      uniq_list_ngb_2=np.unique(uniq_list_ngb_2)
      for _ngb in uniq_list_ngb_2:
        curr_i_x=curr_x
        curr_i_y=curr_y
        curr_i_z=curr_z

        curr_j_x=NEW_Verts[_ngb][0]
        curr_j_y=NEW_Verts[_ngb][1]
        curr_j_z=NEW_Verts[_ngb][2]

        

        optimized_x=optimized_val[0]
        optimized_y=optimized_val[1]
        optimized_z=optimized_val[2]

        DIRECTION= [optimized_x-curr_j_x,optimized_y-curr_j_y,optimized_z-curr_j_z]
        MAG=pow(pow(DIRECTION[0],2)+pow(DIRECTION[1],2)+pow(DIRECTION[2],2),0.5)

        New_x= curr_j_x+Set_Lambda * DIRECTION[0]/MAG
        New_y= curr_j_y+Set_Lambda * DIRECTION[1]/MAG
        New_z= curr_j_z+Set_Lambda * DIRECTION[2]/MAG


        Vert_Cords_Final[_ngb-1][0]=New_x
        Vert_Cords_Final[_ngb-1][1]=New_y
        Vert_Cords_Final[_ngb-1][2]=New_z

        NEW_Verts[_ngb][0]=New_x
        NEW_Verts[_ngb][1]=New_y
        NEW_Verts[_ngb][2]=New_z

        UpdateCount[_ngb]+=1

      #updating central vertex at the end
      DIRECTION= [optimized_x-curr_i_x,optimized_y-curr_i_y,optimized_z-curr_i_z]
      MAG=pow(pow(DIRECTION[0],2)+pow(DIRECTION[1],2)+pow(DIRECTION[2],2),0.5)
      IC_x =  curr_i_x+Set_Lambda * DIRECTION[0]/MAG
      IC_y =  curr_i_y+Set_Lambda * DIRECTION[1]/MAG
      IC_z =  curr_i_z+Set_Lambda * DIRECTION[2]/MAG


      Vert_Cords_Final[curr_point-1][0]=IC_x
      Vert_Cords_Final[curr_point-1][1]=IC_y
      Vert_Cords_Final[curr_point-1][2]=IC_z

      NEW_Verts[curr_point][0]=IC_x
      NEW_Verts[curr_point][1]=IC_y
      NEW_Verts[curr_point][2]=IC_z

      UpdateCount[curr_point]+=1
    else:
      pass




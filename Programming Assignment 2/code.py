import pandas as pd
import math
df_places=pd.read_csv('Data/places.csv', names =['lon','lat'])
#intialize k means param
k=3 #Number of clusters
max_iter=5 #Number of maximum iterations
min_var_change=0.01 #threshold of change of within cluster variance


def update_center(x, y,center):
    center_distance = [ (x-i[0])*(x-i[0]) +(y-i[1])*(y-i[1]) for i in center]
    a=int(center_distance.index(min(center_distance)))
    b = min(center_distance)
    return pd.Series([a,b])

#initialize with kmeans++  efficiency: O(n*k)
center=[]
for j in range(k):
    #randomly choose the first initial center point
    if j==0:
        center.append(df_places.iloc[0])
    else:        
        for i in range(df_places.shape[0]):
            dist =0
            for m in range(len(center)):
                #choose the other intial center point, which has the biggest sum of distance from all existing center points
                dist = dist + math.sqrt((df_places.iloc[i]['lon']-center[m][0])*(df_places.iloc[i]['lon']-center[m][0])+ (df_places.iloc[i]['lat']-center[m][1])*(df_places.iloc[i]['lat']-center[m][1]))                               
            if i==0:
                center.append(df_places.iloc[i])
                temp_dist=dist
            elif dist >= temp_dist:
                temp_dist=dist
                center[m]=df_places.iloc[i]

#clustering with Kmeans  efficiency: O(n*k*m)
for m in range(max_iter):
    #Assign each point to a center & calculate center distance
    df_places[['center_id','center_distance']]=df_places.apply(lambda row: update_center(row['lon'], row['lat'],center), axis=1)
 
    #calculate within cluster variance change
    if m ==0 :
        #for first round of updation of new centers, default change of within cluster variance to 1
        var_change = 1
    else:
        #for subsequent round of updation of new centers, calculate change of within cluster variance
        var_change = abs(df_places['center_distance'].sum() - var)/var
    
    #update within cluster variance benchmark value
    var = df_places['center_distance'].sum()    
    
    #Calculate the new center
    for i in range(k):
        center[i]=(df_places[df_places.center_id==i]['lon'].mean(),df_places[df_places.center_id==i]['lat'].mean())
    
    #if the change of within cluster variance is less than threshold, then break
    if var_change <= min_var_change:
        break

df_places.to_csv('Output/ClusterAnalysis_Assignment1_clusteredPlaces.txt', sep=' ', columns=['center'], header=None)
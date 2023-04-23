import datetime as dt
import pandas as pd
import numpy as np

###########################

time_windows = [['T001','sat1','obs1', dt.time(00, 10, 00, 00000),
                 dt.time(00, 15, 00, 00000), 10, 100],
                 ['T002','sat2','obs2', dt.time(00, 25, 00, 00000),
                  dt.time(00, 00, 35, 00000),10, 100]]
#Dataframe with columns as task id (primary key), satellite id, observation spot id, time window start, time window end, data capacity required and energy required
TWindows = pd.DataFrame(time_windows, columns = ['TaskID','Satellite','Observation','Start_time','end_time',
                                                 'data','energy'])

downloads = [['D001','sat1','stn1', dt.time(00, 5, 00, 00000),
              dt.time(00, 9, 00, 00000), 10, 100],
              ['D002','sat2','stn1', dt.time(00, 15, 00, 00000),
               dt.time(00, 30, 00, 00000), 10, 100] ]
#Dataframe with columns as task id (primary key), satellite id, ground station id, time window start, time window end, data downloadable and energy required
DWindows = pd.DataFrame(downloads, columns = ['TaskID','Satellite','Ground station','Start_time','end_time',
                                                 'data','energy'])

sat_info = [['sat1','100','1000'],['sat2','100','1000']]

#Dataframe with satellite id (primary key), data capacity and energy level
SatInfo = pd.DataFrame(sat_info, columns = ['Satellite','Data_capacity','Energy_level'])

###############################

# Input : TWindows - every possible observation (combination of satellite and observation spot) task id, time window, data and energy consumed
#         DWindows - every possible download (combination of satellite and groundstation) task id, time window, data downloadable, energy consumed
#         SatInfo - Data and Energy levels of every satellite
#(Note: Task ids are unique to every observation and download task, for Observation it is T00x and for download it is D00x)
# Output : Plan of schedule with task ids and satellite which will perform the task

def Schedule_task(TWindows,DWindows,SatInfo):
    plan = []
    t = dt.time(00, 00, 00, 00000)
    #initiallizing time with zero (using local time frame of reference)
    while len(TWindows)>0:
        #taking the satellite, observation spot and time window start of the very first occuring task from the current list of tasks
        sat = TWindows['Satellite'][0]
        obs = TWindows['Observation'][0]
        t_prev = t
        t = TWindows['Start_time'][0]
        for i in range(len(DWindows)):
            #checking if there is any download task for that satellite in between start of next observation task and end of previous observation task
            if (DWindows['Start_time'][i]>= t_prev and DWindows['end_time'][i]<= t and DWindows['Satellite'][i]==sat):
                #if found a download task, add to the plan for that particular satellite
                plan.append([sat,DWindows['TaskID'][i]])
                d = int(SatInfo[SatInfo['Satellite']=='sat1']['Data_capacity'])
                e =  int(SatInfo[SatInfo['Satellite']=='sat1']['Energy_level'])
                #Update the data and energy level of that satellite assuming the entire task was finished
                SatInfo.at[SatInfo[SatInfo['Satellite']==sat].index.values,'Data_capacity']= (d + DWindows['data'][i])
                SatInfo.at[SatInfo[SatInfo['Satellite']==sat].index.values,'Energy_level']= (e - DWindows['energy'][i])
                break;
             #if the satellite data and energy levels allow the observation task (chosen at the begining of iteration),
             #add that to the plan for that satellite  
        if((int(SatInfo[SatInfo['Satellite']=='sat1']['Data_capacity'])>=int(TWindows['data'][0])) and (int(SatInfo[SatInfo['Satellite']=='sat1']['Energy_level'])>=int(TWindows['energy'][0]))):
            plan.append([sat,TWindows['TaskID'][0]])
            o_d = int(SatInfo[SatInfo['Satellite']=='sat1']['Data_capacity'])
            o_e =  int(SatInfo[SatInfo['Satellite']=='sat1']['Energy_level'])
            SatInfo.at[SatInfo[SatInfo['Satellite']==sat].index.values,'Data_capacity']= (o_d + TWindows['data'][0])
            SatInfo.at[SatInfo[SatInfo['Satellite']==sat].index.values,'Energy_level']= (o_e - TWindows['energy'][0])
            t = TWindows['end_time'][0]
            #remove all the observation task for that observation spot from the list and reindex
            TWindows.drop(TWindows[TWindows['Observation']==obs].index.values,axis=0, inplace=True)
            TWindows.reset_index(drop=True, inplace = True)
        else:
            #if task not done, remove that specific observation task for that observation spot from the list and reindex
            TWindows.drop(0,axis=0, inplace=True)
            TWindows.reset_index(drop=True, inplace = True)
            #Next task now comes as the first row of the data frame
    return(plan)
   
#print(Schedule_task(TWindows,DWindows,SatInfo))    
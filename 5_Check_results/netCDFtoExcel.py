# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 15:05:03 2024

@author: Ana
"""

import os
import netCDF4 as nc
import numpy as np
import pandas as pd
from datetime import timedelta


def netCDFtoArray(ncfile, var):
    ncdf = nc.Dataset(ncfile)
    # for output timesteps in days:
    tsteps = np.ma.getdata(ncdf.variables['time'][:,])+1
    data = np.zeros((len(ncdf.variables['time']),len(var)))
    all_units= []
    for v in range(len(var)):
        ## for 2D variables
        if ncdf.variables[var[v]].shape[1] == 1:
            data[:,v] = np.ma.getdata(ncdf.variables[var[v]][:,0]) 
        ## for 3D variables
        else:       
            data[:,v] = np.ma.getdata(ncdf.variables[var[v]][:,d,0])
        all_units.append(ncdf.variables[var[v]].units)
    return(data,tsteps,all_units)



def Out_to_Excel(case_dir, case_name, params, start_date,path_save,excel_name): 
    print("Soil layer= ", d)
    
    ## case directory
    os.chdir(case_dir)
    
    ##listing all files in the directory
    files = [filename for filename in os.listdir('.') if filename.startswith(case_name)]
    files =sorted(files)
    print(case_name,'\n',files,'\n')
    
    # writing data to array
    full_array = np.zeros((0,len(params)))
    full_days = np.zeros((0,))
    for f in files:
        array,days,full_units = netCDFtoArray(f, params)
        full_array = np.concatenate([full_array,array])
        full_days = np.concatenate([full_days,days])
    
    ## path to save the excel file
    os.chdir(path_save)

    ## creating correct date range
    frequency='D'
    timestamps = pd.date_range(start_date,periods=full_array.shape[0], freq=frequency)
    ## this timedelta is needed because CLM calculates daily means at the end of the day and writes them to the next day only!
    if frequency == 'D':
        timestamps_d = timestamps-timedelta(days=1)

    ## writing parameters to excel file
    df_excel = pd.DataFrame(full_array[:,:], timestamps_d,params)
    path = os.getcwd()
    #excel_name = path.split('\\')[-1]      
    with pd.ExcelWriter(excel_name+'.xlsx') as writer:
        df_excel.to_excel(writer)

#%%     
# writing all outputs in one array
d=2 # soil layer
param_list = ['GPP','NEE','ER', 'QFLX_EVAP_VEG', 'QFLX_EVAP_TOT', 'Qh', 'Qle', 'EFLX_LH_TOT', 'FSH', 'Rnet', 'NPP','HR', 'AR',
         'TLAI', 'LEAFC', 'GRAINC', 'FROOTC', 'LIVESTEMC', 'GRAINC_TO_FOOD', 'GDDPLANT', 'TSA', 'QIRRIG', 'QIRRIG_DEMAND',
         'QINTR', 'QDRIP', 'QSOIL', 'QVEGE', 'QVEGT','QINFL','QOVER','TG','H2OSOI','SMP', 'TV', 'GDDPLANT', 'DEADSTEMC', 'TSOI']

# Sim 1 to compare
path = r'/p/scratch/cslts/gonzalez5/10_clm5_0/CLM5_DATA/Archive/lnd/hist'
casename= 'Test_WC_01_soil_var.clm2.h0'
excelname= 'Test_WC_01_soil_var_soilLay=2_5cm'
Out_to_Excel(path,casename,param_list,'2010-01-01',path,excelname)

# Sim 2 to compare
path = r'/p/scratch/cslts/gonzalez5/10_clm5_0/CLM5_DATA/Archive/lnd/hist'
casename= 'Test_FTWC_wc_peren_0_soil_var.clm2.h0'
excelname= 'Test_FTWC_wc_peren_0_soil_var_soilLay=2_5cm'
Out_to_Excel(path,casename,param_list,'2010-01-01',path,excelname)

### SOIL LAYER d=3 100 cm
# writing all outputs in one array
d=9 # soil layer

# Sim 1 to compare
casename= 'Test_WC_01_soil_var.clm2.h0'
excelname_d9= 'Test_WC_01_soil_var_soilLay=9_100cm'
Out_to_Excel(path,casename,param_list,'2010-01-01',path,excelname_d9)

# Sim 2 to compare
casename= 'Test_FTWC_wc_peren_0_soil_var.clm2.h0'
excelname_d9= 'Test_FTWC_wc_peren_0_soil_var_soilLay=9_100cm'
Out_to_Excel(path,casename,param_list,'2010-01-01',path,excelname_d9)
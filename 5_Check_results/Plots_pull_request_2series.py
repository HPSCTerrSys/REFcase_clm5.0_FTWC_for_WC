# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 16:16:08 2024

@author: Ana
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter
import matplotlib.gridspec as gridspec
import seaborn as sns
sns.set_theme()

#BDT Series 1 = TEST series to check --> new clm5.0_FTWC
#os.chdir(r'C:\0_Ana_Julich\2_PROJECTS\6_clm5_to_eclm_git\Olga_scripts_to_plot_ncresults\01_Check_WC_Peren=0')
os.chdir(r'/p/scratch/cslts/gonzalez5/10_clm5_0/CLM5_DATA/Archive/lnd/hist/')
#files = [filename for filename in os.listdir('.')]
#files =sorted(files)
#print(files,'\n')
bdt_full = pd.read_excel('Test_FTWC_wc_peren_0_soil_var_soilLay=2_5cm.xlsx', index_col=0, header = [0])
bdt_full_sLay9 = pd.read_excel('Test_FTWC_wc_peren_0_soil_var_soilLay=9_100cm.xlsx', index_col=0, header = [0])

#SW
#os.chdir(r'C:\0_Ana_Julich\2_PROJECTS\6_clm5_to_eclm_git\0_Reference_cases\CLM5_FruitTree_TESTING\CASE_OUTPUTS\CLM_def_SW')
#adige_def = pd.read_excel('CLM_def_SW.xlsx', index_col=0, header = [0])
#os.chdir(r'C:\0_Ana_Julich\2_PROJECTS\6_clm5_to_eclm_git\0_Reference_cases\CLM5_FruitTree_TESTING\CASE_OUTPUTS\CLM_fruittree_SW')
#adige_fruittree = pd.read_excel('CLM_fruittree_SW.xlsx', index_col=0, header = [0])
#sw_full = pd.read_excel('CLM_fruittree_SW.xlsx', index_col=0, header = [0])

#apple Series 2 REFERENCE clm5.0_WinterCrops
os.chdir(r'/p/scratch/cslts/gonzalez5/10_clm5_0/CLM5_DATA/Archive/lnd/hist/')
#os.chdir(r'C:\0_Ana_Julich\2_PROJECTS\6_clm5_to_eclm_git\Olga_scripts_to_plot_ncresults\01_Check_WC_Peren=0')
apple_full = pd.read_excel('Test_WC_01_soil_var_soilLay=2_5cm.xlsx', index_col=0, header = [0])
apple_full_sLay9 = pd.read_excel('Test_WC_01_soil_var_soilLay=9_100cm.xlsx', index_col=0, header = [0])

#Path to save plots
os.chdir(r'/p/scratch/cslts/gonzalez5/10_clm5_0/Reference_data/00_Check_FTWC_wc_peren=0_soil_var')
#os.chdir(r'C:\0_Ana_Julich\2_PROJECTS\6_clm5_to_eclm_git\Olga_scripts_to_plot_ncresults\01_Check_WC_Peren=0')

# myFmt = DateFormatter("%Y")
def PlotDefvsFruitTree(df_def,df_fruittree, var,fac,ylbl,ylbl2,ttl):
    fig, axes = plt.subplots(2, 1,figsize=(10, 5), sharex=True, gridspec_kw={'height_ratios': [2, 1]})    
    sns.lineplot(data=df_def*fac, x=df_def.index, y=var,label='CLM_def',ax=axes[0])
    sns.lineplot(data=df_fruittree*fac, x=df_fruittree.index, y=var,label='CLM_fruittree',ax=axes[0])
    axes[0].set_ylabel(ylbl)
    axes[0].set_title(ttl)
    axes[0].legend(loc='upper right')
    sns.lineplot(data=df_def*fac-df_fruittree*fac, x=df_def.index,label='def - fruittree', y=var,ax=axes[1],color='black')
    axes[1].set_ylabel(ylbl2)
    axes[1].legend(loc='upper right')
    fig.tight_layout()
    plt.savefig(var,dpi=400)
    plt.show()

def Scatter(df_def,df_fruittree,var,fac,ylbl,xlbl,ttl):
    fig,ax = plt.subplots(figsize=(4,4))
    sns.scatterplot(data=None,x=df_def[var]*fac, y=df_fruittree[var]*fac,color='#DAA520',linewidth=0)
    ax.set_ylabel(ylbl)
    ax.set_xlabel(xlbl)
    ax.set_title(ttl)
    fig.tight_layout()
    plt.savefig('Scatter_'+var,dpi=400)
    plt.show()

#### unit conversions
# sec to day
f_h=60*60*24

### plant functional type
#pft='Broadleaf deciduous tree'
# pft='Spring wheat'

# =============================================================================
# PlotDefvsFruitTree(adige_def['2010':'2015'],adige_fruittree['2010':'2015'],'GPP',f_h,'GPP [gC m-2]','Difference [gC m-2]',pft)
# PlotDefvsFruitTree(adige_def['2010':'2015'],adige_fruittree['2010':'2015'],'LEAFC',1,'LEAFC [gC m-2]','Difference [gC m-2]',pft)
# PlotDefvsFruitTree(adige_def['2010':'2015'],adige_fruittree['2010':'2015'],'QFLX_EVAP_TOT',f_h,'ET [mm d-1]','Difference [mm d-1]',pft)
# PlotDefvsFruitTree(adige_def['2010':'2015'],adige_fruittree['2010':'2015'],'TV',1,'T veg [K]','Difference [K]',pft)
# PlotDefvsFruitTree(adige_def['2010':'2015'],adige_fruittree['2010':'2015'],'TOTECOSYSC',1,'TOTECOSYSC [gC m-2]','Difference [gC m-2]',pft)
# PlotDefvsFruitTree(adige_def['2010':'2015'],adige_fruittree['2010':'2015'],'TOTECOSYSN',1,'TOTECOSYSN [gC m-2]','Difference [gC m-2]',pft)
# PlotDefvsFruitTree(adige_def['2010':'2015'],adige_fruittree['2010':'2015'],'TOTSOMC',1,'TOTSOMC [gC m-2]','Difference [gC m-2]',pft)
# 
# Scatter(adige_def['2010':'2015'],adige_fruittree['2010':'2015'],'TOTSOMC',1,'CLM5','CLM5-FruitTree','TOTSOMC [gC m-2]')
# Scatter(adige_def['2010':'2015'],adige_fruittree['2010':'2015'],'TOTECOSYSC',1,'CLM5','CLM5-FruitTree','TOTECOSYSC [gC m-2]')
# Scatter(adige_def['2010':'2015'],adige_fruittree['2010':'2015'],'TOTECOSYSN',1,'CLM5','CLM5-FruitTree','TOTECOSYSN [gN m-2]')
# Scatter(adige_def['2010':'2015'],adige_fruittree['2010':'2015'],'GPP',f_h,'CLM5','CLM5-FruitTree','GPP [gC m-2]')
# Scatter(adige_def['2010':'2015'],adige_fruittree['2010':'2015'],'TLAI',1,'CLM5','CLM5-FruitTree','TLAI [m2 m-2]')
# Scatter(adige_def['2010':'2015'],adige_fruittree['2010':'2015'],'TOTSOMC',1,'CLM5','CLM5-FruitTree','TOTSOMC [gC m-2]')
# Scatter(adige_def['2010':'2015'],adige_fruittree['2010':'2015'],'TWS',1,'CLM5','CLM5-FruitTree','TWS [mm]')
# =============================================================================


#%% PLOT MULTIPLOTS 5-VARIABLES plots
# For this case soil layer =2 

bdt = bdt_full.loc['2010':'2021']              # to test in seconds
bdt_day = bdt_full.loc['2010':'2021']*f_h      # to test in days

apple = apple_full.loc['2010':'2021']          # reference in seconds
apple_day = apple_full.loc['2010':'2021']*f_h  # reference in days

delta = apple-bdt                              # error

def MultiPlot3PFTs(vars_out,vars_out_u,lbl,plotname,test,ref):
    # plotting sensitive parameter against output variable
    fig = plt.figure(constrained_layout=True, figsize=(18, 3))
    # creating subplots and specifying their position
    spec = gridspec.GridSpec(ncols=6, nrows=1, figure=fig)
    ax1 = fig.add_subplot(spec[:, 0])
    ax2 = fig.add_subplot(spec[:, 1])
    ax3 = fig.add_subplot(spec[:, 2])
    ax4 = fig.add_subplot(spec[:, 3])
    ax5 = fig.add_subplot(spec[:, 4])
    
    label_ax =['2008','2010','2012','2014','2016','2018','2020','2022']      # 12 years plot: 2010-2021
    # 
    sns.lineplot(data=test, x=test.index, y=vars_out[0],label='test',ax=ax1,alpha=.7)
    sns.lineplot(data=ref, x=test.index, y=vars_out[0],label='ref',ax=ax1,alpha=.7)
    ax1.set_ylabel(lbl[0]+'   '+'['+vars_out_u[0]+']')
    ax1.set_xticklabels(label_ax,rotation=90, ha='right')    
    # 
    sns.lineplot(data=test, x=test.index, y=vars_out[1],ax=ax2,alpha=.7)
    sns.lineplot(data=ref, x=test.index, y=vars_out[1],ax=ax2,alpha=.7)
    ax2.set_ylabel(lbl[1]+'   '+'['+vars_out_u[1]+']')
    # ax2.set_ylim(-10,3)
    ax2.set_xticklabels(label_ax,rotation=90, ha='right')   
    #ax2.set_xticklabels(['1\n2015','3','5','7','9','11','1\n2016'])    # 1 year plot: 2015
    # 
    sns.lineplot(data=test, x=test.index, y=vars_out[2],ax=ax3,alpha=.7)
    sns.lineplot(data=ref, x=test.index, y=vars_out[2],ax=ax3,alpha=.7)
    ax3.set_ylabel(lbl[2]+'   '+'['+vars_out_u[2]+']')
    # ax3.set_ylim(-1,13)
    ax3.set_xticklabels(label_ax,rotation=90, ha='right')      
    #ax3.set_xticklabels(['1\n2015','3','5','7','9','11','1\n2016'])    # 1 year plot: 2015
    # 
    sns.lineplot(data=test, x=test.index, y=vars_out[3],ax=ax4,alpha=.7)
    sns.lineplot(data=ref, x=test.index, y=vars_out[3],ax=ax4,alpha=.7)
    ax4.set_ylabel(lbl[3]+'   '+'['+vars_out_u[3]+']')
    # ax4.set_ylim(-1,13)
    ax4.set_xticklabels(label_ax,rotation=90, ha='right')      
    #ax4.set_xticklabels(['1\n2015','3','5','7','9','11','1\n2016'])    # 1 year plot: 2015
    # 
    sns.lineplot(data=test, x=test.index, y=vars_out[4],ax=ax5,alpha=.7)
    sns.lineplot(data=ref, x=test.index, y=vars_out[4],ax=ax5,alpha=.7)
    ax5.set_ylabel(lbl[4]+'   '+'['+vars_out_u[4]+']')
    ax5.set_xticklabels(label_ax,rotation=90, ha='right')      
    #ax5.set_xticklabels(['1\n2015','3','5','7','9','11','1\n2016'])     # 1 year plot: 2015
    # 
    #
    fig.tight_layout()
    plt.savefig(plotname,dpi=400)
    fig.show()

## output variables
v1_out = ['GPP','NEE','ER','AR','HR'] # *f_h in days
v2_out = ['QSOIL','QVEGE','QVEGT','QOVER','QIRRIG'] # *f_h in days
v3_out = ['EFLX_LH_TOT','FSH','Rnet','Rnet','QFLX_EVAP_TOT']
v4_out = ['GRAINC','LEAFC','DEADSTEMC','FROOTC','GRAINC_TO_FOOD']

## units for output variables
v1_out_u = ['gC m-2 d-1','gC m-2 d-1','gC m-2 d-1','gC m-2 d-1','gC m-2 d-1'] # *f_h in days
v2_out_u = ['mm d-1','mm d-1','mm d-1','mm d-1','mm d-1']  # *f_h in days
v3_out_u = ['W m-2','W m-2','W m-2','W m-2','kg m-2 s-1']
v4_out_u = ['gC m-2','gC m-2','gC m-2','gC m-2','gC m-2 s-1']

## labels for plots
labels1=['GPP','NEE','ER','AR','HR']
labels2=['QSOIL','QVEGE','QVEGT','QOVER','QIRRIG']
labels3=['LH','FSH','Rnet','Rnet','ET']
labels4=['GRAINC','LEAFC','DEADSTEMC','FROOTC','Harvest']

MultiPlot3PFTs(v1_out,v1_out_u,labels1,'C_fluxes', bdt_day, apple_day)
MultiPlot3PFTs(v2_out,v2_out_u,labels2,'H2O_fluxes', bdt_day, apple_day)
MultiPlot3PFTs(v3_out,v3_out_u,labels3,'Energy_fluxes', bdt, apple)
MultiPlot3PFTs(v4_out,v4_out_u,labels4,'Biomass', bdt, apple)

#%% PLOT MULTIPLOTS DELTA-ERRORS 5-VARIABLES plots
# Soil Layer= 2

def MultiPlot3PFTs_delta(vars_out,vars_out_u,lbl,plotname):
    # plotting sensitive parameter against output variable
    fig = plt.figure(constrained_layout=True, figsize=(18, 3))
    # creating subplots and specifying their position
    spec = gridspec.GridSpec(ncols=6, nrows=1, figure=fig)
    ax1 = fig.add_subplot(spec[:, 0])
    ax2 = fig.add_subplot(spec[:, 1])
    ax3 = fig.add_subplot(spec[:, 2])
    ax4 = fig.add_subplot(spec[:, 3])
    ax5 = fig.add_subplot(spec[:, 4])
    
    label_ax =['2008','2010','2012','2014','2016','2018','2020','2022']      # 12 years plot: 2010-2021
    # 
    sns.lineplot(data=delta, x=delta.index, y=vars_out[0],label='Delta = Ref-Test',ax=ax1,alpha=.7)
    ax1.set_ylabel(lbl[0]+'   '+'['+vars_out_u[0]+']')
    ax1.set_xticklabels(label_ax,rotation=90, ha='right')    
    # 
    sns.lineplot(data=delta, x=delta.index, y=vars_out[1],ax=ax2,alpha=.7)
    ax2.set_ylabel(lbl[1]+'   '+'['+vars_out_u[1]+']')
    # ax2.set_ylim(-10,3)
    ax2.set_xticklabels(label_ax,rotation=90, ha='right')   
    #ax2.set_xticklabels(['1\n2015','3','5','7','9','11','1\n2016'])    # 1 year plot: 2015
    # 
    sns.lineplot(data=delta, x=delta.index, y=vars_out[2],ax=ax3,alpha=.7)
    ax3.set_ylabel(lbl[2]+'   '+'['+vars_out_u[2]+']')
    # ax3.set_ylim(-1,13)
    ax3.set_xticklabels(label_ax,rotation=90, ha='right')      
    #ax3.set_xticklabels(['1\n2015','3','5','7','9','11','1\n2016'])    # 1 year plot: 2015
    # 
    sns.lineplot(data=delta, x=delta.index, y=vars_out[3],ax=ax4,alpha=.7)
    ax4.set_ylabel(lbl[3]+'   '+'['+vars_out_u[3]+']')
    # ax4.set_ylim(-1,13)
    ax4.set_xticklabels(label_ax,rotation=90, ha='right')      
    #ax4.set_xticklabels(['1\n2015','3','5','7','9','11','1\n2016'])    # 1 year plot: 2015
    # 
    sns.lineplot(data=delta, x=delta.index, y=vars_out[4],ax=ax5,alpha=.7)
    ax5.set_ylabel(lbl[4]+'   '+'['+vars_out_u[4]+']')
    ax5.set_xticklabels(label_ax,rotation=90, ha='right')      
    #ax5.set_xticklabels(['1\n2015','3','5','7','9','11','1\n2016'])     # 1 year plot: 2015
    # 
    #
    fig.tight_layout()
    plt.savefig(plotname,dpi=400)
    fig.show()
    
MultiPlot3PFTs_delta(v1_out,v1_out_u,labels1,'Delta_C_fluxes')
MultiPlot3PFTs_delta(v2_out,v2_out_u,labels2,'Delta_H2O_fluxes')
MultiPlot3PFTs_delta(v3_out,v3_out_u,labels3,'Delta_Energy_fluxes')
MultiPlot3PFTs_delta(v4_out,v4_out_u,labels4,'Delta_Biomass')





### PLOT LAYERS 2 & 9 for soil moisture, soil temperature

#%% PLOT MULTIPLOTS 2-VARIABLES plots

def MultiPlot3PFTs_2plots(vars_out,vars_out_u,lbl,plotname,title_layer):
    # plotting sensitive parameter against output variable
    fig = plt.figure(constrained_layout=True, figsize=(18, 3))
    # creating subplots and specifying their position
    spec = gridspec.GridSpec(ncols=2, nrows=1, figure=fig)
    ax1 = fig.add_subplot(spec[:, 0])
    ax2 = fig.add_subplot(spec[:, 1])

    
    label_ax =['2008','2010','2012','2014','2016','2018','2020','2022']      # 12 years plot: 2010-2021
    # 
    sns.lineplot(data=bdt, x=bdt.index, y=vars_out[0],label='test',ax=ax1,alpha=.7)
    #sns.lineplot(data=sw, x=bdt.index, y=vars_out[0],ax=ax1,alpha=.7)
    sns.lineplot(data=apple, x=bdt.index, y=vars_out[0],label='ref',ax=ax1,alpha=.7)
    ax1.set_ylabel(lbl[0]+'   '+'['+vars_out_u[0]+']')
    ax1.set_xticklabels(label_ax,rotation=90, ha='right')    
    # 
    sns.lineplot(data=bdt, x=bdt.index, y=vars_out[1],ax=ax2,alpha=.7)
    #sns.lineplot(data=sw, x=bdt.index, y=vars_out[1],ax=ax2,alpha=.7)
    sns.lineplot(data=apple, x=bdt.index, y=vars_out[1],ax=ax2,alpha=.7)
    ax2.set_ylabel(lbl[1]+'   '+'['+vars_out_u[1]+']')
    # ax2.set_ylim(-10,3)
    ax2.set_xticklabels(label_ax,rotation=90, ha='right')   
    #ax2.set_xticklabels(['1\n2015','3','5','7','9','11','1\n2016'])    # 1 year plot: 2015
    # 
    fig.suptitle(title_layer)
    #
    fig.tight_layout()
    plt.savefig(plotname,dpi=400)
    fig.show()
 
 
# SOIL LAYER = 2, @ 5 cm 
## output variables
v1_out = ['H2OSOI','TSOI']       
## units for output variables  # TSOI in K
v1_out_u = ['mm3/mm3','K']
## labels for plots
labels1=['H2OSOI','TSOI']

MultiPlot3PFTs_2plots(v1_out,v1_out_u,labels1,'soiLay=5cm','SOIL LAYER at 5 cm (d=2)')

# SOIL LAYER = 9, @ 100 cm 
bdt = bdt_full_sLay9.loc['2010':'2021']      # to test
apple = apple_full_sLay9.loc['2010':'2021']  # reference
## output variables
v1_out = ['H2OSOI','TSOI']
## units for output variables  # TSOI in K
v1_out_u = ['mm3/mm3','K']
## labels for plots
labels1=['H2OSOI','TSOI']

MultiPlot3PFTs_2plots(v1_out,v1_out_u,labels1,'soiLay=100cm','SOIL LAYER at 100 cm (d=9)')
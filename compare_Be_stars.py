# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 22:14:52 2017

@author: Oxin
"""
#FYP

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy as sp

data_file = pd.read_excel('C:/Users/Currys/Pictures/College/4TH YEAR/College Backup/FYP/PythonFYPData.xlsx')
#print(data_file[0:3])

#X-Ray Binary Data
vsinXray = data_file.ix[0:268,'v.sin(i)']
EWXray = data_file.ix[0:268,'(-EW)']
DeltaVXray = data_file.ix[0:268,'DeltaV']
FWHMXray = data_file.ix[0:268,'FWHM']

#Be Star Data
vsinBe = data_file.ix[269:438,'v.sin(i)']
EWBe = data_file.ix[269:438,'(-EW)']
DeltaVBe = data_file.ix[269:438,'DeltaV']
FWHMBe = data_file.ix[269:438,'FWHM']

#Gamma-Ray Binary
vsinGamma = data_file.ix[439:629,'v.sin(i)']
EWGamma = data_file.ix[439:629,'(-EW)']
DeltaVGamma = data_file.ix[439:629,'DeltaV']
FWHMGamma = data_file.ix[439:629,'FWHM']

#Seperate Gamma-Ray Binaries
##LSI+61'303/V615 Cas e=0.54
LSIvsinGamma = data_file.ix[439:615,'v.sin(i)']
LSIEWGamma = data_file.ix[439:615,'(-EW)']
LSIDeltaVGamma = data_file.ix[439:615,'DeltaV']
LSIFWHMGamma = data_file.ix[439:615,'FWHM']
##HESS J0632+057/MWC 148 e=0.83
HESSvsinGamma = data_file.ix[616:621,'v.sin(i)']
HESSEWGamma = data_file.ix[616:621,'(-EW)']
HESSDeltaVGamma = data_file.ix[616:621,'DeltaV']
HESSFWHMGamma = data_file.ix[616:621,'FWHM']
##AGL J2241+4454/MWC 656 **Potential G-Ray
AGLvsinGamma = data_file.ix[622:624,'v.sin(i)']
AGLEWGamma = data_file.ix[622:624,'(-EW)']
AGLDeltaVGamma = data_file.ix[622:624,'DeltaV']
AGLFWHMGamma = data_file.ix[622:624,'FWHM']

#Seperate X-Ray Binaries
##4U 1145-619/V801 Cen e=?
X1vsinXray = data_file.ix[0:9,'v.sin(i)']
X1EWXray = data_file.ix[0:9,'(-EW)']
X1DeltaVXray = data_file.ix[0:9,'DeltaV']
X1FWHMXray = data_file.ix[0:9,'FWHM']
##A 0535+26/V725 Tau e=0.47
X2vsinXray = data_file.ix[10:125,'v.sin(i)']
X2EWXray = data_file.ix[10:125,'(-EW)']
X2DeltaVXray = data_file.ix[10:125,'DeltaV']
X2FWHMXray = data_file.ix[10:125,'FWHM']
##V 0332+53/BQ Cam e=0.37
X3vsinXray = data_file.ix[126:142,'v.sin(i)']
X3EWXray = data_file.ix[126:142,'(-EW)']
X3DeltaVXray = data_file.ix[126:142,'DeltaV']
X3FWHMXray = data_file.ix[126:142,'FWHM']
##4U 0115+63/V635Cas e=0.34
X4vsinXray = data_file.ix[143:240,'v.sin(i)']
X4EWXray = data_file.ix[143:240,'(-EW)']
X4DeltaVXray = data_file.ix[143:240,'DeltaV']
X4FWHMXray = data_file.ix[143:240,'FWHM']
##A 1118-617/Hen3-640 e=0
X5vsinXray = data_file.ix[241:247,'v.sin(i)']
X5EWXay = data_file.ix[241:247,'(-EW)']
X5DeltaVXray = data_file.ix[241:247,'DeltaV']
X5FWHMXray = data_file.ix[241:247,'FWHM']
##RX J0812.4-3114/LS 992 e=?
X6vsinXray = data_file.ix[248:249,'v.sin(i)']
X6EWXray = data_file.ix[248:249,'(-EW)']
X6DeltaVXray = data_file.ix[248:249,'DeltaV']
X6FWHMXray = data_file.ix[248:249,'FWHM']
##4U 0728-25
X7vsinXray = data_file.ix[250:255,'v.sin(i)']
X7EWXray = data_file.ix[250:255,'(-EW)']
X7DeltaVXray = data_file.ix[250:255,'DeltaV']
X7FWHMXray = data_file.ix[250:255,'FWHM']
##X Per/HD 24534
X8vsinXray = data_file.ix[256:268,'v.sin(i)']
X8EWXray = data_file.ix[256:268,'(-EW)']
X8DeltaVXray = data_file.ix[256:268,'DeltaV']
X8FWHMXray = data_file.ix[256:268,'FWHM']


########################################

#FWHM - Disk Speed
plt.figure(1)
plt.plot(vsinXray,FWHMXray,'r.') #Red
plt.plot(vsinBe, FWHMBe,'b.') #Blue
plt.plot(LSIvsinGamma, LSIFWHMGamma,'k.') #Green
plt.plot(HESSvsinGamma, HESSFWHMGamma,'k+') #Green
plt.plot(AGLvsinGamma, AGLFWHMGamma,'kD') #Green
plt.legend(['X-Ray Binary', 'Single Be Star', 'LS I+61^303', 'HESS J0632+057AGL', 'AGL J2241+4454'])
plt.xlabel('v.sin(i) (km/s)')
plt.ylabel('FWHM (km/s)')

#EW - Spectra-Feature Strenght
plt.figure(2)
plt.plot(vsinXray,EWXray,'r.') #Red
plt.plot(vsinBe, EWBe,'b.') #Blue
plt.plot(LSIvsinGamma, LSIEWGamma,'k.') #Green
plt.plot(HESSvsinGamma, HESSEWGamma,'k+') #Green
plt.plot(AGLvsinGamma, AGLEWGamma,'kx') #Green
plt.legend(['X-Ray Binary', 'Single Be Star', 'LS I+61^303', 'HESS J0632+057AGL', 'AGL J2241+4454'])
plt.xlabel('v.sin(i) (km/s)')
plt.ylabel('-EW (A)')

#ΔV - Disk Radius
plt.figure(3)
plt.plot(vsinXray,DeltaVXray,'r.') #Red
plt.plot(vsinBe, DeltaVBe,'b.') #Blue
plt.plot(LSIvsinGamma, LSIDeltaVGamma,'k.') #Green
plt.plot(HESSvsinGamma, HESSDeltaVGamma,'k+') #Green
plt.plot(AGLvsinGamma, AGLDeltaVGamma,'kx') #Green
plt.legend(['X-Ray Binary', 'Single Be Star', 'LS I+61^303', 'HESS J0632+057AGL', 'AGL J2241+4454'])
plt.xlabel('v.sin(i) (km/s)')
plt.ylabel('Delta V (km/s)')

#Normalising
N1Xray = np.log(DeltaVXray/(2*vsinXray))
N2Xray = np.log(FWHMXray/(2*vsinXray))
N3Xray = np.log(EWXray)
N4Xray = FWHMXray/vsinXray
N5Xray = DeltaVXray/vsinXray

N1Be = np.log(DeltaVBe/(2*vsinBe))
N2Be = np.log(FWHMBe/(2*vsinBe))
N3Be = np.log(EWBe)
N4Be = FWHMBe/vsinBe
N5Be = DeltaVBe/vsinBe

N1Gamma = np.log(DeltaVGamma/(2*vsinGamma))
N2Gamma = np.log(FWHMGamma/(2*vsinGamma))
N3Gamma = np.log(EWGamma)
N4Gamma = FWHMGamma/vsinGamma
N5Gamma = DeltaVGamma/vsinGamma

########## Gamma-Ray Binaries
##LSI+61'303/V615 Cas
N1LSIGamma = np.log(LSIDeltaVGamma/(2*LSIvsinGamma))
N2LSIGamma = np.log(LSIFWHMGamma/(2*LSIvsinGamma))
N3LSIGamma = np.log(LSIEWGamma)
N4LSIGamma = LSIFWHMGamma/LSIvsinGamma
N5LSIGamma = LSIDeltaVGamma/LSIvsinGamma
##HESS J0632+057/MWC 148
N1HESSGamma = np.log(HESSDeltaVGamma/(2*HESSvsinGamma))
N2HESSGamma = np.log(HESSFWHMGamma/(2*HESSvsinGamma))
N3HESSGamma = np.log(HESSEWGamma)
N4HESSGamma = HESSFWHMGamma/HESSvsinGamma
N5HESSGamma = HESSDeltaVGamma/HESSvsinGamma
##AGL J2241+4454/MWC 656
N1AGLGamma = np.log(AGLDeltaVGamma/(2*AGLvsinGamma))
N2AGLGamma = np.log(AGLFWHMGamma/(2*AGLvsinGamma))
N3AGLGamma = np.log(AGLEWGamma)
N4AGLGamma = AGLFWHMGamma/AGLvsinGamma
N5AGLGamma = AGLDeltaVGamma/AGLvsinGamma

########################################

#Normalising Plots
##X-ray
XP = np.argwhere(np.isnan(N1Xray))      #Finds rows with NaN
XQ = np.argwhere(np.isnan(N3Xray))      #Same for other axes rows
XO = np.concatenate((XP, XQ), axis=0)   #Adds both row numbers together
arrX1 = np.array(N1Xray)                #Turns data into an array
arrX3 = np.array(N3Xray)
XY = np.delete(arrX1, XO, axis=0)       #Deletes rows with NaN values from initial data
XX = np.delete(arrX3, XO, axis=0)
##Be Star
BP = np.argwhere(np.isnan(N1Be))
BQ = np.argwhere(np.isnan(N3Be))
BO = np.concatenate((BP, BQ), axis=0)
arrB1 = np.array(N1Be)
arrB3 = np.array(N3Be)
BY = np.delete(arrB1, BO, axis=0)
BX = np.delete(arrB3, BO, axis=0)
##Gamma-Ray
GP = np.argwhere(np.isnan(N1Gamma))
GQ = np.argwhere(np.isnan(N3Gamma))
GO = np.concatenate((GP, GQ), axis=0)
arrG1 = np.array(N1Gamma)
arrG3 = np.array(N3Gamma)
GY = np.delete(arrG1, GO, axis=0)
GX = np.delete(arrG3, GO, axis=0)

#Log(-EW/A) vs Log(DeltaV/2v.sin(i) - Differences point to different disk densities (Zamanov et al 2000)
plt.figure(4)
plt.plot(N3Xray, N1Xray,'r.') #Red
plt.plot(N3Be, N1Be,'b.') #Blue
plt.plot(N3LSIGamma, N1LSIGamma,'k.') #Green
plt.plot(N3HESSGamma, N1HESSGamma,'k+') #Green
plt.plot(N3AGLGamma, N1AGLGamma,'kx') #Green
p1 = sp.polyfit(XX,XY,1)
plt.plot(XX, sp.polyval(p1,XX), 'r-')
p2 = sp.polyfit(BX,BY,1)
plt.plot(BX, sp.polyval(p2,BX), 'b-')
p3 = sp.polyfit(GX,GY,1)
plt.plot(GX, sp.polyval(p3,GX), 'k-')
        
plt.legend(['X-Ray Binary', 'Single Be Star', 'LS I+61^303', 'HESS J0632+057AGL', 'AGL J2241+4454'])
plt.xlabel('Log(-EW/A)')
plt.ylabel('Log(DeltaV/2v.sin(i)')

########################################

#Log(-EW/A) vs Log(FWHM/2v.sin(i) - Processes relevant to line broadening are the same
#[Kepler Rotation, Thermal Broadening, Non-Coherent Scattering] (Zamanov et al 2000)
plt.figure(5)
plt.plot(N3Xray,N2Xray,'r.') #Red
plt.plot(N3Be, N2Be,'b.') #Blue
plt.plot(N3LSIGamma, N2LSIGamma,'k.') #Green
plt.plot(N3HESSGamma, N2HESSGamma,'k+') #Green
plt.plot(N3AGLGamma, N2AGLGamma,'kx') #Green
plt.legend(['X-Ray Binary', 'Single Be Star', 'LS I+61^303', 'HESS J0632+057AGL', 'AGL J2241+4454'])
plt.xlabel('Log(-EW/A)')
plt.ylabel('Log(FWHM/2v.sin(i)')

########################################

#DeltaV/v.sin(i) vs FWHM/2v.sin(i) - The higher DeltaV (further right), implies smaller disks for the same effective emitting size
# Indications as to outer parts of disks missing due to truncation by larger mass body (Zamanov et al 2000)
XP = np.argwhere(np.isnan(N4Xray))      #Finds rows with NaN
XQ = np.argwhere(np.isnan(N5Xray))      #Same for other axes rows
XO = np.concatenate((XP, XQ), axis=0)   #Adds both row numbers together
arrX4 = np.array(N4Xray)                #Turns data into an array
arrX5 = np.array(N5Xray)
XY = np.delete(arrX4, XO, axis=0)       #Deletes rows with NaN values from initial data
XX = np.delete(arrX5, XO, axis=0)

BP = np.argwhere(np.isnan(N4Be))
BQ = np.argwhere(np.isnan(N5Be))
BO = np.concatenate((BP, BQ), axis=0)
arrB4 = np.array(N4Be)
arrB5 = np.array(N5Be)
BY = np.delete(arrB4, BO, axis=0)
BX = np.delete(arrB5, BO, axis=0)
'''
GP = np.argwhere(np.isnan(N4Gamma))
GQ = np.argwhere(np.isnan(N5Gamma))
GO = np.concatenate((GP, GQ), axis=0)
arrG4 = np.array(N4Gamma)
arrG5 = np.array(N5Gamma)
GY = np.delete(arrG4, GO, axis=0)
GX = np.delete(arrG5, GO, axis=0)
'''

plt.figure(6)
plt.plot(N5Xray,N4Xray,'r.') #Red
plt.plot(N5Be, N4Be,'b.') #Blue
plt.plot(N5LSIGamma, N4LSIGamma,'k.') #Green
plt.plot(N5HESSGamma, N4HESSGamma,'k+') #Green
plt.plot(N5AGLGamma, N4AGLGamma,'kx') #Green
p1 = sp.polyfit(XX,XY,1)
plt.plot(XX, sp.polyval(p1,XX), 'r-')
p2 = sp.polyfit(BX,BY,1)
plt.plot(BX, sp.polyval(p2,BX), 'b-')
        
plt.legend(['X-Ray Binary', 'Single Be Star', 'LS I+61^303', 'HESS J0632+057AGL', 'AGL J2241+4454'])
plt.xlabel('DeltaV/v.sin(i)')
plt.ylabel('FWHM/2v.sin(i)')

##Ratio - Radius Ratio [Disk Radius/Star Radius]
RatioXray = ((2*vsinXray)/DeltaVXray)**2
RatioBe = ((2*vsinBe)/DeltaVBe)**2
RatioHESSGamma = ((2*HESSvsinGamma)/HESSDeltaVGamma)**2
RatioAGLGamma = ((2*AGLvsinGamma)/AGLDeltaVGamma)**2
RatioLSIGamma = ((2*LSIvsinGamma)/LSIDeltaVGamma)**2

RatioXray1 = ((2*X1vsinXray)/X1DeltaVXray)**2
RatioXray2 = ((2*X2vsinXray)/X2DeltaVXray)**2
RatioXray3 = ((2*X3vsinXray)/X3DeltaVXray)**2
RatioXray4 = ((2*X4vsinXray)/X4DeltaVXray)**2
RatioXray5 = ((2*X5vsinXray)/X5DeltaVXray)**2
RatioXray6 = ((2*X6vsinXray)/X6DeltaVXray)**2
RatioXray7 = ((2*X7vsinXray)/X7DeltaVXray)**2
RatioXray8 = ((2*X8vsinXray)/X8DeltaVXray)**2

########################################

#Plot of Star-Disk Variability at Different Stellar Rotational Velocities (Gamma-Ray)
plt.figure(7)
#plt.plot(vsinXray,RatioXray,'r.') #Red
#plt.plot(vsinBe, RatioBe,'b.') #Blue
plt.plot(LSIvsinGamma, RatioLSIGamma,'k.') #Black dot
plt.plot(HESSvsinGamma, RatioHESSGamma,'k+') #Black +
plt.plot(AGLvsinGamma, RatioAGLGamma,'kx') #Black X
      
plt.legend(['LS I+61^303', 'HESS J0632+057AGL', 'AGL J2241+4454'])
plt.xlabel('v.sin(i)')
plt.ylabel('R(disk/star)')

########################################

#Plot of Star-Disk Variability at Different Stellar Rotational Velocities (X-Ray)
plt.figure(8)
plt.plot(X1vsinXray,RatioXray1,'r.') #Red
plt.plot(X2vsinXray,RatioXray2,'b.') #Bue
plt.plot(X3vsinXray,RatioXray3,'g.') #Green
plt.plot(X4vsinXray,RatioXray4,'m.') #Magenta
plt.plot(X5vsinXray,RatioXray5,'c.') #Cyan
plt.plot(X6vsinXray,RatioXray6,'kx') #Black(x)
plt.plot(X7vsinXray,RatioXray7,'y.') #Yellow
plt.plot(X8vsinXray,RatioXray8,'k.') #Black(Dots)
      
plt.legend(['4U 1145-619/V801 Cen', 'A 0535+26/V725 Tau', 'V 0332+53/BQ Cam', '4U 0115+63/V635Cas', 'A 1118-617/Hen3-640', 'RX J0812.4-3114/LS 992', '4U 0728-25', 'X Per/HD 24534'])
plt.xlabel('v.sin(i)')
plt.ylabel('R(disk/star)')


#Delta V vs Disk Ratio (Proving the link between measurement and disk size)
plt.figure(9)
#plt.plot(DeltaVXray,RatioXray,'r.') #Red
#plt.plot(DeltaVBe, RatioBe,'b.') #Blue
plt.plot(LSIDeltaVGamma, RatioLSIGamma,'k.') #Black dot
plt.plot(HESSDeltaVGamma, RatioHESSGamma,'k+') #Black +
plt.plot(AGLDeltaVGamma, RatioAGLGamma,'kx') #Black X
      
plt.legend(['X-Ray Binary', 'Single Be Star', 'LS I+61^303', 'HESS J0632+057AGL', 'AGL J2241+4454'])
plt.xlabel('DeltaV')
plt.ylabel('R(disk/star)')

########################################

#Delta V vs Disk Ratio - For Xray Sources (Proving the link between measurement and disk size)
plt.figure(10)
plt.plot(X1DeltaVXray,RatioXray1,'r.') #Red
plt.plot(X2DeltaVXray,RatioXray2,'b.') #Bue
plt.plot(X3DeltaVXray,RatioXray3,'g.') #Green
plt.plot(X4DeltaVXray,RatioXray4,'m.') #Magenta
#plt.plot(X5DeltaVXray,RatioXray5,'c.') #Cyan
plt.plot(X6DeltaVXray,RatioXray6,'kx') #Black(x)
plt.plot(X7DeltaVXray,RatioXray7,'y.') #Yellow
plt.plot(X8DeltaVXray,RatioXray8,'k.') #Black(Dots)
      
plt.legend(['4U 1145-619/V801 Cen', 'A 0535+26/V725 Tau', 'V 0332+53/BQ Cam', '4U 0115+63/V635Cas', 'RX J0812.4-3114/LS 992', '4U 0728-25', 'X Per/HD 24534'])
plt.xlabel('DeltaV')
plt.ylabel('R(disk/star)')

#print (RatioLSIGamma)

import numpy as np
import h5py as h5

def randoms_lightcone(NR, Z_gal):
    '''generate NR random points in the light cone footprint, reshuffling the observed redshifts
    
    Parameters
    ----------
        NR    : int, number of random points to be generated
        Z_gal : numpy array, containing redshifts for reshuffling
        
    Returns
    -------
        RA_R  : numpy array of length NR, containg RA of randoms in degrees
        DEC_R : numpy array of length NR, containg DEC of randoms in degrees
        Z_R   : numpy array of length NR, containg redshift of randoms
    '''
    #survey footprint boundaries in radian
    RA_min = 0.
    RA_max = 90.*np.pi/180.
    DEC_min = -46.*np.pi/180.
    DEC_max = 0.
    
    #generate NR coordinates uniformly distributed between RA_min and RA_max
    RA_R = RA_min +(RA_max - RA_min)*np.random.sample(size = NR)
    #covert to degree
    RA_R *= 180./np.pi

    #generate NR coordinates uniformly distributed in sin(DEC) between DEC_min and DEC_max
    DEC_R = np.arcsin(np.sin(DEC_min)+(np.sin(DEC_max)-np.sin(DEC_min))*np.random.sample(size = NR))
    #covert to degree
    DEC_R *= 180./np.pi
    
    #generate NR redshifts from resampling input Z
    Z_R = np.random.choice(Z_gal,size = NR, replace =True)
    return RA_R, DEC_R, Z_R


#read in lightcone catalog to extract redshifts
infile = h5.File("C_mock_lightcone.h5", 'r')
galaxies = infile['galaxies']
Z_red = galaxies['Z_red']
#number of random points to be generated
NR = 10000
#generate NR random points in the light cone footprint, reshuffling the observed redshifts
RA,DEC,Z = randoms_lightcone(NR, Z_red)
import numpy as np
import h5py as h5
import scipy.stats
import matplotlib.pyplot as plt

def randoms_lightcone(NR, Z_gal, shuffle = True):
    '''generate NR random points in the light cone footprint, reshuffling the observed redshifts
    
    Parameters
    ----------
        NR     : int; number of random points to be generated
        Z_gal  : numpy array; containing data redshifts
        shuffle: bool, optional; switches between random redshifts from reshuffling (True)
                                 and drawing from smoothed input distribution (False)
    Returns
    -------
        RA_R   : numpy array of length NR; contains RA of randoms in degrees
        DEC_R  : numpy array of length NR; contains DEC of randoms in degrees
        Z_R    : numpy array of length NR; contains redshift of randoms
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
    
    if shuffle:
        #generate NR redshifts from resampling input Z
        Z_R = np.random.choice(Z_gal,size = NR, replace =True)
    else:
        #generate scipy.stats distribution from historgam of input n(z)
        #use coarse binning to smooth over big wall-like structures
        hist_dist = scipy.stats.rv_histogram(np.histogram(Z_gal, bins=10))
        Z_R = hist_dist.rvs(size=NR)
    return RA_R, DEC_R, Z_R


#read in lightcone catalog to extract redshifts
infile = h5.File("C_mock_lightcone.h5", 'r')
galaxies = infile['galaxies']
Z_red = galaxies['Z_red']
#number of random points to be generated
NR = 1000000
#generate NR random points in the light cone footprint, drawing random redshifts from smoothed input distribution
RA,DEC,Z = randoms_lightcone(NR, Z_red, shuffle = False)

#plot data and random redshift distributions
plt.hist(Z, density = True, bins=100, alpha=0.4, label="randoms")
plt.hist(Z_red,  density = True, bins=100, alpha=0.4, label="data")
plt.xlabel("z")
plt.ylabel("n(z)")
plt.legend(loc = 4)
plt.show()

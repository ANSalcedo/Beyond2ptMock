import h5py as h5

infile = h5.File("<mock_filename>", 'r')

galaxies = infile['galaxies']

#For the real-space snapshot

x = galaxies['x'] #each in units of comoving-Mpc/h
y = galaxies['y']
z = galaxies['z']

#For the redshift-space snapshot

x     = galaxies['x'] #each in units of comoving-Mpc/h
y     = galaxies['y']
z_los = galaxies['z_los']

#For the lightcone

RA    = galaxies['RA'] #RA and DEC in degrees
DEC   = galaxies['DEC']
Z_red = galaxies['Z_red']

infile.close()

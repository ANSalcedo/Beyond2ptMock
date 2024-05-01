# Beyond-2pt parameter masked data challenge

This data challenge for analyses of galaxy redshift surveys consists of galaxy mock catalogs constructed from N-body halo catalogs using HOD-based galaxy assignments. 


The simulated galaxy catalogs are available in three different coordinate systems with increasing analysis complexity:


## Flat LCDM catalogs

### ([Real-space snapshot](https://github.com/ANSalcedo/Beyond2ptMock/tree/main/LCDM_lightcone))

Ten realizations of one LCDM cosmology with real-space galaxy coordinates from a 8,0 (Gpc/h)^3 snapshot at z=1.0 with periodic boundary conditions (box length = 2000.0 Mpc/h). For each galaxy, the file contains coordinates ``x,y,z`` in Mpc/h with the box center at ``(1000,1000,1000)``. The galaxy number density is ~ 4.5e-4 (Mpc/h)^{-3}.

### ([Redshift-space snapshot](https://github.com/ANSalcedo/Beyond2ptMock/tree/main/LCDM_redshift_space))

Ten realizations of one LCDM cosmology with redshift-space galaxy coordinates for a line-of-sight along the ``z`` coordinate axis with redshift space distortions calculated in the plane-parallel approximation from a 8.0 (Gpc/h)^3 snapshot at z=1.0 with periodic boundary conditions (box length = 2000.0 Mpc/h). For each galaxy, the file contains ``x,y,z_los`` in Mpc/h with the box center at ``(1000,1000,1000)``. The galaxy number density is ~ 4.5e-4 (Mpc/h)^{-3}.

### Light cone ([mock_lcdm_lightcone.h5](https://github.com/ANSalcedo/Beyond2ptMock/blob/main/LCDM_lightcone/mock_lcdm_lightcone.h5))

One LCDM lightcone with angular coordinates ``RA,DEC`` and redshift ``Z_red`` for a galaxy sample in the redshift range [0.8,1.3]. The survey footprint is 0.0<sup>&#9702;</sup> < RA < 90.0<sup>&#9702;</sup> and -46<sup>&#9702;</sup> < DEC < 0<sup>&#9702;</sup>, with uniform coverage across the redshift range. The galaxy number density at z = 1 is ~ 4.5e-4 (Mpc/h)^-3.


The fiducial cosmolgies fo the mocks are drawn from the prior specified in this ([script](https://github.com/ANSalcedo/Beyond2ptMock/blob/main/parameters_theta_s_constrained.ipynb)). A minimal example for reading in the catalogs is provided ([here](https://github.com/ANSalcedo/Beyond2ptMock/blob/main/read_hdf5_example.py)).
## Issues and Questions

Please create an issue or email ```ansalcedo@arizona.edu```, ```yosukekobayashi@arizona.edu```, and ```krausee@arizona.edu``` with any questions or requests.

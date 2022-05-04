## Beyond-2pt blind data challenge
This data challenge for analyses of galaxy-redshift surveys consists of galaxy mock catalogs constructed from N-body halo catalogs using HOD-based galaxy assignments. The simulated galaxy catalogs are available in three different coordinate systems with increasing analysis complexity:
### Real-space snapshot ([A_mock_real-space.h5](https://github.com/ANSalcedo/Beyond2ptMock/blob/main/A_mock_real-space.h5))
Real-space galaxy coordinates from a ~1.3 (Gpc/h)^3 snapshot at z=1.0 with periodic boundary conditions (box length = 1100.0 Mpc/h). For each galaxy, the file contains coordinates ``x,y,z`` in Mpc/h with the box center at ``(0,0,0)``. The galaxy number density is ~ 4e-4 (Mpc/h)^3.
### Redshift space snapshot ([B_mock_redshift-space.h5](https://github.com/ANSalcedo/Beyond2ptMock/blob/main/B_mock_redshift-space.h5))
Redshift-space galaxy coordinates for a line-of-sight along the ``z`` coordinate axis with redshift space distortions calculated in the plane-parallel approximation from a ~1.3 (Gpc/h)^3 snapshot at z=1.0 with periodic boundary conditions (box length = 1100.0 Mpc/h). For each galaxy, the file contains ``x,y,z_los`` in Mpc/h with the box center at ``(0,0,0)``. The galaxy number density is ~ 5.5 (Mpc/h)^3.
### Light cone ([C_mock_lightcone.h5](https://github.com/ANSalcedo/Beyond2ptMock/blob/main/C_mock_lightcone.h5))
Angular coordinates ``RA,DEC`` and redshift ``Z_red`` for a galaxy sample in the redshift range [0.8,1.3]. The survey footprint is 0.0<sup>&#9702;</sup> < RA < 90.0<sup>&#9702;</sup> and -46<sup>&#9702;</sup> < DEC < 0<sup>&#9702;</sup>, with uniform coverage across the redshift range. The galaxy number density at z = 1 is ~ 5e-4 (Mpc/h)^-3.

_These catalogs are generated at three different cosmologies (Box A,B,C), so that e.g., an analysis of the real space catalog will not unblind the light cone data._

### Issues and Questions
Please create an issue or email ```ansalcedo@arizona.edu```, ```yosukekobayashi@arizona.edu```, and ```krausee@arizona.edu``` with any questions or requests.

## Flat $w$CDM catalogs

### Real-space snapshot ([A_mock_real-space.h5](https://github.com/ANSalcedo/Beyond2ptMock/blob/main/A_mock_real-space.h5))
Real-space galaxy coordinates from a ~1.3 (Gpc/h)^3 snapshot at z=1.0 with periodic boundary conditions (box length = 1100.0 Mpc/h). For each galaxy, the file contains coordinates ``x,y,z`` in Mpc/h with the box center at ``(550,550,550)``. The galaxy number density is ~ 4e-4 (Mpc/h)^{-3}.
### Redshift space snapshot ([B_mock_redshift-space.h5](https://github.com/ANSalcedo/Beyond2ptMock/blob/main/B_mock_redshift-space.h5))
Redshift-space galaxy coordinates for a line-of-sight along the ``z`` coordinate axis with redshift space distortions calculated in the plane-parallel approximation from a ~1.3 (Gpc/h)^3 snapshot at z=1.0 with periodic boundary conditions (box length = 1100.0 Mpc/h). For each galaxy, the file contains ``x,y,z_los`` in Mpc/h with the box center at ``(550,550,550)``. The galaxy number density is ~ 5.5e-4 (Mpc/h)^{-3}.
### Light cone ([C_mock_lightcone.h5](https://github.com/ANSalcedo/Beyond2ptMock/blob/main/C_mock_lightcone.h5))
Angular coordinates ``RA,DEC`` and redshift ``Z_red`` for a galaxy sample in the redshift range [0.8,1.3]. The survey footprint is 0.0<sup>&#9702;</sup> < RA < 90.0<sup>&#9702;</sup> and -46<sup>&#9702;</sup> < DEC < 0<sup>&#9702;</sup>, with uniform coverage across the redshift range. The galaxy number density at z = 1 is ~ 5e-4 (Mpc/h)^-3.
### Large real-space snapshot ([D_mock_real-space_large.h5](https://github.com/ANSalcedo/Beyond2ptMock/blob/main/D_mock_real-space_large.h5))
Real-space galaxy coordinates from a 8.0 (Gpc/h)^3 snapshot at z=1.025 with periodic boundary conditions (box length = 2000.0 Mpc/h). For each galaxy, the file contains coordinates ``x,y,z`` in Mpc/h with the box center at ``(1000,1000,1000)``. The galaxy number density is ~ 4.5e-4 (Mpc/h)^{-3}.
### Large redshift space snapshot ([E_mock_redshift-space_large.h5](https://github.com/ANSalcedo/Beyond2ptMock/blob/main/E_mock_redshift-space_large.h5))
Redshift-space galaxy coordinates for a line-of-sight along the ``z`` coordinate axis with redshift space distortions calculated in the plane-parallel approximation from a 8.0 (Gpc/h)^3 snapshot at z=1.025 with periodic boundary conditions (box length = 2000.0 Mpc/h). For each galaxy, the file contains ``x,y,z_los`` in Mpc/h with the box center at ``(1000,1000,1000)``. The galaxy number density is ~ 5.7e-4 (Mpc/h)^{-3}.
### Lower density real-space snapshot ([F_mock_real-space.h5](https://github.com/ANSalcedo/Beyond2ptMock/blob/main/F_mock_real-space.h5))
Real-space galaxy coordinates from a ~1.3 (Gpc/h)^3 snapshot at z=1.0 with periodic boundary conditions (box length = 1100.0 Mpc/h). For each galaxy, the file contains coordinates ``x,y,z`` in Mpc/h with the box center at ``(550,550,550)``. The galaxy number density is ~ 1e-4 (Mpc/h)^{-3}.

_These catalogs are generated at five different flat wCDM cosmologies (Box A/F,B,C,D,E), so that e.g., an analysis of the real space catalog will not unblind the light cone data._

import numpy as np
import matplotlib.pyplot as plt
import psi4
import nglview as nv

#molecule layout
water_template = """ 
O1
H2 1 1.0
H3 1 1.0 2 104.5
x4 2 1.0 1 90.0 3 180.0
--
O5 2 **R** 4 90.0 1 180.0
H6 5 1.0 2 120.0 4 90.0
H7 5 1.0 2 120.0 4 -90.0
units angstrom
"""

water_dimer = psi4.geometry(water_template.replace('**R**', str(2.0)))
water_structure = nv.Psi4Structure(water_dimer)
#store molecule image as variable
water_image = nv.NGLWidget(water_structure)

rvalues1 = np.linspace(1.4,2.5,12)
rvalues2 = np.array([3.0, 3.5])
rvalues = np.concatenate((rvalues1, rvalues2))

energies = []

for r in rvalues:
    water_dimer = psi4.geometry(water_template.replace('**R**', str(r)))
    energy = psi4.energy('hf/aug-cc-pvdz', molecule = water_dimer, bsse_type = 'cp')
    # Change the energy unit from Hartrees to kcal/mole
    energy = energy * 627.509
    energies.append(energy)

#plotting data from energies array
plt.plot(rvalues, energies, 'o')
#display molecule
water_image

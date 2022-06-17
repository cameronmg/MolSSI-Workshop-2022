import nglview as nv
import psi4
import numpy as np
import qcelemental as qc
import scipy.optimize as scipy
#prevent pop ups from inside the program
psi4.core.be_quiet()

#this function will calculate the activation state of the energy
def e_activation(transition_state, reactant, product):
   
    if(reactant > product):
        activation_energy = reactant - product
       
        return activation_energy
    else:
        activation_energy = product - reactant
       
        return activation_energy
       
#The first number in the sequence is telling the program which element to bond to
#The second number in the sequence tells the atoms how long the bond is
#The third number in the sequence also lets the element know what to bond to
#The fourth number in the series represents the bond angle

trans_state_temp = """
C1
I2 1 1.79
H3 1 1.09 2 90.0
H4 1 1.09 2 90.0 3 120
H5 1 1.09 2 90.0 3 -120
--
Br6 1 1.79 3 90 2 180
"""

trans_state = psi4.geometry(trans_state_temp.replace('**R**', str(1.79)))
trans_structure = nv.Psi4Structure(trans_state)
trans_image = nv.NGLWidget(trans_structure)

psi4.set_options({'reference': 'uhf'})
trans_energy = -627.509 * psi4.energy("hf/sto-3g", molecule = trans_state)

#use for loop for input to search pubchem -->input
iodomethane = psi4.geometry("pubchem:6328")
energy_iodo = -627.509 * psi4.energy("hf/sto-3g", molecule = iodomethane)

bromomethane = psi4.geometry("pubchem:6323")
energy_bromo = -627.509 * psi4.energy("hf/sto-3g", molecule = bromomethane)

print(F' \nThe energy of activation is {e_activation(trans_energy, energy_iodo, energy_bromo):.3f} kCal/mol')

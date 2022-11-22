import os
import sys
module_path = os.path.abspath(os.path.join('..'))

if module_path not in sys.path:
    sys.path.append(module_path)
import pandas as pd
from pyscf import scf, gto 
from src.polaritization_propagator import Prop_pol as pp
from src.help_functions import extra_functions
import matplotlib.pyplot as plt
import pandas as pd

text = 'test_w_T_B.txt'

if os.path.exists(text):
	os.remove(text)


mol = gto.M( atom=   '''
        O1   1
        O2   1 1.45643942
        H1   2 0.97055295 1 99.79601616
        H2   1 0.97055295 2 99.79601616 3 100''', basis='ccpvdz') 
mf = scf.RHF(mol).run()
ppobj = pp(mf)
#print('SSC in Hz with canonical orbitals')
fcsd = ppobj.kernel_select(FC=False, FCSD=True, PSO=False,atom1=[2], atom2=[3])
fc = ppobj.kernel_select(FC=True, FCSD=False, PSO=False,atom1=[2], atom2=[3])
pso = ppobj.kernel_select(FC=False, FCSD=False, PSO=True,atom1=[2], atom2=[3])

print('SD =',fcsd-fc)
print('FC =',fc)
print('PSO =',pso)
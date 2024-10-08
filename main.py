from pint import UnitRegistry, get_application_registry
from bartz import Bartz
import numpy as np


UR = UnitRegistry(system='mks')
UR = get_application_registry()
Q_ = UR.Quantity


engineDt = Q_(2.25,"inch")
combVisc = Q_(0.915,"millipoise")
Pc = Q_(400,"pound/inch**2")
Mc = 0.089
gam = 1.187
engineR = Q_(0.636,"inch")
cStar = Q_(1720,"meter/second")
At_Ac = 0.15

combPr = 0.6036
combCp = Q_(2.6,"kilojoule/kilogram/degK")

for Twg_Tc in np.arange(0.4,1.6,0.1):

    hg = Bartz(engineDt,combVisc,combCp,combPr,Pc,Mc,gam,engineR,cStar,At_Ac,Twg_Tc)

    print(hg)
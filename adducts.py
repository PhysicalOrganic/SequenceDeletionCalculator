# -*- coding: utf-8 -*-
#!/usr/bin/env python3

# This software is licensed under the MIT License.
# See the LICENSE file for more information.

'''
Contains adduct definitions
'''

from dataclasses import dataclass

# Data class to contain mass spec adduct information
@dataclass
class Adduct:
    '''Dataclass for holding adduct information'''
    name: str
    terminus: str
    charge: str
    mass: float

# Define adducts of interest by specify a name, teminus
# charge, and mass.
# KEEP ADDUCT NAMES TO LESS THAN OR EQUAL TO 30 CHARACTERS.
ADDUCTS = [Adduct(charge="+1",
                  terminus="N-Fmoc, OH",
                  name="+H+",
                  mass=197.09555),
           Adduct(charge="+1",
                  terminus="N-Fmoc, OH",
                  name="+NH4+",
                  mass=214.12210),
           Adduct(charge="+1",
                  terminus="N-Fmoc, OH",
                  name="+Na+",
                  mass=219.07749),
           Adduct(charge="+1",
                  terminus="N-Fmoc, OH",
                  name="+FA+H+",
                  mass=243.10103),
           Adduct(charge="+1",
                  terminus="N-Fmoc, OH",
                  name="+MeCN +NH4+",
                  mass=255.14864),

           Adduct(charge="+1",
                  terminus="N-Fmoc, OCF3",
                  name="+H+",
                  mass=293.07893),
           Adduct(charge="+1",
                  terminus="N-Fmoc, OCF3",
                  name="+NH4+",
                  mass=310.10494),
           Adduct(charge="+1",
                  terminus="N-Fmoc, OCF3",
                  name="+Na+",
                  mass=315.06033),
           Adduct(charge="+1",
                  terminus="N-Fmoc, OCF3",
                  name="+FA+H+",
                  mass=339.08387),
           Adduct(charge="+1",
                  terminus="N-Fmoc, OCF3",
                  name="+MeCN +NH4+",
                  mass=351.13149),

           Adduct(charge="+1",
                  terminus="N-Ac, OH",
                  name="+H+",
                  mass=17.03804),
           Adduct(charge="+1",
                  terminus="N-Ac, OH",
                  name="+NH4+",
                  mass=34.06459),
           Adduct(charge="+1",
                  terminus="N-Ac, OH",
                  name="+Na+",
                  mass=39.01998),
           Adduct(charge="+1",
                  terminus="N-Ac, OH",
                  name="+FA+H+",
                  mass=63.04352),
           Adduct(charge="+1",
                  terminus="N-Ac, OH",
                  name="+MeCN +NH4+",
                  mass=75.09114),

           Adduct(charge="+1",
                  terminus="N-Ac, OCF3",
                  name="+H+",
                  mass=113.02088),
           Adduct(charge="+1",
                  terminus="N-Ac, OCF3",
                  name="+NH4+",
                  mass=130.04743),
           Adduct(charge="+1",
                  terminus="N-Ac, OCF3",
                  name="+Na+",
                  mass=135.00282),
           Adduct(charge="+1",
                  terminus="N-Ac, OCF3",
                  name="+FA+H+",
                  mass=159.02636),
           Adduct(charge="+1",
                  terminus="N-Ac, OCF3",
                  name="+MeCN +NH4+",
                  mass=171.07398),

           Adduct(charge="+2",
                  terminus="N-Fmoc, OH",
                  name="+2H+",
                  mass=198.10283),
           Adduct(charge="+2",
                  terminus="N-Fmoc, OH",
                  name="+H+ +NH4+",
                  mass=215.12937),
           Adduct(charge="+2",
                  terminus="N-Fmoc, OCF3",
                  name="+2H+",
                  mass=294.08566),
           Adduct(charge="+2",
                  terminus="N-Fmoc, OCF3",
                  name="+H+ +NH4+",
                  mass=311.11221),
           Adduct(charge="+2",
                  terminus="N-Ac, OH",
                  name="+2H+",
                  mass=18.04531),
           Adduct(charge="+2",
                  terminus="N-Ac, OH",
                  name="+H+ +NH4+",
                  mass=35.07186),
           Adduct(charge="+2",
                  terminus="N-Ac, OCF3",
                  name="+2H+",
                  mass=114.02815),
           Adduct(charge="+2",
                  terminus="N-Ac, OCF3",
                  name="+H+ +NH4+",
                  mass=131.0547),

           Adduct(charge="-1",
                  terminus="N-Fmoc, OH",
                  name="-H+",
                  mass=195.08099),
           Adduct(charge="-1",
                  terminus="N-Fmoc, OH",
                  name="+Cl-",
                  mass=231.05767),
           Adduct(charge="-1",
                  terminus="N-Fmoc, OH",
                  name="+FA-H+",
                  mass=241.08647),
           Adduct(charge="-1",
                  terminus="N-Fmoc, OH",
                  name="+TFA-H+",
                  mass=309.07386),
           Adduct(charge="-1",
                  terminus="N-Fmoc, OH",
                  name="-Fmoc + e-",
                  mass=17.00274),

           Adduct(charge="-1",
                  terminus="N-Fmoc, OCF3",
                  name="-H+",
                  mass=291.06383),
           Adduct(charge="-1",
                  terminus="N-Fmoc, OCF3",
                  name="+Cl-",
                  mass=327.04051),
           Adduct(charge="-1",
                  terminus="N-Fmoc, OCF3",
                  name="+FA-H+",
                  mass=337.06931),
           Adduct(charge="-1",
                  terminus="N-Fmoc, OCF3",
                  name="+TFA-H+",
                  mass=405.0567),
           Adduct(charge="-1",
                  terminus="N-Fmoc, OCF3",
                  name="-Fmoc + e-",
                  mass=112.98558),

           Adduct(charge="-1",
                  terminus="N-Ac, OH",
                  name="-H+",
                  mass=15.02348),
           Adduct(charge="-1",
                  terminus="N-Ac, OH",
                  name="+Cl-",
                  mass=51.00016),
           Adduct(charge="-1",
                  terminus="N-Ac, OH",
                  name="+FA-H+",
                  mass=61.02896),
           Adduct(charge="-1",
                  terminus="N-Ac, OH",
                  name="+TFA-H+",
                  mass=129.01635),

           Adduct(charge="-1",
                  terminus="N-Ac, OCF3",
                  name="-H+",
                  mass=111.00632),
           Adduct(charge="-1",
                  terminus="N-Ac, OCF3",
                  name="+Cl-",
                  mass=146.98300),
           Adduct(charge="-1",
                  terminus="N-Ac, OCF3",
                  name="+FA-H+",
                  mass=157.01180),
           Adduct(charge="-1",
                  terminus="N-Ac, OCF3",
                  name="+TFA-H+",
                  mass=224.99919),
           ]

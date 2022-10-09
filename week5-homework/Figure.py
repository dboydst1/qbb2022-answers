#!usr/bin/env python

import sys
import numpy
import matplotlib.pyplot as plt
import bdg_loader

D0_H3K27ac_treat = bdg_loader.load_data('Cropped_Scaled_D0_H3K27ac_treat.bdg')
D2_H3K27ac_treat = bdg_loader.load_data('Cropped_Scaled_D2_H3K27ac_treat.bdg')
D2_Klf4_treat = bdg_loader.load_data('Cropped_Scaled_D2_Klf4_treat.bdg')
NA_treat_pileup = bdg_loader.load_data('Cropped_Scaled_NA_treat_pileup.bdg')

fig, (ax1, ax2, ax3, ax4) = plt.subplots(4)
ax1.bar(D0_H3K27ac_treat['X'], D0_H3K27ac_treat['Y'], width = 100)
ax1.set_ylabel("D0 H3K27ac")
ax2.bar(D2_H3K27ac_treat['X'], D2_H3K27ac_treat['Y'], width = 100)
ax2.set_ylabel("D2 H3K27ac")
ax3.bar(D2_Klf4_treat['X'], D2_Klf4_treat['Y'], width = 100)
ax3.set_ylabel("D2 Klf4")
ax4.bar(NA_treat_pileup['X'], NA_treat_pileup['Y'], width = 100)
ax4.set_ylabel("D2 Sox2 R1")
ax4.set_xlabel("Position")
plt.savefig('Ex1_pt5.png')
plt.show()
plt.close()
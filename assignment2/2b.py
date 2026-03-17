import matplotlib.pyplot as plt
import numpy as np
from astropy import constants as c
from astropy import units as u

v_c = 100 * u.km/u.s

def sigma(r):
    return np.sqrt(1+1/(2*r))


fig, ax = plt.subplots(figsize=(4, 3.5))

r_rinf = np.logspace(-2, 1, 100)

ax.plot(r_rinf, sigma(r_rinf))
ax.set_ylabel(r"$\frac{\sigma(r/R_{\mathrm{inf}})}{v_c}$", fontsize=14)
ax.set_xlabel(r"$\frac{r}{R_{\mathrm{inf}}}$", fontsize=14)
ax.axhline(1, ls='dashed', c='k', label='Background')
ax.set_xscale('log')
ax.set_yscale('log')

ax.scatter(1/6, 2, marker='x', c='k', zorder=3)
ax.text(1/6*1.1, 2*1.1, '200%')
ax.scatter(((1.1**2-1)*2)**-1, 1.1, marker='x', c='k', zorder=3)
ax.text(((1.1**2-1)*2)**-1*1.1, 1.1*1.1, '10%')

plt.tight_layout()
plt.show()

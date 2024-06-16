import numpy as np
from scipy.interpolate import UnivariateSpline
import matplotlib.pyplot as plt

lva_velocity = [0.848637616,
                    0.80701909,
                    0.847125648,
                    0.938298849,
                    1.254212349,
                    1.891392824,
                    2.027271038,
                    1.77177903,
                    1.792383614,
                    1.913592303,
                    1.888049839,
                    1.740999381,
                    1.520779612,
                    1.344482404,
                    1.382113934,
                    1.499291641,
                    1.443681085,
                    1.329292421,
                    1.29572188,
                    1.23181514,
                    1.178122082,
                    1.174780102,
                    1.136369058,
                    1.022520303,
                    0.93012271,
                    0.912917651,
                    0.920154996,
                    0.895582053,
                    0.942527649,
                    0.936963696]

t = np.linspace(0, 951, len(lva_velocity))

spl = UnivariateSpline(t, lva_velocity, k=5)


plt.plot(t, lva_velocity, 'ro', ms=5)
plt.plot(t, lva_velocity, 'r', linestyle='--', lw=0.5)

tnew = np.linspace(0, 951, 1000)
spl.set_smoothing_factor(0.1)
plt.plot(tnew, spl(tnew), 'b', lw=3)

plt.show()
plt.close()

rva_velocity = [0.247426581,
                0.422073122,
                0.810264593,
                1.229616588,
                2.163382059,
                3.7332934,
                4.550075292,
                4.245502431,
                4.118670492,
                3.095260393,
                2.180491478,
                1.521510309,
                0.758527135,
                0.368080821,
                0.481735522,
                0.380346012,
                0.185040665,
                0.10628233,
                0.119750561,
                0.234517943,
                0.396352626,
                0.375314551,
                0.332350363,
                0.251735247,
                0.234669003,
                0.182901337,
                0.299768979,
                0.433334731,
                0.381273636,
                0.319951809]

t = np.linspace(0, 951, len(rva_velocity))

spl = UnivariateSpline(t, rva_velocity, k=5)


plt.plot(t, rva_velocity, 'ro', ms=5)
plt.plot(t, rva_velocity, 'r', linestyle='--', lw=0.5)

tnew = np.linspace(0, 951, 1000)
spl.set_smoothing_factor(0.1)
plt.plot(tnew, spl(tnew), 'b', lw=3)

plt.show()

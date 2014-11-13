# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np

plt.ylabel("Kiirus (MBit/s)")
plt.xlabel("Aeg (sek)")
t = np.arange(1, 26, 1)
plt.plot(t, [0.459, 0.131, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.655, 0.721, 0.655, 0.590, 0.721, 0.786, 1.114, 2.753, 2.294, 3.539, 4.915, 4.850, 5.046], 'gs-', label='TCP 1', linewidth=2)
plt.plot(t, [7.799, 1.704, 7.406, 2.228, 6.291, 6.095, 5.046, 1.311, 9.306, 1.507, 7.012, 7.274, 7.274, 0.786, 9.372, 2.621, 7.733, 9.765, 10.289, 1.049, 6.226, 2.621, 6.685, 10.027, 8.585], 'rs-', label='TCP 2', linewidth=2)
plt.plot(t, [6.095, 6.160, 6.226, 6.947, 7.340, 5.046, 5.243, 4.391, 5.636, 6.554, 5.439, 5.571, 4.784, 4.981, 4.325, 6.226, 5.308, 5.046, 4.260, 2.490, 4.653, 5.112, 3.015, 4.129, 4.456], 'bs-', label='TCP 3', linewidth=2)
plt.plot(t, [3.399, 0, 0, 0, 0, 0.882, 2.129, 0, 0, 0, 0, 0, 0.517, 0.894, 0.706, 0, 0, 0, 0, 0, 0.529, 0, 0, 0, 0], 'co-', label='UDP 1', linewidth=2)
plt.plot(t, [2.717, 0, 0, 0, 0, 0.529, 0, 0, 0, 0, 0, 0.717, 0.706, 0.706, 0.353, 0, 0, 0, 0, 0.706, 0, 0, 0, 0, 0], 'mo-', label='UDP 2', linewidth=2)
plt.plot(t, [2.740, 0, 0, 0, 0, 0.882, 0.353, 0, 0, 0, 0, 0.529, 0.894, 0.353, 0.353, 0, 0, 0, 0, 0.529, 0, 0, 0, 0, 0], 'yo-', label='UDP 3', linewidth=2)
plt.xticks(np.arange(0, max(t)+1, 2.5))
plt.yticks(np.arange(0, 11, 0.5))
plt.grid()
plt.title("802.11g (2.4Ghz) kanal 11")
plt.legend(ncol=2, fontsize='medium', frameon=False)
plt.show()
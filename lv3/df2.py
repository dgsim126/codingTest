import numpy as np
import matplotlib.pyplot as plt

R_L = [0, 104.9, 205.0, 303.0, 405.0, 507, 606, 706, 804, 903, 1002, 1101, 1200, 1300, 1404, 1502, 2002, 3002, 3998, 4990]
V_L = [0, 0.833, 1.502, 2.070, 2.559, 2.982, 3.354, 3.67, 3.97, 4.22, 4.46, 4.68, 4.87, 5.05, 5.21, 5.36, 5.96, 6.72, 7.17, 7.47]
P_L = []

for V, R in zip(V_L, R_L):
    if R != 0:
        power = (V ** 2) / R
        power_mW = power * 1000
    else:
        power_mW = 0
    P_L.append(power_mW)

# 결과 반환
for i in range(len(P_L)):
    print(P_L[i])

# 그래프 출력
plt.figure(figsize=(8, 6))
plt.plot(np.array(R_L) / 1000, P_L, marker='o', linestyle='-', color='black')  # Converting R_L to kΩ for plotting
plt.xlabel(r'$R_L$ (k$\Omega$)')
plt.ylabel('$P_L$ (mW)')
plt.grid(True)
plt.axvline(x=1, linestyle='--', color='gray')  # Example of a reference line at R_L = 1 kΩ
plt.show()

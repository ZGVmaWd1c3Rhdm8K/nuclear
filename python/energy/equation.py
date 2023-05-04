import math

# Constants
C = 299792458  # speed of light in m/s
EFFICIENCY = 0.05  # typical efficiency of nuclear weapons

# User input
megatons = float(input("Enter the number of megatons: "))

# Energy calculation
E_megatons = megatons * 4.184 * 10**15  # energy per megaton in J
E_total = E_megatons * 1.5111 * 10**4  # total energy in J
E_total_formatted = f"{E_total:.2e}"  # formatted string of total energy

# Mass calculation
m = E_total / (C**2 * EFFICIENCY)  # mass in kg
m_formatted = f"{m:.4e}"  # formatted string of mass

# Weight of uranium-235 required
u235_weight = m / 1000  # weight of uranium-235 in kg

# Output equation
print(f"Energy:\nE_total = {megatons:.2f} megatons x 4.184 x 10¹⁵ J/megaton")
print(f"E_total = {E_total_formatted} J\n")
print("Mass:\nm =", end=" ")
print(f"E_total / (c² x eficiência)")
print(f"m = {m_formatted} kg\n")

# Output weight of uranium-235
print(f"Weight of uranium-235 required: {u235_weight:.4f} kg")

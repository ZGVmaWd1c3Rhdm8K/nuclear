import math

# Constants
megaton_to_joules = 4.184e15
c_squared = 9e16
efficiency = 0.05
uranium_density = 19050 # kg/m³

# User input
megatons = float(input("Digite o número de megatons: "))

# Energy calculation
energy_megatons = megatons * megaton_to_joules
energy_joules = energy_megatons * 1e6
print(f"E = {megatons:.3f} megatons x {megaton_to_joules} J/megaton")
print(f"E = {energy_joules} J")

# Mass calculation
mass_kg = energy_joules / (c_squared * efficiency)
print(f"m = {energy_joules} J / ({c_squared} m²/s² x {efficiency})")
print(f"m = {mass_kg:.4f} kg")

# Uranium weight calculation
uranium_weight = mass_kg / 1000 / uranium_density # converted to kg
print(f"Peso necessário de urânio-235: {uranium_weight:.4f} toneladas")

# Vessel parameters calculation
required_heat = energy_joules / 3600 # J/s
radius = 25 # meters
height = mass_kg / (uranium_density * math.pi * radius ** 2 * 2)
thickness = required_heat / (2 * math.pi * radius * height * 20)
diameter = math.sqrt(4 * math.pi * radius ** 2 * height)
volume = math.pi * radius ** 2 * height
vessel_mass = uranium_density * (math.pi * radius ** 2 * thickness + 2 * math.pi * radius * height * thickness)

# Output
print(f"Energy = {energy_joules} J")
print(f"Temperature = {energy_joules / 1e6} K")
print(f"Volume = {volume} m³")
print(f"Massa da vasília = {vessel_mass} kg")
print(f"Taxa de transferência de calor = {2 * math.pi * radius * height * thickness * 1000} J/s")  # kg/s to J/s

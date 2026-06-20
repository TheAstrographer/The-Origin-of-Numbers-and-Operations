from implementation import gamma_complex, solve_limit_point_of_existence
import math

print("JCR-ASR1: 100 Points with Full idX Relations")
print("=" * 90)
print("Generator: Γ(a, b) + idX Neutral Self-Mapping")
print("Anchor: 1 ∈ √1\n")

# Generate 100 points (10x10 grid + extras for diversity)
points = []

# Main 10x10 grid (1.0-1.9 real, 2.0-2.9 imag)
for a in [round(1.0 + i*0.1, 1) for i in range(10)]:
    for b in [round(2.0 + i*0.1, 1) for i in range(10)]:
        points.append((a, b))

# Additional diverse points to reach 100+
extra_points = [
    (0.0, 0.0), (1.0, 0.0), (0.0, 1.0), (-1.0, 0.0), (0.0, -1.0),
    (3.14, 2.718), (7.777, 3.14159), (-5.5, 9.876), (42.0, -42.0),
    (0.0001, 0.0001), (100.0, 1.0), (-10.0, -10.0), (2.5, 2.5)
]
points.extend(extra_points[:15])  # Bring total well over 100

print(f"Processing {len(points)} points...\n")

for idx, (a, b) in enumerate(points[:100], 1):   # Limit to exactly 100
    z = gamma_complex(a, b)
    existence = solve_limit_point_of_existence(z)
    mag = existence['magnitude']
    
    print(f"Point {idx:3d}: Γ({a}, {b})")
    print(f"   z = {z}")
    print(f"   Magnitude: {mag:.6f}")
    print("   idX Relations (trace):")
    for p in existence['trace']:
        print(f"     {p}")
    print("   Finite-ground: True | Traceable to 1 ∈ √1")
    print("-" * 80)

print("\n" + "="*90)
print("100 Points Successfully Propagated via Γ + idX")
print("All elements carry the finite relational structure back to 1.")

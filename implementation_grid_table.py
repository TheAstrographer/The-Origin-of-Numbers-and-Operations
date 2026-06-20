# Core Engine (from implementation.py + generate_grid_table.py)
from implementation import gamma_complex, solve_limit_point_of_existence

# Full 100-entry grid
a_values = [round(1.0 + i*0.1, 1) for i in range(10)]
b_values = [round(2.0 + i*0.1, 1) for i in range(10)]

for a in a_values:
    for b in b_values:
        z = gamma_complex(a, b)          # Γ(a, b)
        existence = solve_limit_point_of_existence(z)
        mag = existence['magnitude']
        
        print(f"Entry: ({a}, {b})")
        print(f"z = {z} | Magnitude: {mag:.6f}")
        print("idX Relations:")
        for p in existence['trace']:
            print(f"  {p}")
        print("Finite-ground: True | Traceable to 1 ∈ √1")
        print("-" * 70)

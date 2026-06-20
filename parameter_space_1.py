# ==================
# PARAMETER SPACE 1
# ==================

import cmath

# Core definitions
i = complex(0, 1)          # √-1
zero = complex(0, 0)
one = complex(1, 0)

print("=== PARAMETER SPACE 1 ===")
print(f"1 ∈ √1 = {one} ⊆ (1, √1), (√1, 1), (1,1)")
print(f"1-1 = {one - one} ⊆ (1,-1), (0,1), (0,-1), (0,0)")

# Imaginary unit relations
print(f"√-1 = i = {i}")
print(f"Γ1/i = {-i} ⊆ (i,1), (1,i), (0,i)")
print(f"Γ-i/i = {-1} ⊆ (i,-1), (-1,i), (-i,-1), (-1,-i), (-1,0)")

# Complex operations
print(f"Γi+i = {i + i} ⊆ (i,i), (i,2*i), (2*i,0)")
print(f"i² = {i*i} ⊆ (i,i), (i,-1), (-1,0)")
print(f"Γ2i-i = {2*i - i} ⊆ (2*i, i), (i,i)")

# Identity function
def idX(x):
    """idX(x) ≔ x ∀x ∈ X"""
    return x

print("\n=== Identity & Set Relations ===")
X = one
print(f"idX({X}) = {idX(X)}")
print("X(x) ⊆ (X₁, Xᵢ), (x₁,xᵢ), (X,0), (x,0), (0,X), (0,x), (1,X), (1,x), ...")

# Complex number example
def gamma_complex(a, b):
    """Γa1+bi = z"""
    z = complex(a, b)
    return z

z = gamma_complex(1, 1)
print(f"Γ1+1i = {z} → gcd(p,q)=1 → ℕ ∈ ℤ ∈ ℚ ∈ ℝ → ℝ² = ℂ")

# Integer / Natural number increments
print("\n=== Integer Operations ===")
print(f"Γ1+1 = {1+1} ⊆ (1,1), (1,2), (2,0)")
print(f"Γ9+1 = {9+1} → Γ99+1 = {99+1}")
n = 99
print(f"n+1 : ({n},1) → (1, {n+1}) → ({n+1},0)")

# Subtraction
print(f"\nΓ1-2 = {1-2} ⊆ (1,-2), (2,-1), (-1,0)")
print(f"1-n : (1,n) → (-n, solution) → (solution,0)")

# Fraction demonstrations
print("\n=== Fraction Operations ===")
fractions = [
    (2, 0.5),
    (3, 1/3),
    (4, 0.25),
    (5, 0.2),
    (6, 1/6),
    (7, 1/7),
    (8, 0.125),
    (9, 1/9),
    (10, 0.1)
]

for d, val in fractions:
    print(f"Γ1/{d} = {val} ⊆ (1,{d}), ({d},{val}), ({val},0)")

# Reciprocal examples
print(f"\nΓ1/.5 = {1/0.5} ⊆ (1,0.5), (0.5,2), (2,0)")
print(f"Γ1/.999999999 ≈ {1/0.999999999:.10f} ⊆ (1,.999999999), (.999999999,1.000000001), (1.000000001,0)")

# Complex verification block
print("\n=== Complex Verification ===")
print(f"i * i = {i*i} (should be -1)")
print(f"1/i = {1/i}")
print(f"i + i = {i+i}")
print(f"2i - i = {2*i - i}")

print("\n=== End of Parameter Space 1 Execution ===")

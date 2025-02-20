import cmath

def solve_linear(a, b):
    if a == 0:
        return "Az egyenletnek nincs megoldása, mivel a = 0."
    else:
        return -b / a

def solve_quadratic(a, b, c):
    d = cmath.sqrt(b**2 - 4*a*c)
    root1 = (-b + d) / (2*a)
    root2 = (-b - d) / (2*a)
    return root1, root2

def main():
    equation_type = input("Milyen féle egyenletet oldjak meg? (1: elsőfokú, 2: másodfokú): ")

    if equation_type == "1":
        equation = input("Írja be az egyenletet (pl. 2x+3=0): ").replace(" ", "")
        parts = equation.split('x')
        a = float(parts[0])
        b = float(parts[1].replace('=', '').replace('0', ''))
        result = solve_linear(a, b)
        print(f"Az egyenlet megoldása: {result}")

    elif equation_type == "2":
        equation = input("Írja be az egyenletet (pl. 1x^2+2x+1=0): ").replace(" ", "")
        parts = equation.split('x')
        a = float(parts[0].replace('^2', ''))
        b = float(parts[1].replace('^2', '').replace('=', '').replace('0', ''))
        c = float(parts[2].replace('=', '').replace('0', ''))
        roots = solve_quadratic(a, b, c)
        print(f"Az egyenlet gyökei: {roots[0]} és {roots[1]}")

    else:
        print("Azt kell megadni hogy 1. vagy 2.")

    print("Viszlát!")

if __name__ == "__main__":
    main()

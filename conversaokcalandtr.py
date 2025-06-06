def kcalh_para_tr(kcal_h):
    # Fator de conversão fornecido
    fator = 0.000330693393277316
    tr = kcal_h * fator
    return tr

# Exemplo de uso
kcal_h = float(input("Digite o valor em kcal/h: "))
resultado = kcalh_para_tr(kcal_h)
print(f"{kcal_h} kcal/h equivalem a {resultado:.6f} TR")


# Exemplo de uso
# kcal_h = 1000 # resultado = kcalh_para_tr(kcal_h)
# print(f"{kcal_h} kcal/h equivalem a {resultado:.6f} TR")
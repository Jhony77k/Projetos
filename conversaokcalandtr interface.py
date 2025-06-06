def kcalh_para_tr(kcal_h):
    # Etapas da conversã:
    # 1 kcal/h -> 1 / 0.859845227859 Watt
    watt_por_kcalh = 1 / 0.859845227859  # Conversão de kcal/h para Watt
    
    # 1 Watt -> 0.000284345136094 TR
    
    tr_por_watt = 0.000284345136094  # Conversão de Watt para TR
    
    # Conversão: kcal/h → Watt → TR
    tr = kcal_h * watt_por_kcalh * tr_por_watt
    return tr

# Exemplo de uso
kcal_h = float(input("Digite o valor em kcal/h: "))  # Usuário entra com a quantidade de kcal/h
resultado = kcalh_para_tr(kcal_h)  # Realiza a conversão
print(f"{kcal_h} kcal/h equivalem a {resultado:.6f} TR")  # Mostra o resultado em TR



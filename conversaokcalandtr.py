def kcalh_para_tr(kcal_h):
    
    watt_por_kcalh = 1 / 0.859845227859  
    tr_por_watt = 0.000284345136094 
    tr = kcal_h * watt_por_kcalh * tr_por_watt
    return tr

kcal_h = float(input("Digite o valor em kcal/h: ")) 
resultado = kcalh_para_tr(kcal_h) 
print(f"{kcal_h} kcal/h equivalem a {resultado:.6f} TR")  



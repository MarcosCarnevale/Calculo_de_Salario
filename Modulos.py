# Def de input obrigatório de valor
def askint(msg):
    while True:
        try:
            val = float(input(msg))
        except:
            print ("Você não digitou um número!")
            continue
        else:
            print ("Valor gravado")
            break
    return  val

# Def calculo INSS
def inss (val):
    if val <= 1751.81:
        x = 0.08

    elif val > 1751.81 and val <= 2919.72:
        x = 0.09

    elif val > 2919.72 and val <= 5839.45:
        x = 0.11

    elif val > 5839.45:
        x = 0.11
    else:
        x = 0
    return float(val) * x if val <=5839.45 else 5839.45 * 0.11

def aliq_irrf (val):
    if val <= 1903.98:
        x = 0
    elif val > 1903.98 and val <= 2826.65:
        x = 0.075
    elif val > 2826.65 and val <= 3751.05:
        x = 0.15
    elif val > 3751.05 and val <= 4664.48:
        x = 0.225
    else:
        x = 0.275
    return float(x)





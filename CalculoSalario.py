import Modulos as md



nome = input("Bem vindo! Para uma melhor experiência me informe seu nome.")
print('Bem vindo '+nome.capitalize()+', vamos começar!')

salario = md.askint('Utilize "." (Ponto) para separação das casas decimais \nInforme seu salario bruto: ')


#Calculo aliquota INSS
inss = md.inss(salario)

#Base IRRF
base_irrf = salario - inss

aliq_irrf = md.aliq_irrf(base_irrf)

#Dedução IRRF
if aliq_irrf == 0.0:
    deducao_irrf = 0
elif aliq_irrf == 0.075:
    deducao_irrf = 142
elif aliq_irrf == 0.15:
    deducao_irrf = 354.80
elif aliq_irrf == 0.225:
    deducao_irrf = 636.13
else:
    deducao_irrf = 869.36
#IRRF
irrf =((base_irrf * aliq_irrf)-deducao_irrf)

#Desconto de VT

resp_desc_vt = str.lower(input('Há desconto  de Vale transporte? Y/N'))

while (resp_desc_vt!= 'y' and resp_desc_vt!= 'n'):
    resp_desc_vt = (input('Selecione um dos valores validos entre Y/N'))

#Validar resposta
if resp_desc_vt == 'y':
    desc_vt = salario * 0.06
else:
    desc_vt = 0

#Assistencia Medica

resp_desc_am = str.lower(input('Há desconto de Assistencia Médica? Y/N'))
while (resp_desc_am!= 'y' and resp_desc_am!= 'n'):
    resp_desc_am = (input('Selecione um dos valores validos entre Y/N'))


if resp_desc_am == 'y':
    resp_depend_am = str.lower(input('Há dependentes no plano? Y/N'))
    while (resp_depend_am!='y' and resp_depend_am!='n'):
        resp_depend_am = (input('Selecione um dos valores validos entre Y/N'))

    if resp_depend_am == 'y':
        qtd_pess_plano_am = int(md.askint('Quantos dependentes?'))+1
        print('Quantidade de pessoas no plano, incluindo você: '+ str(qtd_pess_plano_am))

        vlr_plano_am = md.askint('Indique o valor do plano')
        

    else:
        qtd_pess_plano_am = 1
        vlr_plano_am = 0

#-------------------------------------------------------------------------------------------------------------


# Assistencia Odontologica

resp_desc_ao = str.lower(input('Há desconto de Assistencia Odondologica? Y/N'))
while (resp_desc_ao != 'y' and resp_desc_ao != 'n'):
    resp_desc_ao = (input('Selecione um dos valores validos entre Y/N'))

if resp_desc_ao == 'y':
    resp_depend_ao = str.lower(input('Há dependentes no plano? Y/N'))
    while (resp_depend_ao!= 'y' and resp_depend_ao!= 'n'):
        resp_depend_ao = (input('Selecione um dos valores validos entre Y/N'))

    if resp_depend_ao == 'y':
        qtd_pess_plano_ao = int(md.askint('Quantos dependentes?')) + 1
        print(qtd_pess_plano_ao)

        vlr_plano_ao = md.askint('Indique o valor do plano')
        print(vlr_plano_ao)

    else:
        qtd_pess_plano_ao = 1
        vlr_plano_am = 0

#-----------------------------------------------------------------------------------------------------------

#Desconto VR
resp_desc_vr = str.lower(input('Há desconto de Vale Refeição? Y/N'))
while (resp_desc_vr!= 'y' and resp_desc_vr!= 'n'):
    resp_desc_vr = (input('Selecione um dos valores validos entre Y/N'))
if resp_desc_vr == 'y':
    desc_vr = md.askint('Indique o valor de desconto do VR:')
else:
    desc_vr = 0

desc_plano_am = (qtd_pess_plano_am * vlr_plano_am)
desc_plano_ao = (qtd_pess_plano_ao * vlr_plano_ao)

salario_liquido = salario - inss - irrf - desc_vt - desc_vr - desc_plano_am - desc_plano_ao

print('Salario Bruto'+((40-len('Salario Bruto'))*'-')+str(salario))
print('Desc INSS'+((40-len('Desc INSS'))*'-')+str(inss))
print('Desc IRRF'+((40-len('Desc IRRF'))*'-')+str(irrf))
print('Desc VT'+((40-len('Desc VT'))*'-')+str(desc_vt))
print('Desc AM'+((40-len('Desc AM'))*'-')+str(desc_plano_am))
print('Desc AO'+((40-len('Desc AO'))*'-')+str(desc_plano_ao))
print('Salario liquido'+((40-len('salario liquido'))*'-')+str(salario_liquido))




fusca_azul = 201
fusca_preto = 200
fuscas_em_igualdade = fusca_azul == fusca_preto

print(fusca_azul , "fuscas azuis.")
print(fusca_preto , "fuscas pretos.")

if fuscas_em_igualdade:
    print("O mundo está em paz, tudo está muito bom.")

def dif_fuscas(fusca_azul, fusca_preto):

    if fusca_azul > fusca_preto:
            fuscas_a_menos = fusca_azul - fusca_preto
            #print(f"Temos {fuscas_a_menos} fuscas pretos a menos que fuscas azuis.")
            return f"Temos {fuscas_a_menos} fuscas azuis a menos que fuscas_pretos."
        
    elif fusca_azul < fusca_preto:
            fuscas_a_menos = fusca_preto - fusca_azul
            #print(f"Temos {fuscas_a_menos} fuscas azuis a menos que fuscas_pretos.")
            return f"Temos {fuscas_a_menos} fuscas azuis a menos que fuscas_pretos."

#resultado = dif_fuscas(fusca_azul, fusca_preto)
#print(resultado)
    
print(dif_fuscas(fusca_azul, fusca_preto))

if fusca_azul != fusca_preto:  #Esta condição deve ser verdadeira para rodar o código.
    dif_fuscas(fusca_azul, fusca_preto)

    if fusca_azul < fusca_preto or fusca_azul > fusca_preto:    #Se uma dessas condições for verdadeira, ele roda o código abaixo.
        print("Os fuscas devem estar em equilíbrio, se não o mundo acaba.") 

if fusca_preto == 0 and fusca_azul == 0:    #Se essas duas condições não forem satisfeitas o código não roda.
    print("Fabriquem fuscas imediatamente.")   

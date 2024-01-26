fusca_azul = 200
fusca_preto = 12
fuscas_em_igualdade = None

if fusca_azul == fusca_preto and fusca_azul != None and fusca_preto != None:
    fuscas_em_igualdade = True

else:
    fuscas_em_igualdade = False

print(fusca_azul , "fuscas azuis.")
print(fusca_preto , "fuscas pretos.")

if fuscas_em_igualdade == True:
    print("O mundo está em paz, tudo está muito bom.")

else:

    def dif_fuscas(fusca_azul, fusca_preto):

        if fusca_azul > fusca_preto:
            fuscas_a_menos = fusca_azul - fusca_preto
            print(f"Temos {fuscas_a_menos} fuscas pretos a menos que fuscas azuis.")
        
        if fusca_azul < fusca_preto:
            fuscas_a_menos = fusca_preto - fusca_azul
            print(f"Temos {fuscas_a_menos} fuscas azuis a menos que fuscas_pretos.")

    if fusca_azul != fusca_preto:  #Esta condição deve ser verdadeira para rodar o código.
        dif_fuscas(fusca_azul, fusca_preto)

    if fusca_azul < fusca_preto or fusca_azul > fusca_preto:    #Se uma dessas condições for verdadeira, ele roda o código abaixo.
        print("Os fuscas devem estar em equilíbrio, se não o mundo acaba.") 

    if fusca_preto == 0 and fusca_azul == 0:    #Se essas duas condições não forem satisfeitas o código não roda.
        print("Fabriquem fuscas imediatamente.")

    
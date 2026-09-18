# Solicita o tipo de imóvel
tipo_imovel = input("Digite o tipo de imóvel (1 - comercial, 2 - casa, 3 - apartamento): ")

# Solicita o consumo mensal de água
consumo_mensal_m3 = float(input("Digite o consumo mensal de água em metros cúbicos (m³): "))

# Classifica o consumo de acordo com o tipo de imóvel
match tipo_imovel:
    case "1" | "comercial" | "Comercial" | "COMERCIAL":
        print(f"Seu consumo mensal de água é de {consumo_mensal_m3:.2f} m³. Tarifa comercial aplicada - consulte o plano corporativo.")

    case "3" | "apartamento" | "Apartamento" | "APARTAMENTO":
        if consumo_mensal_m3 < 10:
            print(f"Seu consumo mensal de água é de {consumo_mensal_m3:.2f} m³. Consumo econômico - excelente controle de água!")
        elif consumo_mensal_m3 <= 25:
            print(f"Seu consumo mensal de água é de {consumo_mensal_m3:.2f} m³. Consumo moderado - dentro do padrão residencial.")
        else:
            print(f"Seu consumo mensal de água é de {consumo_mensal_m3:.2f} m³. Consumo excessivo - adote medidas de economia e verifique vazamentos.")

    case "2" | "casa" | "Casa" | "CASA":
        if consumo_mensal_m3 <= 25:
            print(f"Seu consumo mensal de água é de {consumo_mensal_m3:.2f} m³. Consumo moderado - dentro do padrão residencial.")
        else:
            print(f"Seu consumo mensal de água é de {consumo_mensal_m3:.2f} m³. Consumo excessivo - adote medidas de economia e verifique vazamentos.")

    case _:
        print("Tipo de imóvel inválido.")

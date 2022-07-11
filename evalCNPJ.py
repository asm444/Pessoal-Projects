def validar_cnpj(cnpj):
    teste = False
    a = None

    cnpj = list(cnpj)

    for i in range(len(cnpj)):
        try:
            a = int(cnpj[i])
        except:
            teste = True

    if teste:
        CNPJ = []

        for i in range(len(cnpj)):
            try:
                CNPJ.append(int(cnpj[i]))
            except:
                continue
    else:
        CNPJ = cnpj

    pd = CNPJ[-2]
    sd = CNPJ[-1]
    first = [5,4,3,2,9,8,7,6,5,4,3,2]
    second = [6,5,4,3,2,9,8,7,6,5,4,3,2]

    multiplicar = [CNPJ[i]*first[i] for i in range(len(CNPJ[:-2]))]
    validar_pd = 11 - sum(multiplicar)%11

    if validar_pd>9:
        validar_pd = 0

    if pd != validar_pd:
        return False
    
    multiplicar = [CNPJ[i]*second[i] for i in range(len(CNPJ[:-1]))]
    validar_sd = 11 - sum(multiplicar)%11

    if validar_sd>9:
        validar_sd = 0

    if sd != validar_sd:
        return False
    else:
        return True

while True:
    cnpj = input("Digite o cnpj para validação: ")
    if validar_cnpj(cnpj) == True:
        print("CNPJ é válido!")
    else:
        print("CNPJ não é válido!")

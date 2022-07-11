# Sistema de Inscrições para a XXVII Semanade da Física

# Apresentação do Sistema de Inscrições para a XXVII Semanade da Física

from os.path import isfile
from tkinter.messagebox import NO

def inscrito_new(nome, email,matricula, curso, grade, instituicao, publico, data_de_inscricao, estado): 
        
        inscrito = dict()
        inscrito['nome'] = nome.title() #Deixando a primeira letra de cada nome em maiúscula
        inscrito['email'] = email
        inscrito['matricula'] = matricula
        inscrito['curso'] = curso.title()
        inscrito['grade'] = grade.title()
        inscrito['instituicao'] = instituicao
        inscrito['publico'] = publico
        inscrito['data_de_inscricao'] = data_de_inscricao
        inscrito['estado'] = estado
        
        if len(matricula) != 12:
            print("Matrícula inválida!")
            inscrito['matricula'] = input("Matrícula: ")

        return inscrito
    
def Registro():     
               
    if isfile("inscricoes.csv"):
        from pandas import read_csv
        from pandas import DataFrame
            
        df = read_csv("inscricoes.csv")
            
        database = DataFrame(df)
        inscritos = list()
            
        for nome, email, matricula, curso, grade,instituicao, publico, data_de_inscricao, estado in zip(database['nome'],
                                                                                                  database['email'],
                                                                                                  database['matricula'],
                                                                                                  database['curso'],
                                                                                                  database['grade'],
                                                                                                  database['instituicao'],
                                                                                                  database['publico'],
                                                                                                  database['data_de_inscricao'],
                                                                                                  database['estado']):            
            inscritos.append(inscrito_new(nome,
                                          email,
                                          matricula,
                                          curso,
                                          grade,
                                          instituicao,
                                          publico,
                                          data_de_inscricao,
                                          estado))
    if isfile("inscricoes.txt"):
        with open('inscricoes.txt','r+') as file:
            inscritos = file.readlines()
            file.close()
            inscritos = [ inscrito.split(" ") for inscrito in inscritos ]
            inscritos = [ inscrito_new(inscrito[0],
                                       inscrito[1],
                                       inscrito[2],
                                       inscrito[3],
                                       inscrito[4],
                                       inscrito[5],
                                       inscrito[6],
                                       inscrito[7],
                                       inscrito[8],
                                       inscrito[9]) for inscrito in inscritos ]
                  
    else:
        inscritos = list()
        
    return inscritos

inscritos = Registro ()
        
def inscrever(manual= False):
    if manual==False:
        manual = input("Deseja registrar uma inscrição manualmente? (S/N) ") == "S"
    elif manual:
        nome = input("Nome: ")
        email = input("Email: ")
        matricula = input("Matrícula: ")
        curso = input("Curso: ")
        grade = input("Grade: ")
        instituicao = input("Instituição: ")
        publico = input("Publico: ")
        data_de_inscricao = input("Data de inscrição: ")
        estado = input("Estado: ")

        subscribe = inscrito_new(nome,
                    email,
                    matricula,
                    curso,
                    grade,
                    instituicao,
                    publico,
                    data_de_inscricao,
                    estado)
        
        mostrar_inscrito(subscribe)
        print("Inscrição realizada com sucesso!")
        
        return subscribe
    else:
        input("Inscrição não realizada!")
        
def mostrar_inscrito(inscrito):
    print("----------------------------------------------------")
    print("Nome: ", inscrito['nome'])
    print("Email: ", inscrito['email'])
    print("Matrícula: ", inscrito['matricula'])
    print("Curso: ", inscrito['curso'])
    print("Grade: ", inscrito['grade'])
    print("Instituição: ", inscrito['instituicao'])
    print("Publico: ", inscrito['publico'])
    print("Data de inscrição: ", inscrito['data_de_inscricao'])
    print("Estado: ", inscrito['estado'])
    print("----------------------------------------------------")          
        
def consultar(acionado = [], inscritos = inscritos):
    opcoes = [n for n in range(1,11) if n not in acionado]
        
    #Criando um buscador de inscrições 
    print("Opcões de consulta:")
    if 1 in opcoes:
        print("1 - Consultar por nome")
    elif 2 in opcoes:
        print("2 - Consultar por matrícula")
    elif 3 in opcoes:
        print("3 - Consultar por curso")
    elif 4 in opcoes:
        print("4 - Consultar por grade")
    elif 5 in opcoes:
        print("5 - Consultar por instituição")
    elif 6 in opcoes:
        print("6 - Consultar por publico")
    elif 7 in opcoes:
        print("7 - Consultar por estado")
    elif 8 in opcoes:
        print("8 - Consultar por data de inscrição")
    elif 9 in opcoes:
        print("9 - Consultar por todas as inscrições")
    else:
        print("10 - Voltar")
        opcaoo = input("\n\nDigite a opção desejada: ")
        opcaoo = int(opcaoo)
        
    if opcaoo == 10:
        input("Pressione ENTER para sair.")
        exit()
            
    if len(acionado)==0:   
        opcoes = list(range(1,11))
        
    elif len(inscritos) == 0:
        print("Não há inscrições registradas.")
        input("Pressione ENTER para continuar.")
        return
        
    elif opcaoo == 9:
            
        for inscrito in inscritos:
            mostrar_inscrito(inscrito)
                
        print("Total de inscrições: ", len(inscritos))
        pago = len([inscrito for inscrito in inscritos if inscrito['estado'] == "Pago"])
        print("Inscritos com estado Pago: ", pago )
    
        print("Inscritos com estado Não Pago: ", len(inscritos) - pago)
            
        print("Inscritos graduandos: ", len([inscrito for inscrito in inscritos if inscrito['grade'] == "Graduando"]))
        print("Inscritos posgraduandos: ", len([inscrito for inscrito in inscritos if inscrito['grade'] == "Posgraduando"]))
        print("Inscritos professores: ", len([inscrito for inscrito in inscritos if inscrito['grade'] == "Professor"]))
        print("Inscritos servidores: ", len())
        print("Para mais detalhes use opcao Analise.")
            
    else:      
        opcoes_dic = { 1:"Nome",
                       2:"Email",
                       3:"Matricula",
                       4:"Curso",
                       5:"Grade",
                       6:"Instituicao",
                       7:"Publico",
                       8:"Data de inscrição",
                       9:"Estado"}
            
        acionado.append(opcao)
        opcoes.remove(opcao)
            
        inscritos = [inscritos[n] for n in len(inscritos) if inscrito[n] == inscrito[opcoes_dic[opcao]]]
            
        for inscrito in inscritos:
            mostrar_inscrito(inscrito)
                
        if len(inscritos)== 0:
            print("Nenhum resultado encontrado.")
            opcaoo = input("Gostaria de uma nova busca?(S/N) ")
                
            if opcaoo.upper()=='S':
                print('\n\n\n')
                consultar()
            else:
                input("Pressione ENTER para sair.")
                exit()
            
        elif len(inscritos) > 1:
            print("Há ",len(inscritos)," resultados.")
            for inscrito in inscritos:
                mostrar_inscrito(inscrito)
                    
            filtrar = input("Deseja filtrar o resultado?(S/N) ")
                
            if filtrar.upper()=='S':
                print('\n\n\n')
                consultar(acionado, inscritos)
            else:
                input("Pressione ENTER para sair.")
                exit()
                
        else:
            print("\n\n\n")
            mostrar_inscrito(inscritos[0])
            
            opcaoo = input("Deseja alterar a inscrição?(S/N) ") == 'S'
            
            if opcaoo:
                for chaves in inscritos[0].keys:
                    opcaoo = input("Deseja alterar o campo " + chaves + "?(S/N) ") == 'S'
                    if opcaoo:
                        inscritos[0][chaves] = input("Digite o novo valor: ")
            
                print("\n\n\n")
                print("Inscrição alterada com sucesso.")
                mostrar_inscrito(inscritos[0])
                
                return inscritos[0]
            
            else:
                input("Pressione ENTER para continuar.")
                return

print("Bem-vindo ao Sistema de Inscrições para a XXVII Semanade da Física")
print("Opções:")
print("1 - Inscrever-se") # Possui uma atualização de inscrição
print("2 - Consultar inscrições") # v
print("3 - Atualizar dados") # falta
print("4 - Sair") # v

opcao = None
while opcao != '4':
    opcao = input("\n\nDigite a opção desejada: ")

    if opcao == '1':
        inscrito_novo = inscrever(manual=True)
        if inscrito_novo["matricula"] not in inscritos:
            if inscrito_novo["email"] not in inscritos:
                if inscrito_novo["nome"] not in inscritos:
                    inscritos.append(inscrito_novo)
                    inscrito_encontrado, info = None, None
                else:
                    inscrito_encontrado = [inscrito for inscrito in inscritos if inscrito["nome"] == inscrito_novo["nome"]][0]
                    info = 'nome'
            else:
                inscrito_encontrado = [inscrito for inscrito in inscritos if inscrito["email"] == inscrito_novo["email"]][0]
                info = 'email'        
        else:
            inscrito_encontrado = [inscrito for inscrito in inscritos if inscrito["matricula"] == inscrito_novo["matricula"]][0]
            info = 'matricula'
        
            mostrar_inscrito(inscrito_encontrado)
            print("\n\n\n")
            print('Inscrição já existente.')
    
            opcao = input("Deseja alterar a inscrição?(S/N) ") == 'S'
            
            if opcao:
                for chaves in inscritos[0].keys:
                    opcao = input("Deseja alterar o campo " + chaves + "?(S/N) ") == 'S'
                    if opcao:
                        inscritos[0][chaves] = input("Digite o novo valor: ")
            
                    print("\n\n\n")
                    print("Inscrição alterada com sucesso.")
                    mostrar_inscrito(inscritos[0])
                
                    for i in len(inscritos):
                        if inscritos[i][info]==inscrito_encontrado:
                            inscritos[i] = inscrito[0]
                      
    if opcao == '2':
        backup = inscritos
        consultar(inscritos=inscritos)

    if opcao == '3':
        pass

    if opcao == '4':
        with open('inscritos.txt','w') as file:
            for inscrito in backup:
                file.write(str(inscrito['nome']) + ' ' + str(inscrito['email']) + ' ' + str(inscrito['matricula']) + ' ' + str(inscrito['curso']) + ' ' + str(inscrito['grade']) + ' ' + str(inscrito['instituicao']) + ' ' + str(inscrito['publico']) + ' ' + str(inscrito['data_inscricao']) + ' ' + str(inscrito['estado']) + '\n')
            
        file.close()
        input("Os dados foram salvos com sucesso. Pressione ENTER para sair.")

publico = ['graduandos',
            'pós-graduandos',
            'professor',
            'servidor',
            'externo']

grade = ['Bacharelado',
         'Licenciatura',
         'Mestrado',
         'Doutorado']

registro = ['nome',
            'email',
            'matricula',
            'curso',
            'grade',
            'instituicao',
            'tipo_de_inscricao',
            'data_de_inscricao',
            'estado']              
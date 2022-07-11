# Sistema de Inscrições para a XXVII Semanade da Física

# Apresentação do Sistema de Inscrições para a XXVII Semanade da Física

from os.path import isfile


print("Bem-vindo ao Sistema de Inscrições para a XXVII Semanade da Física")
print("Opções:")
print("1 - Inscrever-se")
print("2 - Consultar inscrições")
print("3 - Atualizar dados")
print("4 - Atualizar uma inscrição")
print("5 - Sair")

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

def inscrito(nome, email,matricula, curso, grade, instituicao, publico, data_de_inscricao, estado): 
        
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
            inscritos.append(inscritos(nome,
                                       email,
                                       matricula,
                                       curso,
                                       grade,
                                       instituicao,
                                       publico,
                                       data_de_inscricao,
                                       estado))
    else:
        inscritos = list()
        
    return inscritos

inscritos = Registro ()
        
def inscrever(self):
        
    manual = input("Deseja registrar uma inscrição manualmente? (S/N) ")
        
    if manual.upper()=="S":
        nome = input("Nome: ")
        email = input("Email: ")
        matricula = input("Matrícula: ")
        curso = input("Curso: ")
        grade = input("Grade: ")
        instituicao = input("Instituição: ")
        publico = input("Publico: ")
        data_de_inscricao = input("Data de inscrição: ")
        estado = input("Estado: ")
            
        return inscrito(nome,
                        email,
                        matricula,
                        curso,
                        grade,
                        instituicao,
                        publico,
                        data_de_inscricao,
                        estado)
            
    else:
        input("As inscrições serão registradas automaticamente. Pressione ENTER para continuar.")
            
        from pandas import read_csv
        from pandas import DataFrame
            
        df = read_csv("inscricoes.csv")
            
        database = DataFrame(df)
            
        inscritos = list()
  
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
        
def consultar(self,acionado = [], inscritos = inscritos):
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
        opcao = input("\n\nDigite a opção desejada: ")
        opcao = int(opcao)
    if opcao == 10:
        input("Pressione ENTER para sair.")
        exit()
            
    if len(acionado)==0:   
        opcoes = list(range(1,11))
        
    elif len(inscritos) == 0:
        print("Não há inscrições registradas.")
        input("Pressione ENTER para continuar.")
        return
        
    elif opcao == 9:
        inscritos = self.inscritos
            
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
            opcao = input("Gostaria de uma nova busca?(S/N) ")
                
            if opcao.upper()=='S':
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
                consultar(self, acionado, inscritos)
            else:
                input("Pressione ENTER para sair.")
                exit()
                    
# Sistema de Inscrições para a XXVII Semanade da Física

# Apresentação do Sistema de Inscrições para a XXVII Semanade da Física

from os.path import isfile


print("Bem-vindo ao Sistema de Inscrições para a XXVII Semanade da Física")
print("Opções:")
print("1 - Inscrever-se")
print("2 - Consultar inscrições")
print("3 - Atualizar dados")
print("4 - Sair")

class Registrations:
    
    publico = ['graduandos',
               'pós-graduandos',
               'professor',
               'servidor',
               'externo']
    
    registro = ['nome',
                'email',
                'matricula',
                'curso',
                'instituicao',
                'tipo_de_inscricao',
                'data_de_inscricao',
                'estado']
    
    def inscrito(nome, email,matricula, curso, instituicao, publico, data_de_inscricao, estado): 
        
        inscrito = dict()
        inscrito['nome'] = nome.title() #Deixando a primeira letra de cada nome em maiúscula
        inscrito['email'] = email
        inscrito['matricula'] = matricula
        inscrito['curso'] = curso.title()
        inscrito['instituicao'] = instituicao
        inscrito['publico'] = publico
        inscrito['data_de_inscricao'] = data_de_inscricao
        inscrito['estado'] = estado
        
        if len(matricula) != 12:
            print("Matrícula inválida!")
            inscrito['matricula'] = input("Matrícula: ")

        return inscrito
    
    def __init__(self):
        
        if isfile("cursos.txt"):
            with open("cursos.txt", "r") as f:
                cursos = f.readlines()
                f.close()
                
            self.cursos = set(cursos)
            
        elif isfile("inscricoes.csv"):
            from pandas import read_csv
            from pandas import DataFrame
            
            df = read_csv("inscricoes.csv")
            
            database = DataFrame(df)
            inscritos = list()
            
            for nome, email, matricula, curso, instituicao, publico, data_de_inscricao, estado in zip(database['nome'],
                                                                                                      database['email'],
                                                                                                      database['matricula'],
                                                                                                      database['curso'],
                                                                                                      database['instituicao'],
                                                                                                      database['publico'],
                                                                                                      database['data_de_inscricao'],
                                                                                                      database['estado']):
                
                cursos.add(curso)
                
                inscritos.append(inscritos(nome,
                                           email,
                                           matricula,
                                           curso,
                                           instituicao,
                                           publico,
                                           data_de_inscricao,
                                           estado))
            self.inscritos = inscritos
        
    def inscrever(self):
        
        manual = input("Deseja inscrever manualmente? (S/N) ")
        
        if manual:
            nome = input("Nome: ")
            email = input("Email: ")
            matricula = input("Matrícula: ")
            curso = input("Curso: ")
            instituicao = input("Instituição: ")
            publico = input("Publico: ")
            data_de_vencimento = input("Data de Vencimento: ")
            estado = input("Estado: ")
            
            return Registrations.inscrito(nome,
                            email,
                            matricula,
                            curso,
                            instituicao,
                            publico,
                            data_de_vencimento,
                            estado)
            
        else:
            from pandas import read_csv
            from pandas import DataFrame
            
            df = read_csv("inscricoes.csv")
            
            database = DataFrame(df)
            
            inscritos = list()
            
        
    def consultar(self):
        
        #Criando um buscador de inscrições
        
        print("Opcões de consulta:")
        print("1 - Consultar por nome")
        print("2 - Consultar por matrícula")
        print("3 - Consultar por curso")
        print("4 - Consultar por instituição")
        print("5 - Consultar por tipo de inscrição")
        print("6 - Consultar por data de inscrição")
        
        
        
    
    def atualizar_cadastro(self):
        manual = input("Deseja atualizar manualmente? (S/N) ")
        if manual:
            self.nome = input("Nome: ")
            self.email = input("Email: ")
            self.curso = input("Curso: ")
            self.instituicao = input("Instituição: ")
            self.tipo_de_inscricao = input("Tipo de Inscrição: ")
            self.data_de_inscricao = input("Data de Inscrição: ")
            self.estado = input("Estado: ")
        else:
            from pandas import read_csv
            from pandas import DataFrame
    
            df = read_csv("inscricoes.csv")
    
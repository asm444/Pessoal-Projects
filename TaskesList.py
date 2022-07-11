"""Criei para aprender a colocar e retirar objetos em lista na mesma ordem, bem simples para ter um feedback visual do que está acontecendo. Revisão de python. """
desfazer = []

tarefas = []

def adicionar(tarefas):
    tarefa = input("Anote a tarefa: ")
    tarefas.append(tarefa)

def desfaz(tarefas):
    desfazer.append(tarefas[-1])
    tarefas.remove(tarefas[-1])

def faz(tarefas):
    tarefas.append(desfazer[-1])
    desfazer.remove(desfazer[-1])

def lista_de_tarefas(tarefas):
    print("\n\nLista de tarefas")
    for i in range(len(tarefas)):
        print(f'{1+i} - {tarefas[i]}')
exe = None

while True:
    print("\n"*3 +"\tOpções:\n1 - Adicionar uma Tarefa.\n2 - Listar as tarefas adicionadas.\n3 - Desfazer a última tarefa.\n4 - Voltar a tarefa desfeita.")
    opcao = input("Digite uma opção: ")
    
    if opcao == '1':
        adicionar(tarefas)
    if opcao == '2':
        lista_de_tarefas(tarefas)
    if opcao == '3' and len(tarefas) != 0:
        desfaz(tarefas)
    if opcao == '4' and len(desfazer)!=0:
        faz(tarefas)
        
    

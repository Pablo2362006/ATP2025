[TurmaApp.py](https://github.com/user-attachments/files/23098563/TurmaApp.py)
import Turma as t
turma=[]
res=1
while res!= 0:
    res=t.menu()
    if res == 1:
        t.criarTurma(turma)
        print ("A turma foi criada vazia")
    elif res == 2:
        t.inserirAluno(turma)
    elif res == 3:
        if len(turma)==0:
            print("A lista esta vazia")
        else:    
            t.listarTurma(turma)
    elif res == 4:
        if len(turma)==0:
            print("A lista esta vazia")
        else:    
            t.consultarAluno(turma, input("Introduza o id do aluno"))
    elif res == 8:
        if len(turma)==0:
            print("A lista esta vazia")
        else:    
            t.guardarTurma(turma, input("Introduz o Nome do ficheiro (.txt)"))  
    elif res == 9:
        t.carregarTurma(turma, input("Introduz o Nome do ficheiro (.txt)") )
    else:
        res=0
    

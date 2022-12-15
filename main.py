from Disciplina import Disciplina
from Professor import Professor
from conexaoDB import ConexaoDB
from Funcionario import Funcionario
from Aluno import Aluno
from Curso import Curso


handleWhile = True
while handleWhile:

    handleOption = int(
        input("Deseja 1-Cadastrar, 2-Vizualizar, 3-Deletar, 4-realizar um update? ou 5-Encerrar: ")
    )

    if handleOption == 1:
        select = int(
            input(
                "Deseja cadastrar um 1-Aluno, 2-Professor, 3-Curso ou 4-Disciplina?: "
            )
        )
    if handleOption == 2:
        select = int(
            input(
                "Deseja Vizualizar um 1-Aluno, 2-Professor, 3-Curso ou 4-Disciplina?: "
            )
        )
    if handleOption == 3:
        select = int(
            input("Deseja Deletar um 1-Aluno, 2-Professor, 3-Curso ou 4-Disciplina?: ")
        )
    if handleOption == 4:
        select = int(
            input(
                "Deseja realizar um update em um 1-Aluno, 2-Professor, 3-Curso ou 4-Disciplina?: "
            )
        )
    if handleOption == 5:
       break

    if select == 1:
        openDataBase = ConexaoDB()
        openDataBase.conectar()
        aluno = Aluno
        if handleOption == 1:
            # CADASTRO
            nome = input("Digite o nome do aluno: ")
            matricula = input("Digite sua matricula: ")
            cpf = input("Digite o seu cpf: ")
            curso = input("Digite o seu curso: ")
            aluno = Aluno(nome, matricula, cpf, curso)
            aluno.cadastrar()

        if handleOption == 2:
            # VIZUALIZAR
            openDataBase.executarDQL("select * from aluno")
            aluno.consultar

        if handleOption == 3:
            # DELETE
            cpfDelete = input("Digite o cpf do aluno que deseja deletar: ")

            aluno.excluir(cpfDelete)
        if handleOption == 4:
            # UPDATE
            cpfUpdate = input("Digite o cpf do aluno que deseja realizar o update: ")
            nomeUpdate = input("Digite o novo nome do aluno: ")
            aluno.alterar(nomeUpdate, cpfUpdate)

    if select == 2:
        openDataBase = ConexaoDB()
        openDataBase.conectar()
        professor = Professor
        tecOrProf = int(input("Deseja cadastrar um 1-Professor ou um 2-Tecnico?: "))
        funcionario = Funcionario
        if tecOrProf == 1:
            if handleOption == 1:
                nome = input("Digite o nome do professor: ")
                endereco = input("Digite seu endereco: ")
                telefone = input("Digite o seu telefone: ")
                cpf = input("Digite seu cpf: ")
                salario = input("Digite seu salario: ")
                titulacao = input("Digite sua titulação: ")
                formacao = input("Digite sua Area de formação: ")

                professor = Professor(
                    nome, endereco, telefone, cpf, salario, titulacao, formacao
                )
                professor.cadastrar()
            if handleOption == 2:
                openDataBase.executarDQL("select * from professor")
                professor.consultar
            if handleOption == 3:
                cpfDelete = input("Digite o cpf do professor que deseja deletar:")
                professor.excluir(cpfDelete)
            if handleOption == 4:
                # UPDATE
                cpfUpdate = input(
                    "Digite o cpf do professor que deseja realizar o update: "
                )
                nomeUpdate = input("Digite o novo nome do aluno: ")
                professor.alterar(nomeUpdate, cpfUpdate)

        if tecOrProf == 2:
            if handleOption == 1:
                nome = input("Digite o nome do funcionario: ")
                endereco = input("Digite seu endereco: ")
                telefone = input("Digite o seu telefone: ")
                cpf = input("Digite seu cpf: ")
                salario = input("Digite seu salario: ")
                funcionario = Funcionario(nome, endereco, telefone, cpf, salario)
                funcionario.cadastrar()
            if handleOption == 2:
                openDataBase.executarDQL("select * from funcionario")
                funcionario.consultar
            if handleOption == 3:
                cpfDelete = input("Digite o cpf do tecnico que deseja deletar:")
                funcionario.excluir(cpfDelete)
            if handleOption == 4:
                cpfUpdate = input(
                    "Digite o cpf do funcionario que deseja realizar o update: "
                )
                nomeUpdate = input("Digite o novo nome do aluno: ")
                funcionario.alterar(nomeUpdate, cpfUpdate)
    if select == 3:
        
        openDataBase = ConexaoDB()
        openDataBase.conectar()
        curso = Curso
        if handleOption == 1:
            codigo = input("Digite seu codigo: ")
            nome = input("Digite o nome do curso: ")
            duracao = input("Digite a sua duração: ")
            curso = Curso(codigo, nome, duracao)
            curso.cadastrar()
        if handleOption == 2:    
            openDataBase.executarDQL("select * from curso")
            curso.consultar
        if handleOption == 3:
            codigoDelete = input("Digite o codigo do curso que deseja deletar:")
            curso.excluir(codigoDelete)
        if handleOption == 4:
                codigoUpdate = input(
                    "Digite o codigo do curso que deseja realizar o update: "
                )
                nomeUpdate = input("Digite o novo nome do curso: ")
                curso.alterar(nomeUpdate, codigoUpdate)
    if select == 4:
        openDataBase = ConexaoDB()
        openDataBase.conectar()
        disciplina = Disciplina
        if handleOption == 1:
            codigo = input("Digite seu codigo: ")
            nome = input("Digite o nome da disciplina: ")
            cargaHoraria = input("Digite a sua carga horaria: ")
            disciplina = Disciplina(codigo, nome, cargaHoraria)
            disciplina.cadastrar()

       
        if handleOption == 2:
            openDataBase.executarDQL("select * from disciplina")
            disciplina.consultar
        if handleOption == 3:
            codigoDelete = input("Digite o codigo do disciplina que deseja deletar:")
            disciplina.excluir(codigoDelete)
        if handleOption == 4:
            codigoUpdate = input(
                    "Digite o codigo da disciplina que deseja realizar o update: "
                )
            nomeUpdate = input("Digite o novo nome da disciplina: ")
            urso.alterar(nomeUpdate, codigoUpdate)
 
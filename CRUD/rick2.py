# Nome: Ricardo Alberto Gonzalez Cedeno,  Curso: Analise e Desenvolvimento de Sistemas
# Somativa 2

import json

def salvar_dados(nome_arquivo, dados):
    with open(nome_arquivo, 'w') as arquivo:
        json.dump(dados, arquivo)
        
def carregar_dados(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []

def listar_estudantes():
    if not estudantes:
        print("Não há estudantes listados.")
    else:
        print("Listagem de estudantes:")
        for estudante in estudantes:
            print(f"Código do estudante: {estudante['codigo']}, Nome do Estudante: {estudante['nome']}, CPF do Estudante: {estudante['cpf']}")

def atualizar_estudante():
    if not estudantes:
        print("Não há estudantes para atualizar.")
        return

    try:
        codigo = int(input("Digite o código do estudante que deseja atualizar: "))
        
        estudante_a_atualizar = None
        for estudante in estudantes:
            if estudante['codigo'] == codigo:
                estudante_a_atualizar = estudante
                break

        if estudante_a_atualizar is None:
            print("Estudante não encontrado.")
        else:
            nome = input("Digite o novo nome do estudante: ")
            cpf = input("Digite o novo CPF do estudante: ")
            novo_codigo = int(input("Digite o novo código do estudante: "))
            estudante_a_atualizar['nome'] = nome
            estudante_a_atualizar['cpf'] = cpf
            estudante_a_atualizar['codigo'] = novo_codigo
            print("Estudante atualizado com sucesso.")
    except ValueError:
        print("Por favor, digite apenas números para o código do estudante.")

def incluir_estudante():
    while True:
        try:
            codigo = int(input("Digite o código do estudante: "))
            
            if any(estudante['codigo'] == codigo for estudante in estudantes):
                print("Este código de estudante já existe. Por favor, escolha outro.")
                continue
            break
        except ValueError:
            print("Por favor, digite apenas números para o código do estudante.")

    nome = input("Digite o nome do estudante: ")
    cpf = input("Digite o CPF do estudante: ")

    estudante = {
        'nome': nome,
        'cpf': cpf,
        'codigo': codigo
    }

    estudantes.append(estudante)
    print("Estudante incluído com sucesso.")

def excluir_estudante():
    if not estudantes:
        print("Não há estudantes para excluir.")
        return

    try:
        codigo = int(input("Digite o código do estudante que deseja excluir: "))
        
        estudante_a_excluir = None
        for estudante in estudantes:
            if estudante['codigo'] == codigo:
                estudante_a_excluir = estudante
                break

        if estudante_a_excluir is None:
            print("Estudante não encontrado.")
        else:
            estudantes.remove(estudante_a_excluir)
            print("Estudante excluído com sucesso.")
    except ValueError:
        print("Por favor, digite apenas números para o código do estudante.")


def incluir_professor():
    while True:
        try:
            codigo = int(input("Digite o código do professor: "))
            
            if any(professor['codigo'] == codigo for professor in professores):
                print("Este código de professor já existe. Por favor, escolha outro.")
                continue
            break
        except ValueError:
            print("Por favor, digite apenas números para o código do professor.")

    nome = input("Digite o nome do professor: ")
    cpf = input("Digite o CPF do professor: ")

    professor = {
        'nome': nome,
        'cpf': cpf,
        'codigo': codigo
    }

    professores.append(professor)
    print("Professor incluído com sucesso.")

def listar_professores():
    if not professores:
        print("Não há professores listados.")
    else:
        print("Listagem de professores:")
        for professor in professores:
            print(f"Código do Professor: {professor['codigo']}, Nome do Professor: {professor['nome']}, CPF do Professor: {professor['cpf']}")

def atualizar_professor():
    if not professores:
        print("Não há professores para atualizar.")
        return

    while True:
        try:
            codigo = int(input("Digite o código do professor que deseja atualizar: "))
            break
        except ValueError:
            print("Por favor, digite apenas números para o código do professor.")

    professor_a_atualizar = None
    for professor in professores:
        if professor['codigo'] == codigo:
            professor_a_atualizar = professor
            break

    if professor_a_atualizar is None:
        print("Professor não encontrado.")
    else:
        nome = input("Digite o novo nome do professor: ")
        cpf = input("Digite o novo CPF do professor: ")

        while True:
            try:
                novo_codigo = int(input("Digite o novo código do professor: "))
                break
            except ValueError:
                print("Por favor, digite apenas números para o código do professor.")

        professor_a_atualizar['nome'] = nome
        professor_a_atualizar['cpf'] = cpf
        professor_a_atualizar['codigo'] = novo_codigo

def excluir_professor():
    if not professores:
        print("Não há professores para excluir.")
        return

    try:
        codigo = int(input("Digite o código do professor que deseja excluir: "))
        
        professor_a_excluir = None
        for professor in professores:
            if professor['codigo'] == codigo:
                professor_a_excluir = professor
                break

        if professor_a_excluir is None:
            print("Professor não encontrado.")
        else:
            professores.remove(professor_a_excluir)
            print("Professor excluído com sucesso.")
    except ValueError:
        print("Por favor, digite apenas números para o código do professor.")
        
        
def incluir_disciplina():
    while True:
        try:
            codigo = int(input("Digite o código da disciplina: "))
            
            if any(disciplina['codigo'] == codigo for disciplina in disciplinas):
                print("Este código de disciplina já existe. Por favor, escolha outro.")
                continue
            break
        except ValueError:
            print("Por favor, digite apenas números para o código da disciplina.")

    nome = input("Digite o nome da disciplina: ")

    disciplina = {
        'nome': nome,
        'codigo': codigo
    }

    disciplinas.append(disciplina)
    print("Disciplina incluída com sucesso.")

def listar_disciplinas():
    if not disciplinas:
        print("Não há disciplinas listadas.")
    else:
        print("Listagem de disciplinas:")
        for disciplina in disciplinas:
            print(f"Código da Disciplina: {disciplina['codigo']}, Nome da Disciplina: {disciplina['nome']}")

def atualizar_disciplina():
    if not disciplinas:
        print("Não há disciplinas para atualizar.")
        return

    try:
        codigo = int(input("Digite o código da disciplina que deseja atualizar: "))
        
        disciplina_a_atualizar = None
        for disciplina in disciplinas:
            if disciplina['codigo'] == codigo:
                disciplina_a_atualizar = disciplina
                break

        if disciplina_a_atualizar is None:
            print("Disciplina não encontrada.")
        else:
            nome = input("Digite o novo nome da disciplina: ")
            novo_codigo = int(input("Digite o novo código da disciplina: "))
            disciplina_a_atualizar['nome'] = nome
            disciplina_a_atualizar['codigo'] = novo_codigo
    except ValueError:
        print("Por favor, digite apenas números para o código da disciplina.")

def excluir_disciplina():
    if not disciplinas:
        print("Não há disciplinas para excluir.")
        return

    try:
        codigo = int(input("Digite o código da disciplina que deseja excluir: "))
        
        disciplina_a_excluir = None
        for disciplina in disciplinas:
            if disciplina['codigo'] == codigo:
                disciplina_a_excluir = disciplina
                break

        if disciplina_a_excluir is None:
            print("Disciplina não encontrada.")
        else:
            disciplinas.remove(disciplina_a_excluir)
            print("Disciplina excluída com sucesso.")
    except ValueError:
        print("Por favor, digite apenas números para o código da disciplina.")

def incluir_turma():
    while True:
        try:
            codigo_turma = int(input("Digite o código da turma: "))
            
            if any(turma['codigo_turma'] == codigo_turma for turma in turmas):
                print("Este código de turma já existe. Por favor, escolha outro.")
                continue
            break
        except ValueError:
            print("Por favor, digite apenas números para o código da turma.")

    while True:
        try:
            codigo_professor = int(input("Digite o código do professor: "))
            
            if any(professor['codigo'] == codigo_professor for professor in professores):
                print("Este código de professor já existe. Por favor, escolha outro.")
                continue
            break
        except ValueError:
            print("Por favor, digite apenas números para o código do professor.")

    while True:
        try:
            codigo_disciplina = int(input("Digite o código da disciplina: "))
            
            if any(disciplina['codigo'] == codigo_disciplina for disciplina in disciplinas):
                print("Este código de disciplina já existe. Por favor, escolha outro.")
                continue
            break
        except ValueError:
            print("Por favor, digite apenas números para o código da disciplina.")

    turma = {
        'codigo_turma': codigo_turma,
        'codigo_professor': codigo_professor,
        'codigo_disciplina': codigo_disciplina
    }
    
    turmas.append(turma)
    print("Turma incluída com sucesso.")

def listar_turmas():
    if not turmas:
        print("Não há turmas cadastradas.")
    else:
        print("Listagem de turmas:")
        for turma in turmas:
            print(f"Código da Turma: {turma['codigo_turma']}, Código do Professor: {turma['codigo_professor']}, Código da Disciplina: {turma['codigo_disciplina']}")

def atualizar_turma():
    if not turmas:
        print("Não há turmas para atualizar.")
        return

    try:
        codigo_turma = int(input("Digite o código da turma que deseja atualizar: "))
        
        turma_a_atualizar = None
        for turma in turmas:
            if turma['codigo_turma'] == codigo_turma:  
                turma_a_atualizar = turma
                break

        if turma_a_atualizar is None:
            print("Turma não encontrada.")
        else:
            while True:
                try:
                    novo_codigo_turma = int(input("Digite o novo código da turma: "))
                    break
                except ValueError:
                    print("Por favor, digite apenas números para o código da turma.")
            
            while True:
                try:
                    novo_codigo_professor = int(input("Digite o novo código do professor: "))
                    break
                except ValueError:
                    print("Por favor, digite apenas números para o código do professor.")
            
            while True:
                try:
                    novo_codigo_disciplina = int(input("Digite o novo código da disciplina: "))
                    break
                except ValueError:
                    print("Por favor, digite apenas números para o código da disciplina.")
            
            turma_a_atualizar['codigo_turma'] = novo_codigo_turma
            turma_a_atualizar['codigo_professor'] = novo_codigo_professor
            turma_a_atualizar['codigo_disciplina'] = novo_codigo_disciplina
    except ValueError:
        print("Por favor, digite apenas números para o código da turma.")


def excluir_turma():
    if not turmas:
        print("Não há turmas para excluir.")
        return

    try:
        codigo = int(input("Digite o código da turma que deseja excluir: "))
        
        turma_a_excluir = None
        for turma in turmas:
            if turma['codigo_turma'] == codigo:  
                turma_a_excluir = turma
                break

        if turma_a_excluir is None:
            print("Turma não encontrada.")
        else:
            turmas.remove(turma_a_excluir)
            print("Turma excluída com sucesso.")
    except ValueError:
        print("Por favor, digite apenas números para o código da turma.")

def realizar_matricula():
    while True:
        try:
            codigo_turma = int(input("Digite o código da turma: "))
            codigo_estudante = int(input("Digite o código do estudante: "))
            
            for matricula in matriculas:
                if matricula['codigo_turma'] == codigo_turma and matricula['codigo_estudante'] == codigo_estudante:
                    print("Esta matrícula já existe. Por favor, digite um código de turma e estudante diferentes.")
                    break
            else:
                matriculas.append({
                    'codigo_turma': codigo_turma,
                    'codigo_estudante': codigo_estudante
                })
                break
        except ValueError:
            print("Por favor, digite apenas números para o código da turma e do estudante.")

def listar_matriculas():
    if not matriculas:
        print("Não há matrículas realizadas.")
    else:
        print("Listagem de matrículas:")
        for matricula in matriculas:
            print(f"Código da Turma: {matricula['codigo_turma']}, Código do Estudante: {matricula['codigo_estudante']}")

def atualizar_matricula():
    if not matriculas:
        print("Não há matrículas para atualizar.")
        return

    while True:
        try:
            codigo_turma = int(input("Digite o código da turma cuja matrícula deseja atualizar: "))
            break
        except ValueError:
            print("Por favor, digite apenas números para o código da turma.")

    matricula_a_atualizar = None
    for matricula in matriculas:
        if matricula['codigo_turma'] == codigo_turma:
            matricula_a_atualizar = matricula
            break

    if matricula_a_atualizar is None:
        print("Matrícula não encontrada.")
    else:
        while True:
            try:
                novo_codigo_turma = int(input("Digite o novo código da turma: "))
                novo_codigo_estudante = int(input("Digite o novo código do estudante: "))
                break
            except ValueError:
                print("Por favor, digite apenas números para o código da turma e do estudante.")

        matricula_a_atualizar['codigo_turma'] = novo_codigo_turma
        matricula_a_atualizar['codigo_estudante'] = novo_codigo_estudante
        print("Matrícula atualizada com sucesso.")

def excluir_matricula():
    if not matriculas:
        print("Não há matrículas para excluir.")
        return

    while True:
        try:
            codigo_turma = int(input("Digite o código da turma cuja matrícula deseja excluir: "))
            codigo_estudante = int(input("Digite o código do estudante cuja matrícula deseja excluir: "))
            break
        except ValueError:
            print("Por favor, digite apenas números para o código da turma e do estudante.")

    matricula_a_excluir = None
    for matricula in matriculas:
        if matricula['codigo_turma'] == codigo_turma and matricula['codigo_estudante'] == codigo_estudante:
            matricula_a_excluir = matricula
            break

    if matricula_a_excluir is None:
        print("Matrícula não encontrada.")
    else:
        matriculas.remove(matricula_a_excluir)
        print("Matrícula excluída com sucesso.")
# Carregar os dados dos arquivos JSON

estudantes = carregar_dados("estudantes.json")
professores = carregar_dados("professores.json")
disciplinas = carregar_dados("disciplinas.json")
turmas = carregar_dados("turmas.json")
matriculas = carregar_dados("matriculas.json")
#Loop do menu principal
while True:
    print("=========================================")
    print("          BEM-VINDO AO MENU!")
    print("=========================================")
    print("  1. ESTUDANTES")
    print("  2. PROFESSORES")
    print("  3. DISCIPLINAS")
    print("  4. TURMAS")
    print("  5. MATRÍCULAS")
    print("  6. SAIR ")
    print("=========================================")


#loop para verificar se a opção digitada é válida
    while True:
        try:
            gerenciamento = int(input("Digite a opção desejada: "))
            if gerenciamento < 1 or gerenciamento > 6:
                raise ValueError
            break
        except ValueError:
            print("Por favor, digite um número de 1 a 6.")

    if gerenciamento == 1:
        while True:
            print("=========================================")
            print("          MENU DE ESTUDANTES")
            print("=========================================")
            print("  1. Incluir Estudante")
            print("  2. Listar Estudantes")
            print("  3. Atualizar Estudante")
            print("  4. Excluir Estudante")
            print("  5. Voltar ao Menu Principal")
            print("=========================================")

            while True:
                try:
                    opcao = int(input("Digite a opção desejada: "))
                    if opcao < 1 or opcao > 5:
                        raise ValueError
                    break
                except ValueError:
                    print("Por favor, digite um número de 1 a 5.")

            if opcao == 1:
                incluir_estudante()
                salvar_dados("estudantes.json", estudantes)
            elif opcao == 2:
                listar_estudantes()
                
            elif opcao == 3:
                atualizar_estudante()
                salvar_dados("estudantes.json", estudantes)
            elif opcao == 4:
                excluir_estudante()
                salvar_dados("estudantes.json", estudantes)
            elif opcao == 5:
                break
# Loop Menu de professores
    elif gerenciamento == 2:
        while True:
            print("=========================================")
            print("         MENU DE PROFESSORES")
            print("=========================================")
            print("  1. Incluir Professor")
            print("  2. Listar Professores")
            print("  3. Atualizar Professor")
            print("  4. Excluir Professor")
            print("  5. Voltar ao Menu Principal")
            print("=========================================")

            while True:
                try:
                    opcao = int(input("Digite a opção desejada: "))
                    if opcao < 1 or opcao > 5:
                        raise ValueError
                    break
                except ValueError:
                    print("Por favor, digite um número de 1 a 5.")

            if opcao == 1:
                incluir_professor()
                salvar_dados("professores.json", professores)
            elif opcao == 2:
                listar_professores()
            elif opcao == 3:
                atualizar_professor()
                salvar_dados("professores.json", professores)
            elif opcao == 4:
                excluir_professor()
                salvar_dados("professores.json", professores)
            elif opcao == 5:
                break
#Loop Menu de disciplinas
    elif gerenciamento == 3:
        while True:
            print("=========================================")
            print("         MENU DE DISCIPLINAS")
            print("=========================================")
            print("  1. Incluir Disciplina")
            print("  2. Listar Disciplinas")
            print("  3. Atualizar Disciplina")
            print("  4. Excluir Disciplina")
            print("  5. Voltar ao Menu Principal")
            print("=========================================")

            while True:
                try:
                    opcao = int(input("Digite a opção desejada: "))
                    if opcao < 1 or opcao > 5:
                        raise ValueError
                    break
                except ValueError:
                    print("Por favor, digite um número de 1 a 5.")

            if opcao == 1:
                incluir_disciplina()
                salvar_dados("disciplinas.json", disciplinas)
            elif opcao == 2:
                listar_disciplinas()
            elif opcao == 3:
                atualizar_disciplina()
                salvar_dados("disciplinas.json", disciplinas)
            elif opcao == 4:
                excluir_disciplina()
                salvar_dados("disciplinas.json", disciplinas)
            elif opcao == 5:
                break

    elif gerenciamento == 4:
        while True:
            print("=========================================")
            print("         MENU DE TURMAS")
            print("=========================================")
            print("  1. Incluir Turma")
            print("  2. Listar Turmas")
            print("  3. Atualizar Turma")
            print("  4. Excluir Turma")
            print("  5. Voltar ao Menu Principal")
            print("=========================================")

            while True:
                try:
                    opcao = int(input("Digite a opção desejada: "))
                    if opcao < 1 or opcao > 5:
                        raise ValueError
                    break
                except ValueError:
                    print("Por favor, digite um número de 1 a 5.")

            if opcao == 1:
                incluir_turma()
                salvar_dados("turmas.json", turmas)
            elif opcao == 2:
                listar_turmas()
            elif opcao == 3:
                atualizar_turma()
                salvar_dados("turmas.json", turmas)
            elif opcao == 4:
                excluir_turma()
                salvar_dados("turmas.json", turmas)
            elif opcao == 5:
                break

    elif gerenciamento == 5:
        while True:
            print("=========================================")
            print("         MENU DE MATRÍCULAS")
            print("=========================================")
            print("  1. Incluir Matrícula")
            print("  2. Listar Matrículas")
            print("  3. Atualizar Matrícula")
            print("  4. Excluir Matrícula")
            print("  5. Voltar ao Menu Principal")
            print("=========================================")

            while True:
                try:
                    opcao = int(input("Digite a opção desejada: "))
                    if opcao < 1 or opcao > 5:
                        raise ValueError
                    break
                except ValueError:
                    print("Por favor, digite um número de 1 a 5.")

            if opcao == 1:
                realizar_matricula()
                salvar_dados("matriculas.json", matriculas)
            elif opcao == 2:
                listar_matriculas()
                salvar_dados("matriculas.json", matriculas)
            elif opcao == 3:
                atualizar_matricula()
                salvar_dados("matriculas.json", matriculas)
            elif opcao == 4:
                excluir_matricula()
                salvar_dados("matriculas.json", matriculas)
            elif opcao == 5:
                break


    elif gerenciamento == 6:
        print("Saindo...")
        break

salvar_dados("estudantes.json", estudantes)
salvar_dados("professores.json", professores)
salvar_dados("disciplinas.json", disciplinas)
salvar_dados("turmas.json", turmas)
salvar_dados("matriculas.json", matriculas)

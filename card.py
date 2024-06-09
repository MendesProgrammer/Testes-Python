import json
from random import shuffle

def salvar(nome='arquivo', dado=[]):
    '''Salva objetos em um arquivo .json'''
    with open(f'{nome}.json', 'w') as file:
        file.write(json.dumps(dado))


def ler(nome='arquivo'):
    '''Retorna um objeto com os valores lidos de um arquivo .json'''
    dado = None
    with open(f'{nome}.json', 'r') as file:
        dado = json.loads(file.read())
    return dado


# Executa o arquivo ou cria caso não exista
try:
    dado = ler('card')
except:
    dado = {
        'resultado':[],
        'simbolo1':'=',
        'simbolo2':'-',
        'linha1':50,
        'linha2':50
        }
    salvar('card', dado)

print(dado['simbolo1'] * dado['linha1'])

# Programa principal
while True:
    # Indicador da quantidade de palavra/tradução salvas
    print(f'Quantidade de palavras salvas : {len(dado["resultado"])}')

    # Entrada de dados do usuário, comandos principais
    sec = str(input('Digite o comando(ls manual básico) >>> ')).strip().lower()

    # Gera a lista de instruções, onde cada índice corresponde a um parâmetro
    sel = []
    if '/' in sec:
        msg = ''
        for c in range(0, len(sec)):
            if sec[c] == '/':
                sel.append(msg)
                msg = ''
            else:
                msg += sec[c]
        sel.append(msg)

    else:
        sel = sec.split()

    # Adiciona valores na lista
    if len(sel) == 1 and sel[0] == 'ad':
        while True:
            print(dado['simbolo2'] * dado['linha2'])
            ing = str(input('Palavra/frase na frente(-v voltar) > ')).strip().lower()
            if ing == '-v':
                break
            por = str(input('Palavra/frase no verso(-v voltar) > ')).strip().lower()
            if por == '-v':
                break
            conf = 0
            while conf != 's' and conf != 'n':
                conf = str(input('Confirmar? (s/n) ')).strip().lower()
                if conf == 's':
                    dado['resultado'].append([ing, por])
                    salvar('card', dado)
        print(dado['simbolo2'] * dado['linha2'])

    # Faz um teste com um número indicado pelo usuário de itens
    # ts número_de_itens
    elif len(sel) == 2 and sel[0] == 'ts':
        try:
            n1 = int(sel[1])
            if 0 < n1 <= len(dado['resultado']):
                tra = dado['resultado'][0:n1]
                shuffle(tra)
                acerto = erro = 0
                for c in range(0, n1):
                    print(dado['simbolo2'] * dado['linha2'])
                    print(f'{c+1} -> {tra[c][0]}')
                    tr = str(input('Tradução -> ')).strip().lower()
                    if tr == tra[c][1]:
                        print('Resposta correta')
                        acerto += 1
                    else:
                        print(f'Resposta incorrta, correção: {tra[c][1]}')
                        erro += 1
                print(dado['simbolo2'] * dado['linha2'])
                print(f'Número de acertos: {acerto}')
                print(f'Número de erros: {erro}')
                print(dado['simbolo2'] * dado['linha2'])

        except:
            None

    # Encerra o programa
    elif len(sel) == 1 and sel[0] == 'sair':
        print('Encerrando programa!')
        break

    # Configura o tamanho da linha 1
    elif len(sel) == 2 and sel[0] == 's1-t':
        try:
            n1 = int(sel[1])
            if n1 > 0:
                dado['linha1'] = n1
        except:
            None

    # Configura o tamamnho da linha 2
    elif len(sel) == 2 and sel[0] =='s2-t':
        try:
            n1 = int(sel[1])
            if n1 > 0:
                dado['linha2'] = n1
        except:
            None

    # Modifica o caractere da linha 1
    elif len(sel) == 2 and sel[0] == 's1-s':
        dado['simbolo1'] = sel[1]

    # Modifica o caractere da linha 2
    elif len(sel) == 2 and sel[0] == 's2-s':
        dado['simbolo2'] = sel[1]

    # Mostra um manual básico com as principais intruções
    elif sel[0] == 'ls':
        print(dado['simbolo1'] * dado['linha1'])
        print('<<<Lista de comandos>>>\nad -> adicionar\nts -> teste número\ns1-t -> tamanho linha\ns2-t -> tamanho linha\ns1-s -> caractere da linha\ns2-s -> caractere a linha\ndicio -> Realiza a tradução\nsair')
        print(dado['simbolo1'] * dado['linha1'])

    # Procura um cartão pelo valor digitado e mostra o seu resultado
    elif len(sel) == 2 and sel[0] == 'dicio':
        for d in dado["resultado"]:
            if d[0] == sel[1]:
                print(f'Tradução -> {d[1]}')

            elif d[1] == sel[1]:
                print(f'Tradução -> {d[0]}')

    # Caso nenhuma instrução anterior seja atendida
    else:
        print('Comando incorreto!')

    print(dado['simbolo1'] * dado['linha1'])

    # Mantém o arquivo principal sempre atualizado
    salvar('card', dado)

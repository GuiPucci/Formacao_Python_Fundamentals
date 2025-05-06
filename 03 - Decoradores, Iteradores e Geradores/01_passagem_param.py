def mensagem(nome):
    print('executando mensagem')
    return f'Oi {nome}'


def mensagem_longa(nome):
    print('executando mensagem longa')
    return f'Olá tudo bem cok você {nome}?'


def executar(funcao, nome):
    print('executando execitar')
    return funcao(nome)


print(executar(mensagem, "João"))
print(executar(mensagem_longa, "João"))

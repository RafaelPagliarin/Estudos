def forcar_tipo(*tipos):
    def decorator(funcao):
        def converte(*args, **kwargs):
            novo_args = []
            for(valor, tipo) in zip(args, tipos):
                novo_args.append(tipo(valor))
            return funcao(*novo_args, **kwargs)
        return converte
    return decorator


@forcar_tipo(str, int)
def repete_msg(msg, vezes):
    for x in range(vezes):
        print(msg)

@forcar_tipo(float, float)
def dividir(a,b):
    print(a/b)


repete_msg('Rafael', '4')

dividir('4', 8)
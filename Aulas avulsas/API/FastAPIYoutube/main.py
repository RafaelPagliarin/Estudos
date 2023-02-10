#FAST API

# fast - realmente rapido
# documentação criada automaticamente
# gerenciamento de processos assincronos (vai estar usando o que há de mais novo no python para ser rapido)


from fastapi import FastAPI

app = FastAPI()


@app.get('/') #
def home():
    return 'Minha API está no ar'



"""
GIL - Python Global Interpreter Lock

é um mutex (ou lock) que permite que apenas uma thread tome conta do interpretador Python.

Isso significa que somente uma thread pode estar em um estado de execução em qualquer ponto do tempo.

O impacto do GIL não é comumente visível para desenvolvedores que executam programas single-thread, mas pode
ser uma dor de cabeça para programas que precisam de tempo de resposta em códigos multi-thread.

Desde que o GIL permite apenas uma thread a ser executada, mesmo em computadores multi-threads com arquitetura que
permite utilizar mais de um CPU ou core, o GIL tem ganhado reputação como recurso 'indecente' do Python.

Nesta aula, iremos aprender como o GIL afeta a performance do seu programa Python e também como a gente pode mitigar
o impacto no nosso código.


Como visto na aula passada, Python utiliza reference counting para gerenciamento de memória.
    Isso significa que cada objeto criado em Python mantém uma variável de contagem de referencia que guarda quantas
referências apontam para o objeto. Quando o contador de referencias chega a zero, a memória ocupada é liberada.

O problema é que essa forma de gerenciamento de memória utilizando reference couting precisa de proteção para um
fenômeno chamado 'race conditions', onde duas ou mais threads aumentam ou diminuem seu valor simultaneamente.
    Se isso acontecer, poderá causar problemas de memória que nunca é liberada, ou ainda pior, liberação incorreta de
memória enquanto ainda existe referencia para o objeto.
    E isso pode causar 'crashs' ou outros bugs esquisitos no seu programa Python.

Esse reference couting pode ser mantido seguro adicionando 'locks' em toda estrutura de dados que são compartilhadas
via threads. Desta forma eles não são modificados de forma inconsistente.
    O problema é que adicionar 'locks' em cada objeto ou grupo de objetos significa que múltiplos locks irão existir,
e isso irá causar outro problema - Deadlocks (que só podem existir se houver mais de 1 lock). Outro efeito colateral
seria decaimento da performance causada pela repetida aquisição e liberação dos locks.

O GIL aplica na regra de execução de qualquer código Python o single lock previnindo qualquer deadlock, o que, por outro
lado transforma qualquer código Python em single-thread.
    Vale mencionar que o GIL apesar de ser usado também em outras linguagens de programação, como o Ruby, não é a única
solução.
    Algumas linguagens evitam o uso do GIL para gerenciamento de memória em thread utilizando abordagens diferentes do
reference counting.
    Por exemplo, uma das abordagens que outras linguagens utilizam é o compilador JIT - Just in Time, como o Java.

Conforme pudemos ver, mesmo utilizando multi-thread o tempo de finalização não muda muito.
    A utilização do GIL prejudica a real utilização de multi-cores nas máquinas, o que torna os programas Python lentos
em alguns casos.
    Por outro lado, o GIL torna as aplicações single-thread muito performaticas, e a grande maioria dos aplicativos
não precisam utilizar multi-thread.

Como lidar com o GIL?
    Caso você tenha problemas com o GIL, você pode utilizar multi-processing ao invés de multithreading.
    Utilizando processos ao invés de threads cada processo Python ganha seu proprio interpretador Python e espaço em
memória. Desta forma o GIL não será problema.
    OBS: multi-processing são mais 'pesados' que multi-threading. Pois a cada processo teremos um ambiente Python proprio

    GIL só funciona no python padrão, feito em C (CPython). Embora existam Jyphon(Java), IronPython(C#), PyPy(Python)
"""


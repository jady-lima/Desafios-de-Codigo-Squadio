# Desafios de código Squadio - Intermediário II
 Desafio de código Squadio - Intermediário II

Nesse repositório são apresentados os exercicios executados no modulo de Desafios de Código Squadio - Intermediário II do BootCamp da Dio de Python Data Analytics.

Há então 3 diferentes desafios, sendo eles:
* # Desafio 1 : O Robô Inteligente
    ## Descrição
    Você foi contratado pela empresa DIO Robots para programar um robô capaz de classificar números em uma das seguintes categorias: negativo, positivo ou zero. Para isso, você deve criar uma função de classificação que receba um número como parâmetro e retorne a mensagem "negativo!" ou " positivo!", de acordo com sua categoria.

    O programa deve ser executado continuamente, permitindo que o usuário insira vários números. Quando ele quiser encerrar a execução, deverá digitar um número igual a zero. A cada novo número inserido, o robô deve classificá-lo e exibir a mensagem correspondente. Ao final da execução, o programa deverá exibir a quantidade de números positivos, negativos e zeros que foram inseridos.

    ## Entrada
    A entrada deve receber valores inteiros que pode ser positivo, negativo ou zero. Lembrando que a entrada zero deve encerrar o programa.

    ## Saída
    O código deverá retornar uma mensagem (string) informando se o número é positivo ou não. Ao receber o valor 0, ele deverá encerrar o e informar quantos números foram positivos e negativos.

* # Desafio 2 : A Jornada de Classificação Frutífera
    ## Descrição
    Nesta missão, sua tarefa é mais desafiadora do que nunca! Em um pomar mágico, as frutas têm características únicas que as diferenciam. Seu objetivo é criar um modelo de machine learning capaz de classificar frutas com base em três características: peso, textura (suave ou áspera) e cor (vermelha, laranja ou amarela). Cada tipo de fruta tem limites específicos para essas características.

    - Maçã:
        - Peso mínimo: 130 gramas
        - Textura: Ápera (rough)
        - Cor: Vermelha (red)
    - Laranja:
        - Peso mínimo: 120 gramas
        - Textura: Suave (smooth)
        - Cor: Laranja (orange)
    - Morango:
        - Peso mínimo: 150 gramas
        - Textura: Suave (smooth)
        - Cor: Vermelha (red)
    - Banana:
        - Peso mínimo: 150 gramas
        - Textura: Áspera (rough)
        - Cor: Amarela (yellow)

    ## Entrada
    Seu código deve receber as seguintes entradas do usuário:
    - Peso da fruta (em gramas): um número real que representa o peso da fruta.
    - Textura da fruta (suave ou áspera): uma string indicando se a fruta é suave ("smooth") ou áspera ("rough").
    - Cor da fruta (vermelha, laranja ou amarela): uma string indicando a cor da fruta.

    ## Saída
    O código deve produzir uma saída indicando a classificação da fruta com base nas características fornecidas.

* # Desafio 3 : A Questão Intrincada da Magia Preditiva
    ## Descrição
    No reino mágico onde cada feiticeiro possui uma afinidade elemental única, seu desafio é criar um modelo de machine learning para prever essa afinidade. Os feiticeiros podem pertencer a um dos quatro elementos mágicos: Fogo, Água, Terra ou Ar. A predição será baseada em cinco atributos mágicos: intensidade do feitiço, presença de componente raro, fase lunar, idade do feiticeiro e afinidade com animais mágicos.
    Aqui estão os critérios mágicos para cada elemento:

    - Elemento Fogo:
        Intensidade do feitiço maior ou igual a 5.
        Fase lunar durante o feitiço é crescente.
        Idade do feiticeiro é superior a 100 anos
    -Elemento Água:
        Intensidade do feitiço maior ou igual a 7.
        Presença de componente raro.
        Fase lunar durante o feitiço é cheia.
        Idade do feiticeiro é igual ou inferior a 100 anos.
        Afinidade com animais mágicos.
    - Elemento Terra:
        Intensidade do feitiço maior ou igual a 7.
        Presença de componente raro.
        Fase lunar durante o feitiço é cheia.
        Idade do feiticeiro é igual ou inferior a 100 anos.
        Afinidade com animais mágicos.
    - Elemento Ar:
        Caso não se encaixe nos critérios anteriores.

    ## Entrada
    Seu código deve receber as seguintes entradas do usuário:

    - Intensidade do feitiço (de 1 a 10): um número inteiro representando a força do feitiço.
    - Componente raro (sim ou não): uma string indicando se o feitiço contém um componente raro.
    - Fase lunar (cheia, crescente ou minguante): uma string indicando a fase lunar durante o lançamento do feitiço.
    - Idade do feiticeiro (em anos): um número inteiro representando a idade do feiticeiro.
    - Afinidade com animais mágicos (sim ou não): uma string indicando se o feiticeiro tem afinidade com animais mágicos.

    ## Saída
    O código deve produzir uma saída indicando a afinidade elemental prevista do feiticeiro com base nos atributos fornecidos.
# CriptografiaPython

Projeto para faculdade com um algoritmo em python que criptografa uma mensagem usando a técnica RSA

## A técnica RSA

A técnica RSA é um método de criptografia que utiliza cinco chaves, sendo três privadas e duas públicas. Ela baseia-se em números primos, números coprimos e cálculos de inversão modular para derivar essas chaves e criptografar mensagens. No contexto do RSA, as chaves utilizadas são P, Q, N, Z, E e D. Esta técnica é amplamente adotada em bancos e diversas outras organizações que exigem alta segurança para seus dados.

A força da criptografia RSA reside na dificuldade de descriptografar a mensagem sem conhecimento das chaves apropriadas. Se um usuário não possuir uma das chaves necessárias para a descriptografia, seria necessário conhecer as outras cinco chaves para desvendar a mensagem. Isso torna extremamente desafiador e praticamente impossível para qualquer pessoa decifrar a mensagem sem acesso às chaves corretas.

A dificuldade dessa criptografia reside na dificuldade de encontrar a chave N que é usada como chave publica e privada, sendo N e E as privadas e N e D as publicas, por conta disso se o usuário não souber a chave D ou N ele tera de saber a P, Q, Z e a chave E para poder achar ambas as chaves.

## Explicando o código

Dentro do diretório "Criptografia" reside o arquivo python que será responsável por criptografar a mensagem que tem que ser inserida dentro do arquivo "msg.criptografar.txt" e gerar as 5 chaves de forma aleatória com a biblioteca nativa do python random

### Função responsável por criar as chaves P e Q com o parâmetro de bits para definir o tamanho dos numeros que serão gerados para as chaves

<p align="center">
    <img src="https://bg-so-1.zippyimage.com/2023/10/22/02380c624c271512d4afdb2f79e3ff8a.png" alt="img">
</p>

### Função responsável por criar as chaves N fazendo a multiplicação das chaves P e Q

Essa parte do código também é responsável por abrir o arquivo e escrever a chave se não tiver o arquivo ele cria

<p align="center">
    <img src="https://bg-so-1.zippyimage.com/2023/10/22/8c68c8d30dbf60da75dd694026f1e374.png" alt="img">
</p>

### Função responsável por criar as chaves Z usada para achar a chave E e D

<p align="center">
    <img src="https://bg-so-1.zippyimage.com/2023/10/22/a35b96984b8e9efbadf13f8ca10768cf.png" alt="img">
</p>

### Função responsável por criar as chaves E

Define um valor para achar um coprimo a chave Z definindo um valor máximo divisor comum com a função GDC

<p align="center">
    <img src="https://bg-so-1.zippyimage.com/2023/10/22/636cbe4b74bf7322f44a7124787068ec.png" alt="img">
</p>

### Função responsável por criar as chaves D e inversão modular

Calcula a inversão modular por forma do algoritmo de Euclides Estendido e busca o máximo divisor comum

<p align="center">
    <img src="https://bg-so-1.zippyimage.com/2023/10/22/7d54e1a1b995c03fe46278e088516240.png" alt="img">
</p>

### Função responsável por testar se os valores são primo

Testa se o valor é primo por meio do teste de Miller Rabin

<p align="center">
    <img src="https://bg-so-1.zippyimage.com/2023/10/22/0ef5053c65210007362e83c04efbfcba.png" alt="img">
</p>

## Referência

- [Projeto do github, foi usado para referencia de como escrever o código](https://github.com/Everton42/video-youtube-rsa)

- [🔒COMO CRIAR SUA PRÓPRIA CRIPTOGRAFIA!🔒 - Syoxz](https://www.youtube.com/watch?v=umBAnAMC1-E&list=PLZeN7MDGNYUHuWDnzxrttXVtZKaKo-4_y&index=11)

- [The RSA Encryption Algorithm (1 of 2: Computing an Example)](https://www.youtube.com/watch?v=4zahvcJ9glg&list=PLZeN7MDGNYUHuWDnzxrttXVtZKaKo-4_y&index=12)

- [The RSA Encryption Algorithm (2 of 2: Generating the Keys)](https://www.youtube.com/watch?v=oOcTVTpUsPQ)

- [RSA Encryption From Scratch - Math & Python Code](https://www.youtube.com/watch?v=D_PfV_IcUdA&list=PLZeN7MDGNYUHuWDnzxrttXVtZKaKo-4_y&index=13)

- [Funcionamento Algoritmo RSA Fácil de Entender](https://www.youtube.com/watch?v=9m8enHN13mw&list=PLZeN7MDGNYUHuWDnzxrttXVtZKaKo-4_y&index=14&t=2s)

- [Função totiente de Euler | Ciência da Computação | Khan Academy](https://www.youtube.com/watch?v=3MryVNzS3o4)

- [Algoritmo de Euclides estendido](https://www.youtube.com/watch?v=BsE1IAghIT4&list=TLPQMTgxMDIwMjOsfv5Nxhcw4g&index=2)

- [Python documentação](https://docs.python.org/3/)

# CriptografiaPython

Projeto para faculdade com um algoritmo em python que criptografa uma mensagem usando a técnica RSA

## A técnica RSA

A técnica RSA é um método de criptografia que utiliza cinco chaves, sendo três privadas e duas públicas. Ela baseia-se em números primos, números coprimos e cálculos de inversão modular para derivar essas chaves e criptografar mensagens. No contexto do RSA, as chaves utilizadas são P, Q, N, Z, E e D. Esta técnica é amplamente adotada em bancos e diversas outras organizações que exigem alta segurança para seus dados.

A força da criptografia RSA reside na dificuldade de descriptografar a mensagem sem conhecimento das chaves apropriadas. Se um usuário não possuir uma das chaves necessárias para a descriptografia, seria necessário conhecer as outras cinco chaves para desvendar a mensagem. Isso torna extremamente desafiador e praticamente impossível para qualquer pessoa decifrar a mensagem sem acesso às chaves corretas.

A dificuldade dessa criptografia reside na dificuldade de encontrar a chave N que é usada como chave publica e privada, sendo N e E as privadas e N e D as publicas, por conta disso se o usuário não souber a chave D ou N ele tera de saber a P, Q, Z e a chave E para poder achar ambas as chaves.

## Explicando o código

Dentro do diretório "Criptografia" reside o arquivo python que será responsável por criptografar a mensagem que tem que ser inserida dentro do arquivo "msg.criptografar.txt" e gerar as 5 chaves de forma aleatória com a biblioteca nativa do python random

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

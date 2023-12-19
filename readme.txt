Calculadora de Precisão Ilimitada

Este programa é uma calculadora que pode lidar com números de precisão ilimitada. Ele lê os valores de dois arquivos textos distintos, aqui chamado de V1 e V2 respectivamente
e realiza operações matemáticas básicas, como adição e multiplicação para salvar em um terceiro arquivo, aqui chamado de V3.txt.

Estrutura do Programa

O programa é composto por quatro arquivos:

main.py: 

	Este é o arquivo principal que contém a lógica do menu principal e a interação com o usuário.

funcoes_calculadora.py: 

	Este arquivo contém a classe CalculadoraIlimitada que realiza as operações matemáticas e manipula os valores.

	A classe CalculadoraIlimitada tem os seguintes métodos:

	ler_valores(): Lê os valores do arquivo.
	somar_valores(): Soma os valores lidos.
	multiplicar_valores(): Multiplica os valores lidos.
	salvar_resultados(): Salva os resultados das operações em um arquivo.
	sair_calculadora(): Encerra o programa.

No: 
	Esta classe representa um único nó em uma lista encadeada. 
	Cada nó tem um valor e um proximo ponteiro. O valor é o dado que o nó está armazenando. 
	O proximo é um ponteiro para o próximo nó na lista. Se proximo é None, isso indica que este nó é o último nó na lista.

ListaEncadeada: 
	Esta é uma classe que geralmente acompanha a classe No. Ela gerencia os nós e fornece métodos para manipular a lista, como inserir um novo nó, remover um nó, 
	procurar um valor e etc. As listas encadeadas são úteis porque permitem inserções e remoções eficientes. 
	É possível inserir ou remover um nó em qualquer lugar da lista apenas ajustando alguns ponteiros, sem precisar mover ou reorganizar o restante dos elementos. 
	No entanto, elas têm a desvantagem de que o acesso a um elemento em uma posição específica é menos eficiente do que em um array ou lista Python, 
	pois você precisa percorrer a lista a partir do primeiro nó.

Como Executar
Para executar o programa, você precisa ter Python instalado em seu sistema (versão 3.11.6 conforme orientado), você deverá baixar o pacote do programa, 
abrir um prompt de comando e executar o seguinte comando (se estiver usando Windows):

1. cd c:\seu_diretorio\
2. python main.py
3. O menu será exibido e você pode navegar conforme desejado.

Versão
Este programa foi desenvolvido usando Python 3.8. Outras versões do Python 3 podem funcionar, mas não foram testadas.

Contribuições
Contribuições para este projeto são bem-vindas. Por favor, abra um problema ou faça um pull request se você tiver alguma melhoria ou correção para sugerir.
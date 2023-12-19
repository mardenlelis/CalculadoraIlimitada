from no import No   

class ListaEncadeada():
    """Inicializa a lista ligada com uma cabeça vazia."""
    def __init__(self):
        self.cabeca = None
    
    """Adiciona um novo nó com o valor especificado no final da lista."""
    def inserir_no(self, valor):
        try:
            if not self.cabeca:
                self.cabeca = No(valor)
            else:
                atual = self.cabeca
                while atual.proximo:
                    atual = atual.proximo
                atual.proximo = No(valor)
        except Exception as e:
            print("Erro: {}".format(str(e)))
            raise

       
    def somar_listas(self, outra_lista):
        resultado = ListaEncadeada()
        carry = 0
        atual_self = self.cabeca
        atual_outra = outra_lista.cabeca

        while atual_self is not None or atual_outra is not None or carry > 0:
            valor_self = atual_self.valor if atual_self is not None else 0
            valor_outra = atual_outra.valor if atual_outra is not None else 0

            soma = valor_self + valor_outra + carry
            carry = soma // 10 
            resultado.inserir_no(soma % 10)

            if atual_self is not None: atual_self = atual_self.proximo
            if atual_outra is not None: atual_outra = atual_outra.proximo

        return resultado
    
    def multiplicar_listas(self, outra_lista):
        resultado_final = ListaEncadeada()
        atual1 = self.cabeca
        posicao1 = 0

        while atual1 is not None:
            carry = 0
            resultado_parcial = ListaEncadeada()
            for _ in range(posicao1):
                resultado_parcial.inserir_no(0)

            atual2 = outra_lista.cabeca
            while atual2 is not None:
                multiplicacao = atual1.valor * atual2.valor + carry
                carry = multiplicacao // 10
                resultado_parcial.inserir_no(multiplicacao % 10)

                atual2 = atual2.proximo

            if carry > 0:
                resultado_parcial.inserir_no(carry)

            resultado_final = resultado_final.somar_listas(resultado_parcial)
            atual1 = atual1.proximo
            posicao1 += 1

        return resultado_final
   
    def converter_lista_para_numero(self):
        atual = self.cabeca
        numero_str = ""
        while atual:
            numero_str += str(atual.valor)
            atual = atual.proximo
        return int(numero_str)
    
    """Cria uma lista ligada a partir de um número inteiro."""
    @staticmethod
    def criar_lista(numero_str):        
        lista_encadeada = ListaEncadeada()
        for digito in reversed(str(numero_str)): # Inverte a string para começar pelo dígito menos significativo
            if digito.isdigit():
                lista_encadeada.inserir_no(int(digito))
            else:             
                raise ValueError("O valor {} não é um número válido.".format(digito))
        return lista_encadeada
    
    """Retorna uma representação em string da lista ligada."""
    def __str__(self) -> str:       
        atual = self.cabeca
        lista = []
        while atual:
            lista.append(str(atual.valor))
            atual = atual.proximo
        return ''.join(reversed(lista))

    

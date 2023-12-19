from lista_encadeada import ListaEncadeada
from tkinter import filedialog
from tkinter import Tk
from tkinter import messagebox
import sys

class CalculadoraIlimitada():

    def __init__(self) -> None:
        self.v1 = None
        self.v2 = None
        self.v3 = None 
        self.v4 = None
    
    lista_encadeada = ListaEncadeada()

    def ler_valores(self):
        try:
            print("Selecione o primeiro arquivo com a lista encadeada:")
            root = Tk()        
            root.update() 
            arquivo = filedialog.askopenfilename()                     
            if arquivo:
                with open(arquivo, 'r') as file:
                    print("Lendo o arquivo: {}".format(arquivo))                    
                    numero_str = file.read().strip()
                    resultado = self.lista_encadeada.criar_lista(str(numero_str))
                    print("Arquivo lido com sucesso. Estrutura de dados criada.")    
                    root.destroy()                
            else:                
                print("Nenhum arquivo selecionado.")
                resultado = None
            return resultado
        except Exception as e:
            print(f"Erro ao ler o arquivo: {e}")
            raise
        
        
    def somar_valores(self):
        try:
            if self.valida_arquivo_vazio():          
                self.v3 = self.v1.somar_listas(self.v2)
                print("Soma dos valores: \n {} + {} = {}".format(str(self.v1), str(self.v2), str(self.v3)))
        except Exception as e:
            print("Erro: {}".format(str(e)))
            raise

    def multiplicar_valores(self):
        try:
            if self.valida_arquivo_vazio():  
                self.v4 = self.v1.multiplicar_listas(self.v2)
                print("Produto dos valores: \n {} * {} = {}".format(str(self.v1), str(self.v2), str(self.v4)))
        except Exception as e:
            print("Erro: {}".format(str(e)))
            raise


    def salvar_resultados(self):
        try:
            if self.valida_arquivo_vazio():               
                root = Tk()                
                root.update() 
                arquivo = filedialog.asksaveasfilename(defaultextension=".txt")
                if arquivo:
                    with open (arquivo, 'w') as file:
                        str_soma = "A soma dos valores de {} + {} = {}\n".format(str(self.v1), str(self.v2), str(self.v3))
                        file.write(str_soma)
                        str_multiplicacao = "A multiplicação dos valores de {} * {} = {}\n".format(str(self.v1), str(self.v2), str(self.v4))
                        file.write(str_multiplicacao)
                        root.destroy()
                else:
                    print("Nenhum arquivo foi selecionado para salvar.")
        except Exception as e:
            print("Erro: {}".format(str(e)))
            raise

    def valida_arquivo_vazio(self):
        try:
            retorno = False
            if self.v1 is None and self.v2 is None:
                print("Valores não definidos para v1 e v2.")
                retorno = False
            elif self.v1 is None and self.v2 is not None:
                print("valores não definidos para v1.")
                retorno = False
            elif self.v1 is not None and self.v2 is None:
                print("Valores não definidos para v2.")       
                retorno = False
            else:
                retorno = True
        except Exception as e:
            print("Erro: {}".format(str(e)))
        finally:
            return retorno

    def sair_calculadora(self):
        try:
            root = Tk()
            root.withdraw()
            root.update() 
            resposta_usuario = messagebox.askyesno("Sair", "Você tem certeza que deseja encerrar a calculadora?")            
            if resposta_usuario:
                sys.exit()
        except Exception as e:
            print(f"Erro ao tentar sair: {e}")
        finally:
            root.destroy()

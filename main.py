from funcoes_calculadora import CalculadoraIlimitada

def menu_principal():
    
    try:   

        calculadora = CalculadoraIlimitada()

        opcoes_menu = {
            '1': lambda: setattr(calculadora, 'v1', calculadora.ler_valores()),
            '2': lambda: setattr(calculadora, 'v2', calculadora.ler_valores()),
            '3': lambda: calculadora.somar_valores(),
            '4': lambda: calculadora.multiplicar_valores(),
            '5': lambda: calculadora.salvar_resultados(),
            '6': lambda: calculadora.sair_calculadora()
        }
        
        while True:
            
            print("\nCalculadora de Precisão Ilimitada")
            print("1 - Ler o primeiro valor do arquivo (V1)")
            print("2 - Ler o segundo valor do arquivo (V2)")
            print("3 - Somar V1 com V2 e gerar um terceiro valor (V3)")
            print("4 - Multiplicar V1 por V2 e gerar um terceiro valor (V3)")
            print("5 - Salvar o resultado (V3) em um arquivo")
            print("6 - Sair da calculadora")

            escolha = input("Digite a opção desejada: ")
            acao = opcoes_menu.get(escolha)

            if acao:
                acao()
            else:
                print("Opção inválida. Tente novamente.")
    except Exception as e:
        print("Erro: {}".format(str(e)))
        raise

if __name__ == "__main__":    
        menu_principal()
  
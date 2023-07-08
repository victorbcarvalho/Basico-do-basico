class ControleRemoto:
    
    def __init__(self, televisao, comodo) -> None:
        self.televisao = televisao
        self.comodo = comodo
        
    def avancar_canal(self) -> None:
        print("Canal avançado!")
    
    def voltar_canal(self) -> None:
        print("Voltar o canal")
        
    def escolher_canal(self, canal) -> None:
        print(f"Alterado para o canal {canal}")
        
controle_sala = ControleRemoto("samsung", "sala")
controle_sala.comodo
controle_sala.televisao
controle_sala.avancar_canal()
controle_sala.escolher_canal(4)

controle_quarto = ControleRemoto("LG", "quarto")
print(controle_quarto.comodo)
print(controle_quarto.televisao)

from terrenos.quadrado import TerrenoQuadrado
from terrenos.retangulo import TerrenoRetangulo
from engenheiro import Engenheiro

engenheiro = Engenheiro("Geraldo")
terrenoQuadrado = TerrenoQuadrado(4)
terrenoRetangulo = TerrenoRetangulo(3,4)

engenheiro.medir_perimetro(terrenoQuadrado)
engenheiro.medir_perimetro(terrenoRetangulo)

engenheiro.medir_area(terrenoQuadrado)
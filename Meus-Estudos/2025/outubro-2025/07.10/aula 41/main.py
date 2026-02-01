from classes import Escritor
from classes import Caneta
from classes import MaquinaDeEscrever


escritor = Escritor('Ana')
caneta = Caneta('Compactor')
maquina = MaquinaDeEscrever()

escritor.ferramenta = maquina
escritor.ferramenta.escrever()

del escritor
print(caneta.marca)
maquina.escrever()


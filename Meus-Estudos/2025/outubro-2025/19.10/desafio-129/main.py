"""
Faça uma classe Aluno com atributos: nome,
matricula, notas (lista). Inclua método
media e situacao (aprovado/reprovado).
"""
from classes import Aluno

a = Aluno('Ana', 232345)
a.inserir_nota()
a.calc_media()
a.situacao()

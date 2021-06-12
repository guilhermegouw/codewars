"""
ENUNCIADO
# Desenvolva uma função de auto completar que busque em uma lista passada como
# parâmetro as palavras que se iniciam com a palavra também passada como
# parâmetro. Ignorar case (maiúsculas e minúsculas). Limitar retorno da função
# aos 5 primeiros resultados. Retornar em formato de lista.
#
# Tempo para resolver o problema: 40 minutos
# Início: 15:40
# Fim:
"""
from typing import List


def auto_completar(lista: List, palavra: str) -> List[str]:
    resultado = []

    palavra = palavra.lower()
    for word in lista:
        word_ = word.lower()
        if word_.startswith(palavra):
            resultado.append(word)
    return resultado[:5]

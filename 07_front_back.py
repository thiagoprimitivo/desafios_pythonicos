"""
07. front_back

Considere dividir uma string em duas metades.
Caso o comprimento seja par, a metade da frente e de trás tem o mesmo tamanho.
Caso o comprimento seja impar, o caracter extra fica na metade da frente.

Exemplo: 'abcde', a metade da frente é 'abc' e a de trás é 'de'.

Finalmente, dadas duas strings a e b, retorne uma string na forma:
a-frente + b-frente + a-trás + b-trás
"""


def front_back(a, b):
    size_a, rest_a = divmod(len(a), 2)
    size_b, rest_b = divmod(len(b), 2)

    first_string_a = a[0:size_a]
    last_string_a = a[size_a:]

    first_string_b = b[0:size_b]
    last_string_b = b[size_b:]

    if rest_a > 0:
        first_string_a = a[0:size_a + rest_a]
        last_string_a = a[size_a + rest_a:]

    if rest_b > 0:
        first_string_b = b[0:size_b + rest_b]
        last_string_b = b[size_b + rest_b:]

    final_string = ''.join([first_string_a, first_string_b, last_string_a, last_string_b])

    return final_string


# --- Daqui para baixo são apenas códigos auxiliáries de teste. ---

def test(f, in_, expected):
    """
    Executa a função f com o parâmetro in_ e compara o resultado com expected.
    :return: Exibe uma mensagem indicando se a função f está correta ou não.
    """
    out = f(*in_)

    if out == expected:
        sign = '✅'
        info = ''
    else:
        sign = '❌'
        info = f'e o correto é {expected!r}'

    print(f'{sign} {f.__name__}{in_!r} retornou {out!r} {info}')


if __name__ == '__main__':
    # Testes que verificam o resultado do seu código em alguns cenários.
    test(front_back, ('abcd', 'xy'), 'abxcdy')
    test(front_back, ('abcde', 'xyz'), 'abcxydez')
    test(front_back, ('Kitten', 'Donut'), 'KitDontenut')

"""
c_wrapper.py
Módulo de integração C/Python do PIM
------------------------------------------------
Responsável por conectar o código Python com a
biblioteca C (avg.dll), que realiza cálculos
de média e classificação dos alunos.
------------------------------------------------"""

import ctypes

# === Carregamento da biblioteca C ===
# Caminho absoluto do arquivo DLL gerado pelo código C.
lib = ctypes.CDLL("C:\\Users\\gabri\\OneDrive\\Desktop\\PROJETO PIM 2.0\\c_modules\\avg.dll")

# === Definição dos tipos de parâmetros e retorno ===
# Função calcular_media: recebe vetor de floats e um inteiro (tamanho), retorna float.
lib.calcular_media.argtypes = [ctypes.POINTER(ctypes.c_float), ctypes.c_int]
lib.calcular_media.restype = ctypes.c_float

# Função classificar_media: recebe um float, retorna string (char*).
lib.classificar_media.argtypes = [ctypes.c_float]
lib.classificar_media.restype = ctypes.c_char_p


# === Função principal de integração ===
def processar_aluno_c(aluno_dict):
    """
    Recebe um dicionário de aluno com as notas,
    envia os dados para o módulo C, obtém a média
    e o status (classificação), e retorna o dicionário atualizado.
    """
    # Converte lista de notas em vetor C (float[])
    notas = (ctypes.c_float * len(aluno_dict["notas"]))(*aluno_dict["notas"])

    # Calcula média e status usando funções da DLL
    media = lib.calcular_media(notas, len(aluno_dict["notas"]))
    status = lib.classificar_media(media).decode("utf-8")

    # Atualiza o dicionário do aluno
    aluno_dict["media"] = media
    aluno_dict["status"] = status

    return aluno_dict


# === Teste manual do módulo ===

if __name__ == "__main__":
    print("= Teste manual do módulo C Wrapper =")
    exemplo = {"nome": "Aluno Teste", "notas": [7.0, 8.5, 6.5]}
    resultado = processar_aluno_c(exemplo)
    print("Resultado do processamento:", resultado)
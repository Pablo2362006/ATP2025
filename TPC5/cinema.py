"""
Gestão simples de salas de cinema.
Modelo:
Cinema = [Sala]
Sala = (nlugares, vendidos, filme)
nlugares = int
filme = str
vendidos = [int]

Funções implementadas:
- listar(cinema)
- disponivel(cinema, filme, lugar)
- vendebilhete(cinema, filme, lugar)
- listardisponibilidades(cinema)
- inserirSala(cinema, sala)
- removerSala(cinema, filme)
- procurar_sala_por_filme(cinema, filme)

Interface de texto com menu.
"""

from typing import List, Tuple, Optional

Sala = Tuple[int, List[int], str]
Cinema = List[Sala]


def listar(cinema: Cinema) -> None:
    """Lista todos os filmes em exibição."""
    if not cinema:
        print("Não existem salas no cinema.")
        return
    print("Filmes em exibição:")
    for sala in cinema:
        nlug, vendidos, filme = sala
        print(f"- {filme}")


def procurar_sala_por_filme(cinema: Cinema, filme: str) -> Optional[int]:
    """Retorna o índice da sala onde o filme está a ser exibido, ou None."""
    for i, sala in enumerate(cinema):
        if sala[2].lower() == filme.lower():
            return i
    return None


def disponivel(cinema: Cinema, filme: str, lugar: int) -> bool:
    """True se o lugar está livre na sala onde o filme é exibido."""
    idx = procurar_sala_por_filme(cinema, filme)
    if idx is None:
        print(f"Filme '{filme}' não encontrado no cinema.")
        return False
    nlug, vendidos, _ = cinema[idx]
    if lugar < 1 or lugar > nlug:
        print(f"Lugar {lugar} inválido. A sala tem {nlug} lugares (1-{nlug}).")
        return False
    return lugar not in vendidos


def vendebilhete(cinema: Cinema, filme: str, lugar: int) -> Cinema:
    """Regista venda de bilhete: retorna novo cinema com o lugar adicionado à lista de vendidos."""
    idx = procurar_sala_por_filme(cinema, filme)
    if idx is None:
        print(f"Filme '{filme}' não encontrado.")
        return cinema
    nlug, vendidos, nome_filme = cinema[idx]
    if lugar < 1 or lugar > nlug:
        print(f"Lugar {lugar} inválido para a sala (1-{nlug}).")
        return cinema
    if lugar in vendidos:
        print(f"Lugar {lugar} já está ocupado.")
        return cinema
    # criar cópia do cinema e atualizar a sala
    nova_sala: Sala = (nlug, vendidos + [lugar], nome_filme)
    novo_cinema = cinema.copy()
    novo_cinema[idx] = nova_sala
    print(f"Bilhete vendido para '{nome_filme}', lugar {lugar}.")
    return novo_cinema


def listardisponibilidades(cinema: Cinema) -> None:
    """Para cada sala, mostra o filme e o número de lugares disponíveis."""
    if not cinema:
        print("Não existem salas no cinema.")
        return
    print("Disponibilidades por sala:")
    for sala in cinema:
        nlug, vendidos, filme = sala
        disponiveis = nlug - len(vendidos)
        print(f"- {filme}: {disponiveis} lugar(es) disponíveis ({len(vendidos)} vendidos).")


def inserirSala(cinema: Cinema, sala: Sala) -> Cinema:
    """Insere uma nova sala se o filme não existir ainda; retorna novo cinema."""
    _, _, filme = sala
    if procurar_sala_por_filme(cinema, filme) is not None:
        print(f"Já existe uma sala a exibir '{filme}'. Não foi adicionada.")
        return cinema
    novo_cinema = cinema.copy()
    novo_cinema.append(sala)
    print(f"Sala para '{filme}' adicionada com {sala[0]} lugares.")
    return novo_cinema


def removerSala(cinema: Cinema, filme: str) -> Cinema:
    """Remove a sala que exibe o filme e retorna o novo cinema."""
    idx = procurar_sala_por_filme(cinema, filme)
    if idx is None:
        print(f"Filme '{filme}' não encontrado.")
        return cinema
    novo_cinema = cinema.copy()
    del novo_cinema[idx]
    print(f"Sala que exibia '{filme}' removida.")
    return novo_cinema


def mostrar_menu():
    print('\n=== Gestão de Cinema ===')
    print('1 - Listar filmes')
    print('2 - Verificar disponibilidade de lugar')
    print('3 - Vender bilhete')
    print('4 - Listar disponibilidades')
    print('5 - Inserir sala')
    print('6 - Remover sala')
    print('7 - Mostrar salas (detalhado)')
    print('0 - Sair')


def mostrar_salas_detalhado(cinema: Cinema) -> None:
    if not cinema:
        print('Não existem salas.')
        return
    for i, sala in enumerate(cinema, start=1):
        nlug, vendidos, filme = sala
        vendidos_sorted = sorted(vendidos)
        print(f"Sala {i}: '{filme}' - capacidade {nlug}, vendidos {len(vendidos)} -> lugares ocupados: {vendidos_sorted}")


def main():
    cinema: Cinema = []
    # exemplo: pré-popular com duas salas
    cinema = inserirSala(cinema, (150, [], 'Twilight'))
    cinema = inserirSala(cinema, (200, [], 'Hannibal'))

    while True:
        mostrar_menu()
        escolha = input('Escolha uma opção: ').strip()
        if escolha == '1':
            listar(cinema)
        elif escolha == '2':
            filme = input('Filme: ')
            try:
                lugar = int(input('Lugar (número): '))
            except ValueError:
                print('Número inválido')
                continue
            dispon = disponivel(cinema, filme, lugar)
            print('Disponível' if dispon else 'Ocupado/Inválido')
        elif escolha == '3':
            filme = input('Filme: ')
            try:
                lugar = int(input('Lugar (número): '))
            except ValueError:
                print('Número inválido')
                continue
            cinema = vendebilhete(cinema, filme, lugar)
        elif escolha == '4':
            listardisponibilidades(cinema)
        elif escolha == '5':
            filme = input('Filme: ')
            try:
                nlug = int(input('Número de lugares: '))
            except ValueError:
                print('Número inválido')
                continue
            cinema = inserirSala(cinema, (nlug, [], filme))
        elif escolha == '6':
            filme = input('Filme a remover: ')
            cinema = removerSala(cinema, filme)
        elif escolha == '7':
            mostrar_salas_detalhado(cinema)
        elif escolha == '0':
            print('Até breve!')
            break
        else:
            print('Opção inválida')


if __name__ == '__main__':
    main()

import webbrowser
new = 2

ANIMES = '--animes--'
SERVERS = '--servidores--'

animes = []
servers = []

def init_animes():

    animes.clear()

    my_file = open('open_videos.txt', 'r')

    trigger = False

    for names in my_file:
        name = names.rstrip('\n')

        if name == SERVERS:
            return

        if trigger:
            animes.append(name)

        if name == ANIMES:
            trigger = True
    
    my_file.close()

def init_servers():

    servers.clear()

    my_file = open('open_videos.txt', 'r')

    trigger = False

    for names in my_file:
        name = names.rstrip('\n')

        # if nome == OUTRA_FUNCIONALIDADE:
        #     return

        if trigger:
            servers.append(name)

        if name == SERVERS:
            trigger = True

    my_file.close()

def list_animes():

    print('Lista de Animes: \n')

    for anime in animes:
        new_anime = anime.replace('-', ' ')
        new_anime = new_anime.replace('/', '')
        print(animes.index(anime)+1, '-', new_anime)

def list_servers():

    print('Lista de Servidores: \n')

    for server in servers:
        new_server = server.replace('https://', '')
        new_server = new_server.split('/')
        print(servers.index(server)+1, '-', new_server[0])

def define_domain():
    
    option = True
    site = 0

    while option:

        list_servers()
        site = (int(input('\nQual site acima eu devo usar?! -> ')))-1

        if site < 0 or site > len(servers)-1:
            print('\nSeleção de site inválida! Tente Novamente!\n')
        else:
            option = False

    return site

def define_page():

    option = True
    page = 0

    while option:

        list_animes()
        page = (int(input('\nQual anime acima eu devo usar?! -> ')))-1

        if page < 0 or page > len(animes)-1:
            print('\nSeleção de anime inválida! Tente Novamente!\n')
        else:
            option = False

    return page

def build_url(domain, page):
    return servers[domain]+animes[page]

def open_single_page():
    url = build_url(define_domain(), define_page())
    webbrowser.open(url, new=new)

def open_all_pages():
    domain = define_domain()

    for page in animes:
        url = build_url(domain, animes.index(page))
        webbrowser.open(url, new=new)

def menu():

    option = 0

    print('\n')
    print('1 - Abrir um Anime\n')
    print('2 - Abrir todos Animes\n')
    print('3 - Listar Animes\n')
    print('4 - Listar Sites\n')
    print('5 - Recarregar Listas\n')
    print('0 - Sair\n')
    option = int(input('Quer fazer o que?! -> '))

    if option == 1:
        print('\n')
        open_single_page()
        return option

    elif option == 2:
        print('\n')
        open_all_pages()
        return option

    elif option == 3:
        print('\n')
        list_animes()
        return option

    elif option == 4:
        print('\n')
        list_servers()
        return option

    elif option == 5:
        print('\n')
        init_animes()
        init_servers()
        return option

    elif option == 0:
        print('\nPrograma Finalizado!')
        return option

    else:
        print('\nOpção inválida! Tente Novamente!')
        return option

if __name__ == '__main__':

    option = 1

    init_animes()
    init_servers()

    while option != 0:
        option = menu()
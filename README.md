# downTube pre-alpha v0.0.2 ~AnthonyBata1

> __Sumário :_
> 1. __Introdução :_
> 2. __Requisitos :_
>     - _Dependências PIP_
> 3. __Patch Notes :_
>     - _v.0.0.1_
>     - _v.0.0.2_

## __Introdução :_
Baixe vídeos e áudios direto YouTube usando Python em melhor qualidade.

Primeiro projeto postado aqui no GitHub, a ideia surgiu de madrugada, quando me lembrei das complicações que tive para baixar vídeo ou áudio do YouTube.

Você pode usá-lo à vontade, este programa pode até salvá-lo algum dia. :D


##  __Requisitos :_ 
- Ter instalado no pip PyTube e MoviePy.
  -  Caso não tenha segue os comando para por no terminal. (logo criarei um executável que funcione)
      ```bash
      $ pip install pytube

      $ pip install moviepy
      ```

## __Bugs :_
1. Algumas vezes o Download demora muito, então tenha que reinicializar o software novamente (ainda estou verificando este problema).

2. Em alguns computadores as pastas de download não estão sendo criadas e _Crashando_ o programa.
    - Provavelmente seja algum problema com permissão de _Super Usuário_ ou _Administrador_.

## __Patch Notes :_
### __Versão Pré-Alpha 0.0.1:
___Atualizações:
1. Criado a primeira versão do downTube onde eu ainda vou criar uma branch para a versão do mesmo. (iniciante em Git)

- Primeiro commit do projeto.

### __Versão Pré-Alpha 0.0.2:_
__Atualizações:
1. Nesta versão foi retirada a escolha manual de pasta de download e alocada na pasta raiz do projeto, para que no futuro seja na pasta padrão de download do usuário.

2. Foi retirado algumas partes do código que não estavam sendo utilizadas para nada.

3. Melhorias de texto para a interface foram implementadas para melhor entendimento do usuário.

#### __Bugs Corrigidos :
- #001 - Foi corrigido um bug onde o sistema simplesmente fechava quando perguntava se a URL estava certa e o usuário respondia que "não".

- #002 - Depois que a pasta de Downloads foi alocado para uma padrão os arquivos não tem como mais ser salvo no local errado e ser "perdido" pelo usuário.

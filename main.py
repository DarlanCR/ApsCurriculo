"""
Requisitos: 1 - O programa principal pode ter no máximo 10 linhas;
2 - As funcionalidades deve ser implementadas em funções e chamadas no programa principal ou outras funções
3 - Deve ser postado no portal a solução
4 - Deve ter no mínimo ter 5 informações sendo no mínimo uma LISTA de informações sem quantidade,
devendo utilizar a estrutura de repetição WHILE;
5 - Ter uma foto;
6 - O currículo deve ter fonte diferente e cores (opcional ter utilização de CSS). O layout do currículo deve ser apresentável,
em caso negativo, o aluno poderá perder os pontos resultantes da apresentação técnica
7 - O programa deve gerar um arquivo .html
"""

def habCont():
    testando = input("Deseja cadastrar outra habilidade? ")
    while testando == 'sim':
        habilidade()
        testando = input("Deseja cadastrar outra habilidade? ")

def habilidade():
    hab = input("Digite uma habilidade: ")
    return '''<li> ''' + hab + ''' </li>'''


def exp():
    print("\nEXPERIÊNCIAS")
    emp = input("Digite o nome da empresa: ")
    cargo = input("Digite seu cargo: ")
    data = input("Digite o ano que entrou: ")
    data2 = input("Digite o ano que saiu: ")
    return '''<h2>''' + emp + ''' </h2>\n<h3> ''' + cargo + '''</h3>\n<h4> ''' + data + '''-''' + data2 + '''</h4>'''


def expCont():
    i=0
    exp = []
    testando = input("Deseja cadastrar outra experiência? ")
    while testando == 'sim':
        i = + 1
        exp()
        vezes = exp[i]
        testando = input("Deseja cadastrar outra experiência? ")
        return exp[i]


def facul():
    print("\nFORMAÇÃO")
    form = input("Digite o curso: ")
    ano = input("Digite o ano em que se formou: ")
    curso = input("Digite em qual curso se formou: ")
    return '''<h2> ''' + form + ''' </h2>'''    ''' <h3> ''' + ano + ''' &mdash; <strong> ''' + curso + '''</strong> 
    </h3> '''


def faculCont():
    testando = input("Deseja cadastrar outra formação? ")
    while testando == 'sim':
        facul()
        testando = input("Deseja cadastrar outra formação? ")
        return facul()


def head():
    nome = input("Nome completo: ")
    nasc = input("Data de nascimento: ")
    email = input("Email: ")
    tel = input("Telefone: ")
    end = input("Endereço: ")
    cont = input("Deseja corrigir alguma informação? sim/não ")
    while cont == 'sim':
        info = input("Qual informação gostaria de corrigir:\n nome/nascimento/email/telefone/endereço ")
        if info == 'nome':
            nome = input("Nome completo: ")
        if info == 'nascimento':
            nasc = input("Data de nascimento: ")
        if info == 'email':
            email = input("Email: ")
        if info == 'telefone':
            tel = input("Telefone: ")
        if info == 'endereço':
            end = input("Endereço: ")
        cont = input("Deseja corrigir alguma informação? sim/não ")

    with open("apsCurriculo/index.html", "w", -1, "utf-8") as curriculo:
        curriculo.write('''<!DOCTYPE html>
<html lang="pt-BR">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Currículo</title>

    <link rel="stylesheet" type="text/css" href="http://yui.yahooapis.com/2.7.0/build/reset-fonts-grids/reset-fonts-grids.css" media="all" />
    <link rel="stylesheet" type="text/css" href="style.css" media="all" />

</head>

<body>

    <div id="doc2" class="yui-t7">
        <div id="inner">
            <div id="hd">
                <div class="yui-gc">
                    <div class="yui-u first">
                        <img src="https://icon-library.com/images/icon-for-user/icon-for-user-16.jpg">
                        <h1>''' + nome + '''</h1>
                        <h2>''' + nasc + '''</h2>
                    </div>
                    <div class="yui-u">
                        <div class="contact-info">
                            <h3><a href="mailto:''' + email + '''">''' + email + '''</a></h3>
                            <h3>''' + tel + '''</h3>
                            <h3>''' + end + '''</h3>
                        </div>
                    </div>
                </div>
            </div>

            <div id="bd">
                <div id="yui-main">
                    <div class="yui-b">
                        <div class="yui-gf">
                            <div class="yui-u first">
                                <h2>Habilidades</h2>
                            </div>
                            <div class="yui-u">
                                <ul class="talent">'''
                        + habilidade() + str(habCont()) +
                        '''</ul>
                            </div>
                        </div>
                        <div class="yui-gf">
                            <div class="yui-u first">
                                <h2>Experiência</h2>
                            </div>
                            <div class="yui-u">
                                <div class="job">'''
                        + exp() + str(expCont()) +
                        '''</div>
                            </div>
                        </div>
                        <div class="yui-gf last">
                            <div class="yui-u first">
                                <h2>Formação</h2>
                            </div>
                            <div class="yui-u">'''
                        + facul() + str(faculCont()) +

                        '''  </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>
</body>

</html>''')

    with open("apsCurriculo/style.css", "w") as css:
        css.write('''
        .msg {
    padding: 10px;
    background: #222;
    position: relative;
}

img {
    max-width: 150px;
}

.msg h1 {
    color: #fff;
}

.msg a {
    margin-left: 20px;
    background: #408814;
    color: white;
    padding: 4px 8px;
    text-decoration: none;
}

.msg a:hover {
    background: #266400;
}

body {
    font-family: Georgia;
    color: #444;
}

#inner {
    padding: 10px 80px;
    margin: 80px auto;
    background: #f5f5f5;
    border: solid #666;
    border-width: 8px 0 2px 0;
}

.yui-gf {
    margin-bottom: 2em;
    padding-bottom: 2em;
    border-bottom: 1px solid #ccc;
}

#hd {
    margin: 2.5em 0 3em 0;
    padding-bottom: 1.5em;
    border-bottom: 1px solid #ccc
}

#hd h2 {
    text-transform: uppercase;
    letter-spacing: 2px;
}

#bd,
#ft {
    margin-bottom: 2em;
}

#ft {
    padding: 1em 0 5em 0;
    font-size: 92%;
    border-top: 1px solid #ccc;
    text-align: center;
}

#ft p {
    margin-bottom: 0;
    text-align: center;
}

#hd h1 {
    font-size: 48px;
    text-transform: uppercase;
    letter-spacing: 3px;
}

h2 {
    font-size: 152%
}

h3,
h4 {
    font-size: 122%;
}

h1,
h2,
h3,
h4 {
    color: #333;
}

p {
    font-size: 100%;
    line-height: 18px;
    padding-right: 3em;
}

a {
    color: #990003
}

a:hover {
    text-decoration: none;
}

strong {
    font-weight: bold;
}

li {
    line-height: 24px;
    border-bottom: 1px solid #ccc;
}

p.enlarge {
    font-size: 144%;
    padding-right: 6.5em;
    line-height: 24px;
}

p.enlarge span {
    color: #000
}

.contact-info {
    margin-top: 7px;
}

.first h2 {
    font-style: italic;
}

.last {
    border-bottom: 0
}

.job {
    position: relative;
    margin-bottom: 1em;
    padding-bottom: 1em;
    border-bottom: 1px solid #ccc;
}

.job h4 {
    position: absolute;
    top: 0.35em;
    right: 0
}

.job p {
    margin: 0.75em 0 3em 0;
}

.last {
    border: none;
}

.skills-list ul {
    margin: 0;
}

.skills-list li {
    margin: 3px 0;
    padding: 3px 0;
}

.skills-list li span {
    font-size: 152%;
    display: block;
    margin-bottom: -2px;
    padding: 0
}

.talent {
    width: 32%;
    float: left
}

.talent h2 {
    margin-bottom: 6px;
}

#srt-ttab {
    margin-bottom: 100px;
    text-align: center;
}

#srt-ttab img.last {
    margin-top: 20px
}

.yui-gf .yui-u {
    width: 80.2%;
}

.yui-gf div.first {
    width: 12.3%;
}''')


head()

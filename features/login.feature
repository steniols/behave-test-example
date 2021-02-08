# language: pt

Funcionalidade: realizar login no OpenCMS

  # Contexto são ações que serão executadas antes de cada cenário.
  Contexto: acessar página de teste
    Dado que acesso a página de Login

  Cenário: acessar página de Login e realizar o login
    Dado que preencho o campo username com opensourcecms
    Dado que preencho o campo de password com opensourcecms
    Quando clico no botão login
    Então devo visualizar a tela inicial com No Employees Available
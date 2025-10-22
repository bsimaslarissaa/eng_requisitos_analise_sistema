**DOCUMENTAÇÃO DE REQUISITOS – Sistema de Funcionários**

**1. Introdução**

Nome do sistema: Sistema de Gerenciamento de Funcionários

Descrição geral: O sistema permite cadastrar, listar e buscar funcionários, armazenando seus dados (nome, cargo e salário) em memória.

**2. Técnicas Utilizadas**

**Entrevista com Stakeholders -** Essa técnica consiste em conversar diretamente com os envolvidos no projeto (clientes, usuários, gestores, etc.) para entender suas necessidades, expectativas e objetivos. 
É uma das etapas mais importantes do levantamento de requisitos, pois permite obter informações precisas e reais sobre o que o sistema deve fazer.

**Brainstorming -** É uma técnica em grupo usada para gerar e desenvolver ideias de forma criativa e colaborativa.
Durante o brainstorming, os participantes compartilham livremente suas sugestões para resolver problemas ou propor soluções que atendam às necessidades do projeto.

**Prototipagem -** Consiste em criar uma versão simplificada (protótipo) do sistema que será desenvolvido.
O objetivo é testar ideias, validar requisitos com os usuários e verificar se o projeto está seguindo na direção correta antes da implementação final.

**3. Requisitos funcionais** 

**RF01**	Adicionar funcionário: O sistema deve permitir cadastrar um funcionário informando nome, cargo e salário.

**RF02**	Listar funcionários:	O sistema deve exibir todos os funcionários cadastrados, com nome, cargo e salário formatado.

**RF03**	Buscar funcionário:	O sistema deve permitir buscar um funcionário pelo nome e exibir seu cargo e salário.

**RF04**	Encerrar sistema:	O sistema deve permitir ao usuário encerrar a execução escolhendo a opção “0 - Sair”.

**4. Requisitos não funcionais**

**RNF01**	Linguagem:	O sistema deve ser implementado em Python 3.

**RNF02**	Interface:	O sistema deve operar via interface de linha de comando (CLI).

**RNF03**	Limite de armazenamento:	O sistema deve permitir cadastrar no máximo 100 funcionários.

**RNF04**	Validação de entrada:	O sistema deve validar entradas de dados, impedindo valores inválidos para o salário.

**RNF05**	Desempenho:	As operações devem ser executadas instantaneamente para até 100 registros.

**5. Diagrama de Caso de Uso**

Ator : Usuário (Administrador ou RH), é quem interage com o sistema. Neste caso, iremos colocar o RH como principal autor.


![Diagrama sem nome (17)](https://github.com/user-attachments/assets/d7e2eba3-c953-4160-87d8-c3d0f191c9bf)


**6. Diagrama de atividades**

![Uploading Diagrama sem nome (18).jpg…]()




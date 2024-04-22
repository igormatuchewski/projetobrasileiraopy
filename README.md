# Projeto Brasileirão

Esse foi o meu primeiro projeto de Análise de Dados desenvolvido 100% via Python.
Utilizei a biblioteca Pandas para realizar todos os tratamentos de dados necessários, assim como criação de novas colunas e manipulação de outros dataframes. Apliquei também o Streamlit, biblioteca extremamente poderosa para desenvolvimento de dashboards com a possibilidade de criar diversas páginas, filtros e milhares de outras funcionalidades. A outra biblioteca utilizada foi o Pyploy Express para gerar gráficos interativos e também conectá-los com os filtros, tornando a dashboard dinâmica.
Considero o resultado obtido muito satisfatório, visto que foi o meu primeiro projeto que desenvolvi utilizando o Streamlit e o Pyplot Express, já havia utilizado o Pandas e o Matplotlib para realizar Análises Exploratórias. Apesar de ser fácil a compreensão e muito simples o desenvolvimento (comparado à outras linguagens de programação) considero o PowerBI ainda muito mais intuitivo e fácil de utilizar. É claro que conforme a utilização a velocidade de desenvolvimento também aumenta.
Embora atualmente (março/2024) eu ainda considero que minha capacidade de desenvolvimento de dashboards via PowerBI seja mais rápida e completa, há de se destacar pontos relevantes em que o Python se destaca quando comparamos ao PowerBI:

* Velocidade de leitura e processamento dos dados: quando trabalhamos com muitos dados conectados ao PowerBI e ainda mais, quando são tratados via Power Query, o carregamento e a visualização fica extremamente lenta, levando alguns segundos para carregar e, dependendo do tamanho do arquivo, até minutos;
* Limitação de linhas: o PowerBI possui uma limitação de 1.048.576 linhas *(fonte: https://support.microsoft.com/pt-br/office/power-query-especifica%C3%A7%C3%B5es-e-limites-no-excel-5fb2807c-1b16-4257-aa5b-6793f051a9f4)* o que pode ser algo muito negativo dependendo do negócio que estamos trabalhando, algo que não existe no Python;
* Liberdade de personalização: aqui nesse projeto fiz a utlilzação do Streamlit, nessa bilioteca em específico a customização não é o foco, se tornando menos customizável do que o PowerBI, no entanto, existe uma biblioteca chamada 'dash' que é muito mais capaz nesse quesito e pode superar o PowerBI.

  ## O Projeto em si

  Utilizei uma base de dados do Campeonato Brasileiro de 2003 até 2023, que trás alguns dados de todas essas edições e fiz algumas análises simples, visto que não há uma quantidade grande de dados disponíveis nesse dataset. O intuito aqui realmente foi explorar as bibliotecas, praticar e ver mais do que eram capazes no mundo dos Dados!

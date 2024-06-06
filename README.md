<table>
<tr>
<td>
<a href= "https://www.btgpactual.com/"><img src="./artefatos/img/Btg-logo-blue.png" alt="BTG Pactual" border="0" width="70%"></a>
</td>
<td><a href= "https://www.inteli.edu.br/"><img src="./inteli-logo.png" alt="Inteli - Instituto de Tecnologia e Liderança" border="0" width="30%"></a>
</td>
</tr>
</table>

# Projeto: *Reinforcement Matching*

# Grupo: *NeuroPricing*

# Integrantes:

* Allan Casado <allan.casado@sou.inteli.edu.br>
* Arthur Reis <arthur.reis@sou.inteli.edu.br>
* Gabriel Carneiro <gabriel.carneiro@sou.inteli.edu.br>
* Gabriel Nhoncanse <gabriel.nhoncanse@sou.inteli.edu.br>
* João Pedro Alcaraz <joao.alcaraz@sou.inteli.edu.br>
* Melyssa Rojas <melyssa.rojas@sou.inteli.edu.br>
* Vitor Barros <vitor.barros@sou.inteli.edu.br>

# Descrição

O projeto desenvolvido tem foco em Aprendizado por Reforço para aplicação com redes neurais artificiais, tem como objetivo principal a otimização da precificação de ativos de renda fixa sintética, visando alcançar uma rentabilidade equivalente a 100% do CDI. Este desafio envolve a identificação de combinações ideais de negociações à vista e à termo de ações, utilizando técnicas de aprendizado por reforço. O projeto tem como parceiro o BTG Pactual S.A, o maior banco de investimento da América Latina, e se concentra em aprimorar as rotinas diárias de precificação, aumentando a assertividade dos preços e reduzindo a necessidade de intervenções manuais.

# Configuração para desenvolvimento

## Pré-requisitos
* Ter o Python instalado na máquina. Recomenda-se o Python 3.8 ou superior.
* Conhecimento básico de operação do terminal ou linha de comando.
* Acesso aos dois notebooks Jupyter mencionados e ao arquivo requirements.txt.

## Passo a Passo

1. Configurar o Ambiente Virtual
Primeiro, é importante configurar um ambiente virtual. Isso garante que as dependências do projeto não afetem outras instalações do Python na máquina. Abra o terminal ou linha de comando e siga estes passos:

    1.1. Navegue até o diretório do projeto onde os notebooks e o requirements.txt estão salvos.

    1.2. Execute o comando para criar um ambiente virtual (substitua myenv pelo nome que desejar para o ambiente):
    ```
    python -m venv myenv
    ```

    1.3. Ative o ambiente virtual. No windows isso pode ser feito com o comando
    ```
    myenv\Source\activate
    ```

2. Instalar as Dependências

Com o ambiente virtual ativado, instale todas as dependências listadas no arquivo requirements.txt:
```
pip install -r requirements.txt
```

3. Executar o Primeiro Notebook (Pré-processamento)

    3.1 Inicie o Jupyter Notebook.

    3.2 Abra o arquivo de pré-processamento.

    3.3 Altere a variável "file_path" com o caminho da pasta que possui as bases de compra e venda, que devem ser nomeadas como "base2023_compra.xlsb" e "base2023_venda.xlsb".

    3.4 Executa todas as células do notebook, o que gerará um arquio ".txt", que será usando como input para o segundo notebook

4. Executar o Segundo Notebook (Agente e Ambiente)

    4.1 Executar as células de load dos dados e de definição do ambiente e do agente

    4.2 Caso queira treinar o agente novamente e salvar um novo modelo, rodar a penúltima célula

    4.3 Caso queira apenas utilizar o modelo já treinado para realizar inferência, rodar a última célula

# Tags

- Sprint 1
    - Entendimento de Negócios
    - Entendimento de Usuário
    - Modelagem da solução
- Sprint 2
    - Atualização README.md
    - Implementação sprint 2 code
- Sprint 3
    - Implementação sprint 3 code
- Sprint 4
    - Artigo Sprint 4
    - Adição sprint 4 notebook
- Sprint 5
    - Finalização artigo
    - Refatoração do código
    - Relatório final

## 📋 Licença/License

<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/">

<a property="dct:title" rel="cc:attributionURL">Grupo</a> by <a rel="cc:attributionURL dct:creator" property="cc:attributionName">Inteli, Allan Casado, Gabriel Nhoncanse, João Alcaraz, Arthur Reis, Gabriel Carneiro, Vitor Barros e Melyssa Rojas </a> is licensed under <a href="https://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" rel="license noopener noreferrer" style="display:inline-block;">Attribution 4.0 International</a>.</p>

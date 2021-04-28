# Usando MapReduce em Grandes Volumes de Dados: Job MapReduce


Este artigo foi inspirado no conteúdo do curso de Formação de Cientista de Dados, módulo Engenharia de Dados com Hadoop e Spark na Data Science Academy [http://www.datascienceacademy.com.br](http://www.datascienceacademy.com.br) 


O Hadoop MapReduce é uma ferramenta para escrever aplicativos que processam grandes quantidades de dados em paralelo em clusters de hardware de maneira confiável e tolerante a falha. O objetivo central deste artigo é abordar como trabalhar com MapReduce pode ser útil para uma empresa. Propõe-se, assim, apresentar um exemplo de análise de dados.


### Hipótese


Um cientista de dados é contratado para trabalhar em um projeto de análise com grande volume, na casa de milhões ou bilhões de registros. Aonde irá armazenar e processar esse volume de dados?

Se o profissional for trabalhar com banco de dados relacional, não terá ambiente distribuído a sua disposição, e ao executar a tarefa de análise não terá desempenho suficiente para o seu processo, e quando o trabalho estiver sendo processando, com milhões ou bilhões de registros, será inviável. 


###  Análise de Dados com Hadoop MapReduce


Trabalharemos neste exemplo, com um conjunto de dados pequeno em um container Docker com Apache Hadoop Pseudo Distribuido: Ambiente de teste.


### Pré-requisitos:  

- Máquina local ou virtual com sistema operacional Linux;
- [Python Fundamentos para Análise de Dados](https://www.datascienceacademy.com.br/course?courseid=python-fundamentos);
- [Java(TM) SE Runtime Environment (build 1.8.0_281-b09)](https://www.java.com/pt-BR/download/ie_manual.jsp?locale=pt_BR);
- [Docker instalado e configurado](https://www.docker.com/get-started); 
- [Apache Hadoop Pseudo Cluster instalado e configurado](https://github.com/carlosemsantana/docker-hadoop);
- [Anaconda Python instalado](https://www.anaconda.com/products/individual#Downloads);
- [MRJOB - Biblioteca de mapeamento e redução para Python](https://github.com/Yelp/mrjob);


### Definição do problema


Criar um programa para contabilizar quantos registros de transações e-commerce realizados em uma loja virtual na Internet foram aprovados, cancelados e abandonados desde que a loja foi inaugurada.

### Cenário atual
O servidor de banco de dados está hospedado em um Provedor de Serviços na Internet, e seu programa deve ser capaz de analisar e processar bilhões de registros.


### Proposição

Nesse caso, trazemos os dados para o Apache Hadoop HDFS, para que possamos usar as vantagens de ter um ambiente distribuído em cluster de computadores. Com isso será possível armazenar e processar grandes volumes de dados de forma distribuída. 

Uma vez que os registros estejam armazenados no HDFS será possível realizamos o trabalho de análise e processamento dos dados com o Apache Hadoop Map Reduce de maneira distribuída.

Trabalhar com Apache Hadoop Map Reduce é uma <u>sugestão</u>, alternativamente, podemos usar o Apache Spark, o Apache Storm, entretanto, o Apache Hadoop Map Reduce é o mais indicado, porque foi desenvolvido para processar volumes realmente grande de dados, na casa de petabyte ou yottabyte de dados.


# Atividades 


Para ilustrarmos este exemplo, vamos aproveitar o dataset gravado no artigo anterior <b>Importando Dados do MySQL para o HDFS com Sqoop</b> e considerar que o ambiente com Hadoop já existe. 

Datasert: [https://github.com/carlosemsantana/docker-mysql-hdfs](https://github.com/carlosemsantana/docker-mysql-hdfs)


#### Coleta dos dados



A primeira tarefa seria importar os dados do banco de dados relacional que está no Provedor de Serviços e gravar no HDFS. Esta é uma das atividades do Engenheiro de Dados, porém, em algumas situações o Cientista de Dados precisará exercer temporariamente este papel.


#### Examinar os dados


Quando terminar atividade de coleta de dados, copie os arquivos gerados do HDFS para sua máquina local para que possa examinar e entender os dados.


Exibir a fonte de dados:

<!-- #region -->
```bash 
$  hdfs dfs -ls /user/hadoop/pedido
``` 
<!-- #endregion -->

A fonte de dados com as transações da loja foi gravada no HDFS no diretório pedido.


![](img/hdfs-dfs-ls.png)


Baixar a fonte de dados:

<!-- #region -->
```bash 
$  hdfs dfs -get /user/hadoop/pedido/* /home/hadoop/fonteDados/
``` 
<!-- #endregion -->

![](img/get.png)


A fonte de dados com as transações da loja foi gravada na máquina local, agora, vamos examinar o conteúdo do arquivo e enteder os dados para criarmos o programa de análise que irá responder as pergutas do cliente.

<!-- #region -->
```bash 
$  head /home/hadoop/fonteDados/part-m-00000
``` 
<!-- #endregion -->

![](img/head.png)


No formato que os dados estão, será importante obter mais informações para ajudar no entendimento.


Em contato com equipe desenvolvimento do cliente, conseguimos nome e descrição dos atributos da fonte de dados disponibilizada.


![](img/desc-tabela.png)


Neste exercício o que precisamos responder: Quantas transações e-commerce realizadas na loja virtual foram aprovados, cancelados e abandonados desde que a loja foi inaugurada?


Estamos prontos para criar o programa que irá contabilizar registros e gerar a resposta para o cliente.


#### Programação


Para nos ajudar a escrever e executar jobs mapreduce usaremos a biblioteca open source [MRJOB](https://github.com/Yelp/mrjob) para Python.

<!-- #region -->
A instalação do MRJOB é simples, digite: 

```bash 
$ pip install mrjob 
```
<!-- #endregion -->

<!-- #region -->
Pronto! crie um arquivo de configuração do mrjob com nome de ```.mrjob.conf``` no diretório home do usuário hadoop, com seguinte conteúdo e identação: 

```bash
runners: 
	hadoop:
		python_bin: /home/hadoop/anaconda3/bin/python
```
<!-- #endregion -->

<!-- #region -->
```bash 
$ touch /home/hadoop/.mrjob.conf 
```
<!-- #endregion -->

```python
Script AvaliaFilme.py
```

```python

```

```python

```

#### 4. Análise dos dados


### Workflow do MapReduce


<b>Agendamento</b> - Os jobs são divididos em pedaços menores chamados tarefas. As tarefas são agendadas pelo YARN (Gerenciador de recursos).<br>
<b>Localização de tarefas</b> - As tarefas são colocadas nos nodes que armazenam os segmentos de dados. O código é movido para onde o dado está.<br>
<b>Tratamento de erros</b> - Falhas são um comportamento esperado e no caso de falhas, as tarefas são automaticamente enviadas a outros nodes.<br>
<b>Sincronização dos dados</b> - Os dados são randomicamente agrupados e movidos entre os nodes. Imput e Output são coordenados pelo framework.



### YARN


Apache YARN é a camada de gerenciamento de recursos e agendamento de tarefas (jobs) do Hadoop, roda acima do HDFS. O Apache YARN é considerado 
como o sistema operacional de dados do Hadoop. A arquitetura do YARN fornece uma plataforma de processamento de dados de uso geral que não
se limita apenas ao MapReduce.









```python

```

# Resultados


Assinatura


# Referências:


- [http://www.datascienceacademy.com.br](http://www.datascienceacademy.com.br)<br>
- [https://hadoop.apache.org/docs/current/hadoop-mapreduce-client/hadoop-mapreduce-client-core/MapReduceTutorial.html](https://hadoop.apache.org/docs/current/hadoop-mapreduce-client/hadoop-mapreduce-client-core/MapReduceTutorial.html)<br>
- [https://hadoop.apache.org/docs/current/hadoop-yarn/hadoop-yarn-site/YARN.html](https://hadoop.apache.org/docs/current/hadoop-yarn/hadoop-yarn-site/YARN.html)<br>
- [https://hadoop.apache.org/docs/current/hadoop-project-dist/hadoop-hdfs/HdfsDesign.html](https://hadoop.apache.org/docs/current/hadoop-project-dist/hadoop-hdfs/HdfsDesign.html)<br>
- [https://github.com/Yelp/mrjob](https://github.com/Yelp/mrjob);

```python

```

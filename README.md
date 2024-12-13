== Fase I
Etapa exploratória em que alguns testes foram feitos para se avaliar a viabilidade do trabalho proposto e buscar uma linha de solução.

== Fase II
Códigos foram reescritos com mais generalidade e com algumas checagens básicas no script do método húngaro.

Geramos várias partições para testes, mas não chegamos a usar nem mesmo os 100_1000, pois o GPT-4o está limitado em 128k tokens.

Adicionamos a interação manual com o cliente do Abacus.ai. Apesar de usar a API ter sido a ideia original, esta não fez mais sentido quando percebeu-se que o limite de dados seria pequeno e que a variabilidade é praticamente nula para os mesmos prompts.

para rodar:

- instalar o pipenv e as dependências
- executar o experimento.py para visualizar o método húngaro (gera txt de resposta)

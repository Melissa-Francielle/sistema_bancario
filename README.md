# sistema_bancario
Crie um sistema bancario com as operações:
- Sacar
- Depositar
- Visualizar extrato 

Esse banco deseja modernizar suas operações e para isso escolheu a linguagem Python. 
Para a primeira versão do sistema devemos implementar apenas 3 operações - deposito, saque, extrato 


Operação de deposito 
Deve ser possível depositar valores positivos para a minha conta bancaria. A v1 do projeto trabalha apenas com 1 usuario, dessa forma não precisamos nos preocupar em identificar qual é o numero da agencia e conta bancaria. 
Todos os depositos devem ser armazenados em uma variavel e exibidos na operação de extrato. 

Operação de saque 
O sistema deve permitir realizar 3 saques diários com limite máximo de 500,00 por saque. Caso o usuário não tenha saldo em conta, o sistema deve exibir uma mensagem informando que não será possível sacar o dinheiro por falta de saldo 
Todos os saques devem ser armazenados em uma variavel e exibidos na operação de extrato.

Operação do extrato 
Essa operação deve listar todo os depositos e saques realizados na conta. No fim da listagem deve ser exibido o saldo atual da conta. 
Os valores devem ser exibidos utilizando o formato R$ XXX.XX, exemplo:  R$ 1500.45

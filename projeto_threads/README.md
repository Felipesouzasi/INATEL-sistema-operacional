# Password Cracker Multithreaded

## Descrição
Este projeto é uma aplicação Java que utiliza múltiplas threads para realizar um ataque de força bruta a uma senha numérica de 4 dígitos. Cada thread tenta descobrir a senha dentro de um intervalo específico, distribuindo a carga de trabalho para otimizar o tempo de execução.

## Como Funciona
1. O usuário informa o número de threads a serem utilizadas.
2. O usuário digita uma senha de 4 dígitos para ser "quebrada".
3. O programa cria múltiplas threads que tentam adivinhar a senha, dividindo o intervalo de tentativas entre si.
4. Assim que uma thread encontra a senha, todas as outras threads interrompem a execução.

## Estrutura do Código
- `Main.java`: 
  - Recebe a entrada do usuário.
  - Inicia o número de threads especificado.
  - Valida a senha fornecida.
- `PasswordBroken.java`:
  - Define a lógica da tentativa de quebra da senha.
  - Cada thread percorre um intervalo de números.
  - A primeira thread a encontrar a senha notifica as outras para interromperem suas execuções.

## Como Executar
### Pré-requisitos
- Java 8 ou superior instalado.
- Um terminal ou IDE compatível com Java.

### Compilando o Código
Abra o terminal na pasta onde está localizado o arquivo `Main.java` e execute:
```sh
javac Main.java
```

### Executando o Programa
Após compilar, execute o seguinte comando:
```sh
java Main
```

## Exemplo de Uso
```
Digite o número de threads: 
4
Digite a senha de 4 números a ser quebrada: 
1234
Thread 0 tentando a senha: 0000
Thread 1 tentando a senha: 2500
Thread 2 tentando a senha: 5000
Thread 3 tentando a senha: 7500
...
Senha encontrada: 1234 pela Thread 2
```

## Melhorias Futuras
- Implementar suporte para senhas alfanuméricas.
- Melhorar a eficiência com otimizações baseadas em heurísticas.
- Criar uma interface gráfica para facilitar a interação do usuário.

## Autor
Desenvolvido por Felipe Santos de Souza.

## Licença
Este projeto é de código aberto sob a licença MIT. Sinta-se à vontade para modificá-lo e melhorá-lo!

Este é um script Python simples que reproduz um som de alarme com base em uma probabilidade definida pelo usuário.

Como funciona
O script solicita que o usuário insira um número de 0 a 100, que representa a chance percentual de o alarme soar. Em seguida, ele gera um único número inteiro aleatório entre 0 e 99.

Em um loop que é executado a cada segundo, o script verifica se o número inserido pelo usuário é maior ou igual ao número gerado aleatoriamente. Se a condição for atendida, o som de alarme (alarme.mp3) é reproduzido, uma mensagem de confirmação é impressa e o programa é encerrado.

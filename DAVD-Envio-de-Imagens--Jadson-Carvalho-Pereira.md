# Aplicações de redes para transferência de arquivos

Soluções de redes voltadas para Centro de Educação e Ciências Humanas CECH

## Modelo de Proposta de Protocolo

1. Autor: Jadson Carvalho Pereira

2. Descrição

> Essa aplicação oferece a possibilidade do envio de imagens para o servidor. Tal funcionalidade será utilizada em uma tarefa específica do curso de Design na qual é necessário entregar um logotipo.

3. Protocolo de transporte: TCP

4. Número de porta: 50000

5. Formato das mensagens
- 'enviar' 'nome da turma' 'caminho da imagem': faz o envio de imagens para o servidor, e essas serão salvas na pasta da turma especificada.
- 'ajuda': lista as mensagens que são aceitas.

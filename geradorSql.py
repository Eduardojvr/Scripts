with open('arquivo.txt', 'w') as arquivo:
    for i in range(1000):
        linha = ''
        if(i == 0 ):
            linha = f"INSERT into parcela values(default, 'testes',	'450.0',	'2'	, '2023-03-01',	'6',	'0', null,'01754399150','6', '9', null, '0','1'),\n" 
        else:
            linha = f"(default, 'testes',	'450.0',	'2'	, '2023-03-01',	'6',	'0', null,'01754399150','6', '9', null,'0','1'),\n"
            
        
        arquivo.write(linha)
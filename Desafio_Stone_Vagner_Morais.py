class desafio:
    def teste():
        listaEmails = [ 'a_vanessinha_1990@hotmail.com', 'a3sign@pandora.be', 'aaanika2@hotmail.com', 'aaron2003s@bol.com.br', 'aaron--21@hotmail.com', 'abidoral@hotmail.com', 'abk_333@hotmail.com', 'abner_bim@hotmail.com', 'abner_bim@hotmail.com', 'acacio_divix@hotmail.com', 'academia.boaforma@yahoo.com.br', 'ac-ferian@bol.com.br', 'acordarsono@hotmail.com', 'acsa_lim@yahoo.com.br', 'adamyth@gmail.com', 'add_ae_jente@yahoo.com.br', 'addgeral@gmail.com', 'addyevusk@yahoo.com.br', 'adeozemir@yahoo.com.br', 'adhaha@gmail.com', 'adhaha@gmail.com', 'adidas__star@hotmail.com', 'adilio-vidaloka@yahoo.com.br', 'adilson.mariano5@terra.com.br', 'admgerald1@yahoo.com.br', 'adri_barboza@hotmail.com', 'adriaens@pandora.be', 'adrian_boyzinhu@yahoo.com.br', 'adriana_lemes_farias@hotmail.com', 'adrianacpx@yahoo.com.br', 'adriane_do_prado@yahoo.com.br']

        listaMercado = [
                       {'nomeItem' : 'arroz',
                        'quantidade': 1,
                        'preco': 1002},
                       {'nomeItem' : 'feijao',
                        'quantidade': 3,
                        'preco': 1500},
                       {'nomeItem' : 'frango',
                        'quantidade': 7,
                        'preco': 1726},
                       {'nomeItem' : 'carne',
                        'quantidade': 11,
                        'preco': 2009},
                       {'nomeItem' : 'leite',
                        'quantidade': 13,
                        'preco': 1562},
                       {'nomeItem' : 'iogurte',
                        'quantidade': 20,
                        'preco': 50},
                       {'nomeItem' : 'cerveja',
                        'quantidade': 4,
                        'preco': 63}
                        ]
                        
        return desafio.RateioCompras(listaMercado, listaEmails)


    def RateioCompras(listaMercado, listaEmails):
        if (not(listaEmails)):
            return('Erro: a lista de emails está vazia')
        if (not(listaMercado)):
            return('Erro: a lista de mercado está vazia')

        # Iniciando variáveis
        valorTotalItem = 0
        valorTotalCompras = 0
        valorPorPessoa = 0
        index = 1
        print(len(listaEmails))

        # Removendo emails duplicados
        listaEmails = list(dict.fromkeys(listaEmails))
        print(len(listaEmails))

        # Início do cálculo do rateio
        for item in listaMercado:
            valorTotalItem = item['quantidade'] * item['preco']
            valorTotalCompras += valorTotalItem
            quantidadePessoas = len(listaEmails)
            valorPorPessoa = valorTotalCompras // quantidadePessoas
            resto = valorTotalCompras % quantidadePessoas

        dicionarioRateio = {}
        for email in listaEmails:
            dicionarioRateio[email] = valorPorPessoa
        print(resto)


        # Distribuindo o resto da divisão entre os participantes do rateio
        while(resto > 0):
            dicionarioRateio[listaEmails[-index]] += 1
            resto -= 1
            index += 1

        for valor in dicionarioRateio:
            dicionarioRateio[valor] = str(dicionarioRateio[valor]) + ' centavos'
        return dicionarioRateio

#Início do Código Principal
if __name__ == "__main__":

    resultado = desafio.teste()
    print(resultado)

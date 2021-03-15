from BancoNapp.contas.Conta import Conta


class ContaPoupanca(Conta):
    def __init__(self,  **kwargs):
        """
        Construtor da classe Poupanca.
        Extrai do dicionário kwargs a profissao do correntista.
        """
        
        self.profissao = kwargs.get('profissao', '')
        self.nome = kwargs.get('nome', None)
        self.saldo = kwargs.get('saldo', '')
        # test saldo positivo
        super(ContaPoupanca, self).__init__(**kwargs)
        self.limite = kwargs.get('limite', 0)

    def saque(self, valor):
        """
        Método para realizar saque.
        Este método suporta somente números maiores que zero.

        Args: valor (float ou int): Valor positivo do saque

        Raises:
            ValueError: Erro ocorre quando é informado valor negativo.
            TypeError: Quando o tipo passado não for inteiro ou float.

        Returns:
            Float: Valor do saque realizado.
        """
        if isinstance(valor, (float, int)):
            '''if valor > (self.saldo + self.limite):
                raise ValueError('Valor do saque supera seu saldo e seu limite')
                return
            else:'''
            if valor > self.saldo:
                raise ValueError('Valor do saque supera seu saldo.')
                return

            self.saldo = self.saldo - valor
            self.extrato.append(('S', valor))
            return valor
        raise TypeError('O valor do saque precisa ser numérico')

    def rendimento_aniversario(self, valorjuros):
        if valorjuros < 0 or valorjuros > 1:
            raise ValueError('Os juros precisam ser entre 0 (0%) e 1 (100%).')
        self.saldo += self.saldo * valorjuros

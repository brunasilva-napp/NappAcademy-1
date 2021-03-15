from BancoNapp.contas.Conta import Conta


class ContaPessoaJuridica(Conta):
    def __init__(self,  **kwargs):
        """
        Construtor da classe PessoaFísica.
        
        """
        super(ContaPessoaJuridica, self).__init__(**kwargs)
        self.empresa = kwargs.get('empresa', '')
        self.limite = kwargs.get('limite', 1500)

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
            if valor > (self.saldo + self.limite):
                raise ValueError('Valor do saque supera seu saldo e seu limite')
                return
            self.saldo = self.saldo - valor
            self.extrato.append(('S', valor))
            return valor
        raise TypeError('O valor do saque precisa ser numérico')
class Conta:
    def __init__(self, **kwargs):
        """
        Construtor da classe Conta.
        Recebe por kwargs :
        - nome
        - limite
        - saldo

        Raises:
            ValueError: Caso o saldo seja menor ou igual a zero.
        """
        self.extrato = []
        self.limite = kwargs.get('limite', 500)
        self.nome = kwargs.get('nome', None)
        self.saldo = kwargs.get('saldo', 0)

        if self.saldo < 0:
            raise ValueError('Saldo negativo')
        self.extrato.append(('I', self.saldo))

    def deposito(self, valor):
        """
        Método para realizar depósito.
        Este método suporta somente números maiores que zero.

        Args: valor (float ou int): Valor positivo do depósito

        Raises:
            ValueError: Erro ocorre quando é informado valor negativo.
            TypeError: Quando o tipo passado não for inteiro ou float.
        """
        if isinstance(valor, (float, int)):
            if valor <= 0:
                raise ValueError('Valor do depósito precisa ser maior que zero')
            self.saldo = self.saldo + valor
            self.extrato.append(('D', valor))
            return
        raise TypeError('O depósito precisa ser numérico')

    def get_extrato(self):
        return self.extrato


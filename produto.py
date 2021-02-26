class produto(object):

    def __init__(self,id, cod_produto, data_prioridade, data_entrega,qtd):
        self.id=id
        self.cod_produto=cod_produto
        self.data_prioridade=data_prioridade
        self.data_entrega=data_entrega
        self.vetor_ofs=[]
        self.qtd=qtd
        self.espessura_inicial = 0
        self.espessura_final = 0
        self.largura = 0
        self.comprimento = 0

    def __repr__(self):
        return str(self.id)

    def adicionar_of(self,of):
        self.vetor_ofs.append(of)


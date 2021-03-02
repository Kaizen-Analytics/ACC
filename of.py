class of(object):

    def __init__(self,id, ct,cod_of,t_producao):

        self.id=id
        self.ct = ct
        self.cod_of=cod_of
        self.data_inicio=0
        self.id_slot_inicio_turno=-1
        self.data_fim=0
        self.id_alocada=0
        self.t_producao=t_producao
        self.vetor_maquinas=[]
        #self.vetor_produtos=[] não me interessa, desde que tenha a data min e a data de entrega
        self.vetor_data_min=[]
        self.vetor_data_entrega=[]
        self.data_min=99999

    def __repr__(self):
        return str(self.id)

    def adicionar_maquinas(self,maquinas):
        self.vetor_maquinas=maquinas

    def adicionar_produto(self,data_prioridade,data_entrega):
        self.vetor_data_min.append(data_prioridade)
        self.vetor_data_entrega.append(data_entrega)

    def definir_data_min(self):
        self.data_min=min(self.vetor_data_min)


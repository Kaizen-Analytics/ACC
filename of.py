class of(object):

    def __init__(self,id, ct,cod_of,t_producao):

        self.id=id
        self.cod_of=cod_of
        self.ct=ct
        self.data_inicio=0
        self.turno=0
        self.data_fim=0
        self.id_alocada=0
        self.t_producao=t_producao
        self.vetor_maquinas=[]

    def __repr__(self):
        return str(self.id)

    def adicionar_maquinas(self,maquinas):
        self.vetor_maquinas=maquinas
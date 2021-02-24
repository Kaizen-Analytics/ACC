class of(object):

    def __init__(self,id, cod_of, dimensao,t_producao):

        self.id=id
        self.cod_of=cod_of
        self.dimensao=dimensao
        self.data_inicio=0
        self.turno=0
        self.data_fim=0
        self.id_alocada=0
        self.t_producao=t_producao
        self.vetor_maquinas=[]

    def __repr__(self):
        return str(self.id)

    def adicionar_maquina(self,maquina):
        self.vetor_maquinas.append(maquina)

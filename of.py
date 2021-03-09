from datetime import datetime

class of(object):

    def __init__(self,id, ct,cod_of,descricao_material,t_producao,id_precedencias,data_entrega):

        self.id=id
        self.ct = ct
        self.cod_of=str(cod_of)
        self.data_inicio=0
        self.id_slot_inicio_turno=-1
        self.data_fim=0
        self.id_alocada=0
        self.t_producao=t_producao
        self.vetor_maquinas=[]
        self.vetor_data_min=[]
        self.vetor_data_entrega=[]
        self.data_min=99999
        self.descricao_material = descricao_material
        self.dimensao=self.descricao_material.split(" ")[3:][0]
        self.material = self.descricao_material.split(" ", 2)[2].rsplit("/", 1)[0]
        self.pronta_a_iniciar=0
        self.delta=99999
        self.data_entrega = data_entrega
        self.id_precedencias=id_precedencias

    def __repr__(self):
        return str(self.id)

    def adicionar_maquinas(self,maquinas):
        self.vetor_maquinas=maquinas

    def adicionar_produto(self,data_prioridade,data_entrega):
        self.vetor_data_min.append(data_prioridade)
        self.vetor_data_entrega.append(data_entrega)

    def definir_data_min(self):

        if len(self.vetor_data_min)>0:
            self.data_min=min(self.vetor_data_min)

    def update_delta(self):

        format = "%d/%m"
        d2 = "05/03"
        d1 = "01/03"
        d1 = datetime.strptime(d1, format)
        d2 = datetime.strptime(d1, format)
        d2 = (d2 - d1).total_seconds() / 60

        self.delta=self.data_entrega-(self.data_min+self.t_producao)

        return self.delta

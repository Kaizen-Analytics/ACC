class maquina(object):

    def __init__(self,id,nome,grupo):
        self.nome=nome
        self.id = id
        self.grupo = grupo
        self.vetor_slots=[]
        self.setups=[]
        self.id_inicio_turno=[]
        # definir capacidade turno
        # setups diferentes turno. guardar dimensoes

    def __repr__(self):
        self.id

    def adicionar_slot(self,slot):
        self.vetor_slots.append(slot)

    def adicionar_setup(self,setup):
        self.setups.append(setup)

    def adicionar_inicio_turno(self):
        self.inicio_turno.append(0)


class maquina(object):

    def __init__(self,id,nome):
        self.nome=nome
        self.vetor_slots=[]
        self.setups=[]
        self.inicio_turno=[]
        # definir capacidade turno
        # dimensoes diferentes turno. guardar dimensoes

    def __repr__(self):
        self.id

    def adicionar_slot(self,slot):
        self.vetor_slots.append(slot)

    def adicionar_setup(self,setup):
        self.setups.append(setup)

    def adicionar_inicio_turno(self):
        self.inicio_turno.append(0)


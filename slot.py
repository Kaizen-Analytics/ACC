class slot(object):

    def __init__(self,id,inicio, fim, turno):

        self.id=id
        self.inicio=inicio
        self.fim=fim
        self.turno=turno

    def __repr__(self):
        return str(self.id)


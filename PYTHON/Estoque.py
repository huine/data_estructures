from DLL import DLL


class Estoque(object):
    """Docstring for estoque."""

    def __init__(self):
        """."""
        self.lista_mecadoria = DLL()
        self.id_merc = 0
        self.len_merc = 0

    def id(self):
        """."""
        self.id_merc += 1
        return self.id_merc

    def cadastrar_mercadoria(self, nome, preco, qtd, min_qtd):
        """."""
        merc = Mercadoria(id=self.id(), nome=nome, preco=preco,
                          qtd=qtd, min_qtd=min_qtd)

        self.lista_mecadoria.insert_after(merc)


class Mercadoria(object):
    """Docstring for mercadoria."""

    def __init__(self, id, nome='', preco=0, qtd=0, min_qtd=0):
        """."""
        self.id = id
        self.nome = nome
        self.preco = preco
        self.qtd = qtd
        self.min_qtd = min_qtd

    def __str__(self):
        """."""
        return "id: %s\tnome: %s\tpreco: %s\tqtd: %s\tmin_qtd: %s\t" % (
            self.id, self.nome, self.preco, self.qtd, self.min_qtd)

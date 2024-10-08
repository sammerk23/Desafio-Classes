class hero:
    def init(self,nome,idade,tipo):
        self.nome = nome
        self.idade = idade
        self.tipo = tipo
    
    
    def atacar(tipo):
        if tipo == "Guerreiro":
            ataque = "Espada"
        elif tipo == "Mago":
            ataque = "Magia"
        elif tipo == "Monge":
            ataque = "Artes Marciais"
        else:
            ataque = "Shuriken"
        print("o {} atacou usando {}".format(tipo,ataque))

heroi = hero.init(hero,"Herói", 20, "Guerreiro")
hero.atacar("Ninja")
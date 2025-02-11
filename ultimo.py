class heroi():
    def __init__(self, nome, idade, tipo):
        self.nome = nome
        self.idade= idade
        self.tipo=tipo
        self.tipoMagia=["guerreiro", "mago", "monge", "ninja"]
        
        if tipo not in self.tipoMagia:
            print("Tipo de herói inválido")
    def ataque(self):
        if self.tipo==("guerreiro"):
            ataque= "usou espada"
        elif self.tipo ==("mago"):
            ataque = ("usou magia")
        elif self.tipo ==("monge"):
            ataque = ("Artes maciais")
        elif self.tipo == ("ninja"):
            ataque = ("usou shuriken")
        else:
            print("invalido")
        return ataque
    
heroi1 = heroi("kaua", 19, "monge")
ataque1 = heroi1.ataque()
(heroi1.idade)
(heroi1.tipo)
(ataque1)
print("O nome do heroi é: ", heroi1.tipo, "idade de : ", heroi1.idade, "atacou usando: ", ataque1)

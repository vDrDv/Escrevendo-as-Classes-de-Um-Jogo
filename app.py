class Heroi:
    
    def __init__(self, nome, idade, tipo):
        self.nome = nome
        self.idade = idade
        self.tipo = tipo

    def atacar(self):
        ataque = ""
        if self.tipo == "mago":
            ataque = "usou magia"
        elif self.tipo == "guerreiro":
            ataque = "usou espada"
        elif self.tipo == "monge":
            ataque = "usou artes marciais"
        elif self.tipo == "ninja":
            ataque = "usou shuriken"

        mensagem = f"o {self.tipo} atacou usando {ataque}"
        print(mensagem)

heroi1 = Heroi("Gandalf", 150, "mago")
heroi2 = Heroi("Aragorn", 37, "guerreiro")
heroi3 = Heroi("Bruce Lee", 32, "monge")
heroi4 = Heroi("Hattori Hanzo", 28, "ninja")

heroi1.atacar()
heroi2.atacar()
heroi3.atacar()
heroi4.atacar()

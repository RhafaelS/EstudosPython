class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type


    def describe_restaurant(self):
        print("O nome do restaurante é: " + Restaurant.restaurant_name.title)
        print("E o tipo da cozinha é: " + Restaurant.cuisine_type.title)

    def open_restaurant(self):
        print("O restaurante está aberto.")


#Instância da classe Restaurant para criar uma sorveteria
class IceCreamStand(Restaurant):

    def __init__(self, restaurant_name, cuisine_type, flavors):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.flavors = flavors
        super().__init__(restaurant_name, cuisine_type)

    #Método para printar os sabores adicionados na lista flavors
    def show_flavors(self):
        for flavor in self.flavors:
            print(flavor)

minhaSorveteria = IceCreamStand('Sorveteria Laricão', 'Sorvete de Cannabis', 'Chocolate')

minhaSorveteria.describe_restaurant()

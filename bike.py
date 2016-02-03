class Bike:
    def __init__(self, colour, frame_material):
        self.colour = colour
        self.frame_material = frame_material
		
    def brake(self):
        print("Braking!")
		
#Instancias
red_bike = Bike('Red', 'Carbon fiber')
blue_bike = Bike('Blue', 'Steel')

#Imprimir instancias
print(red_bike.colour)
print(red_bike.frame_material)
print(blue_bike.colour)
print(blue_bike.frame_material)

#Brake
red_bike.brake()
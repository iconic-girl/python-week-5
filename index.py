
class Smartphone:
    def __init__(self, brand, model, storage, battery, camera_mp):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.battery = battery
        self.camera_mp = camera_mp
        self.is_on = False

    def turn_on(self):
        if not self.is_on:
            print(f"{self.brand} {self.model} is turning on...")
            self.is_on = True
        else:
            print(f"{self.brand} {self.model} is already on.")

    def turn_off(self):
        if self.is_on:
            print(f"{self.brand} {self.model} is turning off...")
            self.is_on = False
        else:
            print(f"{self.brand} {self.model} is already off.")
    
    def take_photo(self):
        if self.is_on:
            print(f"Taking a photo with the {self.camera_mp}MP camera.")
        else:
            print(f"Cannot take a photo. {self.brand} {self.model} is off.")

    def check_specs(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Storage: {self.storage}GB")
        print(f"Battery: {self.battery}mAh")
        print(f"Camera: {self.camera_mp}MP")

# Example usage
my_phone = Smartphone("Samsung", "Galaxy S23", 256, 4000, 50)
my_phone.check_specs()
my_phone.turn_on()
my_phone.take_photo()
my_phone.turn_off()

another_phone = Smartphone("Apple", "iPhone 15", 512, 3500, 48)
another_phone.turn_on()
another_phone.take_photo()
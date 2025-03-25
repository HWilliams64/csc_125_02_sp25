from csc_125_02_sp25.m04_03_25.phone_plan import Carrier, Network

class SmartPhone:

    def __init__(self, make: str, model: str, carrier: Carrier) -> None:
        self.__model = model
        self.__make = make
        self.__carrier = carrier

    def __str__(self) -> str:
        return f"{self.__make} {self.__model} {self.__carrier.phone_number}"

    @property
    def phone_number(self) -> str:
        return self.__carrier.phone_number

    def call(self, number: str, minutes:int) -> int: 
        # Check if the other phone exists
        if not self.__carrier.network.exists(number):
            # return zero minute total call if the other phone does not exist
            # because there was no phone to call...
            return 0
        else:
            # Otherwise make the call and return the total length of time the
            # call lasted
            return self.__carrier.phone_plan.call(minutes)

    def text(self, number: str) -> bool:
        if not self.__carrier.network.exists(number):
            return False
        else:
            return self.__carrier.phone_plan.text()
    
    def surf(self, used_data_bytes: int) -> int:
        return self.__carrier.phone_plan.surf(used_data_bytes)
    

if __name__ == "__main__":

    us_network = Network()

    t_mobile_carrier = Carrier(
        us_network,
        "T-Mobile",
        "+1 617-123-4567",
        talk_min=-1, text=100, data_bytes=-1
    )

    verizon_carrier = Carrier(
        us_network,
        "Verizon",
        "+1 781-123-4567",
        talk_min=100, text=100, data_bytes=-1
    )

    iphone = SmartPhone("Apple", "iphone 17", t_mobile_carrier)
    pixel = SmartPhone("Google", "pixel 23", verizon_carrier)

    result = iphone.call(pixel.phone_number, 10)
    print(f"Call total time: {result}")

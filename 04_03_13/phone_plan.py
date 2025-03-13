class PhonePlan:
    def __init__(self, talk_min: int = 0, text: int = 0, data_bytes: int = 0) -> None:
        self.__talk_min = talk_min 
        self.__text = text
        self.__data_bytes = data_bytes

    def call(self, minutes:int) -> int: # Return the length of the call
        if self.__talk_min < 0:
            return  minutes

        # Do we have any minutes left?
        if self.__talk_min > 0:
            # Are there more min left than we want to call for?
            if self.__talk_min > minutes:
                # subtract the call length from the minutes we have left
                self.__talk_min -= minutes
                return minutes
            else:
                # The length of the call will be the minutes we have left
                # We set the minutes we have left to 0
                min_left = self.__talk_min
                self.__talk_min = 0
                return min_left
        # The were no minutes left in the plan so no call was made thus the 
        # call length is 0 minutes
        return 0 

    def surf(self, used_data_bytes: int) -> int:  # Return the length of the call
        if self.__data_bytes < 0:
            return used_data_bytes

        if self.__data_bytes > 0:
            if self.__data_bytes > used_data_bytes:
                self.__data_bytes -= used_data_bytes
                return used_data_bytes
            else:
                bytes_used = self.__data_bytes
                self.__data_bytes = 0
                return bytes_used
        return 0

    def text(self) -> bool:
        if self.__text < 0:
            return True

        # Do we have at least one message left to send
        if self.__text > 0:
            # Subtract one from the message
            self.__text -= 1
            return True
        # Otherwise no message was send
        return False

    def __str__(self) -> str:
        talk_str = "Unlimited" if self.__talk_min < 0 else self.__talk_min
        text_str = "Unlimited" if self.__text < 0 else self.__text
        data_str = "Unlimited" if self.__data_bytes < 0 else self.__data_bytes

        return f"Talk: {talk_str} Text: {text_str} Data: {data_str}"

class Carrier:

    def __init__(self, company_name: str, phone_number: str, talk_min: int = 0, text: int = 0, data_bytes: int = 0) -> None:
        self.__company_name = company_name
        self.__phone_number = phone_number
        self.__phone_plan = PhonePlan(talk_min, text, data_bytes)

    @property
    def company_name(self) -> str:
        return self.__company_name

    @property
    def phone_number(self) -> str:
        return self.__phone_number

    @property
    def phone_plan(self) -> PhonePlan:
        return self.__phone_plan

if __name__ == "__main__":
    carrier = Carrier(
        "T-Mobile", 
        "+1 617-123-4567",
        talk_min=-1, text=100, data_bytes=-1
    )
    
    print("My Phone Plan", carrier.phone_plan)

    length_of_call = carrier.phone_plan.call(20)
    print(f"Call Length: {length_of_call}")
    print("My Phone Plan", carrier.phone_plan)

    print("="*30)
    length_of_call = carrier.phone_plan.call(200)
    print(f"Call Length: {length_of_call}")
    print("My Phone Plan", carrier.phone_plan)

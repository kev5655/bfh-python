class PhoneKeyboard:
    """
    Class that simulates the keyboard of a phone. Each digit that is
    pressed (method press()) are added to the phoneNumber attribute.
    The simulation of dialing (method dial()) happens only if at least
    10 digits have been pressed. A backspace key (method  backspace())
    removes the last pressed digit. The clear key (method clear)
    clears all the digits that have been pressed.
    """

    def __init__(self) -> None:
        """
        Constructor that defines the two required attributes.
        This method is automatically invoked when a new object is instanced
        """
        self.minDialSize = 10  # minimum number of digits to dial the number
        self.phoneNumber = ""  # collects the pressed digits

    def press(self, digit: str) -> None:
        """
        Simulates that a digit is pressed, if something else than a digit is pressed
        nothing happens.
        """
        # Since Python does not have single character data type but string of length 1
        # digit here is a string that might have a length greater than 1
        if len(digit) == 1 and digit in "0123456789":
            self.phoneNumber += digit  # add the pressed digit to the phone number

    def dial(self) -> None:
        """
        Simulates the dialing (just print the phone number) then clears phone number.
        If the number of pressed digits is smaller than minDialSize then nothing happens.
        """
        if len(self.phoneNumber) >= self.minDialSize:
            print(self.phoneNumber)  # phone number dialed only if at least 10 digits are pressed
            self.clear()

    def clear(self) -> None:
        """Clears the phone number"""
        self.phoneNumber = ""

    def backspace(self) -> None:
        """Removes the last pressed digit."""
        # Strings are immutable. Here the last character is not removed,
        # but a new string is created without the last character.
        self.phoneNumber = self.phoneNumber[:-1]


def main():
    """ Launcher """
    phone = PhoneKeyboard()  # creates an instance phone of PhoneKeyboard class

    print(phone.minDialSize)  # display the minimum number of digits to dial the number

    phone.press('0')  # simulates pressing on '0' digit
    phone.press('9')
    phone.backspace()
    phone.press('3')
    phone.press('2')
    phone.press('3')
    phone.press('2')
    phone.press('1')
    phone.press('6')
    phone.press('3')
    phone.press('2')
    phone.press('4')
    phone.dial()
    # number 0323216324 has been pressed and automatically dialed then cleared


if __name__ == "__main__":
    main()

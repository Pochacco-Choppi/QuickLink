class Error:
    def __init__(self, name, text):
        self.name = name
        self.text = text


WRONG_URL_FORMAT = Error(name="WRONG_URL_FORMAT", text="Wrong url format")
SOMETHING_GOES_WRONG = Error(name="SOMETHING_GOES_WRONG", text="Woops something goes wrong")

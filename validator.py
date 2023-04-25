VALID_ACTIONS = ["blur", "smooth", "edge", "sharpen", "detail", "contour", "grayscale", "flip", "mirror", "invert"]
VALID_TYPES = ["png", "jpg", "jpeg"]


class Validator:
    def __init__(self, input: str, output: str, action: str):
        self._input = input
        self._output = output
        self._action = action
        self.validate()
    
    def validate(self):
        self.validate_types()
        self.validate_output()
        self.validate_action()

    def validate_types(self):
        attributes = [self.input, self.output]
        for attr in attributes:
            if attr.split(".")[-1] not in VALID_TYPES:
                raise ValueError(f"Invalid file type, valid types: {VALID_TYPES}")

    def validate_output(self):
        if self.input.split(".")[-1] != self.output.split(".")[-1]:
            raise ValueError("Input and output files should have the same type")

    def validate_action(self):
        if self.action not in VALID_ACTIONS:
            raise ValueError(f"Invalid action, valid actions: {VALID_ACTIONS}")

    @property
    def input(self):
        return self._input
    
    @property
    def output(self):
        return self._output
    
    @property
    def action(self):
        return self._action

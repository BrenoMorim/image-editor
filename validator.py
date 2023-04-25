VALID_ACTIONS = ["blur", "smooth", "edge", "sharpen", "detail", "contour", "grayscale", "flip", "mirror", "invert", "resize"]
VALID_TYPES = ["png", "jpg", "jpeg"]


class Validator:

    """
    Class used to validate and store the command line arguments provided by the argparser lib in the main file
    """

    def __init__(self, input: str, output: str, action: str, size: str=''):
        """
        Constructor to make sure that all the attributes are valid
        """
        self._input = input
        self._output = output
        self._action = action
        self.validate()
        self.validate_size(size)
    
    def validate(self):
        """
        Centralizes all the validations in only one function
        """
        self.validate_types()
        self.validate_output()
        self.validate_action()

    def validate_types(self):
        """
        Checks if both input and output have valid types (.png, .jpg, .jpeg)
        """
        attributes = [self.input, self.output]
        for attr in attributes:
            if attr.split(".")[-1] not in VALID_TYPES:
                raise ValueError(f"Invalid file type, valid types: {VALID_TYPES}")

    def validate_output(self):
        """
        Checks if the output has the same format as the input
        """
        if self.input.split(".")[-1] != self.output.split(".")[-1]:
            raise ValueError("Input and output files should have the same type")

    def validate_action(self):
        """
        Makes sure that the selected action exists
        """
        if self.action not in VALID_ACTIONS:
            raise ValueError(f"Invalid action, valid actions: {VALID_ACTIONS}")
        
    def validate_size(self, size):
        """
        If the action is 'resize', checks if the given size is valid. Then, set a value for the size attribute
        """
        if self.action != "resize":
            return
        
        if size == None or size == '':
            raise ValueError("If the action is resize, you must specify the size")
        try:
            self._size = (int(size.split("x")[0]), int(size.split("x")[1]))
        except Exception:
            raise ValueError("Invalid size was given, follow the example: --size 1920x1080")

    @property
    def input(self):
        return self._input
    
    @property
    def output(self):
        return self._output
    
    @property
    def action(self):
        return self._action

    @property
    def size(self):
        return self._size

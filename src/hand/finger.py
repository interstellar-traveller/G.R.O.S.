import hand

class finger(hand):
    def __init__(self, label:str, lms:list) -> None:
        """Initialize a finger object

        Args:
            label (str): the name of the finger object
            lms (list): landmarks on the finger object
        """
        self.label = label
        self.lms = lms

    
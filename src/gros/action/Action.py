import sys
sys.path.append("f:/0Desk/IBDP/ComputerScience/IA/code/GROS/src")

from gros.action.ActionSet import *

class Action():
    def __init__(self, action:str, activate:bool=False):
        """Defines an action.
        Decides whether an action is activated when instantiated.

        Args:
            action (str): the name of the action
            activate (bool, optional): the activation status of this action. Defaults to True.
        """
        self.name = action
        self.activate = activate
        
    def get_name(self):
        """get the name of this action

        Returns:
            name ([str]): name of this action
        """
        return self.name
    
    def get_activate_status(self):
        """get the activation status of this action

        Returns:
            activate ([bool]): the activation status of this action
        """
        return self.activate
    
    def update_activatation_status(self, activate:bool):
        """update the activation status of this action

        Args:
            activate (bool): the activation status. Either True or False.
        """
        self.activate = activate
        
    def use(self):
        """triggers the action
        """
        action_set = ActionSet()
        if self.activate:
            getattr(action_set, self.name)()
        

# switch = Action("switch")
# switch.use()
    
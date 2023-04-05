from __future__ import annotations
import uuid


class Foo():
    """This is the awesome Foo class"""
    
    def __init__(self):
        """ Initialize the Foo class with a unique uuid"""
        
        self.id = uuid.uuid4()
    
    def greet_with_google_docstring(self, name: str = "") -> Foo:
        """
        This is a Google-Doctstring 

        Args:
            name (str): The name of someone that should be greeted
            
        Returns:
            bool: True if successful, False otherwise
            
        Raises:
            ValueError: if user forgets to supply a name
        """
        if not name:
            raise ValueError("No name specified")
        print(f"Foo-{self.id} greets {name}")
        return self

    def greet_with_sphinx_docstring(self, name: str = None) -> Foo:
        """
        This is a reST-Doctstring 

        :param name: The name of the person to greet
        :type name: str       
        :return: True if successful, False otherwise
        :rtype: bool
        """
        if not name:
            raise ValueError("No name specified")
        print(f"Foo-{self.id} greets {name}")
        return self
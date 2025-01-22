class Event:
    """A generic class that provides signal/slot functionality"""

    def __init__(self):
        self.listeners = []

    def connect(self, listener: callable) -> None:
        """Connect a listener to this event"""
        self.listeners.append(listener)

    def fire(self, *args, **kwargs) -> None:
        """Fire the event, passing the arguments to all listeners"""
        for listener in self.listeners:
            listener(*args, **kwargs)

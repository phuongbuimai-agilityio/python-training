from unittest import mock
import unittest
from ..event import Event


class EventTest(unittest.TestCase):
    def test_a_listerner_is_notified_when_an_event_is_raised(self):
        """
        Verify that a listener is called when an event is fired.

        This test ensures the core functionality of the Event system:
        1. Listeners can be connected to an event
        2. When the event is fired, all connected listeners are called
        3. The listener is invoked even without any arguments

        Test Steps:
        1. Create a mock listener object
        2. Create an Event instance
        3. Connect the mock listener to the event
        4. Fire the event without any arguments
        5. Assert that the listener was called

        The test demonstrates the basic event notification mechanism:
        - Listeners can be dynamically added to an event
        - Events can be fired without requiring arguments
        - The event system tracks and calls all connected listeners

        Note:
            Uses mock.Mock() to simulate and verify listener behavior
            Checks the 'called' attribute to confirm listener invocation
        """
        listener = mock.Mock()
        event = Event()
        event.connect(listener)
        event.fire()
        self.assertTrue(listener.called)

    def test_a_listener_is_passed_right_parameters(self):
        """
        Verify that event listeners receive the correct parameters when an event is fired.

        This test ensures that:
        1. The event system correctly passes both positional and keyword arguments
        2. Listeners are called with the exact arguments used when firing the event

        Test Steps:
        1. Create a mock listener
        2. Create an Event instance
        3. Connect the mock listener to the event
        4. Fire the event with specific arguments
        5. Assert that the listener was called with the correct arguments

        The test demonstrates the event system's ability to:
        - Propagate positional arguments (5)
        - Propagate keyword arguments (shape="square")
        - Maintain argument integrity during event firing

        Note:
            Uses mock.Mock() to simulate and verify listener behavior
        """
        listener = mock.Mock()
        event = Event()
        event.connect(listener)
        event.fire(5, shape="square")
        listener.assert_called_with(5, shape="square")

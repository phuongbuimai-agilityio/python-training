import unittest
from unittest import mock
import smtplib

from ..action import EmailAction


class EmailActionTest(unittest.TestCase):
    def setUp(self):
        self.action = EmailAction(to="siddharta@silverstripesoftware.com")

    def test_email_is_sent_to_the_right_server(self, mock_smtp_class: mock.MagicMock):
        self.action.execute("MSFT has crossed $10 price level")
        mock_smtp_class.assert_called_with("email.stocks.com")

    def test_connection_closed_after_sending_mail(
        self, mock_smtp_class: mock.MagicMock
    ):
        """
        Verify that SMTP connection is properly closed after sending an email.

        This test ensures the correct resource management in the email action:
        1. Confirm that an email is sent successfully
        2. Verify that the SMTP connection is closed immediately after sending
        3. Check the sequence of method calls during the email sending process

        Test Steps:
        1. Create a mock SMTP connection
        2. Execute the email action with a test message
        3. Assert that the send_message method is called with the correct arguments
        4. Verify that the quit() method is called to close the connection
        5. Check the sequence of method calls matches the expected workflow

        Args:
            mock_smtp_class (mock.MagicMock): Mocked SMTP connection class for testing

        Note:
            - Uses mock assertions to verify method calls
            - Checks both individual method calls and the overall call sequence
        """
        mock_smtp = mock_smtp_class.return_value
        self.action.execute("MSFT has crossed $10 price level")
        mock_smtp.send_message.assert_called_with(mock.ANY)
        self.assertTrue(mock_smtp.quit.called)
        mock_smtp.assert_has_calls([mock.call.send_message(mock.ANY), mock.call.quit()])

    def test_connection_closed_if_send_gives_error(
        self, mock_smtp_class: mock.MagicMock
    ):
        """
        Verify that SMTP connection is closed even if an error occurs during email sending.

        This test ensures robust error handling in the email action:
        1. Simulate an SMTP server disconnection error
        2. Confirm that the SMTP connection is always closed, regardless of send status

        Test Steps:
        1. Create a mock SMTP connection
        2. Configure the mock to raise an SMTPServerDisconnected exception
        3. Attempt to execute the email action (which will trigger the error)
        4. Assert that the connection's quit() method is called


        Args:
            mock_smtp_class (mock.MagicMock): Mocked SMTP connection class for testing

        Raises:
            smtplib.SMTPServerDisconnected: Simulated SMTP server disconnection error

        Note:
            - Uses exception handling to simulate and test error scenarios
            - Checks connection closure independent of error propagation
        """
        mock_smtp = mock_smtp_class.return_value
        mock_smtp.send_message.side_effect = smtplib.SMTPServerDisconnected()
        try:
            self.action.execute("MSFT has crossed $10 price level")
        except Exception:
            pass
        self.assertTrue(mock_smtp.quit.called)

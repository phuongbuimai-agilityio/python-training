# Example: Use a context manager to ensure resources are properly managed
class MyContextManager:
    """A demonstration context manager that shows basic resource management.

    This context manager implements the context management protocol (__enter__
    and __exit__) to demonstrate proper resource acquisition and cleanup,
    along with exception handling.

    Example:
        >>> with MyContextManager() as resource:
        ...     print(f"Using the resource: {resource}")
        Entering the context
        Using the resource: Acquired Resource
        Exiting the context
        Releasing Resource

    Note:
        - Resources are acquired in __enter__ and released in __exit__
        - Exceptions within the context are not suppressed
        - All cleanup operations are performed even if exceptions occur
    """

    def __enter__(self):
        print("Entering the context")
        self.resource = "Acquired Resource"  # Acquire resource
        return self.resource  # Return the resource to be used in the 'with' block

    def __exit__(self, exc_type: type, exc_val: Exception, exc_tb: object) -> bool:
        """Handle context exit and resource cleanup.

        Args:
            exc_type: The type of the exception that occurred, if any
            exc_val: The instance of the exception that occurred, if any
            exc_tb: The traceback of the exception that occurred, if any

        Returns:
            bool: False to indicate that exceptions should not be suppressed

        Note:
            This method ensures resources are properly released even if an
            exception occurs within the context. It prints diagnostic information
            about any exceptions but does not suppress them.
        """
        print("Exiting the context")
        if exc_type:
            print(f"An exception of type {exc_type} occurred: {exc_val}")
        print("Releasing Resource")  # Release resource
        return False  # Do not suppress exception


with MyContextManager() as resource:
    print(f"Using the resource: {resource}")
    # raise ValueError("Something went wrong!") #Uncomment to test exception handling
print("Outside the context")

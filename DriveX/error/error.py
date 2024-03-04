from ..error.ERR import *

class GoogleDriveErrorHandler:
    """Handles errors that may occur during interactions with Google Drive."""

    def __init__(self):
        """Initialize the GoogleDriveErrorHandler."""
        pass

    def handle_error(self, exception):
        """Handles the given exception and provides an explanation to the user."""
        try:
            if isinstance(exception, AuthenticationError):
                print("Authentication error occurred:", exception)
                print("Please check your credentials and try again.")
            elif isinstance(exception, FileError):
                print("File-related error occurred:", exception)
                print("Please check the file and try again.")
            elif isinstance(exception, FolderError):
                print("Folder-related error occurred:", exception)
                print("Please check the folder and try again.")
            elif isinstance(exception, RateLimitError):
                print("Rate limit exceeded error occurred:", exception)
                print("Please wait and try again later.")
            elif isinstance(exception, NetworkError):
                print("Network error occurred:", exception)
                print("Please check your internet connection and try again.")
            elif isinstance(exception, PermissionError):
                print("Permission error occurred:", exception)
                print("You do not have sufficient permissions to perform this action.")
            elif isinstance(exception, QuotaError):
                print("Quota error occurred:", exception)
                print("Your storage quota is exceeded. Please free up space or upgrade your plan.")
            elif isinstance(exception, NotFoundError):
                print("Resource not found error occurred:", exception)
                print("The requested resource was not found.")
            elif isinstance(exception, ConflictError):
                print("Conflict error occurred:", exception)
                print("There was a conflict with existing resources.")
            elif isinstance(exception, InvalidRequestError):
                print("Invalid request error occurred:", exception)
                print("The request made is invalid.")
            elif isinstance(exception, ValueError):
                print("Value error occurred:", exception)
                print("Please provide valid input.")
            elif isinstance(exception, TypeError):
                print("Type error occurred:", exception)
                print("Please check the data types being used.")
            elif isinstance(exception, IndexError):
                print("Index error occurred:", exception)
                print("Please check the index value being used.")
            elif isinstance(exception, KeyError):
                print("Key error occurred:", exception)
                print("Please check if the key exists in the dictionary.")
            elif isinstance(exception, NotImplementedError):
                print("Not implemented error occurred:", exception)
                print("This feature is not implemented yet.")
            elif isinstance(exception, TimeoutError):
                print("Timeout error occurred:", exception)
                print("The request timed out. Please try again later.")
            elif isinstance(exception, TooManyRequestsError):
                print("Too many requests error occurred:", exception)
                print("You have exceeded the maximum number of requests. Please try again later.")
            elif isinstance(exception, ServerError):
                print("Server error occurred:", exception)
                print("There was an internal server error. Please try again later.")
            elif isinstance(exception, ClientError):
                print("Client error occurred:", exception)
                print("There was an error on the client side. Please try again.")
            else:
                print("An unknown error occurred:", exception)
                print("Please try again later or contact support.")
        except Exception as e:
            print("Error handling error:", e)
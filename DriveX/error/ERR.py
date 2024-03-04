class GoogleDriveError(Exception):
    """Base class for Google Drive API errors."""
    pass

class AuthenticationError(GoogleDriveError):
    """Error raised for authentication-related issues."""
    pass

class FileError(GoogleDriveError):
    """Error raised for file-related issues."""
    pass

class FolderError(GoogleDriveError):
    """Error raised for folder-related issues."""
    pass

class RateLimitError(GoogleDriveError):
    """Error raised when the API rate limit is exceeded."""
    pass

class NetworkError(GoogleDriveError):
    """Error raised for network-related issues."""
    pass

class PermissionError(GoogleDriveError):
    """Error raised when permissions are insufficient."""
    pass

class QuotaError(GoogleDriveError):
    """Error raised when storage quota is exceeded."""
    pass

class NotFoundError(GoogleDriveError):
    """Error raised when a resource is not found."""
    pass

class ConflictError(GoogleDriveError):
    """Error raised when there is a conflict with existing resources."""
    pass

class InvalidRequestError(GoogleDriveError):
    """Error raised when an invalid request is made."""
    pass

class TooManyRequestsError(GoogleDriveError):
    """Error raised when the API rate limit is exceeded."""
    pass

class ServerError(GoogleDriveError):
    """Error raised for server-related issues."""
    pass

class ClientError(GoogleDriveError):
    """Error raised for client-related issues."""
    pass

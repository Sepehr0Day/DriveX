from ...error.error import *
from ..Authenticator.Authenticator import Authenticator 
from googleapiclient.discovery import build

class ServiceBuilder:
    """Builds the Google Drive service."""

    def __init__(self, credentials_path, token_path, token_name ,scopes="https://www.googleapis.com/auth/drive"):
        """Initialize the ServiceBuilder.

        Args:
            credentials_path (str): Path to the credentials file.
            token_path (str): Path to the token file.
            scopes (str or list of str): The scope or scopes to be requested during the authorization flow.
        """
        self.credentials_path = credentials_path
        self.token_path = token_path
        self.token_name = token_name
        self.scopes = scopes

    def build_service(self):
        """Builds and returns the Google Drive service.

        Returns:
            googleapiclient.discovery.Resource: Google Drive service object.
        """
        try:
            authenticator = Authenticator(self.credentials_path, f"{self.token_path}/{self.token_name}.pickle" , self.scopes)
            credentials = authenticator.get_credentials()
            service = build('drive', 'v3', credentials=credentials)
            return service
        except GoogleDriveError as e:
            raise GoogleDriveError(f"Failed to build service: {str(e)}")

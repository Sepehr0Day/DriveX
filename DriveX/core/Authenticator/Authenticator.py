from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
import os, pickle, json

class Authenticator:
    """Responsible for handling authentication with Google Drive."""

    def __init__(self, credentials_path, token_path, scopes):
        """Initialize the Authenticator.

        Args:
            credentials_path (str): Path to the credentials file.
            token_path (str): Path to the token file.
            scopes (str or list of str): The scope or scopes to be requested during the authorization flow.
        """
        self.credentials_path = credentials_path
        self.token_path = token_path
        self.scopes = scopes

    def get_credentials(self):
        """Retrieve or generate OAuth2 credentials for accessing Google Drive.

        Returns:
            google.oauth2.credentials.Credentials: OAuth2 credentials.
        """
        creds = None
        if os.path.exists(self.token_path):
            with open(self.token_path, 'rb') as token:
                creds = pickle.load(token)
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_config(
                    self._read_credentials_file(), self.scopes)
                creds = flow.run_local_server(port=0)
            with open(self.token_path, 'wb') as token:
                pickle.dump(creds, token)
        return creds

    def _read_credentials_file(self):
        """Read the credentials file and return its content.

        Returns:
            dict: Content of the credentials file.
        """
        with open(self.credentials_path) as f:
            return json.load(f)

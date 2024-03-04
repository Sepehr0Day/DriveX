from ...error.error import *
from datetime import datetime

class GoogleDriveAPI:
    """Provides an interface for interacting with Google Drive."""

    def __init__(self, credentials, service):
        self.credentials = credentials
        self.service = service

    def list_files(self, page_size=10, query=None):
        """
        List files in Google Drive.

        Args:
            page_size (int, optional): Number of files to retrieve per page. Defaults to 10.
            query (str, optional): Query string to filter the files. Defaults to None.

        Returns:
            list: List of files matching the query.
        """
        try:
            query_params = {'pageSize': page_size, 'fields': 'nextPageToken, files(id, name, createdTime, permissions)'}
            if query:
                query_params['q'] = query
            results = self.service.files().list(**query_params).execute()
            items = results.get('files', [])
            
            for item in items:
                permissions = item.get('permissions', [])
                if isinstance(permissions, str):
                    permissions = eval(permissions)
                item['permissions'] = self.format_permissions(permissions)
            
            return items
        except Exception as e:
            raise FolderError(f"Failed to list files: {str(e)}")

    def _convert_size(self, size_bytes):
        """
        Convert file size in bytes to human-readable format.

        Args:
            size_bytes (int or str): File size in bytes.

        Returns:
            str: Human-readable file size.
        """
        try:
            size_bytes = int(size_bytes)
        except ValueError:
            return size_bytes

        sizes = ['Bytes', 'KB', 'MB', 'GB', 'TB']
        i = 0
        while size_bytes >= 1024 and i < len(sizes) - 1:
            size_bytes /= 1024.0
            i += 1
        return "{:.2f} {}".format(size_bytes, sizes[i])

    def get_file_info(self, file_id):
        """
        Get detailed information about a file.

        Args:
            file_id (str): ID of the file.

        Returns:
            dict: File metadata.
        """
        try:
            file = self.service.files().get(fileId=file_id).execute()
            return file
        except Exception as e:
            raise FileError(f"Failed to get file info: {str(e)}")

    @staticmethod
    def format_permissions(permissions):
        """
        Format permissions for display.

        Args:
            permissions (list): List of permission dictionaries.

        Returns:
            str: Formatted permissions string.
        """
        if not permissions:
            return "No permissions"
        permissions_str = ""
        for perm in permissions:
            role = perm.get("role", "Unknown role")
            email = perm.get("emailAddress", "Unknown email")
            permissions_str += f"Role: {role}, Email: {email}\n"
        return permissions_str

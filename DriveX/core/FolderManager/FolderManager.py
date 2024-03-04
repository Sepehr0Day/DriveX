from ...error.error import *

class FolderManager:
    """Handles folder-related operations in Google Drive."""

    def __init__(self, service):
        self.service = service

    def create_folder(self, folder_name, parent_folder_id=None):
        """
        Create a new folder in Google Drive.

        Args:
            folder_name (str): Name of the new folder.
            parent_folder_id (str, optional): ID of the parent folder. Defaults to None.

        Returns:
            str: ID of the newly created folder.
        """
        try:
            folder_metadata = {
                'name': folder_name,
                'mimeType': 'application/vnd.google-apps.folder'
            }
            if parent_folder_id:
                folder_metadata['parents'] = [parent_folder_id]
            folder = self.service.files().create(body=folder_metadata, fields='id').execute()
            return folder.get('id')
        except Exception as e:
            raise FolderError(f"Failed to create folder: {str(e)}")

    def move_file(self, file_id, new_parent_id):
        """
        Move a file to a different folder.

        Args:
            file_id (str): ID of the file to move.
            new_parent_id (str): ID of the new parent folder.

        Returns:
            dict: Updated file metadata.
        """
        try:
            file = self.service.files().get(fileId=file_id, fields='parents').execute()
            previous_parents = ",".join(file.get('parents'))
            file = self.service.files().update(
                fileId=file_id,
                addParents=new_parent_id,
                removeParents=previous_parents,
                fields='id, parents'
            ).execute()
            return file
        except Exception as e:
            raise FolderError(f"Failed to move file: {str(e)}")

    def copy_folder(self, folder_id, new_parent_id=None):
        """
        Copy a folder in Google Drive.

        Args:
            folder_id (str): ID of the folder to copy.
            new_parent_id (str, optional): ID of the new parent folder. Defaults to None.

        Returns:
            str: ID of the newly copied folder.
        """
        try:
            folder = {'parents': []}
            if new_parent_id:
                folder['parents'].append(new_parent_id)
            copied_folder = self.service.files().copy(fileId=folder_id, body=folder).execute()
            return copied_folder.get('id')
        except Exception as e:
            raise FolderError(f"Failed to copy folder: {str(e)}")

    def delete_folder(self, folder_id):
        """
        Delete a folder from Google Drive.

        Args:
            folder_id (str): ID of the folder to delete.

        Returns:
            None
        """
        try:
            self.service.files().delete(fileId=folder_id).execute()
        except Exception as e:
            raise FolderError(f"Failed to delete folder: {str(e)}")
import os, io
from ...error import *
from googleapiclient.http import MediaFileUpload, MediaIoBaseDownload


class FileManager:
    """Handles file-related operations in Google Drive."""

    def __init__(self, service):
        self.service = service

    def upload_file(self, file_path, folder_id=None):
        """
        Upload a file to Google Drive.

        Args:
            file_path (str): Path to the file to upload.
            folder_id (str, optional): ID of the folder to upload the file to. Defaults to None.

        Returns:
            str: ID of the uploaded file.
        """
        try:
            file_metadata = {'name': os.path.basename(file_path)}
            if folder_id:
                file_metadata['parents'] = [folder_id]
            media = MediaFileUpload(file_path, resumable=True)
            file = self.service.files().create(body=file_metadata, media_body=media, fields='id').execute()
            return file.get('id')
        except Exception as e:
            raise FileError(f"Failed to upload file: {str(e)}")

    def download_file(self, file_id, destination_path):
        """
        Download a file from Google Drive.

        Args:
            file_id (str): ID of the file to download.
            destination_path (str): Path to save the downloaded file.

        Returns:
            None
        """
        try:
            request = self.service.files().get_media(fileId=file_id)
            with open(destination_path, 'wb') as fh:
                downloader = MediaIoBaseDownload(fh, request)
                done = False
                while not done:
                    status, done = downloader.next_chunk()
        except Exception as e:
            raise FileError(f"Failed to download file: {str(e)}")

    def read_file(self, file_id):
        """
        Read the contents of a file from Google Drive.

        Args:
            file_id (str): ID of the file to read.

        Returns:
            str: Contents of the file.
        """
        try:
            request = self.service.files().get_media(fileId=file_id)
            downloaded_file = io.BytesIO()
            downloader = MediaIoBaseDownload(downloaded_file, request)
            done = False
            while not done:
                status, done = downloader.next_chunk()
            return downloaded_file.getvalue().decode('utf-8')
        except Exception as e:
            raise FileError(f"Failed to read file: {str(e)}")

    def delete_file(self, file_id):
        """
        Delete a file from Google Drive.

        Args:
            file_id (str): ID of the file to delete.

        Returns:
            None
        """
        try:
            self.service.files().delete(fileId=file_id).execute()
        except Exception as e:
            raise FileError(f"Failed to delete file: {str(e)}")
    
    def copy_file(self, file_id, new_parent_id=None):
        """
        Copy a file in Google Drive.

        Args:
            file_id (str): ID of the file to copy.
            new_parent_id (str, optional): ID of the new parent folder. Defaults to None.

        Returns:
            str: ID of the newly copied file.
        """
        try:
            file = {'parents': []}
            if new_parent_id:
                file['parents'].append(new_parent_id)
            copied_file = self.service.files().copy(fileId=file_id, body=file).execute()
            return copied_file.get('id')
        except Exception as e:
            raise FolderError(f"Failed to copy file: {str(e)}")
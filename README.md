# DriveX

## Connect to Google Drive

1. **Installation:**

   Install the DriveX library from PyPI or GitHub.
   
   ```bash
   pip install DriveX
   ```
   
   or
   
   ```bash
   git clone https://github.com/Sepehr0Day/DriveX.git
   ```

2. **Obtain Google Drive API Credentials:**

   - Create a project in the Google Cloud Console.
   - Enable the Google Drive API for your project.
   - Create OAuth client ID credentials.
   - Download the credentials JSON file.

3. **Code:**

   ```python
   from DriveX import ServiceBuilder, GoogleDriveAPI
   
   # Path to the credentials JSON file
   credentials_path = 'credentials.json'
   
   # Path to save token
   token_path = 'Resources/Authenticator'
   
   # Name for the token file
   token_name = 'token'
   
   # Create ServiceBuilder object
   service_builder = ServiceBuilder(credentials_path=credentials_path, token_path=token_path, token_name=token_name)
   
   try:
       # Build service
       drive_service = service_builder.build_service()
       
       # Connect to Google Drive API
       drive_api = GoogleDriveAPI(service=drive_service, credentials=credentials_path)
       
       print("You Successfully Connected To Your Google Drive Account!")     
   
   except Exception as e:
       print(f"An error occurred: {e}")
   ```

   Make sure to replace `'credentials.json'` with the path to your credentials JSON file obtained from the Google Cloud Console.

## Documentation DriveX:

   For more information and advanced usage, refer to the [DriveX documentation](https://Sepehr0day.github.io/DriveX.html).

  
## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/Sepehr0Day/DriveX/blob/main/LICENSE) file for details.

<a href="https://pypi.org/project/DriveX/"><img src="https://img.shields.io/badge/DriveX-1.0-blue"></a> 

## Developer
- **Telegram**: [t.me/Sepehr0Day](https://t.me/Sepehr0Day)

---

Feel free to contribute to the project or report any issues on the GitHub repository!
from setuptools import setup, find_packages

setup(
    name='DriveX',
    version='0.1',
    packages=find_packages(),
    license='MIT',
    description='DriveX library to connect and work with Google Drive!',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Sepehr',
    author_email='sphrz2324@gmail.com',
    url='https://github.com/Sepehr0Day/DriveX/',
    install_requires=[
        'google-auth-oauthlib',
        'google-auth'
    ],
)

import pickle
import os
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload, MediaIoBaseDownload
from google.auth.transport.requests import Request
import logging  # Added for logging

def Create_Service(client_secret_file, api_name, api_version, *scopes):
  """Creates a Google API service object with authentication handling and token caching.

  Args:
      client_secret_file (str): Path to the file containing your OAuth 2.0 credentials (JSON)
      api_name (str): The name of the Google API to access (e.g., 'drive')
      api_version (str): The version of the API to use (e.g., 'v3')
      *scopes (list): A list of scopes required by the API (e.g., ['https://www.googleapis.com/auth/drive'])

  Returns:
      googleapiclient.discovery.Resource: The created service object, or None on error.
  """

  logging.basicConfig(level=logging.DEBUG)  # Configure logging (optional)

  # Print arguments for debugging (uncomment if needed)
  # print(client_secret_file, api_name, api_version, scopes, sep='-')

  # Define the pickle file path for storing credentials
  pickle_file = f'token_{api_name}_{api_version}.pickle'

  # Try loading credentials from the pickle file
  cred = None
  if os.path.exists(pickle_file):
    with open(pickle_file, 'rb') as token:
      cred = pickle.load(token)

  # If credentials are not valid, refresh or obtain new ones
  if not cred or not cred.valid:
    if cred and cred.expired and cred.refresh_token:
      cred.refresh(Request())
    else:
      flow = InstalledAppFlow.from_client_secrets_file(client_secret_file, SCOPES=scopes)
      cred = flow.run_local_server()

    # Save the refreshed or new credentials to the pickle file
    with open(pickle_file, 'wb') as token:
      pickle.dump(cred, token)

  # Build the service object using the credentials
  try:
    service = build(api_name, api_version, credentials=cred)
    logging.info(f'{api_version} service created successfully')
    return service
  except Exception as e:
    logging.error('Unable to connect.')
    logging.error(e)
    return None

# Example usage (replace with your actual information)
# CLIENT_SECRET_FILE = 'path/to/your/credentials.json'
# API_NAME = 'drive'
# API_VERSION = 'v3'
# SCOPES = ['https://www.googleapis.com/auth/drive']
# 
# service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

# Use the service object for your API interactions (refer to Google API documentation)

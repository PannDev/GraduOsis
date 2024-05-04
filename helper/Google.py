from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import json  # for reading credentials

def Create_Service(credentials_file, api_name, api_version, scopes):
  """
  Creates a Google API service object with OAuth 2.0 authentication.

  Args:
      credentials_file (str): Path to the file containing your OAuth 2.0 credentials (JSON)
      api_name (str): The name of the Google API to access (e.g., 'drive')
      api_version (str): The version of the API to use (e.g., 'v3')
      scopes (list): A list of scopes required by the API (e.g., ['https://www.googleapis.com/auth/drive'])

  Returns:
      googleapiclient.discovery.Resource: The created service object.

  Raises:
      Exception: If there's an error creating the service.
  """

  try:
    # Read credentials from the specified file
    with open(credentials_file, 'r') as f:
      credentials = json.load(f)

    # Create an OAuth 2.0 flow object
    flow = InstalledAppFlow.from_client_secrets_file(
        credentials_file, scopes=scopes)

    # Use system-wide token if available (replace with custom token flow if needed)
    credentials = flow.run_local_server(port=0)

    # Build the service object
    service = build(api_name, api_version, credentials=credentials)
    return service
  except Exception as e:
    print(f"Error creating service: {e}")
    raise

# Example usage (replace with your actual information)
# CLIENT_SECRET_FILE = 'path/to/your/credentials.json'  # Replace with your credentials file path
# API_NAME = 'drive'  # Replace with the API name
# API_VERSION = 'v3'  # Replace with the API version
# SCOPES = ['https://www.googleapis.com/auth/drive']  # Replace with required scopes
# 
# service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

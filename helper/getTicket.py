# getTicket
from helper.Google import Create_Service #custom lib
from googleapiclient.http import MediaFileUpload
#Import googleapiclient.http could not be resolved
CLIENT_SECRET_FILE = 'credentials.json'
API_NAME = 'drive'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/drive']
service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

ListIDS = [f'{i}.png' for i in range(1, 40)]  # filenames

def get_folder_id_by_name(folder_name):
    query = f"name='{folder_name}' and mimeType='application/vnd.google-apps.folder' and trashed=false"
    response = service.files().list(q=query, fields='files(id)').execute()
    folders = response.get('files', [])

    if folders:
        return folders[0]['id']
    else:
        return None


def getTicket(folder_name):
    folder_id = get_folder_id_by_name(folder_name)
    if folder_id:
        qFiles = [f"name = '{e}'" for e in ListIDS]
        query = "(" + " or ".join(qFiles) + \
            ") and trashed = false and '" + folder_id + "' in parents"
        response = service.files().list(q=query, fields='files(id,name)').execute()
        files = response.get('files')
        # print(len(files))
        values = {}
        for f in ListIDS:
            for file in files: 
                if f == file.get('name'):
                    file_id = file.get('id')
                    file_url = "https://drive.google.com/file/d/" + file_id + "/view?usp=sharing"
                    # print(f"{f} -> {file_url}")
                    values[f] = file_url
        return values
    else:
        return None
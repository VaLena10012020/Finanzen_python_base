import onedrivesdk
from onedrivesdk.helpers import GetAuthCodeServer


# Install with pip install https://github.com/OneDrive/onedrive-sdk-python/archive/master.zip


class OneDriveConnector:
    def __init__(self, client_id: str, client_secret: str):
        redirect_uri = 'http://localhost:2030/'
        scopes = ['wl.signin', 'wl.offline_access', 'onedrive.readwrite']
        self.client = onedrivesdk.get_default_client(
            client_id=client_id, scopes=scopes)
        auth_url = self.client.auth_provider.get_auth_url(redirect_uri)
        # this will block until we have the code
        code = GetAuthCodeServer.get_auth_code(auth_url, redirect_uri)
        self.client.auth_provider.authenticate(code, redirect_uri, client_secret)
        self.root_folder = self.client.item(drive='me', id='root').children.get()
        # Set connection status
        self.connected = True

    def show_files_in_folder(self, onedrive_path: str, storage: bool = True):
        path_list = onedrive_path.split(sep="/")
        if storage:
            path_list = ["Storage"] + path_list
        parent_folder = self.root_folder
        child_folder = ""
        for path_folder in path_list:
            for folder in parent_folder:
                if folder.name == path_folder:
                    child_folder = folder
                else:
                    pass
            parent_folder = self.client.item(drive='me', id=child_folder.id).children.get()

        files = {}
        for file in parent_folder:
            files.update({file.name: file.id})
        return files

    def download_file(self, id_of_file, name_of_file):
        self.client.item(drive='me', id=id_of_file).download(name_of_file)

    def test_connection(self):
        self.connected = self.show_files_in_folder("TestFolder") == {'MyTestFile.txt': 'F5EDA0E3F2AF815!132'}
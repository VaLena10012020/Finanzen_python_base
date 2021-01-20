import os
import pandas as pd


class credential:
    def __init__(self, filepath, credential_type, fileName = "credentials.csv"):
        self.credential_type = credential_type
        self.credential_available = False
        self.filePath = os.path.join(filepath, fileName)
        
        if os.path.isfile(self.filePath):
            self.credentials = pd.read_csv(self.filePath)
            
            if self.credentials.type.str.contains(self.credential_type).any():
                self.credential_available = True
            else:
                self.credential_available = False
        else:
            self.credential_available = False

    def get_credentials(self):
        if self.credential_available:
            type_user = self.credentials.name.where(self.credentials["type"] == self.credential_type).dropna().tolist()[0]
            type_pw = self.credentials.password.where(self.credentials["type"] == self.credential_type).dropna().tolist()[0]
            return type_user, type_pw
        else:
            return '', ''
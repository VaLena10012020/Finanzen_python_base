import pytest
import os
from Utils.credentials import credential
from Utils.OneDriveConnector import OneDriveConnector


credentials = credential(filepath='/home/valentin/Projekte/Finanzen', credential_type='onedrive')
sec1, sec2 = credentials.get_credentials()
con = OneDriveConnector(sec1, sec2)

def test_showFiles():
    assert con.show_files_in_folder("TestFolder") == {'MyTestFile.txt': 'F5EDA0E3F2AF815!132'}

def test_downloadFile():
    con.download_file(id_of_file='F5EDA0E3F2AF815!132', name_of_file='MyTestFile.txt')
    assert os.path.isfile('MyTestFile.txt')
    os.remove('MyTestFile.txt')
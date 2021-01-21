import pytest
import os

from Utils.credentials import credential

def test_credential_false():
    credentials_false = credential('filepath', 'mail')
    assert credentials_false.credential_available == False
    assert credentials_false.filePath == 'filepath/credentials.csv'
    user, pw = credentials_false.get_credentials()
    assert user == ''
    assert pw == ''
    
def test_credential_path_test():
    credentials_true = credential('/home/valentin/Projekte/Finanzen','tests')
    assert credentials_true.credential_available == True
    user, pw = credentials_true.get_credentials()
    assert user == 'tests'
    assert pw == 'tests'

def test_credential_credentialsfalse():
    credentials_false = credential('/home/valentin/Projekte/Finanzen','notavailable')
    assert credentials_false.credential_available == False
    user, pw = credentials_false.get_credentials()
    assert user == ''
    assert pw == ''

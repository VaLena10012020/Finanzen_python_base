from finanzen_base.Utils import credentials

def test_credential_false():
    credentials_false = credentials('filepath', 'mail')
    assert credentials_false.credential_available == False
    assert credentials_false.filePath == 'filepath/credentials.csv'
    user, pw = credentials_false.get_credentials()
    assert user == ''
    assert pw == ''
    
def test_credential_path_test():
    credentials_true = credentials('/home/valentin/Projekte/Finanzen','tests')
    assert credentials_true.credential_available == True
    user, pw = credentials_true.get_credentials()
    assert user == 'tests'
    assert pw == 'tests'

def test_credential_credentialsfalse():
    credentials_false = credentials('/home/valentin/Projekte/Finanzen','notavailable')
    assert credentials_false.credential_available == False
    user, pw = credentials_false.get_credentials()
    assert user == ''
    assert pw == ''

from unittest.mock import patch

import pytest
from unittest import mock

import main_folder.session
from main_folder.session import Session

@pytest.fixture
def fake_session():
    session = Session(nick="fakeuser")
    session.db_password = "fakepassword"
    session.usertype = "normal"
    return session

def test_authentication_correct_password(fake_session):
    fake_session.password = "fakepassword"
    assert fake_session.authentication() == True

def test_authentication_incorrect_password(fake_session):
    fake_session.password = "wrongpassword"
    assert fake_session.authentication() == False

def test_check_privilages_unknown_user_type(fake_session, capsys):
    fake_session.usertype = "unknown"
    fake_session.check_privilages()
    assert capsys.readouterr().out == "Unknown user type, back to main menu\n"

def test_no_nick_given(fake_session, capsys):
    fake_session.nickname = None
    assert fake_session.log_in() == False
    assert capsys.readouterr().out == "No username is given, returning to main menu...\n\n"


@mock.patch("main_folder.session.Session.read_password", return_value="")
@mock.patch("main_folder.session.Session.authentication", return_value=False)
def test_three_unsuccessful_login_attempts(mocker, _password, fake_session):
    fake_session.log_in()
    assert mocker.call_count == 3
    assert fake_session.log_in() == False






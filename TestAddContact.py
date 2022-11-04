# -*- coding: utf-8 -*-
from python_train.contact import Contact
from application import Application
import pytest

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_contact(app):
    app.login(username="admin", password="secret")
    app.create_contact(Contact(firstname="First", middlename="Middle", lastname="Last", nickname="Nick", title="Title", company="Company", address="Address", home="+79010001100", mobile="+79010001101", work="+79010001102", fax="netu faxa", email="email@email.com", email2="email2@email.com", email3="email3@email.com", homepage="ya.ru", bday="1", bmonth="January", byear="1993", aday="2", amonth="February", ayear="1994", address2="Address2", phone2="phone2 495", notes="note note note"))
    app.logout()

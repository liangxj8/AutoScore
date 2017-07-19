# -*- coding: utf-8 -*-
import requests
import configparser
from bs4 import BeautifulSoup

session = requests.Session()


def login(url, username=None, password=None):
    if not username:
        username = input('Please input your NetID: ')
    if not password:
        password = input('Please input your password: ')
    response = session.get(url, cookies=session.cookies)
    try:
        soup = BeautifulSoup(response.text, 'html.parser')
        lt = soup.find('input', {'name': 'lt'})['value']
        execution = soup.find('input', {'name': 'execution'})['value']
        payload = {
            'username': username,
            'password': password,
            'lt': lt,
            'execution': execution,
            '_eventId': 'submit',
            'submit': '登录'
        }
        response = session.post(url, data=payload, cookies=session.cookies)
        return response
    except TypeError:
        # 已经登录
        return response


def cas_login(url, username, password):
    response = login(url, username, password)
    soup = BeautifulSoup(response.text, 'html.parser')
    while soup.find_all(class_="errors"):
        print(soup.find(id='msg').string, end="\n\n")
        response = login(url)
        soup = BeautifulSoup(response.text, 'html.parser')
    print('Log In Successful')
    return response


def cas_logout():
    session.get('https://cas.sysu.edu.cn/cas/logout', cookies=session.cookies)

if __name__ == '__main__':
    config = configparser.ConfigParser()
    config.read('config.ini')
    NetID = config['CAS']['netid']
    Password = config['CAS']['password']
    cas_login('https://cas.sysu.edu.cn/cas/login', NetID, Password)

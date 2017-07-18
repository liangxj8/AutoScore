# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup


def login(url, username=None, password=None):
    if not username:
        username = input('Please input your NetID: ')
    if not password:
        password = input('Please input your password: ')
    soup = BeautifulSoup(requests.get(url).text, 'html.parser')
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
    response = requests.post(url, data=payload)
    return response


def cas_login(url, username, password):
    response = login(url, username, password)
    soup = BeautifulSoup(response.text, 'html.parser')
    while soup.find(id='msg'):
        print(soup.find(id='msg').string, end="\n\n")
        response = login(url)
        soup = BeautifulSoup(response.text, 'html.parser')
    print('Log In Successful')
    return response


if __name__ == '__main__':
    cas_login('https://cas.sysu.edu.cn/cas/login')

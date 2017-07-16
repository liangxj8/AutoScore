# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup


def login():
    username = input('Please input your NetID: ')
    password = input('Please input your password: ')
    soup = BeautifulSoup(requests.get('https://cas.sysu.edu.cn/cas/login').text, 'html.parser')
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
    return BeautifulSoup(requests.post('https://cas.sysu.edu.cn/cas/login', data=payload).text, 'html.parser')


def cas_login():
    soup = login()
    while soup.find(id='msg').string:
        print(soup.find(id='msg').string, end="\n\n")
        soup = login()
    print('Log In Successful')


if __name__ == '__main__':
    cas_login()

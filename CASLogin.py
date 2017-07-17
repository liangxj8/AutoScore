# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup


def login(url):
    username = input('Please input your NetID: ')
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


def cas_login(url):
    response = login(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    while soup.find(id='msg'):
        print(soup.find(id='msg').string, end="\n\n")
        response = login(url)
        soup = BeautifulSoup(response.text, 'html.parser')
    print('Log In Successful', end="\n\n")
    return response


if __name__ == '__main__':
    cas_login('https://cas.sysu.edu.cn/cas/login')

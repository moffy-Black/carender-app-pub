# -*- coding:utf-8 -*-

from app.urls import api

if __name__ == '__main__':
    address = '0.0.0.0'
    port = 5051
    api.run()
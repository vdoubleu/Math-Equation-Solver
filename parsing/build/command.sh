#!/bin/bash
chmod u+x command.sh
python server.py
npm start
g++ parse.cpp -std=c++11 -O3 -lboost_system -lboost_thread -lpthread

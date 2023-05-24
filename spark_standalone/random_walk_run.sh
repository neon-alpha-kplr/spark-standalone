#!/bin/bash

rm -dr in/AAPL/*
rm -dr in/AMZN/*
rm -dr in/GOOG/*
rm -dr in/GOOGL/*
rm -dr in/MSFT/*

python random_walk.py --symbol=AAPL --max_iter=1000 --batch=10 --interval=90 &
python random_walk.py --symbol=AMZN --max_iter=1000 --batch=10 --interval=90 &
python random_walk.py --symbol=GOOG --max_iter=1000 --batch=10 --interval=90 &
python random_walk.py --symbol=GOOGL --max_iter=1000 --batch=10 --interval=90 &
python random_walk.py --symbol=MSFT --max_iter=1000 --batch=10 --interval=90 &

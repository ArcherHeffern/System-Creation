#!/usr/bin/env bash

# TODO: Sleep .5 is sketchy

python3 math_server.py&
sleep .5
i=$!
python math_client.py
kill $i

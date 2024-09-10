#!/usr/bin/env bash

python3 math_server.py&
sleep .5
i=$!
python3 math_client.py
kill $i

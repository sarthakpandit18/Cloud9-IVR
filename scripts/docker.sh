#!/bin/bash
docker build -t --no-cache group19 .
docker run -p 127.0.0.1:8000:8000 --name c1 group19
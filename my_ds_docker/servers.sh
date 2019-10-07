#!/bin/bash

nohup jupyter-notebook --allow-root --no-browser --ip='*' &
nohup streamlit hello &

sleep infinity

#!/bin/bash

mkdir -p ~/.streamlit
cat config.toml  >~/.streamlit/config.toml
cat credentials.toml  >~/.streamlit/credentials.toml

#EOF
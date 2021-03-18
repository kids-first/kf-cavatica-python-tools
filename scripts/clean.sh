#!/bin/bash

black --check --line-length 80 kf_lib_data_ingest tests
flake8 --ignore=E501,W503,E203 kf_lib_data_ingest
flake8 --ignore=E501,W503,E203 tests
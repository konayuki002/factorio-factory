#!/bin/bash

black .
isort .
ruff format .

# daas_py_auth
## Project

Refrence of DaaS Project - https://github.com/nealrout/daas_docs

## Description
authentication and authorization entry point.  The core apis will require consumers to   
1.) Call http://localhost/api/auth/login/ with basic auth . If successfully get JWT (access token)  
2.) Update bearer token before calling domain apis.  
3.) Provide list of fac_code in the query paramenter facility.

## Table of Contents
- [Requirements](#requirements)
- [Install-Uninstall](#install-uninstall)
- [Usage](#usage)
- [Features](#features)
- [Miscellaneous](#miscellaneous)
- [Contact](#contact)

## Requirements


## Install-Uninstall
__Install:__  
python -m pip install daas_py_auth

__Uninstall:__  
python -m pip uninstall daas_py_auth

__Rebuild from source:__  
python -m pip install --no-binary :all: .

## Usage
from daas_py_auth.logging_config import logger

## Package
python -m build daas_py_auth

## Features
- 

## Miscellaneous


## Contact
Neal Routson  
nroutson@gmail.com

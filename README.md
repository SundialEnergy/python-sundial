# sundial
Sundial optimises renewable power generation

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 1.0.0
- Package version: 1.0.0
- Build package: io.swagger.codegen.v3.generators.python.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import sundial 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import sundial
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import sundial
from sundial.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = sundial.AdviceControllerApi(sundial.ApiClient(configuration))
id = 1.2 # float | 

try:
    api_response = api_instance.advice_controller_get_plant_advice(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdviceControllerApi->advice_controller_get_plant_advice: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *https://api.sundial.energy*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AdviceControllerApi* | [**advice_controller_get_plant_advice**](docs/AdviceControllerApi.md#advice_controller_get_plant_advice) | **GET** /plants/{id}/advice | 
*PlantControllerApi* | [**plant_controller_create**](docs/PlantControllerApi.md#plant_controller_create) | **POST** /plants | 
*PlantControllerApi* | [**plant_controller_delete_by_id**](docs/PlantControllerApi.md#plant_controller_delete_by_id) | **DELETE** /plants/{id} | 
*PlantControllerApi* | [**plant_controller_find**](docs/PlantControllerApi.md#plant_controller_find) | **GET** /plants | 
*PlantControllerApi* | [**plant_controller_find_by_id**](docs/PlantControllerApi.md#plant_controller_find_by_id) | **GET** /plants/{id} | 
*PlantControllerApi* | [**plant_controller_replace_by_id**](docs/PlantControllerApi.md#plant_controller_replace_by_id) | **PUT** /plants/{id} | 

## Documentation For Models

 - [Advice](docs/Advice.md)
 - [AdviceRecommendations](docs/AdviceRecommendations.md)
 - [NewPlant](docs/NewPlant.md)
 - [OneOfPlantFilter1Order](docs/OneOfPlantFilter1Order.md)
 - [OneOfPlantFilterOrder](docs/OneOfPlantFilterOrder.md)
 - [Plant](docs/Plant.md)
 - [PlantFields](docs/PlantFields.md)
 - [PlantFilter](docs/PlantFilter.md)
 - [PlantFilter1](docs/PlantFilter1.md)

## Documentation For Authorization


## jwt



## Author



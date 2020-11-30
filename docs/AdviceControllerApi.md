# sundial.AdviceControllerApi

All URIs are relative to *https://api.sundial.energy*

Method | HTTP request | Description
------------- | ------------- | -------------
[**advice_controller_get_plant_advice**](AdviceControllerApi.md#advice_controller_get_plant_advice) | **GET** /plants/{id}/advice | 

# **advice_controller_get_plant_advice**
> Advice advice_controller_get_plant_advice(id)



### Example
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

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**|  | 

### Return type

[**Advice**](Advice.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


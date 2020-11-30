# sundial.PlantControllerApi

All URIs are relative to *https://api.sundial.energy*

Method | HTTP request | Description
------------- | ------------- | -------------
[**plant_controller_create**](PlantControllerApi.md#plant_controller_create) | **POST** /plants | 
[**plant_controller_delete_by_id**](PlantControllerApi.md#plant_controller_delete_by_id) | **DELETE** /plants/{id} | 
[**plant_controller_find**](PlantControllerApi.md#plant_controller_find) | **GET** /plants | 
[**plant_controller_find_by_id**](PlantControllerApi.md#plant_controller_find_by_id) | **GET** /plants/{id} | 
[**plant_controller_replace_by_id**](PlantControllerApi.md#plant_controller_replace_by_id) | **PUT** /plants/{id} | 

# **plant_controller_create**
> Plant plant_controller_create(body=body)



### Example
```python
from __future__ import print_function
import time
import sundial
from sundial.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = sundial.PlantControllerApi(sundial.ApiClient(configuration))
body = sundial.NewPlant() # NewPlant |  (optional)

try:
    api_response = api_instance.plant_controller_create(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlantControllerApi->plant_controller_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NewPlant**](NewPlant.md)|  | [optional] 

### Return type

[**Plant**](Plant.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **plant_controller_delete_by_id**
> plant_controller_delete_by_id(id)



### Example
```python
from __future__ import print_function
import time
import sundial
from sundial.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = sundial.PlantControllerApi(sundial.ApiClient(configuration))
id = 1.2 # float | 

try:
    api_instance.plant_controller_delete_by_id(id)
except ApiException as e:
    print("Exception when calling PlantControllerApi->plant_controller_delete_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**|  | 

### Return type

void (empty response body)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **plant_controller_find**
> list[Plant] plant_controller_find(filter=filter)



### Example
```python
from __future__ import print_function
import time
import sundial
from sundial.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = sundial.PlantControllerApi(sundial.ApiClient(configuration))
filter = sundial.PlantFilter1() # PlantFilter1 |  (optional)

try:
    api_response = api_instance.plant_controller_find(filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlantControllerApi->plant_controller_find: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | [**PlantFilter1**](.md)|  | [optional] 

### Return type

[**list[Plant]**](Plant.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **plant_controller_find_by_id**
> Plant plant_controller_find_by_id(id, filter=filter)



### Example
```python
from __future__ import print_function
import time
import sundial
from sundial.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = sundial.PlantControllerApi(sundial.ApiClient(configuration))
id = 1.2 # float | 
filter = sundial.PlantFilter() # PlantFilter |  (optional)

try:
    api_response = api_instance.plant_controller_find_by_id(id, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlantControllerApi->plant_controller_find_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**|  | 
 **filter** | [**PlantFilter**](.md)|  | [optional] 

### Return type

[**Plant**](Plant.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **plant_controller_replace_by_id**
> plant_controller_replace_by_id(id, body=body)



### Example
```python
from __future__ import print_function
import time
import sundial
from sundial.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = sundial.PlantControllerApi(sundial.ApiClient(configuration))
id = 1.2 # float | 
body = sundial.Plant() # Plant |  (optional)

try:
    api_instance.plant_controller_replace_by_id(id, body=body)
except ApiException as e:
    print("Exception when calling PlantControllerApi->plant_controller_replace_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**|  | 
 **body** | [**Plant**](Plant.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


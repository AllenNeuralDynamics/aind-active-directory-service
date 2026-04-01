# aind_active_directory_service_client.DefaultApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_user_from_active_directory**](DefaultApi.md#get_user_from_active_directory) | **GET** /user_info/{username} | Get User From Active Directory


# **get_user_from_active_directory**
> UserInfo get_user_from_active_directory(username)

Get User From Active Directory

Queries active directory for user information

Params:
    username (str): user login or full name

Returns:
    UserInfo: user information from Active Directory

### Example


```python
import aind_active_directory_service_client
from aind_active_directory_service_client.models.user_info import UserInfo
from aind_active_directory_service_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = aind_active_directory_service_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with aind_active_directory_service_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = aind_active_directory_service_client.DefaultApi(api_client)
    username = 'username_example' # str | 

    try:
        # Get User From Active Directory
        api_response = api_instance.get_user_from_active_directory(username)
        print("The response of DefaultApi->get_user_from_active_directory:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_user_from_active_directory: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 

### Return type

[**UserInfo**](UserInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


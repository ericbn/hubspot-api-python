# coding: utf-8

"""
    Properties

    All HubSpot objects store data in default and custom properties. These endpoints provide access to read and modify object properties in HubSpot.  # noqa: E501

    The version of the OpenAPI document: v3
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from hubspot.crm.properties.api_client import ApiClient
from hubspot.crm.properties.exceptions import ApiTypeError, ApiValueError


class BatchApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def archive(self, object_type, batch_input_property_name, **kwargs):  # noqa: E501
        """Archive a batch of properties  # noqa: E501

        Archive a provided list of properties. This method will return a 204 No Content response on success regardless of the initial state of the property (e.g. active, already archived, non-existent).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.archive(object_type, batch_input_property_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str object_type: (required)
        :param BatchInputPropertyName batch_input_property_name: (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        return self.archive_with_http_info(
            object_type, batch_input_property_name, **kwargs
        )  # noqa: E501

    def archive_with_http_info(
        self, object_type, batch_input_property_name, **kwargs
    ):  # noqa: E501
        """Archive a batch of properties  # noqa: E501

        Archive a provided list of properties. This method will return a 204 No Content response on success regardless of the initial state of the property (e.g. active, already archived, non-existent).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.archive_with_http_info(object_type, batch_input_property_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str object_type: (required)
        :param BatchInputPropertyName batch_input_property_name: (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ["object_type", "batch_input_property_name"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        for key, val in six.iteritems(local_var_params["kwargs"]):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'" " to method archive" % key
                )
            local_var_params[key] = val
        del local_var_params["kwargs"]
        # verify the required parameter 'object_type' is set
        if self.api_client.client_side_validation and (
            "object_type" not in local_var_params
            or local_var_params["object_type"] is None  # noqa: E501
        ):  # noqa: E501
            raise ApiValueError(
                "Missing the required parameter `object_type` when calling `archive`"
            )  # noqa: E501
        # verify the required parameter 'batch_input_property_name' is set
        if self.api_client.client_side_validation and (
            "batch_input_property_name" not in local_var_params
            or local_var_params["batch_input_property_name"] is None  # noqa: E501
        ):  # noqa: E501
            raise ApiValueError(
                "Missing the required parameter `batch_input_property_name` when calling `archive`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "object_type" in local_var_params:
            path_params["objectType"] = local_var_params["object_type"]  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if "batch_input_property_name" in local_var_params:
            body_params = local_var_params["batch_input_property_name"]
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(
            ["*/*"]
        )  # noqa: E501

        # HTTP header `Content-Type`
        header_params[
            "Content-Type"
        ] = self.api_client.select_header_content_type(  # noqa: E501
            ["application/json"]
        )  # noqa: E501

        # Authentication setting
        auth_settings = ["hapikey", "oauth2"]  # noqa: E501

        return self.api_client.call_api(
            "/crm/v3/properties/{objectType}/batch/archive",
            "POST",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get("async_req"),
            _return_http_data_only=local_var_params.get(
                "_return_http_data_only"
            ),  # noqa: E501
            _preload_content=local_var_params.get("_preload_content", True),
            _request_timeout=local_var_params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def create(self, object_type, batch_input_property_create, **kwargs):  # noqa: E501
        """Create a batch of properties  # noqa: E501

        Create a batch of properties using the same rules as when creating an individual property.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create(object_type, batch_input_property_create, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str object_type: (required)
        :param BatchInputPropertyCreate batch_input_property_create: (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: BatchResponseProperty
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        return self.create_with_http_info(
            object_type, batch_input_property_create, **kwargs
        )  # noqa: E501

    def create_with_http_info(
        self, object_type, batch_input_property_create, **kwargs
    ):  # noqa: E501
        """Create a batch of properties  # noqa: E501

        Create a batch of properties using the same rules as when creating an individual property.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_with_http_info(object_type, batch_input_property_create, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str object_type: (required)
        :param BatchInputPropertyCreate batch_input_property_create: (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(BatchResponseProperty, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ["object_type", "batch_input_property_create"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        for key, val in six.iteritems(local_var_params["kwargs"]):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'" " to method create" % key
                )
            local_var_params[key] = val
        del local_var_params["kwargs"]
        # verify the required parameter 'object_type' is set
        if self.api_client.client_side_validation and (
            "object_type" not in local_var_params
            or local_var_params["object_type"] is None  # noqa: E501
        ):  # noqa: E501
            raise ApiValueError(
                "Missing the required parameter `object_type` when calling `create`"
            )  # noqa: E501
        # verify the required parameter 'batch_input_property_create' is set
        if self.api_client.client_side_validation and (
            "batch_input_property_create" not in local_var_params
            or local_var_params["batch_input_property_create"] is None  # noqa: E501
        ):  # noqa: E501
            raise ApiValueError(
                "Missing the required parameter `batch_input_property_create` when calling `create`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "object_type" in local_var_params:
            path_params["objectType"] = local_var_params["object_type"]  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if "batch_input_property_create" in local_var_params:
            body_params = local_var_params["batch_input_property_create"]
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json", "*/*"]
        )  # noqa: E501

        # HTTP header `Content-Type`
        header_params[
            "Content-Type"
        ] = self.api_client.select_header_content_type(  # noqa: E501
            ["application/json"]
        )  # noqa: E501

        # Authentication setting
        auth_settings = ["hapikey", "oauth2"]  # noqa: E501

        return self.api_client.call_api(
            "/crm/v3/properties/{objectType}/batch/create",
            "POST",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="BatchResponseProperty",  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get("async_req"),
            _return_http_data_only=local_var_params.get(
                "_return_http_data_only"
            ),  # noqa: E501
            _preload_content=local_var_params.get("_preload_content", True),
            _request_timeout=local_var_params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def read(self, object_type, batch_read_input_property_name, **kwargs):  # noqa: E501
        """Read a batch of properties  # noqa: E501

        Read a provided list of properties.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.read(object_type, batch_read_input_property_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str object_type: (required)
        :param BatchReadInputPropertyName batch_read_input_property_name: (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: BatchResponseProperty
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        return self.read_with_http_info(
            object_type, batch_read_input_property_name, **kwargs
        )  # noqa: E501

    def read_with_http_info(
        self, object_type, batch_read_input_property_name, **kwargs
    ):  # noqa: E501
        """Read a batch of properties  # noqa: E501

        Read a provided list of properties.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.read_with_http_info(object_type, batch_read_input_property_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str object_type: (required)
        :param BatchReadInputPropertyName batch_read_input_property_name: (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(BatchResponseProperty, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ["object_type", "batch_read_input_property_name"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        for key, val in six.iteritems(local_var_params["kwargs"]):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'" " to method read" % key
                )
            local_var_params[key] = val
        del local_var_params["kwargs"]
        # verify the required parameter 'object_type' is set
        if self.api_client.client_side_validation and (
            "object_type" not in local_var_params
            or local_var_params["object_type"] is None  # noqa: E501
        ):  # noqa: E501
            raise ApiValueError(
                "Missing the required parameter `object_type` when calling `read`"
            )  # noqa: E501
        # verify the required parameter 'batch_read_input_property_name' is set
        if self.api_client.client_side_validation and (
            "batch_read_input_property_name" not in local_var_params
            or local_var_params["batch_read_input_property_name"] is None  # noqa: E501
        ):  # noqa: E501
            raise ApiValueError(
                "Missing the required parameter `batch_read_input_property_name` when calling `read`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "object_type" in local_var_params:
            path_params["objectType"] = local_var_params["object_type"]  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if "batch_read_input_property_name" in local_var_params:
            body_params = local_var_params["batch_read_input_property_name"]
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json", "*/*"]
        )  # noqa: E501

        # HTTP header `Content-Type`
        header_params[
            "Content-Type"
        ] = self.api_client.select_header_content_type(  # noqa: E501
            ["application/json"]
        )  # noqa: E501

        # Authentication setting
        auth_settings = ["hapikey", "oauth2"]  # noqa: E501

        return self.api_client.call_api(
            "/crm/v3/properties/{objectType}/batch/read",
            "POST",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="BatchResponseProperty",  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get("async_req"),
            _return_http_data_only=local_var_params.get(
                "_return_http_data_only"
            ),  # noqa: E501
            _preload_content=local_var_params.get("_preload_content", True),
            _request_timeout=local_var_params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

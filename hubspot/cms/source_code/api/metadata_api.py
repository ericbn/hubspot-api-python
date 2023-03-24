# coding: utf-8

"""
    CMS Source Code

    Endpoints for interacting with files in the CMS Developer File System. These files include HTML templates, CSS, JS, modules, and other assets which are used to create CMS content.  # noqa: E501

    The version of the OpenAPI document: v3
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from hubspot.cms.source_code.api_client import ApiClient
from hubspot.cms.source_code.exceptions import ApiTypeError, ApiValueError


class MetadataApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get(self, environment, path, **kwargs):  # noqa: E501
        """Get the metadata for a file  # noqa: E501

        Gets the metadata object for the file at the specified path in the specified environment.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get(environment, path, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str environment: The environment of the file (\"draft\" or \"published\"). (required)
        :param str path: The file system location of the file. (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: AssetFileMetadata
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        return self.get_with_http_info(environment, path, **kwargs)  # noqa: E501

    def get_with_http_info(self, environment, path, **kwargs):  # noqa: E501
        """Get the metadata for a file  # noqa: E501

        Gets the metadata object for the file at the specified path in the specified environment.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_with_http_info(environment, path, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str environment: The environment of the file (\"draft\" or \"published\"). (required)
        :param str path: The file system location of the file. (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(AssetFileMetadata, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ["environment", "path"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        for key, val in six.iteritems(local_var_params["kwargs"]):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'" " to method get" % key
                )
            local_var_params[key] = val
        del local_var_params["kwargs"]
        # verify the required parameter 'environment' is set
        if self.api_client.client_side_validation and (
            "environment" not in local_var_params
            or local_var_params["environment"] is None  # noqa: E501
        ):  # noqa: E501
            raise ApiValueError(
                "Missing the required parameter `environment` when calling `get`"
            )  # noqa: E501
        # verify the required parameter 'path' is set
        if self.api_client.client_side_validation and (
            "path" not in local_var_params
            or local_var_params["path"] is None  # noqa: E501
        ):  # noqa: E501
            raise ApiValueError(
                "Missing the required parameter `path` when calling `get`"
            )  # noqa: E501

        if (
            self.api_client.client_side_validation
            and "path" in local_var_params
            and not re.search(r".+", local_var_params["path"])
        ):  # noqa: E501
            raise ApiValueError(
                "Invalid value for parameter `path` when calling `get`, must conform to the pattern `/.+/`"
            )  # noqa: E501
        collection_formats = {}

        path_params = {}
        if "environment" in local_var_params:
            path_params["environment"] = local_var_params["environment"]  # noqa: E501
        if "path" in local_var_params:
            path_params["path"] = local_var_params["path"]  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json", "*/*"]
        )  # noqa: E501

        # Authentication setting
        auth_settings = ["hapikey", "oauth2"]  # noqa: E501

        return self.api_client.call_api(
            "/cms/v3/source-code/{environment}/metadata/{path}",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="AssetFileMetadata",  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get("async_req"),
            _return_http_data_only=local_var_params.get(
                "_return_http_data_only"
            ),  # noqa: E501
            _preload_content=local_var_params.get("_preload_content", True),
            _request_timeout=local_var_params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

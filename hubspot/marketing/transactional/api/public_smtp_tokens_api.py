# coding: utf-8

"""
    Transactional Email

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v3
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from hubspot.marketing.transactional.api_client import ApiClient
from hubspot.marketing.transactional.exceptions import ApiTypeError, ApiValueError


class PublicSmtpTokensApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def archive_token(self, token_id, **kwargs):  # noqa: E501
        """Delete a single token by ID.  # noqa: E501

        Delete a single token by ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.archive_token(token_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str token_id: Identifier generated when a token is created. (required)
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
        return self.archive_token_with_http_info(token_id, **kwargs)  # noqa: E501

    def archive_token_with_http_info(self, token_id, **kwargs):  # noqa: E501
        """Delete a single token by ID.  # noqa: E501

        Delete a single token by ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.archive_token_with_http_info(token_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str token_id: Identifier generated when a token is created. (required)
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

        all_params = ["token_id"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        for key, val in six.iteritems(local_var_params["kwargs"]):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method archive_token" % key
                )
            local_var_params[key] = val
        del local_var_params["kwargs"]
        # verify the required parameter 'token_id' is set
        if self.api_client.client_side_validation and (
            "token_id" not in local_var_params
            or local_var_params["token_id"] is None  # noqa: E501
        ):  # noqa: E501
            raise ApiValueError(
                "Missing the required parameter `token_id` when calling `archive_token`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "token_id" in local_var_params:
            path_params["tokenId"] = local_var_params["token_id"]  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(
            ["*/*"]
        )  # noqa: E501

        # Authentication setting
        auth_settings = ["oauth2"]  # noqa: E501

        return self.api_client.call_api(
            "/marketing/v3/transactional/smtp-tokens/{tokenId}",
            "DELETE",
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

    def create_token(self, smtp_api_token_request_egg, **kwargs):  # noqa: E501
        """Create a SMTP API token.  # noqa: E501

        Create a SMTP API token.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_token(smtp_api_token_request_egg, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param SmtpApiTokenRequestEgg smtp_api_token_request_egg: A request object that includes the campaign name tied to the token and whether contacts should be created for email recipients. (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: SmtpApiTokenView
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        return self.create_token_with_http_info(
            smtp_api_token_request_egg, **kwargs
        )  # noqa: E501

    def create_token_with_http_info(
        self, smtp_api_token_request_egg, **kwargs
    ):  # noqa: E501
        """Create a SMTP API token.  # noqa: E501

        Create a SMTP API token.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_token_with_http_info(smtp_api_token_request_egg, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param SmtpApiTokenRequestEgg smtp_api_token_request_egg: A request object that includes the campaign name tied to the token and whether contacts should be created for email recipients. (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(SmtpApiTokenView, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ["smtp_api_token_request_egg"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        for key, val in six.iteritems(local_var_params["kwargs"]):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_token" % key
                )
            local_var_params[key] = val
        del local_var_params["kwargs"]
        # verify the required parameter 'smtp_api_token_request_egg' is set
        if self.api_client.client_side_validation and (
            "smtp_api_token_request_egg" not in local_var_params
            or local_var_params["smtp_api_token_request_egg"] is None  # noqa: E501
        ):  # noqa: E501
            raise ApiValueError(
                "Missing the required parameter `smtp_api_token_request_egg` when calling `create_token`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if "smtp_api_token_request_egg" in local_var_params:
            body_params = local_var_params["smtp_api_token_request_egg"]
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
        auth_settings = ["oauth2"]  # noqa: E501

        return self.api_client.call_api(
            "/marketing/v3/transactional/smtp-tokens",
            "POST",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="SmtpApiTokenView",  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get("async_req"),
            _return_http_data_only=local_var_params.get(
                "_return_http_data_only"
            ),  # noqa: E501
            _preload_content=local_var_params.get("_preload_content", True),
            _request_timeout=local_var_params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def get_token_by_id(self, token_id, **kwargs):  # noqa: E501
        """Query a single token by ID.  # noqa: E501

        Query a single token by ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_token_by_id(token_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str token_id: Identifier generated when a token is created. (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: SmtpApiTokenView
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        return self.get_token_by_id_with_http_info(token_id, **kwargs)  # noqa: E501

    def get_token_by_id_with_http_info(self, token_id, **kwargs):  # noqa: E501
        """Query a single token by ID.  # noqa: E501

        Query a single token by ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_token_by_id_with_http_info(token_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str token_id: Identifier generated when a token is created. (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(SmtpApiTokenView, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ["token_id"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        for key, val in six.iteritems(local_var_params["kwargs"]):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_token_by_id" % key
                )
            local_var_params[key] = val
        del local_var_params["kwargs"]
        # verify the required parameter 'token_id' is set
        if self.api_client.client_side_validation and (
            "token_id" not in local_var_params
            or local_var_params["token_id"] is None  # noqa: E501
        ):  # noqa: E501
            raise ApiValueError(
                "Missing the required parameter `token_id` when calling `get_token_by_id`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "token_id" in local_var_params:
            path_params["tokenId"] = local_var_params["token_id"]  # noqa: E501

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
        auth_settings = ["oauth2"]  # noqa: E501

        return self.api_client.call_api(
            "/marketing/v3/transactional/smtp-tokens/{tokenId}",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="SmtpApiTokenView",  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get("async_req"),
            _return_http_data_only=local_var_params.get(
                "_return_http_data_only"
            ),  # noqa: E501
            _preload_content=local_var_params.get("_preload_content", True),
            _request_timeout=local_var_params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def get_tokens_page(self, **kwargs):  # noqa: E501
        """Query SMTP API tokens by campaign name or an emailCampaignId.  # noqa: E501

        Query multiple SMTP API tokens by campaign name or a single token by emailCampaignId.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_tokens_page(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str campaign_name: A name for the campaign tied to the SMTP API token.
        :param str email_campaign_id: Identifier assigned to the campaign provided during the token creation.
        :param str after: Starting point to get the next set of results.
        :param int limit: Maximum number of tokens to return.
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: CollectionResponseSmtpApiTokenViewForwardPaging
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        return self.get_tokens_page_with_http_info(**kwargs)  # noqa: E501

    def get_tokens_page_with_http_info(self, **kwargs):  # noqa: E501
        """Query SMTP API tokens by campaign name or an emailCampaignId.  # noqa: E501

        Query multiple SMTP API tokens by campaign name or a single token by emailCampaignId.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_tokens_page_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str campaign_name: A name for the campaign tied to the SMTP API token.
        :param str email_campaign_id: Identifier assigned to the campaign provided during the token creation.
        :param str after: Starting point to get the next set of results.
        :param int limit: Maximum number of tokens to return.
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(CollectionResponseSmtpApiTokenViewForwardPaging, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            "campaign_name",
            "email_campaign_id",
            "after",
            "limit",
        ]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        for key, val in six.iteritems(local_var_params["kwargs"]):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_tokens_page" % key
                )
            local_var_params[key] = val
        del local_var_params["kwargs"]

        collection_formats = {}

        path_params = {}

        query_params = []
        if (
            "campaign_name" in local_var_params
            and local_var_params["campaign_name"] is not None
        ):  # noqa: E501
            query_params.append(
                ("campaignName", local_var_params["campaign_name"])
            )  # noqa: E501
        if (
            "email_campaign_id" in local_var_params
            and local_var_params["email_campaign_id"] is not None
        ):  # noqa: E501
            query_params.append(
                ("emailCampaignId", local_var_params["email_campaign_id"])
            )  # noqa: E501
        if (
            "after" in local_var_params and local_var_params["after"] is not None
        ):  # noqa: E501
            query_params.append(("after", local_var_params["after"]))  # noqa: E501
        if (
            "limit" in local_var_params and local_var_params["limit"] is not None
        ):  # noqa: E501
            query_params.append(("limit", local_var_params["limit"]))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json", "*/*"]
        )  # noqa: E501

        # Authentication setting
        auth_settings = ["oauth2"]  # noqa: E501

        return self.api_client.call_api(
            "/marketing/v3/transactional/smtp-tokens",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="CollectionResponseSmtpApiTokenViewForwardPaging",  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get("async_req"),
            _return_http_data_only=local_var_params.get(
                "_return_http_data_only"
            ),  # noqa: E501
            _preload_content=local_var_params.get("_preload_content", True),
            _request_timeout=local_var_params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def reset_password(self, token_id, **kwargs):  # noqa: E501
        """Reset the password of an existing token.  # noqa: E501

        Allows the creation of a replacement password for a given token. Once the password is successfully reset, the old password for the token will be invalid.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.reset_password(token_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str token_id: Identifier generated when a token is created. (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: SmtpApiTokenView
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        return self.reset_password_with_http_info(token_id, **kwargs)  # noqa: E501

    def reset_password_with_http_info(self, token_id, **kwargs):  # noqa: E501
        """Reset the password of an existing token.  # noqa: E501

        Allows the creation of a replacement password for a given token. Once the password is successfully reset, the old password for the token will be invalid.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.reset_password_with_http_info(token_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str token_id: Identifier generated when a token is created. (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(SmtpApiTokenView, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ["token_id"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        for key, val in six.iteritems(local_var_params["kwargs"]):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method reset_password" % key
                )
            local_var_params[key] = val
        del local_var_params["kwargs"]
        # verify the required parameter 'token_id' is set
        if self.api_client.client_side_validation and (
            "token_id" not in local_var_params
            or local_var_params["token_id"] is None  # noqa: E501
        ):  # noqa: E501
            raise ApiValueError(
                "Missing the required parameter `token_id` when calling `reset_password`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "token_id" in local_var_params:
            path_params["tokenId"] = local_var_params["token_id"]  # noqa: E501

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
        auth_settings = ["oauth2"]  # noqa: E501

        return self.api_client.call_api(
            "/marketing/v3/transactional/smtp-tokens/{tokenId}/password-reset",
            "POST",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="SmtpApiTokenView",  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get("async_req"),
            _return_http_data_only=local_var_params.get(
                "_return_http_data_only"
            ),  # noqa: E501
            _preload_content=local_var_params.get("_preload_content", True),
            _request_timeout=local_var_params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

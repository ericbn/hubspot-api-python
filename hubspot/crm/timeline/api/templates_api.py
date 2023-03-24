# coding: utf-8

"""
    Timeline events

    This feature allows an app to create and configure custom events that can show up in the timelines of certain CRM objects like contacts, companies, tickets, or deals. You'll find multiple use cases for this API in the sections below.  # noqa: E501

    The version of the OpenAPI document: v3
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from hubspot.crm.timeline.api_client import ApiClient
from hubspot.crm.timeline.exceptions import ApiTypeError, ApiValueError


class TemplatesApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def archive(self, event_template_id, app_id, **kwargs):  # noqa: E501
        """Deletes an event template for the app  # noqa: E501

        This will delete the event template. All associated events will be removed from search results and the timeline UI.  This action can't be undone, so it's highly recommended that you stop using any associated events before deleting a template.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.archive(event_template_id, app_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str event_template_id: The event template ID. (required)
        :param int app_id: The ID of the target app. (required)
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
            event_template_id, app_id, **kwargs
        )  # noqa: E501

    def archive_with_http_info(self, event_template_id, app_id, **kwargs):  # noqa: E501
        """Deletes an event template for the app  # noqa: E501

        This will delete the event template. All associated events will be removed from search results and the timeline UI.  This action can't be undone, so it's highly recommended that you stop using any associated events before deleting a template.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.archive_with_http_info(event_template_id, app_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str event_template_id: The event template ID. (required)
        :param int app_id: The ID of the target app. (required)
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

        all_params = ["event_template_id", "app_id"]  # noqa: E501
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
        # verify the required parameter 'event_template_id' is set
        if self.api_client.client_side_validation and (
            "event_template_id" not in local_var_params
            or local_var_params["event_template_id"] is None  # noqa: E501
        ):  # noqa: E501
            raise ApiValueError(
                "Missing the required parameter `event_template_id` when calling `archive`"
            )  # noqa: E501
        # verify the required parameter 'app_id' is set
        if self.api_client.client_side_validation and (
            "app_id" not in local_var_params
            or local_var_params["app_id"] is None  # noqa: E501
        ):  # noqa: E501
            raise ApiValueError(
                "Missing the required parameter `app_id` when calling `archive`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "event_template_id" in local_var_params:
            path_params["eventTemplateId"] = local_var_params[
                "event_template_id"
            ]  # noqa: E501
        if "app_id" in local_var_params:
            path_params["appId"] = local_var_params["app_id"]  # noqa: E501

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
        auth_settings = ["developer_hapikey"]  # noqa: E501

        return self.api_client.call_api(
            "/crm/v3/timeline/{appId}/event-templates/{eventTemplateId}",
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

    def create(
        self, app_id, timeline_event_template_create_request, **kwargs
    ):  # noqa: E501
        """Create an event template for your app  # noqa: E501

        Event templates define the general structure for a custom timeline event. This includes formatted copy for its heading and details, as well as any custom property definitions. The event could be something like viewing a video, registering for a webinar, or filling out a survey. A single app can define multiple event templates.  Event templates will be created for contacts by default, but they can be created for companies, tickets, and deals as well.  Each event template contains its own set of tokens and `Markdown` templates. These tokens can be associated with any CRM object properties via the `objectPropertyName` field to fully build out CRM objects.  You must create an event template before you can create events.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create(app_id, timeline_event_template_create_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int app_id: The ID of the target app. (required)
        :param TimelineEventTemplateCreateRequest timeline_event_template_create_request: The new event template definition. (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: TimelineEventTemplate
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        return self.create_with_http_info(
            app_id, timeline_event_template_create_request, **kwargs
        )  # noqa: E501

    def create_with_http_info(
        self, app_id, timeline_event_template_create_request, **kwargs
    ):  # noqa: E501
        """Create an event template for your app  # noqa: E501

        Event templates define the general structure for a custom timeline event. This includes formatted copy for its heading and details, as well as any custom property definitions. The event could be something like viewing a video, registering for a webinar, or filling out a survey. A single app can define multiple event templates.  Event templates will be created for contacts by default, but they can be created for companies, tickets, and deals as well.  Each event template contains its own set of tokens and `Markdown` templates. These tokens can be associated with any CRM object properties via the `objectPropertyName` field to fully build out CRM objects.  You must create an event template before you can create events.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_with_http_info(app_id, timeline_event_template_create_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int app_id: The ID of the target app. (required)
        :param TimelineEventTemplateCreateRequest timeline_event_template_create_request: The new event template definition. (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(TimelineEventTemplate, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ["app_id", "timeline_event_template_create_request"]  # noqa: E501
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
        # verify the required parameter 'app_id' is set
        if self.api_client.client_side_validation and (
            "app_id" not in local_var_params
            or local_var_params["app_id"] is None  # noqa: E501
        ):  # noqa: E501
            raise ApiValueError(
                "Missing the required parameter `app_id` when calling `create`"
            )  # noqa: E501
        # verify the required parameter 'timeline_event_template_create_request' is set
        if self.api_client.client_side_validation and (
            "timeline_event_template_create_request" not in local_var_params
            or local_var_params["timeline_event_template_create_request"]  # noqa: E501
            is None
        ):  # noqa: E501
            raise ApiValueError(
                "Missing the required parameter `timeline_event_template_create_request` when calling `create`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "app_id" in local_var_params:
            path_params["appId"] = local_var_params["app_id"]  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if "timeline_event_template_create_request" in local_var_params:
            body_params = local_var_params["timeline_event_template_create_request"]
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
        auth_settings = ["developer_hapikey"]  # noqa: E501

        return self.api_client.call_api(
            "/crm/v3/timeline/{appId}/event-templates",
            "POST",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="TimelineEventTemplate",  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get("async_req"),
            _return_http_data_only=local_var_params.get(
                "_return_http_data_only"
            ),  # noqa: E501
            _preload_content=local_var_params.get("_preload_content", True),
            _request_timeout=local_var_params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def get_all(self, app_id, **kwargs):  # noqa: E501
        """List all event templates for your app  # noqa: E501

        Use this to list all event templates owned by your app.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_all(app_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int app_id: The ID of the target app. (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: CollectionResponseTimelineEventTemplateNoPaging
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        return self.get_all_with_http_info(app_id, **kwargs)  # noqa: E501

    def get_all_with_http_info(self, app_id, **kwargs):  # noqa: E501
        """List all event templates for your app  # noqa: E501

        Use this to list all event templates owned by your app.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_all_with_http_info(app_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int app_id: The ID of the target app. (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(CollectionResponseTimelineEventTemplateNoPaging, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ["app_id"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        for key, val in six.iteritems(local_var_params["kwargs"]):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'" " to method get_all" % key
                )
            local_var_params[key] = val
        del local_var_params["kwargs"]
        # verify the required parameter 'app_id' is set
        if self.api_client.client_side_validation and (
            "app_id" not in local_var_params
            or local_var_params["app_id"] is None  # noqa: E501
        ):  # noqa: E501
            raise ApiValueError(
                "Missing the required parameter `app_id` when calling `get_all`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "app_id" in local_var_params:
            path_params["appId"] = local_var_params["app_id"]  # noqa: E501

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
        auth_settings = ["developer_hapikey"]  # noqa: E501

        return self.api_client.call_api(
            "/crm/v3/timeline/{appId}/event-templates",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="CollectionResponseTimelineEventTemplateNoPaging",  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get("async_req"),
            _return_http_data_only=local_var_params.get(
                "_return_http_data_only"
            ),  # noqa: E501
            _preload_content=local_var_params.get("_preload_content", True),
            _request_timeout=local_var_params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def get_by_id(self, event_template_id, app_id, **kwargs):  # noqa: E501
        """Gets a specific event template for your app  # noqa: E501

        View the current state of a specific template and its tokens.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_by_id(event_template_id, app_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str event_template_id: The event template ID. (required)
        :param int app_id: The ID of the target app. (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: TimelineEventTemplate
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        return self.get_by_id_with_http_info(
            event_template_id, app_id, **kwargs
        )  # noqa: E501

    def get_by_id_with_http_info(
        self, event_template_id, app_id, **kwargs
    ):  # noqa: E501
        """Gets a specific event template for your app  # noqa: E501

        View the current state of a specific template and its tokens.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_by_id_with_http_info(event_template_id, app_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str event_template_id: The event template ID. (required)
        :param int app_id: The ID of the target app. (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(TimelineEventTemplate, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ["event_template_id", "app_id"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        for key, val in six.iteritems(local_var_params["kwargs"]):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_by_id" % key
                )
            local_var_params[key] = val
        del local_var_params["kwargs"]
        # verify the required parameter 'event_template_id' is set
        if self.api_client.client_side_validation and (
            "event_template_id" not in local_var_params
            or local_var_params["event_template_id"] is None  # noqa: E501
        ):  # noqa: E501
            raise ApiValueError(
                "Missing the required parameter `event_template_id` when calling `get_by_id`"
            )  # noqa: E501
        # verify the required parameter 'app_id' is set
        if self.api_client.client_side_validation and (
            "app_id" not in local_var_params
            or local_var_params["app_id"] is None  # noqa: E501
        ):  # noqa: E501
            raise ApiValueError(
                "Missing the required parameter `app_id` when calling `get_by_id`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "event_template_id" in local_var_params:
            path_params["eventTemplateId"] = local_var_params[
                "event_template_id"
            ]  # noqa: E501
        if "app_id" in local_var_params:
            path_params["appId"] = local_var_params["app_id"]  # noqa: E501

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
        auth_settings = ["developer_hapikey"]  # noqa: E501

        return self.api_client.call_api(
            "/crm/v3/timeline/{appId}/event-templates/{eventTemplateId}",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="TimelineEventTemplate",  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get("async_req"),
            _return_http_data_only=local_var_params.get(
                "_return_http_data_only"
            ),  # noqa: E501
            _preload_content=local_var_params.get("_preload_content", True),
            _request_timeout=local_var_params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def update(
        self,
        event_template_id,
        app_id,
        timeline_event_template_update_request,
        **kwargs
    ):  # noqa: E501
        """Update an existing event template  # noqa: E501

        Updates an existing template and its tokens. This is primarily used to update the headerTemplate/detailTemplate, and those changes will take effect for existing events.  You can also update or replace all the tokens in the template here instead of doing individual API calls on the `/tokens` endpoint.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update(event_template_id, app_id, timeline_event_template_update_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str event_template_id: The event template ID. (required)
        :param int app_id: The ID of the target app. (required)
        :param TimelineEventTemplateUpdateRequest timeline_event_template_update_request: The updated event template definition. (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: TimelineEventTemplate
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        return self.update_with_http_info(
            event_template_id, app_id, timeline_event_template_update_request, **kwargs
        )  # noqa: E501

    def update_with_http_info(
        self,
        event_template_id,
        app_id,
        timeline_event_template_update_request,
        **kwargs
    ):  # noqa: E501
        """Update an existing event template  # noqa: E501

        Updates an existing template and its tokens. This is primarily used to update the headerTemplate/detailTemplate, and those changes will take effect for existing events.  You can also update or replace all the tokens in the template here instead of doing individual API calls on the `/tokens` endpoint.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_with_http_info(event_template_id, app_id, timeline_event_template_update_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str event_template_id: The event template ID. (required)
        :param int app_id: The ID of the target app. (required)
        :param TimelineEventTemplateUpdateRequest timeline_event_template_update_request: The updated event template definition. (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(TimelineEventTemplate, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            "event_template_id",
            "app_id",
            "timeline_event_template_update_request",
        ]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        for key, val in six.iteritems(local_var_params["kwargs"]):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'" " to method update" % key
                )
            local_var_params[key] = val
        del local_var_params["kwargs"]
        # verify the required parameter 'event_template_id' is set
        if self.api_client.client_side_validation and (
            "event_template_id" not in local_var_params
            or local_var_params["event_template_id"] is None  # noqa: E501
        ):  # noqa: E501
            raise ApiValueError(
                "Missing the required parameter `event_template_id` when calling `update`"
            )  # noqa: E501
        # verify the required parameter 'app_id' is set
        if self.api_client.client_side_validation and (
            "app_id" not in local_var_params
            or local_var_params["app_id"] is None  # noqa: E501
        ):  # noqa: E501
            raise ApiValueError(
                "Missing the required parameter `app_id` when calling `update`"
            )  # noqa: E501
        # verify the required parameter 'timeline_event_template_update_request' is set
        if self.api_client.client_side_validation and (
            "timeline_event_template_update_request" not in local_var_params
            or local_var_params["timeline_event_template_update_request"]  # noqa: E501
            is None
        ):  # noqa: E501
            raise ApiValueError(
                "Missing the required parameter `timeline_event_template_update_request` when calling `update`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "event_template_id" in local_var_params:
            path_params["eventTemplateId"] = local_var_params[
                "event_template_id"
            ]  # noqa: E501
        if "app_id" in local_var_params:
            path_params["appId"] = local_var_params["app_id"]  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if "timeline_event_template_update_request" in local_var_params:
            body_params = local_var_params["timeline_event_template_update_request"]
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
        auth_settings = ["developer_hapikey"]  # noqa: E501

        return self.api_client.call_api(
            "/crm/v3/timeline/{appId}/event-templates/{eventTemplateId}",
            "PUT",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="TimelineEventTemplate",  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get("async_req"),
            _return_http_data_only=local_var_params.get(
                "_return_http_data_only"
            ),  # noqa: E501
            _preload_content=local_var_params.get("_preload_content", True),
            _request_timeout=local_var_params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

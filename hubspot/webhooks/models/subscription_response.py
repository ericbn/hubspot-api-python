# coding: utf-8

"""
    Webhooks API

    Provides a way for apps to subscribe to certain change events in HubSpot. Once configured, apps will receive event payloads containing details about the changes at a specified target URL. There can only be one target URL for receiving event notifications per app.  # noqa: E501

    The version of the OpenAPI document: v3
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from hubspot.webhooks.configuration import Configuration


class SubscriptionResponse(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        "event_type": "str",
        "property_name": "str",
        "active": "bool",
        "id": "str",
        "created_at": "datetime",
        "updated_at": "datetime",
    }

    attribute_map = {
        "event_type": "eventType",
        "property_name": "propertyName",
        "active": "active",
        "id": "id",
        "created_at": "createdAt",
        "updated_at": "updatedAt",
    }

    def __init__(
        self,
        event_type=None,
        property_name=None,
        active=None,
        id=None,
        created_at=None,
        updated_at=None,
        local_vars_configuration=None,
    ):  # noqa: E501
        """SubscriptionResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._event_type = None
        self._property_name = None
        self._active = None
        self._id = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None

        self.event_type = event_type
        if property_name is not None:
            self.property_name = property_name
        self.active = active
        self.id = id
        self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def event_type(self):
        """Gets the event_type of this SubscriptionResponse.  # noqa: E501

        Type of event to listen for. Can be one of `create`, `delete`, `deletedForPrivacy`, or `propertyChange`.  # noqa: E501

        :return: The event_type of this SubscriptionResponse.  # noqa: E501
        :rtype: str
        """
        return self._event_type

    @event_type.setter
    def event_type(self, event_type):
        """Sets the event_type of this SubscriptionResponse.

        Type of event to listen for. Can be one of `create`, `delete`, `deletedForPrivacy`, or `propertyChange`.  # noqa: E501

        :param event_type: The event_type of this SubscriptionResponse.  # noqa: E501
        :type: str
        """
        if (
            self.local_vars_configuration.client_side_validation and event_type is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `event_type`, must not be `None`"
            )  # noqa: E501
        allowed_values = [
            "contact.propertyChange",
            "company.propertyChange",
            "deal.propertyChange",
            "ticket.propertyChange",
            "product.propertyChange",
            "line_item.propertyChange",
            "contact.creation",
            "contact.deletion",
            "contact.privacyDeletion",
            "company.creation",
            "company.deletion",
            "deal.creation",
            "deal.deletion",
            "ticket.creation",
            "ticket.deletion",
            "product.creation",
            "product.deletion",
            "line_item.creation",
            "line_item.deletion",
            "conversation.creation",
            "conversation.deletion",
            "conversation.newMessage",
            "conversation.privacyDeletion",
            "conversation.propertyChange",
        ]  # noqa: E501
        if (
            self.local_vars_configuration.client_side_validation
            and event_type not in allowed_values
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `event_type` ({0}), must be one of {1}".format(  # noqa: E501
                    event_type, allowed_values
                )
            )

        self._event_type = event_type

    @property
    def property_name(self):
        """Gets the property_name of this SubscriptionResponse.  # noqa: E501

        The internal name of the property being monitored for changes. Only applies when `eventType` is `propertyChange`.  # noqa: E501

        :return: The property_name of this SubscriptionResponse.  # noqa: E501
        :rtype: str
        """
        return self._property_name

    @property_name.setter
    def property_name(self, property_name):
        """Sets the property_name of this SubscriptionResponse.

        The internal name of the property being monitored for changes. Only applies when `eventType` is `propertyChange`.  # noqa: E501

        :param property_name: The property_name of this SubscriptionResponse.  # noqa: E501
        :type: str
        """

        self._property_name = property_name

    @property
    def active(self):
        """Gets the active of this SubscriptionResponse.  # noqa: E501

        Determines if the subscription is active or paused.  # noqa: E501

        :return: The active of this SubscriptionResponse.  # noqa: E501
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this SubscriptionResponse.

        Determines if the subscription is active or paused.  # noqa: E501

        :param active: The active of this SubscriptionResponse.  # noqa: E501
        :type: bool
        """
        if (
            self.local_vars_configuration.client_side_validation and active is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `active`, must not be `None`"
            )  # noqa: E501

        self._active = active

    @property
    def id(self):
        """Gets the id of this SubscriptionResponse.  # noqa: E501

        The unique ID of the subscription.  # noqa: E501

        :return: The id of this SubscriptionResponse.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SubscriptionResponse.

        The unique ID of the subscription.  # noqa: E501

        :param id: The id of this SubscriptionResponse.  # noqa: E501
        :type: str
        """
        if (
            self.local_vars_configuration.client_side_validation and id is None
        ):  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def created_at(self):
        """Gets the created_at of this SubscriptionResponse.  # noqa: E501

        When this subscription was created. Formatted as milliseconds from the [Unix epoch](#).  # noqa: E501

        :return: The created_at of this SubscriptionResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this SubscriptionResponse.

        When this subscription was created. Formatted as milliseconds from the [Unix epoch](#).  # noqa: E501

        :param created_at: The created_at of this SubscriptionResponse.  # noqa: E501
        :type: datetime
        """
        if (
            self.local_vars_configuration.client_side_validation and created_at is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `created_at`, must not be `None`"
            )  # noqa: E501

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this SubscriptionResponse.  # noqa: E501

        When this subscription was last updated. Formatted as milliseconds from the [Unix epoch](#).  # noqa: E501

        :return: The updated_at of this SubscriptionResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this SubscriptionResponse.

        When this subscription was last updated. Formatted as milliseconds from the [Unix epoch](#).  # noqa: E501

        :param updated_at: The updated_at of this SubscriptionResponse.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(
                    map(lambda x: x.to_dict() if hasattr(x, "to_dict") else x, value)
                )
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(
                    map(
                        lambda item: (item[0], item[1].to_dict())
                        if hasattr(item[1], "to_dict")
                        else item,
                        value.items(),
                    )
                )
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SubscriptionResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SubscriptionResponse):
            return True

        return self.to_dict() != other.to_dict()

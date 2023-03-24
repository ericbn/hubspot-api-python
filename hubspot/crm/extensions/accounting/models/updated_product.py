# coding: utf-8

"""
    Accounting Extension

    These APIs allow you to interact with HubSpot's Accounting Extension. It allows you to: * Specify the URLs that HubSpot will use when making webhook requests to your external accounting system. * Respond to webhook calls made to your external accounting system by HubSpot   # noqa: E501

    The version of the OpenAPI document: v3
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from hubspot.crm.extensions.accounting.configuration import Configuration


class UpdatedProduct(object):
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
        "sync_action": "str",
        "updated_at": "datetime",
        "price": "float",
        "currency_code": "str",
        "id": "str",
        "properties": "dict(str, str)",
    }

    attribute_map = {
        "sync_action": "syncAction",
        "updated_at": "updatedAt",
        "price": "price",
        "currency_code": "currencyCode",
        "id": "id",
        "properties": "properties",
    }

    def __init__(
        self,
        sync_action=None,
        updated_at=None,
        price=None,
        currency_code=None,
        id=None,
        properties=None,
        local_vars_configuration=None,
    ):  # noqa: E501
        """UpdatedProduct - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._sync_action = None
        self._updated_at = None
        self._price = None
        self._currency_code = None
        self._id = None
        self._properties = None
        self.discriminator = None

        self.sync_action = sync_action
        self.updated_at = updated_at
        self.price = price
        if currency_code is not None:
            self.currency_code = currency_code
        self.id = id
        self.properties = properties

    @property
    def sync_action(self):
        """Gets the sync_action of this UpdatedProduct.  # noqa: E501

        The operation to be performed.  # noqa: E501

        :return: The sync_action of this UpdatedProduct.  # noqa: E501
        :rtype: str
        """
        return self._sync_action

    @sync_action.setter
    def sync_action(self, sync_action):
        """Sets the sync_action of this UpdatedProduct.

        The operation to be performed.  # noqa: E501

        :param sync_action: The sync_action of this UpdatedProduct.  # noqa: E501
        :type: str
        """
        if (
            self.local_vars_configuration.client_side_validation and sync_action is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `sync_action`, must not be `None`"
            )  # noqa: E501
        allowed_values = ["CREATE", "UPDATE", "DELETE"]  # noqa: E501
        if (
            self.local_vars_configuration.client_side_validation
            and sync_action not in allowed_values
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `sync_action` ({0}), must be one of {1}".format(  # noqa: E501
                    sync_action, allowed_values
                )
            )

        self._sync_action = sync_action

    @property
    def updated_at(self):
        """Gets the updated_at of this UpdatedProduct.  # noqa: E501

        The timestamp (ISO8601 format) when the product was updated in the external accounting system.  # noqa: E501

        :return: The updated_at of this UpdatedProduct.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this UpdatedProduct.

        The timestamp (ISO8601 format) when the product was updated in the external accounting system.  # noqa: E501

        :param updated_at: The updated_at of this UpdatedProduct.  # noqa: E501
        :type: datetime
        """
        if (
            self.local_vars_configuration.client_side_validation and updated_at is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `updated_at`, must not be `None`"
            )  # noqa: E501

        self._updated_at = updated_at

    @property
    def price(self):
        """Gets the price of this UpdatedProduct.  # noqa: E501

        The price of the product.  # noqa: E501

        :return: The price of this UpdatedProduct.  # noqa: E501
        :rtype: float
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this UpdatedProduct.

        The price of the product.  # noqa: E501

        :param price: The price of this UpdatedProduct.  # noqa: E501
        :type: float
        """
        if (
            self.local_vars_configuration.client_side_validation and price is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `price`, must not be `None`"
            )  # noqa: E501

        self._price = price

    @property
    def currency_code(self):
        """Gets the currency_code of this UpdatedProduct.  # noqa: E501

        The ISO 4217 currency code that represents the currency of the product price.  # noqa: E501

        :return: The currency_code of this UpdatedProduct.  # noqa: E501
        :rtype: str
        """
        return self._currency_code

    @currency_code.setter
    def currency_code(self, currency_code):
        """Sets the currency_code of this UpdatedProduct.

        The ISO 4217 currency code that represents the currency of the product price.  # noqa: E501

        :param currency_code: The currency_code of this UpdatedProduct.  # noqa: E501
        :type: str
        """

        self._currency_code = currency_code

    @property
    def id(self):
        """Gets the id of this UpdatedProduct.  # noqa: E501

        The ID of the product in the external accounting system.  # noqa: E501

        :return: The id of this UpdatedProduct.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UpdatedProduct.

        The ID of the product in the external accounting system.  # noqa: E501

        :param id: The id of this UpdatedProduct.  # noqa: E501
        :type: str
        """
        if (
            self.local_vars_configuration.client_side_validation and id is None
        ):  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def properties(self):
        """Gets the properties of this UpdatedProduct.  # noqa: E501

        A map of key-value product properties to be imported.  # noqa: E501

        :return: The properties of this UpdatedProduct.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this UpdatedProduct.

        A map of key-value product properties to be imported.  # noqa: E501

        :param properties: The properties of this UpdatedProduct.  # noqa: E501
        :type: dict(str, str)
        """
        if (
            self.local_vars_configuration.client_side_validation and properties is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `properties`, must not be `None`"
            )  # noqa: E501

        self._properties = properties

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
        if not isinstance(other, UpdatedProduct):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UpdatedProduct):
            return True

        return self.to_dict() != other.to_dict()

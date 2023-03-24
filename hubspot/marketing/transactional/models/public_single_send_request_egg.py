# coding: utf-8

"""
    Transactional Email

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v3
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from hubspot.marketing.transactional.configuration import Configuration


class PublicSingleSendRequestEgg(object):
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
        "email_id": "int",
        "message": "PublicSingleSendEmail",
        "contact_properties": "dict(str, str)",
        "custom_properties": "dict(str, object)",
    }

    attribute_map = {
        "email_id": "emailId",
        "message": "message",
        "contact_properties": "contactProperties",
        "custom_properties": "customProperties",
    }

    def __init__(
        self,
        email_id=None,
        message=None,
        contact_properties=None,
        custom_properties=None,
        local_vars_configuration=None,
    ):  # noqa: E501
        """PublicSingleSendRequestEgg - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._email_id = None
        self._message = None
        self._contact_properties = None
        self._custom_properties = None
        self.discriminator = None

        self.email_id = email_id
        self.message = message
        if contact_properties is not None:
            self.contact_properties = contact_properties
        if custom_properties is not None:
            self.custom_properties = custom_properties

    @property
    def email_id(self):
        """Gets the email_id of this PublicSingleSendRequestEgg.  # noqa: E501

        The content ID for the transactional email, which can be found in email tool UI.  # noqa: E501

        :return: The email_id of this PublicSingleSendRequestEgg.  # noqa: E501
        :rtype: int
        """
        return self._email_id

    @email_id.setter
    def email_id(self, email_id):
        """Sets the email_id of this PublicSingleSendRequestEgg.

        The content ID for the transactional email, which can be found in email tool UI.  # noqa: E501

        :param email_id: The email_id of this PublicSingleSendRequestEgg.  # noqa: E501
        :type: int
        """
        if (
            self.local_vars_configuration.client_side_validation and email_id is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `email_id`, must not be `None`"
            )  # noqa: E501

        self._email_id = email_id

    @property
    def message(self):
        """Gets the message of this PublicSingleSendRequestEgg.  # noqa: E501


        :return: The message of this PublicSingleSendRequestEgg.  # noqa: E501
        :rtype: PublicSingleSendEmail
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this PublicSingleSendRequestEgg.


        :param message: The message of this PublicSingleSendRequestEgg.  # noqa: E501
        :type: PublicSingleSendEmail
        """
        if (
            self.local_vars_configuration.client_side_validation and message is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `message`, must not be `None`"
            )  # noqa: E501

        self._message = message

    @property
    def contact_properties(self):
        """Gets the contact_properties of this PublicSingleSendRequestEgg.  # noqa: E501

        The contactProperties field is a map of contact property values. Each contact property value contains a name and value property. Each property will get set on the contact record and will be visible in the template under {{ contact.NAME }}. Use these properties when you want to set a contact property while you’re sending the email. For example, when sending a reciept you may want to set a last_paid_date property, as the sending of the receipt will have information about the last payment.  # noqa: E501

        :return: The contact_properties of this PublicSingleSendRequestEgg.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._contact_properties

    @contact_properties.setter
    def contact_properties(self, contact_properties):
        """Sets the contact_properties of this PublicSingleSendRequestEgg.

        The contactProperties field is a map of contact property values. Each contact property value contains a name and value property. Each property will get set on the contact record and will be visible in the template under {{ contact.NAME }}. Use these properties when you want to set a contact property while you’re sending the email. For example, when sending a reciept you may want to set a last_paid_date property, as the sending of the receipt will have information about the last payment.  # noqa: E501

        :param contact_properties: The contact_properties of this PublicSingleSendRequestEgg.  # noqa: E501
        :type: dict(str, str)
        """

        self._contact_properties = contact_properties

    @property
    def custom_properties(self):
        """Gets the custom_properties of this PublicSingleSendRequestEgg.  # noqa: E501

        The customProperties field is a map of property values. Each property value contains a name and value property. Each property will be visible in the template under {{ custom.NAME }}. Note: Custom properties do not currently support arrays. To provide a listing in an email, one workaround is to build an HTML list (either with tables or ul) and specify it as a custom property.  # noqa: E501

        :return: The custom_properties of this PublicSingleSendRequestEgg.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._custom_properties

    @custom_properties.setter
    def custom_properties(self, custom_properties):
        """Sets the custom_properties of this PublicSingleSendRequestEgg.

        The customProperties field is a map of property values. Each property value contains a name and value property. Each property will be visible in the template under {{ custom.NAME }}. Note: Custom properties do not currently support arrays. To provide a listing in an email, one workaround is to build an HTML list (either with tables or ul) and specify it as a custom property.  # noqa: E501

        :param custom_properties: The custom_properties of this PublicSingleSendRequestEgg.  # noqa: E501
        :type: dict(str, object)
        """

        self._custom_properties = custom_properties

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
        if not isinstance(other, PublicSingleSendRequestEgg):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PublicSingleSendRequestEgg):
            return True

        return self.to_dict() != other.to_dict()

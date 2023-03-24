# coding: utf-8

"""
    FormsExternalService

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v3
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from hubspot.marketing.forms.configuration import Configuration


class FormStyle(object):
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
        "font_family": "str",
        "background_width": "str",
        "label_text_color": "str",
        "label_text_size": "str",
        "help_text_color": "str",
        "help_text_size": "str",
        "legal_consent_text_color": "str",
        "legal_consent_text_size": "str",
        "submit_color": "str",
        "submit_alignment": "str",
        "submit_font_color": "str",
        "submit_size": "str",
    }

    attribute_map = {
        "font_family": "fontFamily",
        "background_width": "backgroundWidth",
        "label_text_color": "labelTextColor",
        "label_text_size": "labelTextSize",
        "help_text_color": "helpTextColor",
        "help_text_size": "helpTextSize",
        "legal_consent_text_color": "legalConsentTextColor",
        "legal_consent_text_size": "legalConsentTextSize",
        "submit_color": "submitColor",
        "submit_alignment": "submitAlignment",
        "submit_font_color": "submitFontColor",
        "submit_size": "submitSize",
    }

    def __init__(
        self,
        font_family=None,
        background_width=None,
        label_text_color=None,
        label_text_size=None,
        help_text_color=None,
        help_text_size=None,
        legal_consent_text_color=None,
        legal_consent_text_size=None,
        submit_color=None,
        submit_alignment=None,
        submit_font_color=None,
        submit_size=None,
        local_vars_configuration=None,
    ):  # noqa: E501
        """FormStyle - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._font_family = None
        self._background_width = None
        self._label_text_color = None
        self._label_text_size = None
        self._help_text_color = None
        self._help_text_size = None
        self._legal_consent_text_color = None
        self._legal_consent_text_size = None
        self._submit_color = None
        self._submit_alignment = None
        self._submit_font_color = None
        self._submit_size = None
        self.discriminator = None

        self.font_family = font_family
        self.background_width = background_width
        self.label_text_color = label_text_color
        self.label_text_size = label_text_size
        self.help_text_color = help_text_color
        self.help_text_size = help_text_size
        self.legal_consent_text_color = legal_consent_text_color
        self.legal_consent_text_size = legal_consent_text_size
        self.submit_color = submit_color
        self.submit_alignment = submit_alignment
        self.submit_font_color = submit_font_color
        self.submit_size = submit_size

    @property
    def font_family(self):
        """Gets the font_family of this FormStyle.  # noqa: E501


        :return: The font_family of this FormStyle.  # noqa: E501
        :rtype: str
        """
        return self._font_family

    @font_family.setter
    def font_family(self, font_family):
        """Sets the font_family of this FormStyle.


        :param font_family: The font_family of this FormStyle.  # noqa: E501
        :type: str
        """
        if (
            self.local_vars_configuration.client_side_validation and font_family is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `font_family`, must not be `None`"
            )  # noqa: E501

        self._font_family = font_family

    @property
    def background_width(self):
        """Gets the background_width of this FormStyle.  # noqa: E501


        :return: The background_width of this FormStyle.  # noqa: E501
        :rtype: str
        """
        return self._background_width

    @background_width.setter
    def background_width(self, background_width):
        """Sets the background_width of this FormStyle.


        :param background_width: The background_width of this FormStyle.  # noqa: E501
        :type: str
        """
        if (
            self.local_vars_configuration.client_side_validation
            and background_width is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `background_width`, must not be `None`"
            )  # noqa: E501

        self._background_width = background_width

    @property
    def label_text_color(self):
        """Gets the label_text_color of this FormStyle.  # noqa: E501


        :return: The label_text_color of this FormStyle.  # noqa: E501
        :rtype: str
        """
        return self._label_text_color

    @label_text_color.setter
    def label_text_color(self, label_text_color):
        """Sets the label_text_color of this FormStyle.


        :param label_text_color: The label_text_color of this FormStyle.  # noqa: E501
        :type: str
        """
        if (
            self.local_vars_configuration.client_side_validation
            and label_text_color is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `label_text_color`, must not be `None`"
            )  # noqa: E501

        self._label_text_color = label_text_color

    @property
    def label_text_size(self):
        """Gets the label_text_size of this FormStyle.  # noqa: E501


        :return: The label_text_size of this FormStyle.  # noqa: E501
        :rtype: str
        """
        return self._label_text_size

    @label_text_size.setter
    def label_text_size(self, label_text_size):
        """Sets the label_text_size of this FormStyle.


        :param label_text_size: The label_text_size of this FormStyle.  # noqa: E501
        :type: str
        """
        if (
            self.local_vars_configuration.client_side_validation
            and label_text_size is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `label_text_size`, must not be `None`"
            )  # noqa: E501

        self._label_text_size = label_text_size

    @property
    def help_text_color(self):
        """Gets the help_text_color of this FormStyle.  # noqa: E501


        :return: The help_text_color of this FormStyle.  # noqa: E501
        :rtype: str
        """
        return self._help_text_color

    @help_text_color.setter
    def help_text_color(self, help_text_color):
        """Sets the help_text_color of this FormStyle.


        :param help_text_color: The help_text_color of this FormStyle.  # noqa: E501
        :type: str
        """
        if (
            self.local_vars_configuration.client_side_validation
            and help_text_color is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `help_text_color`, must not be `None`"
            )  # noqa: E501

        self._help_text_color = help_text_color

    @property
    def help_text_size(self):
        """Gets the help_text_size of this FormStyle.  # noqa: E501


        :return: The help_text_size of this FormStyle.  # noqa: E501
        :rtype: str
        """
        return self._help_text_size

    @help_text_size.setter
    def help_text_size(self, help_text_size):
        """Sets the help_text_size of this FormStyle.


        :param help_text_size: The help_text_size of this FormStyle.  # noqa: E501
        :type: str
        """
        if (
            self.local_vars_configuration.client_side_validation
            and help_text_size is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `help_text_size`, must not be `None`"
            )  # noqa: E501

        self._help_text_size = help_text_size

    @property
    def legal_consent_text_color(self):
        """Gets the legal_consent_text_color of this FormStyle.  # noqa: E501


        :return: The legal_consent_text_color of this FormStyle.  # noqa: E501
        :rtype: str
        """
        return self._legal_consent_text_color

    @legal_consent_text_color.setter
    def legal_consent_text_color(self, legal_consent_text_color):
        """Sets the legal_consent_text_color of this FormStyle.


        :param legal_consent_text_color: The legal_consent_text_color of this FormStyle.  # noqa: E501
        :type: str
        """
        if (
            self.local_vars_configuration.client_side_validation
            and legal_consent_text_color is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `legal_consent_text_color`, must not be `None`"
            )  # noqa: E501

        self._legal_consent_text_color = legal_consent_text_color

    @property
    def legal_consent_text_size(self):
        """Gets the legal_consent_text_size of this FormStyle.  # noqa: E501


        :return: The legal_consent_text_size of this FormStyle.  # noqa: E501
        :rtype: str
        """
        return self._legal_consent_text_size

    @legal_consent_text_size.setter
    def legal_consent_text_size(self, legal_consent_text_size):
        """Sets the legal_consent_text_size of this FormStyle.


        :param legal_consent_text_size: The legal_consent_text_size of this FormStyle.  # noqa: E501
        :type: str
        """
        if (
            self.local_vars_configuration.client_side_validation
            and legal_consent_text_size is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `legal_consent_text_size`, must not be `None`"
            )  # noqa: E501

        self._legal_consent_text_size = legal_consent_text_size

    @property
    def submit_color(self):
        """Gets the submit_color of this FormStyle.  # noqa: E501


        :return: The submit_color of this FormStyle.  # noqa: E501
        :rtype: str
        """
        return self._submit_color

    @submit_color.setter
    def submit_color(self, submit_color):
        """Sets the submit_color of this FormStyle.


        :param submit_color: The submit_color of this FormStyle.  # noqa: E501
        :type: str
        """
        if (
            self.local_vars_configuration.client_side_validation
            and submit_color is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `submit_color`, must not be `None`"
            )  # noqa: E501

        self._submit_color = submit_color

    @property
    def submit_alignment(self):
        """Gets the submit_alignment of this FormStyle.  # noqa: E501


        :return: The submit_alignment of this FormStyle.  # noqa: E501
        :rtype: str
        """
        return self._submit_alignment

    @submit_alignment.setter
    def submit_alignment(self, submit_alignment):
        """Sets the submit_alignment of this FormStyle.


        :param submit_alignment: The submit_alignment of this FormStyle.  # noqa: E501
        :type: str
        """
        if (
            self.local_vars_configuration.client_side_validation
            and submit_alignment is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `submit_alignment`, must not be `None`"
            )  # noqa: E501
        allowed_values = ["left", "right", "center"]  # noqa: E501
        if (
            self.local_vars_configuration.client_side_validation
            and submit_alignment not in allowed_values
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `submit_alignment` ({0}), must be one of {1}".format(  # noqa: E501
                    submit_alignment, allowed_values
                )
            )

        self._submit_alignment = submit_alignment

    @property
    def submit_font_color(self):
        """Gets the submit_font_color of this FormStyle.  # noqa: E501


        :return: The submit_font_color of this FormStyle.  # noqa: E501
        :rtype: str
        """
        return self._submit_font_color

    @submit_font_color.setter
    def submit_font_color(self, submit_font_color):
        """Sets the submit_font_color of this FormStyle.


        :param submit_font_color: The submit_font_color of this FormStyle.  # noqa: E501
        :type: str
        """
        if (
            self.local_vars_configuration.client_side_validation
            and submit_font_color is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `submit_font_color`, must not be `None`"
            )  # noqa: E501

        self._submit_font_color = submit_font_color

    @property
    def submit_size(self):
        """Gets the submit_size of this FormStyle.  # noqa: E501


        :return: The submit_size of this FormStyle.  # noqa: E501
        :rtype: str
        """
        return self._submit_size

    @submit_size.setter
    def submit_size(self, submit_size):
        """Sets the submit_size of this FormStyle.


        :param submit_size: The submit_size of this FormStyle.  # noqa: E501
        :type: str
        """
        if (
            self.local_vars_configuration.client_side_validation and submit_size is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `submit_size`, must not be `None`"
            )  # noqa: E501

        self._submit_size = submit_size

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
        if not isinstance(other, FormStyle):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FormStyle):
            return True

        return self.to_dict() != other.to_dict()

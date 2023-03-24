# coding: utf-8

"""
    Blog Post endpoints

    Use these endpoints for interacting with Blog Posts, Blog Authors, and Blog Tags  # noqa: E501

    The version of the OpenAPI document: v3
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from hubspot.cms.blogs.blog_posts.configuration import Configuration


class Styles(object):
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
        "vertical_alignment": "str",
        "background_color": "RGBAColor",
        "background_image": "BackgroundImage",
        "background_gradient": "Gradient",
        "max_width_section_centering": "int",
        "force_full_width_section": "bool",
        "flexbox_positioning": "str",
    }

    attribute_map = {
        "vertical_alignment": "verticalAlignment",
        "background_color": "backgroundColor",
        "background_image": "backgroundImage",
        "background_gradient": "backgroundGradient",
        "max_width_section_centering": "maxWidthSectionCentering",
        "force_full_width_section": "forceFullWidthSection",
        "flexbox_positioning": "flexboxPositioning",
    }

    def __init__(
        self,
        vertical_alignment=None,
        background_color=None,
        background_image=None,
        background_gradient=None,
        max_width_section_centering=None,
        force_full_width_section=None,
        flexbox_positioning=None,
        local_vars_configuration=None,
    ):  # noqa: E501
        """Styles - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._vertical_alignment = None
        self._background_color = None
        self._background_image = None
        self._background_gradient = None
        self._max_width_section_centering = None
        self._force_full_width_section = None
        self._flexbox_positioning = None
        self.discriminator = None

        self.vertical_alignment = vertical_alignment
        self.background_color = background_color
        self.background_image = background_image
        self.background_gradient = background_gradient
        self.max_width_section_centering = max_width_section_centering
        self.force_full_width_section = force_full_width_section
        self.flexbox_positioning = flexbox_positioning

    @property
    def vertical_alignment(self):
        """Gets the vertical_alignment of this Styles.  # noqa: E501


        :return: The vertical_alignment of this Styles.  # noqa: E501
        :rtype: str
        """
        return self._vertical_alignment

    @vertical_alignment.setter
    def vertical_alignment(self, vertical_alignment):
        """Sets the vertical_alignment of this Styles.


        :param vertical_alignment: The vertical_alignment of this Styles.  # noqa: E501
        :type: str
        """
        if (
            self.local_vars_configuration.client_side_validation
            and vertical_alignment is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `vertical_alignment`, must not be `None`"
            )  # noqa: E501
        allowed_values = ["TOP", "MIDDLE", "BOTTOM"]  # noqa: E501
        if (
            self.local_vars_configuration.client_side_validation
            and vertical_alignment not in allowed_values
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `vertical_alignment` ({0}), must be one of {1}".format(  # noqa: E501
                    vertical_alignment, allowed_values
                )
            )

        self._vertical_alignment = vertical_alignment

    @property
    def background_color(self):
        """Gets the background_color of this Styles.  # noqa: E501


        :return: The background_color of this Styles.  # noqa: E501
        :rtype: RGBAColor
        """
        return self._background_color

    @background_color.setter
    def background_color(self, background_color):
        """Sets the background_color of this Styles.


        :param background_color: The background_color of this Styles.  # noqa: E501
        :type: RGBAColor
        """
        if (
            self.local_vars_configuration.client_side_validation
            and background_color is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `background_color`, must not be `None`"
            )  # noqa: E501

        self._background_color = background_color

    @property
    def background_image(self):
        """Gets the background_image of this Styles.  # noqa: E501


        :return: The background_image of this Styles.  # noqa: E501
        :rtype: BackgroundImage
        """
        return self._background_image

    @background_image.setter
    def background_image(self, background_image):
        """Sets the background_image of this Styles.


        :param background_image: The background_image of this Styles.  # noqa: E501
        :type: BackgroundImage
        """
        if (
            self.local_vars_configuration.client_side_validation
            and background_image is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `background_image`, must not be `None`"
            )  # noqa: E501

        self._background_image = background_image

    @property
    def background_gradient(self):
        """Gets the background_gradient of this Styles.  # noqa: E501


        :return: The background_gradient of this Styles.  # noqa: E501
        :rtype: Gradient
        """
        return self._background_gradient

    @background_gradient.setter
    def background_gradient(self, background_gradient):
        """Sets the background_gradient of this Styles.


        :param background_gradient: The background_gradient of this Styles.  # noqa: E501
        :type: Gradient
        """
        if (
            self.local_vars_configuration.client_side_validation
            and background_gradient is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `background_gradient`, must not be `None`"
            )  # noqa: E501

        self._background_gradient = background_gradient

    @property
    def max_width_section_centering(self):
        """Gets the max_width_section_centering of this Styles.  # noqa: E501


        :return: The max_width_section_centering of this Styles.  # noqa: E501
        :rtype: int
        """
        return self._max_width_section_centering

    @max_width_section_centering.setter
    def max_width_section_centering(self, max_width_section_centering):
        """Sets the max_width_section_centering of this Styles.


        :param max_width_section_centering: The max_width_section_centering of this Styles.  # noqa: E501
        :type: int
        """
        if (
            self.local_vars_configuration.client_side_validation
            and max_width_section_centering is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `max_width_section_centering`, must not be `None`"
            )  # noqa: E501

        self._max_width_section_centering = max_width_section_centering

    @property
    def force_full_width_section(self):
        """Gets the force_full_width_section of this Styles.  # noqa: E501


        :return: The force_full_width_section of this Styles.  # noqa: E501
        :rtype: bool
        """
        return self._force_full_width_section

    @force_full_width_section.setter
    def force_full_width_section(self, force_full_width_section):
        """Sets the force_full_width_section of this Styles.


        :param force_full_width_section: The force_full_width_section of this Styles.  # noqa: E501
        :type: bool
        """
        if (
            self.local_vars_configuration.client_side_validation
            and force_full_width_section is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `force_full_width_section`, must not be `None`"
            )  # noqa: E501

        self._force_full_width_section = force_full_width_section

    @property
    def flexbox_positioning(self):
        """Gets the flexbox_positioning of this Styles.  # noqa: E501


        :return: The flexbox_positioning of this Styles.  # noqa: E501
        :rtype: str
        """
        return self._flexbox_positioning

    @flexbox_positioning.setter
    def flexbox_positioning(self, flexbox_positioning):
        """Sets the flexbox_positioning of this Styles.


        :param flexbox_positioning: The flexbox_positioning of this Styles.  # noqa: E501
        :type: str
        """
        if (
            self.local_vars_configuration.client_side_validation
            and flexbox_positioning is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `flexbox_positioning`, must not be `None`"
            )  # noqa: E501
        allowed_values = [
            "TOP_LEFT",
            "TOP_CENTER",
            "TOP_RIGHT",
            "MIDDLE_LEFT",
            "MIDDLE_CENTER",
            "MIDDLE_RIGHT",
            "BOTTOM_LEFT",
            "BOTTOM_CENTER",
            "BOTTOM_RIGHT",
        ]  # noqa: E501
        if (
            self.local_vars_configuration.client_side_validation
            and flexbox_positioning not in allowed_values
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `flexbox_positioning` ({0}), must be one of {1}".format(  # noqa: E501
                    flexbox_positioning, allowed_values
                )
            )

        self._flexbox_positioning = flexbox_positioning

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
        if not isinstance(other, Styles):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Styles):
            return True

        return self.to_dict() != other.to_dict()

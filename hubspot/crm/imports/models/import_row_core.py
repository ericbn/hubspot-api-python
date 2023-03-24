# coding: utf-8

"""
    CRM Imports

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v3
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from hubspot.crm.imports.configuration import Configuration


class ImportRowCore(object):
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
        "line_number": "int",
        "row_data": "list[str]",
        "file_id": "int",
        "page_name": "str",
    }

    attribute_map = {
        "line_number": "lineNumber",
        "row_data": "rowData",
        "file_id": "fileId",
        "page_name": "pageName",
    }

    def __init__(
        self,
        line_number=None,
        row_data=None,
        file_id=None,
        page_name=None,
        local_vars_configuration=None,
    ):  # noqa: E501
        """ImportRowCore - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._line_number = None
        self._row_data = None
        self._file_id = None
        self._page_name = None
        self.discriminator = None

        self.line_number = line_number
        self.row_data = row_data
        self.file_id = file_id
        if page_name is not None:
            self.page_name = page_name

    @property
    def line_number(self):
        """Gets the line_number of this ImportRowCore.  # noqa: E501


        :return: The line_number of this ImportRowCore.  # noqa: E501
        :rtype: int
        """
        return self._line_number

    @line_number.setter
    def line_number(self, line_number):
        """Sets the line_number of this ImportRowCore.


        :param line_number: The line_number of this ImportRowCore.  # noqa: E501
        :type: int
        """
        if (
            self.local_vars_configuration.client_side_validation and line_number is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `line_number`, must not be `None`"
            )  # noqa: E501

        self._line_number = line_number

    @property
    def row_data(self):
        """Gets the row_data of this ImportRowCore.  # noqa: E501


        :return: The row_data of this ImportRowCore.  # noqa: E501
        :rtype: list[str]
        """
        return self._row_data

    @row_data.setter
    def row_data(self, row_data):
        """Sets the row_data of this ImportRowCore.


        :param row_data: The row_data of this ImportRowCore.  # noqa: E501
        :type: list[str]
        """
        if (
            self.local_vars_configuration.client_side_validation and row_data is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `row_data`, must not be `None`"
            )  # noqa: E501

        self._row_data = row_data

    @property
    def file_id(self):
        """Gets the file_id of this ImportRowCore.  # noqa: E501


        :return: The file_id of this ImportRowCore.  # noqa: E501
        :rtype: int
        """
        return self._file_id

    @file_id.setter
    def file_id(self, file_id):
        """Sets the file_id of this ImportRowCore.


        :param file_id: The file_id of this ImportRowCore.  # noqa: E501
        :type: int
        """
        if (
            self.local_vars_configuration.client_side_validation and file_id is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `file_id`, must not be `None`"
            )  # noqa: E501

        self._file_id = file_id

    @property
    def page_name(self):
        """Gets the page_name of this ImportRowCore.  # noqa: E501


        :return: The page_name of this ImportRowCore.  # noqa: E501
        :rtype: str
        """
        return self._page_name

    @page_name.setter
    def page_name(self, page_name):
        """Sets the page_name of this ImportRowCore.


        :param page_name: The page_name of this ImportRowCore.  # noqa: E501
        :type: str
        """

        self._page_name = page_name

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
        if not isinstance(other, ImportRowCore):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ImportRowCore):
            return True

        return self.to_dict() != other.to_dict()

# coding: utf-8

"""
    CMS Site Search

    Use these endpoints for searching content on your HubSpot hosted CMS website(s).  # noqa: E501

    The version of the OpenAPI document: v3
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from hubspot.cms.site_search.configuration import Configuration


class PublicSearchResults(object):
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
        'total': 'int',
        'offset': 'int',
        'limit': 'int',
        'results': 'list[ContentSearchResult]',
        'search_term': 'str',
        'page': 'int'
    }

    attribute_map = {
        'total': 'total',
        'offset': 'offset',
        'limit': 'limit',
        'results': 'results',
        'search_term': 'searchTerm',
        'page': 'page'
    }

    def __init__(self, total=None, offset=None, limit=None, results=None, search_term=None, page=None, local_vars_configuration=None):  # noqa: E501
        """PublicSearchResults - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._total = None
        self._offset = None
        self._limit = None
        self._results = None
        self._search_term = None
        self._page = None
        self.discriminator = None

        self.total = total
        self.offset = offset
        self.limit = limit
        self.results = results
        if search_term is not None:
            self.search_term = search_term
        self.page = page

    @property
    def total(self):
        """Gets the total of this PublicSearchResults.  # noqa: E501


        :return: The total of this PublicSearchResults.  # noqa: E501
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this PublicSearchResults.


        :param total: The total of this PublicSearchResults.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and total is None:  # noqa: E501
            raise ValueError("Invalid value for `total`, must not be `None`")  # noqa: E501

        self._total = total

    @property
    def offset(self):
        """Gets the offset of this PublicSearchResults.  # noqa: E501


        :return: The offset of this PublicSearchResults.  # noqa: E501
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this PublicSearchResults.


        :param offset: The offset of this PublicSearchResults.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and offset is None:  # noqa: E501
            raise ValueError("Invalid value for `offset`, must not be `None`")  # noqa: E501

        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this PublicSearchResults.  # noqa: E501


        :return: The limit of this PublicSearchResults.  # noqa: E501
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this PublicSearchResults.


        :param limit: The limit of this PublicSearchResults.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and limit is None:  # noqa: E501
            raise ValueError("Invalid value for `limit`, must not be `None`")  # noqa: E501

        self._limit = limit

    @property
    def results(self):
        """Gets the results of this PublicSearchResults.  # noqa: E501


        :return: The results of this PublicSearchResults.  # noqa: E501
        :rtype: list[ContentSearchResult]
        """
        return self._results

    @results.setter
    def results(self, results):
        """Sets the results of this PublicSearchResults.


        :param results: The results of this PublicSearchResults.  # noqa: E501
        :type: list[ContentSearchResult]
        """
        if self.local_vars_configuration.client_side_validation and results is None:  # noqa: E501
            raise ValueError("Invalid value for `results`, must not be `None`")  # noqa: E501

        self._results = results

    @property
    def search_term(self):
        """Gets the search_term of this PublicSearchResults.  # noqa: E501


        :return: The search_term of this PublicSearchResults.  # noqa: E501
        :rtype: str
        """
        return self._search_term

    @search_term.setter
    def search_term(self, search_term):
        """Sets the search_term of this PublicSearchResults.


        :param search_term: The search_term of this PublicSearchResults.  # noqa: E501
        :type: str
        """

        self._search_term = search_term

    @property
    def page(self):
        """Gets the page of this PublicSearchResults.  # noqa: E501


        :return: The page of this PublicSearchResults.  # noqa: E501
        :rtype: int
        """
        return self._page

    @page.setter
    def page(self, page):
        """Sets the page of this PublicSearchResults.


        :param page: The page of this PublicSearchResults.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and page is None:  # noqa: E501
            raise ValueError("Invalid value for `page`, must not be `None`")  # noqa: E501

        self._page = page

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
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
        if not isinstance(other, PublicSearchResults):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PublicSearchResults):
            return True

        return self.to_dict() != other.to_dict()

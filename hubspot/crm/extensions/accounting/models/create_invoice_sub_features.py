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


class CreateInvoiceSubFeatures(object):
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
        "create_customer": "bool",
        "taxes": "bool",
        "exchange_rates": "bool",
        "terms": "bool",
        "invoice_comments": "bool",
        "invoice_discounts": "bool",
    }

    attribute_map = {
        "create_customer": "createCustomer",
        "taxes": "taxes",
        "exchange_rates": "exchangeRates",
        "terms": "terms",
        "invoice_comments": "invoiceComments",
        "invoice_discounts": "invoiceDiscounts",
    }

    def __init__(
        self,
        create_customer=None,
        taxes=None,
        exchange_rates=None,
        terms=None,
        invoice_comments=None,
        invoice_discounts=None,
        local_vars_configuration=None,
    ):  # noqa: E501
        """CreateInvoiceSubFeatures - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._create_customer = None
        self._taxes = None
        self._exchange_rates = None
        self._terms = None
        self._invoice_comments = None
        self._invoice_discounts = None
        self.discriminator = None

        self.create_customer = create_customer
        self.taxes = taxes
        self.exchange_rates = exchange_rates
        self.terms = terms
        self.invoice_comments = invoice_comments
        self.invoice_discounts = invoice_discounts

    @property
    def create_customer(self):
        """Gets the create_customer of this CreateInvoiceSubFeatures.  # noqa: E501

        Indicates if a new customer can be created in the external accounting system.  # noqa: E501

        :return: The create_customer of this CreateInvoiceSubFeatures.  # noqa: E501
        :rtype: bool
        """
        return self._create_customer

    @create_customer.setter
    def create_customer(self, create_customer):
        """Sets the create_customer of this CreateInvoiceSubFeatures.

        Indicates if a new customer can be created in the external accounting system.  # noqa: E501

        :param create_customer: The create_customer of this CreateInvoiceSubFeatures.  # noqa: E501
        :type: bool
        """
        if (
            self.local_vars_configuration.client_side_validation
            and create_customer is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `create_customer`, must not be `None`"
            )  # noqa: E501

        self._create_customer = create_customer

    @property
    def taxes(self):
        """Gets the taxes of this CreateInvoiceSubFeatures.  # noqa: E501

        Indicates if taxes can be specified by the HubSpot user for line items.  # noqa: E501

        :return: The taxes of this CreateInvoiceSubFeatures.  # noqa: E501
        :rtype: bool
        """
        return self._taxes

    @taxes.setter
    def taxes(self, taxes):
        """Sets the taxes of this CreateInvoiceSubFeatures.

        Indicates if taxes can be specified by the HubSpot user for line items.  # noqa: E501

        :param taxes: The taxes of this CreateInvoiceSubFeatures.  # noqa: E501
        :type: bool
        """
        if (
            self.local_vars_configuration.client_side_validation and taxes is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `taxes`, must not be `None`"
            )  # noqa: E501

        self._taxes = taxes

    @property
    def exchange_rates(self):
        """Gets the exchange_rates of this CreateInvoiceSubFeatures.  # noqa: E501

        Indicates if the external accounting system supports fetching exchange rates when create an invoice in HubSpot for a customer billed in a different currency.  # noqa: E501

        :return: The exchange_rates of this CreateInvoiceSubFeatures.  # noqa: E501
        :rtype: bool
        """
        return self._exchange_rates

    @exchange_rates.setter
    def exchange_rates(self, exchange_rates):
        """Sets the exchange_rates of this CreateInvoiceSubFeatures.

        Indicates if the external accounting system supports fetching exchange rates when create an invoice in HubSpot for a customer billed in a different currency.  # noqa: E501

        :param exchange_rates: The exchange_rates of this CreateInvoiceSubFeatures.  # noqa: E501
        :type: bool
        """
        if (
            self.local_vars_configuration.client_side_validation
            and exchange_rates is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `exchange_rates`, must not be `None`"
            )  # noqa: E501

        self._exchange_rates = exchange_rates

    @property
    def terms(self):
        """Gets the terms of this CreateInvoiceSubFeatures.  # noqa: E501

        Indicates if the external accounting system supports fetching payment terms.  # noqa: E501

        :return: The terms of this CreateInvoiceSubFeatures.  # noqa: E501
        :rtype: bool
        """
        return self._terms

    @terms.setter
    def terms(self, terms):
        """Sets the terms of this CreateInvoiceSubFeatures.

        Indicates if the external accounting system supports fetching payment terms.  # noqa: E501

        :param terms: The terms of this CreateInvoiceSubFeatures.  # noqa: E501
        :type: bool
        """
        if (
            self.local_vars_configuration.client_side_validation and terms is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `terms`, must not be `None`"
            )  # noqa: E501

        self._terms = terms

    @property
    def invoice_comments(self):
        """Gets the invoice_comments of this CreateInvoiceSubFeatures.  # noqa: E501

        Indicates if a visible comment can be added to invoices.  # noqa: E501

        :return: The invoice_comments of this CreateInvoiceSubFeatures.  # noqa: E501
        :rtype: bool
        """
        return self._invoice_comments

    @invoice_comments.setter
    def invoice_comments(self, invoice_comments):
        """Sets the invoice_comments of this CreateInvoiceSubFeatures.

        Indicates if a visible comment can be added to invoices.  # noqa: E501

        :param invoice_comments: The invoice_comments of this CreateInvoiceSubFeatures.  # noqa: E501
        :type: bool
        """
        if (
            self.local_vars_configuration.client_side_validation
            and invoice_comments is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `invoice_comments`, must not be `None`"
            )  # noqa: E501

        self._invoice_comments = invoice_comments

    @property
    def invoice_discounts(self):
        """Gets the invoice_discounts of this CreateInvoiceSubFeatures.  # noqa: E501

        Indicates if invoice-level discounts can be added to invoices.  # noqa: E501

        :return: The invoice_discounts of this CreateInvoiceSubFeatures.  # noqa: E501
        :rtype: bool
        """
        return self._invoice_discounts

    @invoice_discounts.setter
    def invoice_discounts(self, invoice_discounts):
        """Sets the invoice_discounts of this CreateInvoiceSubFeatures.

        Indicates if invoice-level discounts can be added to invoices.  # noqa: E501

        :param invoice_discounts: The invoice_discounts of this CreateInvoiceSubFeatures.  # noqa: E501
        :type: bool
        """
        if (
            self.local_vars_configuration.client_side_validation
            and invoice_discounts is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `invoice_discounts`, must not be `None`"
            )  # noqa: E501

        self._invoice_discounts = invoice_discounts

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
        if not isinstance(other, CreateInvoiceSubFeatures):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateInvoiceSubFeatures):
            return True

        return self.to_dict() != other.to_dict()

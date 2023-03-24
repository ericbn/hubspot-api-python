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


class HubSpotFormConfiguration(object):
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
        "language": "str",
        "cloneable": "bool",
        "post_submit_action": "FormPostSubmitAction",
        "editable": "bool",
        "archivable": "bool",
        "recaptcha_enabled": "bool",
        "notify_contact_owner": "bool",
        "notify_recipients": "list[str]",
        "create_new_contact_for_new_email": "bool",
        "pre_populate_known_values": "bool",
        "allow_link_to_reset_known_values": "bool",
    }

    attribute_map = {
        "language": "language",
        "cloneable": "cloneable",
        "post_submit_action": "postSubmitAction",
        "editable": "editable",
        "archivable": "archivable",
        "recaptcha_enabled": "recaptchaEnabled",
        "notify_contact_owner": "notifyContactOwner",
        "notify_recipients": "notifyRecipients",
        "create_new_contact_for_new_email": "createNewContactForNewEmail",
        "pre_populate_known_values": "prePopulateKnownValues",
        "allow_link_to_reset_known_values": "allowLinkToResetKnownValues",
    }

    def __init__(
        self,
        language=None,
        cloneable=None,
        post_submit_action=None,
        editable=None,
        archivable=None,
        recaptcha_enabled=None,
        notify_contact_owner=None,
        notify_recipients=None,
        create_new_contact_for_new_email=None,
        pre_populate_known_values=None,
        allow_link_to_reset_known_values=None,
        local_vars_configuration=None,
    ):  # noqa: E501
        """HubSpotFormConfiguration - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._language = None
        self._cloneable = None
        self._post_submit_action = None
        self._editable = None
        self._archivable = None
        self._recaptcha_enabled = None
        self._notify_contact_owner = None
        self._notify_recipients = None
        self._create_new_contact_for_new_email = None
        self._pre_populate_known_values = None
        self._allow_link_to_reset_known_values = None
        self.discriminator = None

        self.language = language
        self.cloneable = cloneable
        self.post_submit_action = post_submit_action
        self.editable = editable
        self.archivable = archivable
        self.recaptcha_enabled = recaptcha_enabled
        self.notify_contact_owner = notify_contact_owner
        self.notify_recipients = notify_recipients
        self.create_new_contact_for_new_email = create_new_contact_for_new_email
        self.pre_populate_known_values = pre_populate_known_values
        self.allow_link_to_reset_known_values = allow_link_to_reset_known_values

    @property
    def language(self):
        """Gets the language of this HubSpotFormConfiguration.  # noqa: E501

        The language of the form.  # noqa: E501

        :return: The language of this HubSpotFormConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this HubSpotFormConfiguration.

        The language of the form.  # noqa: E501

        :param language: The language of this HubSpotFormConfiguration.  # noqa: E501
        :type: str
        """
        if (
            self.local_vars_configuration.client_side_validation and language is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `language`, must not be `None`"
            )  # noqa: E501
        allowed_values = [
            "af",
            "ar-eg",
            "bn",
            "bg",
            "ca-es",
            "cs",
            "da",
            "de",
            "el",
            "en",
            "es",
            "es-mx",
            "fi",
            "fr",
            "hr",
            "hu",
            "id",
            "it",
            "ja",
            "ko",
            "nl",
            "no-no",
            "pl",
            "pt",
            "pt-br",
            "ro",
            "ru",
            "sl",
            "sv",
            "th",
            "tr",
            "uk",
            "vi",
            "zh-cn",
            "zh-hk",
        ]  # noqa: E501
        if (
            self.local_vars_configuration.client_side_validation
            and language not in allowed_values
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `language` ({0}), must be one of {1}".format(  # noqa: E501
                    language, allowed_values
                )
            )

        self._language = language

    @property
    def cloneable(self):
        """Gets the cloneable of this HubSpotFormConfiguration.  # noqa: E501

        Whether the form can be cloned.  # noqa: E501

        :return: The cloneable of this HubSpotFormConfiguration.  # noqa: E501
        :rtype: bool
        """
        return self._cloneable

    @cloneable.setter
    def cloneable(self, cloneable):
        """Sets the cloneable of this HubSpotFormConfiguration.

        Whether the form can be cloned.  # noqa: E501

        :param cloneable: The cloneable of this HubSpotFormConfiguration.  # noqa: E501
        :type: bool
        """
        if (
            self.local_vars_configuration.client_side_validation and cloneable is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `cloneable`, must not be `None`"
            )  # noqa: E501

        self._cloneable = cloneable

    @property
    def post_submit_action(self):
        """Gets the post_submit_action of this HubSpotFormConfiguration.  # noqa: E501


        :return: The post_submit_action of this HubSpotFormConfiguration.  # noqa: E501
        :rtype: FormPostSubmitAction
        """
        return self._post_submit_action

    @post_submit_action.setter
    def post_submit_action(self, post_submit_action):
        """Sets the post_submit_action of this HubSpotFormConfiguration.


        :param post_submit_action: The post_submit_action of this HubSpotFormConfiguration.  # noqa: E501
        :type: FormPostSubmitAction
        """
        if (
            self.local_vars_configuration.client_side_validation
            and post_submit_action is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `post_submit_action`, must not be `None`"
            )  # noqa: E501

        self._post_submit_action = post_submit_action

    @property
    def editable(self):
        """Gets the editable of this HubSpotFormConfiguration.  # noqa: E501

        Whether the form can be edited.  # noqa: E501

        :return: The editable of this HubSpotFormConfiguration.  # noqa: E501
        :rtype: bool
        """
        return self._editable

    @editable.setter
    def editable(self, editable):
        """Sets the editable of this HubSpotFormConfiguration.

        Whether the form can be edited.  # noqa: E501

        :param editable: The editable of this HubSpotFormConfiguration.  # noqa: E501
        :type: bool
        """
        if (
            self.local_vars_configuration.client_side_validation and editable is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `editable`, must not be `None`"
            )  # noqa: E501

        self._editable = editable

    @property
    def archivable(self):
        """Gets the archivable of this HubSpotFormConfiguration.  # noqa: E501

        Whether the form can be archived.  # noqa: E501

        :return: The archivable of this HubSpotFormConfiguration.  # noqa: E501
        :rtype: bool
        """
        return self._archivable

    @archivable.setter
    def archivable(self, archivable):
        """Sets the archivable of this HubSpotFormConfiguration.

        Whether the form can be archived.  # noqa: E501

        :param archivable: The archivable of this HubSpotFormConfiguration.  # noqa: E501
        :type: bool
        """
        if (
            self.local_vars_configuration.client_side_validation and archivable is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `archivable`, must not be `None`"
            )  # noqa: E501

        self._archivable = archivable

    @property
    def recaptcha_enabled(self):
        """Gets the recaptcha_enabled of this HubSpotFormConfiguration.  # noqa: E501

        Whether CAPTCHA (spam prevention) is enabled.  # noqa: E501

        :return: The recaptcha_enabled of this HubSpotFormConfiguration.  # noqa: E501
        :rtype: bool
        """
        return self._recaptcha_enabled

    @recaptcha_enabled.setter
    def recaptcha_enabled(self, recaptcha_enabled):
        """Sets the recaptcha_enabled of this HubSpotFormConfiguration.

        Whether CAPTCHA (spam prevention) is enabled.  # noqa: E501

        :param recaptcha_enabled: The recaptcha_enabled of this HubSpotFormConfiguration.  # noqa: E501
        :type: bool
        """
        if (
            self.local_vars_configuration.client_side_validation
            and recaptcha_enabled is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `recaptcha_enabled`, must not be `None`"
            )  # noqa: E501

        self._recaptcha_enabled = recaptcha_enabled

    @property
    def notify_contact_owner(self):
        """Gets the notify_contact_owner of this HubSpotFormConfiguration.  # noqa: E501

        Whether to send a notification email to the contact owner when a submission is received.  # noqa: E501

        :return: The notify_contact_owner of this HubSpotFormConfiguration.  # noqa: E501
        :rtype: bool
        """
        return self._notify_contact_owner

    @notify_contact_owner.setter
    def notify_contact_owner(self, notify_contact_owner):
        """Sets the notify_contact_owner of this HubSpotFormConfiguration.

        Whether to send a notification email to the contact owner when a submission is received.  # noqa: E501

        :param notify_contact_owner: The notify_contact_owner of this HubSpotFormConfiguration.  # noqa: E501
        :type: bool
        """
        if (
            self.local_vars_configuration.client_side_validation
            and notify_contact_owner is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `notify_contact_owner`, must not be `None`"
            )  # noqa: E501

        self._notify_contact_owner = notify_contact_owner

    @property
    def notify_recipients(self):
        """Gets the notify_recipients of this HubSpotFormConfiguration.  # noqa: E501

        The list of user IDs to receive a notification email when a submission is received.  # noqa: E501

        :return: The notify_recipients of this HubSpotFormConfiguration.  # noqa: E501
        :rtype: list[str]
        """
        return self._notify_recipients

    @notify_recipients.setter
    def notify_recipients(self, notify_recipients):
        """Sets the notify_recipients of this HubSpotFormConfiguration.

        The list of user IDs to receive a notification email when a submission is received.  # noqa: E501

        :param notify_recipients: The notify_recipients of this HubSpotFormConfiguration.  # noqa: E501
        :type: list[str]
        """
        if (
            self.local_vars_configuration.client_side_validation
            and notify_recipients is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `notify_recipients`, must not be `None`"
            )  # noqa: E501

        self._notify_recipients = notify_recipients

    @property
    def create_new_contact_for_new_email(self):
        """Gets the create_new_contact_for_new_email of this HubSpotFormConfiguration.  # noqa: E501

        Whether to create a new contact when a form is submitted with an email address that doesn’t match any in your existing contacts records.  # noqa: E501

        :return: The create_new_contact_for_new_email of this HubSpotFormConfiguration.  # noqa: E501
        :rtype: bool
        """
        return self._create_new_contact_for_new_email

    @create_new_contact_for_new_email.setter
    def create_new_contact_for_new_email(self, create_new_contact_for_new_email):
        """Sets the create_new_contact_for_new_email of this HubSpotFormConfiguration.

        Whether to create a new contact when a form is submitted with an email address that doesn’t match any in your existing contacts records.  # noqa: E501

        :param create_new_contact_for_new_email: The create_new_contact_for_new_email of this HubSpotFormConfiguration.  # noqa: E501
        :type: bool
        """
        if (
            self.local_vars_configuration.client_side_validation
            and create_new_contact_for_new_email is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `create_new_contact_for_new_email`, must not be `None`"
            )  # noqa: E501

        self._create_new_contact_for_new_email = create_new_contact_for_new_email

    @property
    def pre_populate_known_values(self):
        """Gets the pre_populate_known_values of this HubSpotFormConfiguration.  # noqa: E501

        Whether contact fields should pre-populate with known information when a contact returns to your site.  # noqa: E501

        :return: The pre_populate_known_values of this HubSpotFormConfiguration.  # noqa: E501
        :rtype: bool
        """
        return self._pre_populate_known_values

    @pre_populate_known_values.setter
    def pre_populate_known_values(self, pre_populate_known_values):
        """Sets the pre_populate_known_values of this HubSpotFormConfiguration.

        Whether contact fields should pre-populate with known information when a contact returns to your site.  # noqa: E501

        :param pre_populate_known_values: The pre_populate_known_values of this HubSpotFormConfiguration.  # noqa: E501
        :type: bool
        """
        if (
            self.local_vars_configuration.client_side_validation
            and pre_populate_known_values is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `pre_populate_known_values`, must not be `None`"
            )  # noqa: E501

        self._pre_populate_known_values = pre_populate_known_values

    @property
    def allow_link_to_reset_known_values(self):
        """Gets the allow_link_to_reset_known_values of this HubSpotFormConfiguration.  # noqa: E501

        Whether to add a reset link to the form. This removes any pre-populated content on the form and creates a new contact on submission.  # noqa: E501

        :return: The allow_link_to_reset_known_values of this HubSpotFormConfiguration.  # noqa: E501
        :rtype: bool
        """
        return self._allow_link_to_reset_known_values

    @allow_link_to_reset_known_values.setter
    def allow_link_to_reset_known_values(self, allow_link_to_reset_known_values):
        """Sets the allow_link_to_reset_known_values of this HubSpotFormConfiguration.

        Whether to add a reset link to the form. This removes any pre-populated content on the form and creates a new contact on submission.  # noqa: E501

        :param allow_link_to_reset_known_values: The allow_link_to_reset_known_values of this HubSpotFormConfiguration.  # noqa: E501
        :type: bool
        """
        if (
            self.local_vars_configuration.client_side_validation
            and allow_link_to_reset_known_values is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `allow_link_to_reset_known_values`, must not be `None`"
            )  # noqa: E501

        self._allow_link_to_reset_known_values = allow_link_to_reset_known_values

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
        if not isinstance(other, HubSpotFormConfiguration):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, HubSpotFormConfiguration):
            return True

        return self.to_dict() != other.to_dict()

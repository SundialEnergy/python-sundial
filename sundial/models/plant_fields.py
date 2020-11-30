# coding: utf-8

"""
    sundial

    Sundial optimises renewable power generation  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class PlantFields(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'bool',
        'name': 'bool',
        'region': 'bool',
        'capacity': 'bool',
        'ramp_up_rate': 'bool',
        'ramp_down_rate': 'bool',
        'created_at': 'bool',
        'modified_at': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'region': 'region',
        'capacity': 'capacity',
        'ramp_up_rate': 'rampUpRate',
        'ramp_down_rate': 'rampDownRate',
        'created_at': 'createdAt',
        'modified_at': 'modifiedAt'
    }

    def __init__(self, id=None, name=None, region=None, capacity=None, ramp_up_rate=None, ramp_down_rate=None, created_at=None, modified_at=None):  # noqa: E501
        """PlantFields - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._region = None
        self._capacity = None
        self._ramp_up_rate = None
        self._ramp_down_rate = None
        self._created_at = None
        self._modified_at = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if region is not None:
            self.region = region
        if capacity is not None:
            self.capacity = capacity
        if ramp_up_rate is not None:
            self.ramp_up_rate = ramp_up_rate
        if ramp_down_rate is not None:
            self.ramp_down_rate = ramp_down_rate
        if created_at is not None:
            self.created_at = created_at
        if modified_at is not None:
            self.modified_at = modified_at

    @property
    def id(self):
        """Gets the id of this PlantFields.  # noqa: E501


        :return: The id of this PlantFields.  # noqa: E501
        :rtype: bool
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PlantFields.


        :param id: The id of this PlantFields.  # noqa: E501
        :type: bool
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this PlantFields.  # noqa: E501


        :return: The name of this PlantFields.  # noqa: E501
        :rtype: bool
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PlantFields.


        :param name: The name of this PlantFields.  # noqa: E501
        :type: bool
        """

        self._name = name

    @property
    def region(self):
        """Gets the region of this PlantFields.  # noqa: E501


        :return: The region of this PlantFields.  # noqa: E501
        :rtype: bool
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this PlantFields.


        :param region: The region of this PlantFields.  # noqa: E501
        :type: bool
        """

        self._region = region

    @property
    def capacity(self):
        """Gets the capacity of this PlantFields.  # noqa: E501


        :return: The capacity of this PlantFields.  # noqa: E501
        :rtype: bool
        """
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        """Sets the capacity of this PlantFields.


        :param capacity: The capacity of this PlantFields.  # noqa: E501
        :type: bool
        """

        self._capacity = capacity

    @property
    def ramp_up_rate(self):
        """Gets the ramp_up_rate of this PlantFields.  # noqa: E501


        :return: The ramp_up_rate of this PlantFields.  # noqa: E501
        :rtype: bool
        """
        return self._ramp_up_rate

    @ramp_up_rate.setter
    def ramp_up_rate(self, ramp_up_rate):
        """Sets the ramp_up_rate of this PlantFields.


        :param ramp_up_rate: The ramp_up_rate of this PlantFields.  # noqa: E501
        :type: bool
        """

        self._ramp_up_rate = ramp_up_rate

    @property
    def ramp_down_rate(self):
        """Gets the ramp_down_rate of this PlantFields.  # noqa: E501


        :return: The ramp_down_rate of this PlantFields.  # noqa: E501
        :rtype: bool
        """
        return self._ramp_down_rate

    @ramp_down_rate.setter
    def ramp_down_rate(self, ramp_down_rate):
        """Sets the ramp_down_rate of this PlantFields.


        :param ramp_down_rate: The ramp_down_rate of this PlantFields.  # noqa: E501
        :type: bool
        """

        self._ramp_down_rate = ramp_down_rate

    @property
    def created_at(self):
        """Gets the created_at of this PlantFields.  # noqa: E501


        :return: The created_at of this PlantFields.  # noqa: E501
        :rtype: bool
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this PlantFields.


        :param created_at: The created_at of this PlantFields.  # noqa: E501
        :type: bool
        """

        self._created_at = created_at

    @property
    def modified_at(self):
        """Gets the modified_at of this PlantFields.  # noqa: E501


        :return: The modified_at of this PlantFields.  # noqa: E501
        :rtype: bool
        """
        return self._modified_at

    @modified_at.setter
    def modified_at(self, modified_at):
        """Sets the modified_at of this PlantFields.


        :param modified_at: The modified_at of this PlantFields.  # noqa: E501
        :type: bool
        """

        self._modified_at = modified_at

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(PlantFields, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, PlantFields):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
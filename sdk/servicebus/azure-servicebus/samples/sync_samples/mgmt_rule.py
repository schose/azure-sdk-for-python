#!/usr/bin/env python

# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

"""
Example to show managing rule entities under a ServiceBus Subscription, including
    - Create a rule
    - Get rule properties and runtime information
    - Update a rule
    - Delete a rule
    - List rules under the given ServiceBus Subscription
"""

# pylint: disable=C0111

import os
from azure.servicebus.management import ServiceBusAdministrationClient

CONNECTION_STR = os.environ['SERVICE_BUS_CONNECTION_STR']
TOPIC_NAME = "sb_mgmt_demo_topic"
SUBSCRIPTION_NAME = "sb_mgmt_demo_subscription"
RULE_NAME = "sb_mgmt_demo_rule"


def create_rule(servicebus_mgmt_client):
    print("-- Create Rule")
    servicebus_mgmt_client.create_rule(TOPIC_NAME, SUBSCRIPTION_NAME, RULE_NAME)
    print("Rule {} is created.".format(RULE_NAME))
    print("")


def delete_rule(servicebus_mgmt_client):
    print("-- Delete Rule")
    servicebus_mgmt_client.delete_rule(TOPIC_NAME, SUBSCRIPTION_NAME, RULE_NAME)
    print("Rule {} is deleted.".format(RULE_NAME))
    print("")


def list_rules(servicebus_mgmt_client):
    print("-- List Rules")
    for rule_properties in servicebus_mgmt_client.list_rules(TOPIC_NAME, SUBSCRIPTION_NAME):
        print("Rule Name:", rule_properties.name)
    print("")


def get_and_update_rule(servicebus_mgmt_client):
    print("-- Get and Update Rule")
    rule_properties = servicebus_mgmt_client.get_rule(TOPIC_NAME, SUBSCRIPTION_NAME, RULE_NAME)
    print("Rule Name:", rule_properties.name)
    print("Please refer to RuleProperties for complete available properties.")
    print("")
    servicebus_mgmt_client.update_rule(TOPIC_NAME, SUBSCRIPTION_NAME, rule_properties)


with ServiceBusAdministrationClient.from_connection_string(CONNECTION_STR) as servicebus_mgmt_client:
    create_rule(servicebus_mgmt_client)
    list_rules(servicebus_mgmt_client)
    get_and_update_rule(servicebus_mgmt_client)
    delete_rule(servicebus_mgmt_client)

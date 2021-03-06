# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

try:
    from ._models_py3 import AccessKeys
    from ._models_py3 import AuthorizationRule
    from ._models_py3 import AuthorizationRuleListResult
    from ._models_py3 import CheckNameAvailability
    from ._models_py3 import CheckNameAvailabilityResult
    from ._models_py3 import ErrorResponse
    from ._models_py3 import HybridConnection
    from ._models_py3 import HybridConnectionListResult
    from ._models_py3 import Operation
    from ._models_py3 import OperationDisplay
    from ._models_py3 import OperationListResult
    from ._models_py3 import RegenerateAccessKeyParameters
    from ._models_py3 import RelayNamespace
    from ._models_py3 import RelayNamespaceListResult
    from ._models_py3 import RelayUpdateParameters
    from ._models_py3 import Resource
    from ._models_py3 import ResourceNamespacePatch
    from ._models_py3 import Sku
    from ._models_py3 import TrackedResource
    from ._models_py3 import WcfRelay
    from ._models_py3 import WcfRelaysListResult
except (SyntaxError, ImportError):
    from ._models import AccessKeys  # type: ignore
    from ._models import AuthorizationRule  # type: ignore
    from ._models import AuthorizationRuleListResult  # type: ignore
    from ._models import CheckNameAvailability  # type: ignore
    from ._models import CheckNameAvailabilityResult  # type: ignore
    from ._models import ErrorResponse  # type: ignore
    from ._models import HybridConnection  # type: ignore
    from ._models import HybridConnectionListResult  # type: ignore
    from ._models import Operation  # type: ignore
    from ._models import OperationDisplay  # type: ignore
    from ._models import OperationListResult  # type: ignore
    from ._models import RegenerateAccessKeyParameters  # type: ignore
    from ._models import RelayNamespace  # type: ignore
    from ._models import RelayNamespaceListResult  # type: ignore
    from ._models import RelayUpdateParameters  # type: ignore
    from ._models import Resource  # type: ignore
    from ._models import ResourceNamespacePatch  # type: ignore
    from ._models import Sku  # type: ignore
    from ._models import TrackedResource  # type: ignore
    from ._models import WcfRelay  # type: ignore
    from ._models import WcfRelaysListResult  # type: ignore

from ._relay_api_enums import (
    AccessRights,
    KeyType,
    ProvisioningStateEnum,
    Relaytype,
    UnavailableReason,
)

__all__ = [
    'AccessKeys',
    'AuthorizationRule',
    'AuthorizationRuleListResult',
    'CheckNameAvailability',
    'CheckNameAvailabilityResult',
    'ErrorResponse',
    'HybridConnection',
    'HybridConnectionListResult',
    'Operation',
    'OperationDisplay',
    'OperationListResult',
    'RegenerateAccessKeyParameters',
    'RelayNamespace',
    'RelayNamespaceListResult',
    'RelayUpdateParameters',
    'Resource',
    'ResourceNamespacePatch',
    'Sku',
    'TrackedResource',
    'WcfRelay',
    'WcfRelaysListResult',
    'AccessRights',
    'KeyType',
    'ProvisioningStateEnum',
    'Relaytype',
    'UnavailableReason',
]

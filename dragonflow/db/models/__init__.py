#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.
from dragonflow.db.models import legacy

# Remove those once we're done
NbObject = legacy.NbObject
NbDbObject = legacy.NbDbObject
UniqueKeyMixin = legacy.UniqueKeyMixin
LogicalSwitch = legacy.LogicalSwitch
Subnet = legacy.Subnet
LogicalPort = legacy.LogicalPort
LogicalRouter = legacy.LogicalRouter
LogicalRouterPort = legacy.LogicalRouterPort
SecurityGroup = legacy.SecurityGroup
SecurityGroupRule = legacy.SecurityGroupRule
Floatingip = legacy.Floatingip
QosPolicy = legacy.QosPolicy
Publisher = legacy.Publisher
AllowedAddressPairsActivePort = legacy.AllowedAddressPairsActivePort
Listener = legacy.Listener
OvsPort = legacy.OvsPort

UNIQUE_KEY = legacy.UNIQUE_KEY

table_class_mapping = legacy.table_class_mapping
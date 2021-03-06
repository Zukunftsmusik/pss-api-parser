####################################################
##   This file has been generated automatically   ##
####################################################

from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse


class {{entity.name}}Raw():
    XML_NODE_NAME: str = '{{entity.xml_node_name}}'

    def __init__(self, {{entity.name_snake_case}}_info: _EntityInfo) -> None:
{% for property in entity.properties %}
        self.__{{property.name_snake_case}}: {{property.type}} = _parse.pss_{{property.type}}({{entity.name_snake_case}}_info.get('{{property.name}}'))
{% endfor %}
{% for property in entity.properties %}

    @property
    def {{property.name_snake_case}}(self) -> {{property.type}}:
        return self.__{{property.name_snake_case}}
{% endfor %}
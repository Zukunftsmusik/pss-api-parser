####################################################
##   This file has been generated automatically   ##
####################################################

{% for service_import in service.imports %}
{{service_import}}
{% endfor %}

from ... import core as _core
{% for entity_type in service.entity_types %}
from ...entities import {{entity_type}} as _{{entity_type}}
{% endfor %}



# ---------- Constants ----------

{% for endpoint in service.endpoints %}
{{endpoint.base_path_name}}_BASE_PATH: str = '{{service.name}}/{{endpoint.name}}'
{% endfor %}


# ---------- Endpoints ----------

{% for endpoint in service.endpoints %}
async def {{endpoint.name_snake_case}}(production_server: str, {{endpoint.parameter_definitions}}, **params) -> _List[_{{endpoint.return_type}}]:
    params = {
{% for parameter in endpoint.parameters %}
        '{{parameter.name}}': {{parameter.name_snake_case}},
{% endfor %}
    }
    result = await _core.get_entities_from_path(_{{endpoint.return_type}}, '{{endpoint.xml_parent_tag_name}}', production_server, {{endpoint.base_path_name}}_BASE_PATH, **params)
    return result


{% endfor %}
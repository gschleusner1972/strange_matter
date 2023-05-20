from collections import namedtuple
import uuid



Component = namedtuple(
    "Component",
    [
        "component_version",
        "entity_guid",
        "component_guid",
        "name",
        "sequence_name",
        "sequence_id",
        "sequence_value",
        "context",
        "author",
        "source_data",
        "source_data_id",
        "component_type",
        "component_type_reference",
        "version",
        "status",
        "active",
        "author_software",
        "hash1",
        "payload_data_type",
        "date_created",
    ],
)

def create_component(
    component_version: str,
    entity_guid: str,
    component_guid: str,
    name: str,
    sequence_name: str,
    sequence_id: str,
    sequence_value: str,
    context: str,
    author: str,
    source_data: str,
    source_data_id,
    component_type: str,
    component_type_reference: str,
    version: str,
    status: str,
    active: bool,
    author_software: str,
    hash1: str,
    payload_data_type: str,
    date_created: str,
):
    return Component(
        component_version,
        entity_guid,
        component_guid,
        name,
        sequence_name,
        sequence_id,
        sequence_value,
        context,
        author,
        source_data,
        source_data_id,
        component_type,
        component_type_reference,
        version,
        status,
        active,
        author_software,
        hash1,
        payload_data_type,
        date_created,
    )

SubComponent = namedtuple(
    "SubComponent",
    [
        "component",
        "additional_field1",
        "additional_field2",
    ],
)

def create_sub_component(
    component: Component,
    additional_field1: str,
    additional_field2: str,
):
    return SubComponent(
        component,
        additional_field1,
        additional_field2,
    )

# Example usage:
component = create_component(
    "1.0",
    uuid.uuid4,
    uuid.uuid4,
    "name_value",
    "sequence_name_value",
    "sequence_id_value",
    "sequence_value_value",
    "context_value",
    "author_value",
    "source_data_value",
    "source_data_id_value",
    "component_type_value",
    "component_type_reference_value",
    "version_value",
    "status_value",
    True,
    "author_software_value",
    "hash1_value",
    "payload_data_type_value",
    "date_created_value",
)

sub_component = create_sub_component(component, "additional_value1", "additional_value2")

print(component)
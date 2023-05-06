class component:
	def __init__(self, component_version:str, entity_guid:str, component_guid:str, name:str, sequence_name:str, sequence_id:str, sequence_value:str, context:str, author:str, source_data:str, source_data_id, component_type:str, component_type_reference:str, version:str, status:str, active:bool, author_software:str, hash1:str, payload_data_type:str, date_created:str):
		self.component_version = component_version; self.entity_guid = entity_guid; self.component_guid = component_guid; self.name = name; self.sequence_name = sequence_name; self.sequence_id = sequence_id; self.sequence_value = sequence_value; self.context = context; self.author = author; self.source_data = source_data; self.source_data_id = source_data_id; self.component_type = component_type; self.component_type_reference = component_type_reference; self.version = version; self.status = status; self.active = active; self.author_software = author_software; self.hash1 = hash1; self.payload_data_type = payload_data_type; self.date_created = date_created

class relationship(component):
	def __init__(self, component_version:str, entity_guid:str, component_guid:str, name:str, sequence_name:str, sequence_id:str, sequence_value:str, context:str, author:str, source_data:str, source_data_id, component_type:str, component_type_reference:str, version:str, status:str, active:bool, author_software:str, hash1:str, payload_data_type:str, date_created:str, source_entities:list, source_components:list, source_component_type:str, destination_entities:list, destination_components:list, destination_component_type:str, relationship_name:str):
		super().__init__(component_version, entity_guid, component_guid, name, sequence_name, sequence_id, sequence_value, context, author, source_data, source_data_id, component_type, component_type_reference, version, status, active, author_software, hash1, payload_data_type, date_created)
		self.source_entities = source_entities; self.source_components = source_components; self.source_component_type = source_component_type; self.destination_entities = destination_entities; self.destination_components = destination_components; self.destination_component_type = destination_component_type; self.relationship_name = relationship_name

class location_transform(component):
	def __init__(self, component_version:str, entity_guid:str, component_guid:str, name:str, sequence_name:str, sequence_id:str, sequence_value:str, context:str, author:str, source_data:str, source_data_id, component_type:str, component_type_reference:str, version:str, status:str, active:bool, author_software:str, hash1:str, payload_data_type:str, date_created:str, x, y, z):
		super().__init__(component_version, entity_guid, component_guid, name, sequence_name, sequence_id, sequence_value, context, author, source_data, source_data_id, component_type, component_type_reference, version, status, active, author_software, hash1, payload_data_type, date_created)
		self.x = x; self.y = y; self.z = z

class person_details(component):
	def __init__(self, component_version:str, entity_guid:str, component_guid:str, name:str, sequence_name:str, sequence_id:str, sequence_value:str, context:str, author:str, source_data:str, source_data_id, component_type:str, component_type_reference:str, version:str, status:str, active:bool, author_software:str, hash1:str, payload_data_type:str, date_created:str, first:str, last:str, email:str):
		super().__init__(component_version, entity_guid, component_guid, name, sequence_name, sequence_id, sequence_value, context, author, source_data, source_data_id, component_type, component_type_reference, version, status, active, author_software, hash1, payload_data_type, date_created)
		self.first = first; self.last = last; self.email = email

class project_details(component):
	def __init__(self, component_version:str, entity_guid:str, component_guid:str, name:str, sequence_name:str, sequence_id:str, sequence_value:str, context:str, author:str, source_data:str, source_data_id, component_type:str, component_type_reference:str, version:str, status:str, active:bool, author_software:str, hash1:str, payload_data_type:str, date_created:str, project_name:str, number:str, alias:str):
		super().__init__(component_version, entity_guid, component_guid, name, sequence_name, sequence_id, sequence_value, context, author, source_data, source_data_id, component_type, component_type_reference, version, status, active, author_software, hash1, payload_data_type, date_created)
		self.project_name = project_name; self.number = number; self.alias = alias

class project_group(component):
	def __init__(self, component_version:str, entity_guid:str, component_guid:str, name:str, sequence_name:str, sequence_id:str, sequence_value:str, context:str, author:str, source_data:str, source_data_id, component_type:str, component_type_reference:str, version:str, status:str, active:bool, author_software:str, hash1:str, payload_data_type:str, date_created:str, project_group_name:str, group_type:str):
		super().__init__(component_version, entity_guid, component_guid, name, sequence_name, sequence_id, sequence_value, context, author, source_data, source_data_id, component_type, component_type_reference, version, status, active, author_software, hash1, payload_data_type, date_created)
		self.project_group_name = project_group_name; self.group_type = group_type

class service_group(component):
	def __init__(self, component_version:str, entity_guid:str, component_guid:str, name:str, sequence_name:str, sequence_id:str, sequence_value:str, context:str, author:str, source_data:str, source_data_id, component_type:str, component_type_reference:str, version:str, status:str, active:bool, author_software:str, hash1:str, payload_data_type:str, date_created:str, service_group_name:str, service_name:str, service_group_function:str):
		super().__init__(component_version, entity_guid, component_guid, name, sequence_name, sequence_id, sequence_value, context, author, source_data, source_data_id, component_type, component_type_reference, version, status, active, author_software, hash1, payload_data_type, date_created)
		self.service_group_name = service_group_name; self.service_name = service_name; self.service_group_function = service_group_function

class geometry(component):
	def __init__(self, component_version:str, entity_guid:str, component_guid:str, name:str, sequence_name:str, sequence_id:str, sequence_value:str, context:str, author:str, source_data:str, source_data_id, component_type:str, component_type_reference:str, version:str, status:str, active:bool, author_software:str, hash1:str, payload_data_type:str, date_created:str, _geometry:str):
		super().__init__(component_version, entity_guid, component_guid, name, sequence_name, sequence_id, sequence_value, context, author, source_data, source_data_id, component_type, component_type_reference, version, status, active, author_software, hash1, payload_data_type, date_created)
		self._geometry = _geometry

class classfication(component):
	def __init__(self, component_version:str, entity_guid:str, component_guid:str, name:str, sequence_name:str, sequence_id:str, sequence_value:str, context:str, author:str, source_data:str, source_data_id, component_type:str, component_type_reference:str, version:str, status:str, active:bool, author_software:str, hash1:str, payload_data_type:str, date_created:str, classification_name:str):
		super().__init__(component_version, entity_guid, component_guid, name, sequence_name, sequence_id, sequence_value, context, author, source_data, source_data_id, component_type, component_type_reference, version, status, active, author_software, hash1, payload_data_type, date_created)
		self.classification_name = classification_name

class ifc_pset_all(component):
	def __init__(self, component_version:str, entity_guid:str, component_guid:str, name:str, sequence_name:str, sequence_id:str, sequence_value:str, context:str, author:str, source_data:str, source_data_id, component_type:str, component_type_reference:str, version:str, status:str, active:bool, author_software:str, hash1:str, payload_data_type:str, date_created:str, ):
		super().__init__(component_version, entity_guid, component_guid, name, sequence_name, sequence_id, sequence_value, context, author, source_data, source_data_id, component_type, component_type_reference, version, status, active, author_software, hash1, payload_data_type, date_created)
		


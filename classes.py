class component:
	def __init__(self, component_version:str, entity_guid:str, component_guid:str, name:str, context:str, author:str, source_data:str, source_data_id, component_type:str, component_type_reference:str, version:str, status:str, active:bool, authur_software:str, hash1:str, payload_data_type:str, date_created:str, option:str):
		self.component_version = component_version; self.entity_guid = entity_guid; self.component_guid = component_guid; self.name = name; self.context = context; self.author = author; self.source_data = source_data; self.source_data_id = source_data_id; self.component_type = component_type; self.component_type_reference = component_type_reference; self.version = version; self.status = status; self.active = active; self.authur_software = authur_software; self.hash1 = hash1; self.payload_data_type = payload_data_type; self.date_created = date_created; self.option = option

class relationship(component):
	def __init__(self, component_version:str, entity_guid:str, component_guid:str, name:str, context:str, author:str, source_data:str, source_data_id, component_type:str, component_type_reference:str, version:str, status:str, active:bool, authur_software:str, hash1:str, payload_data_type:str, date_created:str, option:str, source_entities:list, source_components:list, source_component_type:str, destination_entities:list, destination_components:list, destination_component_type:str, relationship_name:str):
		super().__init__(component_version, entity_guid, component_guid, name, context, author, source_data, source_data_id, component_type, component_type_reference, version, status, active, authur_software, hash1, payload_data_type, date_created, option)
		self.source_entities = source_entities; self.source_components = source_components; self.source_component_type = source_component_type; self.destination_entities = destination_entities; self.destination_components = destination_components; self.destination_component_type = destination_component_type; self.relationship_name = relationship_name

class location_transform(component):
	def __init__(self, component_version:str, entity_guid:str, component_guid:str, name:str, context:str, author:str, source_data:str, source_data_id, component_type:str, component_type_reference:str, version:str, status:str, active:bool, authur_software:str, hash1:str, payload_data_type:str, date_created:str, option:str, x, y, z):
		super().__init__(component_version, entity_guid, component_guid, name, context, author, source_data, source_data_id, component_type, component_type_reference, version, status, active, authur_software, hash1, payload_data_type, date_created, option)
		self.x = x; self.y = y; self.z = z

class person_details(component):
	def __init__(self, component_version:str, entity_guid:str, component_guid:str, name:str, context:str, author:str, source_data:str, source_data_id, component_type:str, component_type_reference:str, version:str, status:str, active:bool, authur_software:str, hash1:str, payload_data_type:str, date_created:str, option:str, first:str, last:str, email:str):
		super().__init__(component_version, entity_guid, component_guid, name, context, author, source_data, source_data_id, component_type, component_type_reference, version, status, active, authur_software, hash1, payload_data_type, date_created, option)
		self.first = first; self.last = last; self.email = email

class project_details(component):
	def __init__(self, component_version:str, entity_guid:str, component_guid:str, name:str, context:str, author:str, source_data:str, source_data_id, component_type:str, component_type_reference:str, version:str, status:str, active:bool, authur_software:str, hash1:str, payload_data_type:str, date_created:str, option:str, name:str, number:str, alias:str):
		super().__init__(component_version, entity_guid, component_guid, name, context, author, source_data, source_data_id, component_type, component_type_reference, version, status, active, authur_software, hash1, payload_data_type, date_created, option)
		self.name = name; self.number = number; self.alias = alias

class project_group(component):
	def __init__(self, component_version:str, entity_guid:str, component_guid:str, name:str, context:str, author:str, source_data:str, source_data_id, component_type:str, component_type_reference:str, version:str, status:str, active:bool, authur_software:str, hash1:str, payload_data_type:str, date_created:str, option:str, name:str, group_type:str):
		super().__init__(component_version, entity_guid, component_guid, name, context, author, source_data, source_data_id, component_type, component_type_reference, version, status, active, authur_software, hash1, payload_data_type, date_created, option)
		self.name = name; self.group_type = group_type

class service_group(component):
	def __init__(self, component_version:str, entity_guid:str, component_guid:str, name:str, context:str, author:str, source_data:str, source_data_id, component_type:str, component_type_reference:str, version:str, status:str, active:bool, authur_software:str, hash1:str, payload_data_type:str, date_created:str, option:str, name:str, service_name:str, service_group_function:str):
		super().__init__(component_version, entity_guid, component_guid, name, context, author, source_data, source_data_id, component_type, component_type_reference, version, status, active, authur_software, hash1, payload_data_type, date_created, option)
		self.name = name; self.service_name = service_name; self.service_group_function = service_group_function

class geometry(component):
	def __init__(self, component_version:str, entity_guid:str, component_guid:str, name:str, context:str, author:str, source_data:str, source_data_id, component_type:str, component_type_reference:str, version:str, status:str, active:bool, authur_software:str, hash1:str, payload_data_type:str, date_created:str, option:str, _geometry;str):
		super().__init__(component_version, entity_guid, component_guid, name, context, author, source_data, source_data_id, component_type, component_type_reference, version, status, active, authur_software, hash1, payload_data_type, date_created, option)
		self._geometry;str = _geometry;str

class classfication(component):
	def __init__(self, component_version:str, entity_guid:str, component_guid:str, name:str, context:str, author:str, source_data:str, source_data_id, component_type:str, component_type_reference:str, version:str, status:str, active:bool, authur_software:str, hash1:str, payload_data_type:str, date_created:str, option:str, name:str):
		super().__init__(component_version, entity_guid, component_guid, name, context, author, source_data, source_data_id, component_type, component_type_reference, version, status, active, authur_software, hash1, payload_data_type, date_created, option)
		self.name = name

class ifc_pset_all(component):
	def __init__(self, component_version:str, entity_guid:str, component_guid:str, name:str, context:str, author:str, source_data:str, source_data_id, component_type:str, component_type_reference:str, version:str, status:str, active:bool, authur_software:str, hash1:str, payload_data_type:str, date_created:str, option:str, ):
		super().__init__(component_version, entity_guid, component_guid, name, context, author, source_data, source_data_id, component_type, component_type_reference, version, status, active, authur_software, hash1, payload_data_type, date_created, option)
		

class space_details(component):
	def __init__(self, component_version:str, entity_guid:str, component_guid:str, name:str, context:str, author:str, source_data:str, source_data_id, component_type:str, component_type_reference:str, version:str, status:str, active:bool, authur_software:str, hash1:str, payload_data_type:str, date_created:str, option:str, name:str, space_type:str, space_type_id:str):
		super().__init__(component_version, entity_guid, component_guid, name, context, author, source_data, source_data_id, component_type, component_type_reference, version, status, active, authur_software, hash1, payload_data_type, date_created, option)
		self.name = name; self.space_type = space_type; self.space_type_id = space_type_id

class space_measure(component):
	def __init__(self, component_version:str, entity_guid:str, component_guid:str, name:str, context:str, author:str, source_data:str, source_data_id, component_type:str, component_type_reference:str, version:str, status:str, active:bool, authur_software:str, hash1:str, payload_data_type:str, date_created:str, option:str, area:float, count:int):
		super().__init__(component_version, entity_guid, component_guid, name, context, author, source_data, source_data_id, component_type, component_type_reference, version, status, active, authur_software, hash1, payload_data_type, date_created, option)
		self.area = area; self.count = count


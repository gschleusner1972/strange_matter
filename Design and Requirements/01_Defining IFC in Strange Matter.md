# Defining Component Defintions



## Strange Matter

## Entity

In Strange Matter, an Entity is just a UUID7.   Because its is just an ID, it can be understood that there is no Enitity Object, as it's just an identifier for the shared concept being identified. The way an Entity comes into existence is that you make a Component that references the Entity UUID.   There could be reasons in certain storage technologies to create an Entity but from a data perspective; it is not a real “thing”.

## Everything is a Component

Given that Components are used to instantiate data it makes sense to look at Components as the root objects to store data of any kind.  This has yet to be finalized in some of the higher-level concepts of Collection and Scene, but it certainly holds, for instance, data and the relationships. 

## Component

Components are the key to this whols system working.  They hold three key bits of data.  The reference to the Entity th

## Getting Started

The first thing you must do when going down this path is begin with explicit definitions for data. This technique takes data that might be defined in one location but now can be define in many places.  IFC has distributed definitions already so its not to dissimilar.    The following is the JSON-LD representation of a Strange Matter  Header.   Because it's necessary for each component to describe itself there is a fair amount of boiler plate.  When looking at storage this is why the columnar formats are interesting as they can compress data like this very easily. 

# Defining a Component

## Component Header Definition

The definition is broken into several parts. 

### Context 

This the where JSON-LD makes a lot of sense it allows all the difference data sources to be called out. 

```json
    "@context": {
        "strange_matter_component_header_definition_schema_version":"0.1",
        "strange_matter_version_date": "20230827",
        "xsd": "http://www.w3.org/2001/XMLSchema#",
        "strange_matter_definition": "http://example.org/strangematter/v.01/vocab"
    },
```

### Component Defintion

This is a similar concept to classification references in IFC2x3/4 but more robust where this section describes its definition a source.  This could be used to describe specific values but in most cases the component definition is describing the payload. 

```json
 {
            "@type": "ComponentDefinition",
            "component_type": {
                "@value": "<Named Definition for the component>",
                "@type": "xsd:string"
            },
            "component_type_reference": {
                "@value": "<URI to its definition>",
                "@type": "xsd:anyURI"
            },
            "component_type_guid": {
                "@value": "<UUID7 of the Component>",
                "@type": "xsd:string"
            },
            "component_type_version_guid": {
                "@value": "<UUID7 of the Component Version>",
                "@type": "xsd:string"
            },
            "component_version": {
                "@value": "<Semantic Version of the Component Definition>",
                "@type": "xsd:string"
            },
            "classification_reference": {
                "@value": "URI for the Classification Reference.",
                "@type": "xsd:anyURI"
            }
```

### Component Instance Data Source

Where did this data come from, what are the identifiers of the data in the native application etc. 

```json
        {
            "@type": "ComponentInstanceDataSource",
            "author": {
                "@value": ["<Authors name, person or company etc>"],
                "@type": "xsd:string"
            },
            "context": {
                "@value": "<Domain/ Source that the instance data originated from>",
                "@type": "xsd:string"
            },
            "source_data": {
                "@value": "<URL or URI for definition data>",
                "@type": "xsd:anyURI"
            },
            "source_data_file_date": {
                "@value": "<File or file like container date of creation>",
                "@type": "xsd:date"
            },
            "source_data_file_id": {
                "@value": "<File or file like container id>",
                "@type": "xsd:string"
            },
            "source_data_file_version_id": {
                "@value": "<File or file like container version id>",
                "@type": "xsd:string"
            },
            "source_data_item_id": {
                "@value": "<ID from the source application>",
                "@type": "xsd:string"
            },
            "source_data_item_version_id": {
                "@value": "<ID from the source application>",
                "@type": "xsd:string"
            },
            "source_data_other": {
                "@value": "<Other values from the source that are key to identifying the data>",
                "@type": "xsd:string"
            }
```

### Component Instance Header

All the descriptive detail on the Component itself.  Its IDs, Classification. Version, Status Etc. 

```json
        {
            "@type": "ComponentInstanceHeader",
            "entity_guid": {
                "@value": "<UUID7 value to represent the Entity>",
                "@type": "xsd:string"
            },
            "component_guid": {
                "@value": "<UUID7 Value for the Component>",
                "@type": "xsd:string"
            },
            "date_created": {
                "@value": "<Creation_Date_Time of the Payload>",
                "@type": "xsd:dateTime"
            },
            "name": {
                "@value": "<User Name for the item>",
                "@type": "xsd:string"
            },
            "classification_value": {
                "@value": "Classification Value for the item",
                "@type": "xsd:string"
            },
            "sequence_name": {
                "@value": "<If the component is part of a sequence...this names that sequence>",
                "@type": "xsd:string"
            },
            "sequence_id": {
                "@value": "<UUID7 for the sequence>",
                "@type": "xsd:string"
            },
            "sequence_value": {
                "@value": "<Ordered Number for the sequence>",
                "@type": "xsd:integer"
            },
            "option": {
                "@value": "<Specific Option of the data>",
                "@type": "xsd:string"
            },
            "phase": {
                "@value": "<Specific User Data Phase>",
                "@type": "xsd:string"
            },
            "version": {
                "@value": "<Human Readable Semantic Version>",
                "@type": "xsd:string"
            },
            "version_id": {
                "@value": "<UUID7 Version GUID>",
                "@type": "xsd:string"
            },
            "status": {
                "@value": "<WIP,Active,Other>",
                "@type": "xsd:string"
            },
            "active": {
                "@value": "<Active Status Yes/No>",
                "@type": "xsd:string"
            }
```

### Component Instance Payload Details and Component Instance Payload

What is the payload, and the specific of the payload. 

```json
        {
            "@type": "ComponentInstancePayloadDetails",
            "authoring_software": {
                "@value": "<Name of the Authoring Software>",
                "@type": "xsd:string"
            },
            "payload_hash": {
                "@value": "<Payload specific Hash of the payload data>",
                "@type": "xsd:string"
            },
            "hash_definition": {
                "@value": "<Link or description of hash>",
                "@type": "xsd:anyURI"
            },
            "payload_data_type": {
                "@value": "<encoding of the payload>",
                "@type": "xsd:string"
            },
            "payload_data_type_definition": {
                "@value": "<encoding of the payload>",
                "@type": "xsd:anyURI"
            }
        },
        {
            "@type": "ComponentInstancePayload",
            "payload_encoding": {
                "@value": "<Encoding of the payload>",
                "@type": "xsd:string"
            },
            "payload_encryption": {
                "@value": "?",
                "@type": "xsd:string"
            },
            "payload_data": {
                "@value": "<Local path or URL/URI>",
                "@type": "xsd:anyURI"
            }
```

### Component Instance Relationship 

If the component is a relationship component and not a payload component this provides the details. 

```json
        {
            "@type": "ComponentInstanceRelationship",
            "source_entities": {
                "@value": "2XO9sNxaf0tBWBWE4fj28X",
                "@type": "xsd:string"
            },
            "source_components": {
                "@value": "12c5310a-fca8-434f-b36f-494754b157a4",
                "@type": "xsd:string"
            },
            "source_component_type": {
                "@value": "BuildingStory",
                "@type": "xsd:string"
            },
            "destination_entities": {
                "@value": [
                    "2XO9sNxaf0tBWBWF8fj06l", 
                    "2XO9sNxaf0tBWBWF8fj01x", 
                    "2XO9sNxaf0tBWBWF8fj3bd", 
                    // more items ...
                    "2XO9sNxaf0tBWBWE4fj2gH"
                ],
                "@type": "xsd:string"
            },
            "destination_components": {
                "@value": [
                    "1cb6d448-9b57-48d1-8daf-b03e1c3fea86",
                    "32aedccb-4a4b-48fd-9181-0635d6cb281d",
                    // more items ...
                    "0bf7b19a-a6a7-448f-be4f-06d29a5d16c0"
                ],
                "@type": "xsd:string"
            },
            "destination_component_type": {
                "@value": "",
                "@type": "xsd:string"
            }
        }
```

## Description a Component Payload

Next we describe a payload.  

### Strange Matter ID Component

Currently Strange Matter itself only describes 1 component.   That is the ID component.  Its how you make a thing exist.

```json
{
    "@context": {
      "strange_matter_component_payload_definition_version":"0.1",
      "strange_matter_version_date": "20230827",
      "xsd": "http://www.w3.org/2001/XMLSchema#",
      "ID_Component": "http://example.org/vocab#ID_Component",
      "name": {
        "@id": "http://schema.org/name",
        "@type": "xsd:string"
      },
      "usernumber": {
        "@id": "http://example.org/vocab#usernumber",
        "@type": "xsd:string"
      },
      "classification": {
        "@id": "http://example.org/vocab#classification",
        "@type": "xsd:string"
      },
      "description": {
        "@id": "http://schema.org/description",
        "@type": "xsd:string"
      },
      "language": {
        "@id": "http://schema.org/language",
        "@type": "xsd:language"
      }
    }
  }
  
```

## My Fire Rating Component

*This is where the Multi-Source, Assembly Model becomes clear.* Note how this component includes both BSI, and Other Definitions.  

```json
{
  "@context": {
    "strange_matter_component_payload_definition_version":"0.1",
    "strange_matter_version_date": "20230827",  
    "xsd": "http://www.w3.org/2001/XMLSchema#",
      "my_fire_rating_for_walls_slabs": "http://hok.com/vocab#my_fire_rating_for_walls_slabs",
      "Description": "Custom Component for fire rating on US Based Projects for HOK",
      "FireRating": {
          "@id": "https://identifier.buildingsmart.org/uri/buildingsmart/ifc/4.3/prop/FireRating",
          "@type": "xsd:string",
          "@uuid": "a0b1c2d3-e4f5-6789-abcd-0123456789a8",
          "@classification_restriction": ["ifcwall", "wall", "ifcslab", "slab"],
          "@enum" :["1HR, 2HR, 3HR"],
          "@localization":"Hourly Fire Rating"
      },
      "SmokeRating": {
        "@id": "http://hok.com/vocab#SmokeRating",
        "@type": "xsd:string",
        "@uuid": "a0b1c2d3-e4f5-6789-abcd-0123456789at",
        "@classification_restriction": ["ifcwall.partition", "wall.partition"],
        "@enum" :["1HR, 2HR, 3HR"],
        "@localization":"Hourly Smoke Rating"
      },
      "FireSmokeRating": {
        "@id": "http://icc.com/vocab#FireSmokeRating",
        "@type": "xsd:string",
        "@uuid": "a0b1c2d3-e4f5-6789-abcd-01234567891b",
        "@classification_restriction": ["ifcwall.partition", "wall.partition"],
        "@enum" :["1HR, 2HR, 3HR"],
        "@localization":"Hourly Fire/Smoke Rating"
      },
      "unit_time": {
          "@id": "http://example.org/vocab#length_unit",
          "@type": "xsd:string",
          "@uuid": "f6a7b8c9-0123-4567-ghij-567890123ghi",
          "@value": "Hours"
      }
  }
}

```






# IFC on Strange Matter

Strange Matter was born out of the needs expressed by the needs of both the
buildingSMART community for future versions of IFC but also the large community
around the build environment that is looking for a modern flexible way to
connect data.

Strange Matter is an open protocol for working with distributed, heterogeneous
data used before, during, and after all phases of design, construction and
operations of the of the built environment.

Strange matter is format, vendor, and tool agnostic.

It is a way for people, processes, and tools with different requirements working
together on design and construction projects to collaborate on data that has
distributed ownership, comes from different sources, and that is continuously
changing.

Strange Matter does this by providing a universal abstract concept of entity.
That is the thing that people care about (whether it is a particular building,
floor, facade, column, roadway, pile, rail bed, asset, or whatever) and for
which more or less data may be available to different stakeholders over
different periods of time, authored in different pieces of software.

Actual data is organized in components and relationships. Components are JSON
headers that refer to data payloads, which can be in any format a user or tool
generates. Relationships are defined in the same way as components, just without
payloads, and can describe any kind of semantic relation between two components.
A relationship between a component and entity is done by sharing a relationship
with an Entity ID component.

# Strange Matter Design Criteria

Strange Matter was born from the key requirements of the industry. Chief among
them is multiformat and multi standard support. It became clear that to reach
this goal the protocol use to organize data had to be standard agnostic.

Beyond that the actual data representation was informed by broad community input
most of which is captured here.

| **Requirement**                                              | **Type**               | **Design Solution**                                          |
| ------------------------------------------------------------ | ---------------------- | ------------------------------------------------------------ |
| Data is assembled across many sources. It changes over time, has many versions and states. A single thing might be simultaneously in design, construction and operations all at the same time. | Functionality          | Entity Component Model where the Components are Packets of Data. This is augmented by relationships that are also components. This allows data to be continuously added and related together while having no impact on the existing data |
| To describe the built world we need GIS, BIM, text, requirements, issues, inspections, lidar data, point cloud data, products, carbon, energy just to name a few. No format, standard etc. can ever describe all this data so we need to find a way that can connect standard, nonstandard and even proprietary data without taking ownership of its description | Functionality          | Strange matter is format, vendor, and tool agnostic.         |
| Machine to Machine Readable                                  | Functionality          | There have been attempts to package heterogeneous data in formats previously, but the data was only labeled or classified and didn’t allow machine to machine communication. To solve this Strange Matter has proposed robust methods of data description and self-description of payloads |
| Heiarchy is in the eye of the beholder                       | Functionality          |                                                              |
| The data we use to digitally describe the built world relies heavily on relationships. This is often to the service of the format more than it is to the users of the data. |                        | Relationships are just as easy to create and compose as the data itself. This is a key requirement to incorporate automation, workflow and future machine learning capacities. |
| Data needs to work in many platforms, offline, online, archive, |                        | Strange Matter is rather simple in design but meant to work as a complete protocol as its indented to be whole, no matter the system that is used. It’s well suited to be stored, accessed and created in many technologies. <br />It’s simple enough that it can work as a file on disk, but it certainly can be use in SQL, NO-SQL, Graph and other formats. <br />The emergence of Columnar “File as Database” formats like [Apache Parquet](https://parquet.apache.org/) or [LanceDB](https://lancedb.github.io/lance/) that are becoming standard in the data science and ML world are very intriguing as they marry very well the component based approach. This opens the door for native ML and automation capabilities directly on the data. |
| Technology needs to enable solutions independent of contracts, governance or delivery models. |                        | One of the many challenges in the built environment is the variety of ways that the facilities / infrastructure are organized and managed. Strange Matter looks to provide much needed technological flexibility to work in these many different models and to enable the benefits of digitization while doing so. |
| Flexibility in Adoption                                      | Robustness             | Moving from a file-based world to an all web world should not be a requirement for adoption and thus the system is flexible. In reality there is a strong interest in a middle ground that mirrors other distributed design and engineering driven industries like software development and Film and VFX, where file-based systems are used behind change and version management tools like Git and Github. |
| Embrace Web Technologies but don't lose data in doing so     | Robustness             | Strange Matter looks to use the web as much as possible to enable richer developer, user and data experiences but also acknowledges that while the web enables rich experiences it is not permanent. To allow for these two truths it looks reference the web when available but allow provide mechanisms to ensure that data collected in Strange Matter does not loose permanence if its web sources disappear. |
| Data history must be better supported and ownership clearer. | Provenance and History | Strange Matter is design to support this by allowing 2 modes of working. First is the simplest where in situations where no data change management system is in place the data is always immutable. This is possible because Entity, and Component UUIDS are stable for the life of objects. Only the Version UUID is to ever be changed. This can be used in conjunction with semantic versioning to have a copy of every single version of the data. In situations where a Change management system in place its possible for minor versions of the data to be overwritten but any published data should never be overwritten. This has a 1 to 1 parallel with how software code is used where WIP data can be updated but once it packaged it must be stored as a separate artifact. Thus, published data should never be mutated and stay immutable the same should be said where a specific component is authored and augmented by another application. The original data should never be mutated. |
| Data Ownership and Design Transfer.                          | Functionality          | One of the most complex problems in this space is ownership of Geometric and non-Geometric Data by Data Creating Software. The solution to this problem is to move from an editing model to an additive model. Where Components that are authored by one tool cannot be overwritten by another tool. Instead, they must reference the components and make the linkage to the existing Component and Entities and create a new version of the components. This approach has many benefits. It allows for Complex Geometric Data to be used in Simpler forms when the goal is not to exchange ownership but where new components based on the existing data is all that is required. Also, it allows for the “gold version” of complex geometry to be maintained even when its necessary to convert geometry to an applications internal data model. This is possible because components can have more than one geometric representation that can be on the same entity linked by a derives relationship. |
| Share as You need (half)                                     |                        |                                                              |
| definition is not instance data                              |                        |                                                              |
| Git                                                          |                        |                                                              |
| Data is independent of its container                         |                        |                                                              |
| Benefit for all Creators, Adders/Maintainers                 |                        |                                                              |
| Out of Order and Additive                                    |                        |                                                              |
| Protocol not an API…                                         |                        |                                                              |
| Fine Control on Security/ Access                             |                        |                                                              |
| Strange Matter has one component (currently)                 |                        |                                                              |
| Classsifcation is for funtion/ Component Type is for content |                        |                                                              |
|                                                              |                        |                                                              |

# IFC on Strange Matter Design Criteria

| **Requirement**                    | **Type** | **Design Solution** |
|------------------------------------|----------|---------------------|
| Simplify                           |          |                     |
| location and positioning           |          |                     |
| Visuals                            |          |                     |
| Explicit Units                     |          |                     |
| Bools to Bools                     |          |                     |
| Developer Experience               |          |                     |
| Class Structure is for Maintainers |          |                     |

# What is Strange Matter and How does it work?

The main concepts behind Strange Matter come from Entity Component Systems. ECS.
Instead of Inheritance-based objects and data it follows a Composition model.
Here is a good technical background. [Leatherbee
ECS](https://leatherbee.org/index.php/2019/09/12/ecs-1-inheritance-vs-composition-and-ecs-background/)

It should be said from the outset that ECS learns from but given the need to
allow for a distributed approach it diverges in some key areas so while ECS is
the president Strange Matter follows its own rules and so is best described as a
means to compose data .

The graphic below illustrates the core ideas. A single entity might be fully
described using several different types of data, from different standards and
systems. Hence an object-based definition from classical programming is not well
suited.

![A diagram of components with text Description automatically
generated](media/94607d6f445c9433155558dd1a34cabf.jpg)

# Technical Concepts (a WIP Specification)

## Strange Matter

## Entity

In Strange Matter, an Entity is just a UUID7.   Because its is just an ID, it can be understood that there is no Enitity Object, as it's just an identifier for the shared concept being identified. The way an Entity comes into existence is that you make a Component that references the Entity UUID.   There could be reasons in certain storage technologies to create an Entity but from a data perspective; it is not a real “thing”.

## Everything is a Component

Given that Components are used to instantiate data it makes sense to look at Components as the root objects to store data of any kind.  This has yet to be finalized in some of the higher-level concepts of Collection and Scene, but it certainly holds, for instance, data and the relationships. 

![Untitled](Untitled%203.png)

## Component

Components are the key to this whols system working.  They hold three key bits of data.  The reference to the Entity th

## Getting Started

The first thing you must do when going down this path is begin with explicit definitions for data.  The following is the JSON-LD representation of a SM Header.  

```jsx
{
    "@context": {
        "strange_matter_component_header_definition_schema_version":"0.1",
        "strange_matter_version_date": "20230827",
        "xsd": "http://www.w3.org/2001/XMLSchema#",
        "strange_matter_definition": "http://example.org/strangematter/v.01/vocab"
    },
    "@graph": [
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
        },
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
        },
        {
            "@type": "ComponentInstanceDataExtensions",
            "Name_space_1": {
                "Value1": {
                    "@value": "<my value>",
                    "@type": "xsd:string"
                }
            },
            "MyCompany_Workflow_Extention": {
                "Value1": {
                    "@value": "<my value>",
                    "@type": "xsd:string"
                }
            }
        },
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
        },
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
        },
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
    ]
    
}    
```

### Payloads

Payloads is the name given to the data the Component is referencing.  This can be stored “in” the component or referenced. 

### Example Instance Data of an IFC4 Floor converted to Strange Matter

### Transform

```jsx
[
    {
        "component_version" : "00001",
        "entity_guid" : "2XO9sNxaf0tBWBWE4fj03n",
        "component_guid" : "b326e9b2-fd6c-4f30-a55d-2387bf199293",
        "classification_value" : "ifcslab",
        "name" : "Floor:Floor 1:9633",
        "sequence_name" : "a sequence",
        "sequence_id" : "some number",
        "sequence_value" : "00001",
        "context" : "hok.com/projects/123...",
        "author" : "hok",
        "source_data" : "C:\\+HOK\\OneDrive - HOK\\Downloads 677\\Sample_ECS_IFC.ifc",
        "source_data_id" : "4a44f905-356d-4e5d-a413-e9034c4f6495",
        "source_data_other" :"",
        "classification_reference" : "URI for the Classification Reference.",
        "component_type" : "Transform",
        "component_type_reference" : "https://.....",
        "version" : "1",
        "version_id" : "4a44f905-356d-4e5d-a413-e9034c4f5493",
        "status" : "WIP",
        "active" : "1",
        "author_software" : "Revit 2024",
        "hash1" : "",
        "payload_data_type" : "json",
        "date_created" : "20230518095403.5713569",
        "x" : -1316.1383962649138,
        "y" : -420.56892778995643,
        "z" : 0,
        "rotation": 0,
        "scale": 1.0
    }
]
```

### Geometry

Here is a sample of an IFC4,  IFC Floor converted to GeoJSON data and packaged in a “Geometry” component.  The Geometry Component Definition will most likely want to be more precise than just “Geometry,” but this is a sample. 

```jsx
[
    {
        "component_version" : "00001",
        "entity_guid" : "2XO9sNxaf0tBWBWE4fj03n",
        "component_guid" : "b326e9b2-fd6c-4f30-a55d-2387bf199291",
        "classification_value" : "ifcslab",
        "name" : "Floor:Floor 1:9633",
        "sequence_name" : "a sequence",
        "sequence_id" : "some number",
        "sequence_value" : "00001",
        "context" : "hok.com/projects/123...",
        "author" : "hok",
        "source_data" : "C:\\+HOK\\OneDrive - HOK\\Downloads 677\\Sample_ECS_IFC.ifc",
        "source_data_id" : "4a44f905-356d-4e5d-a413-e9034c4f6495",
        "source_data_other" :"",
        "classification_reference" : "URI for the Classification Reference.",
        "component_type" : "IFC_Geometry",
        "component_type_reference" : "https://.....",
        "version" : "1",
        "version_id" : "4a44f905-356d-4e5d-a413-e9034c4f5493",
        "status" : "WIP",
        "active" : "1",
        "author_software" : "Revit 2024",
        "hash1" : "",
        "payload_data_type" : "GeoJson",
        "date_created" : "20230518095403.5713569",
        "geometry" : "{\"type\":\"MultiLineString\",\"coordinates\":[[[-1316.1383963,-420.5689278,0],[-1316.1383963,3779.4310722,0]],[[-1316.1383963,3779.4310722,0],[-1316.1383963,3779.4310722,-300]],[[-1316.1383963,-420.5689278,-300],[-1316.1383963,3779.4310722,-300]],[[-1316.1383963,3779.4310722,0],[6892.6695842,3779.4310722,0]],[[6892.6695842,3779.4310722,0],[6892.6695842,3779.4310722,-300]],[[-1316.1383963,3779.4310722,-300],[6892.6695842,3779.4310722,-300]],[[6892.6695842,3779.4310722,0],[6892.6695842,-420.5689278,0]],[[6892.6695842,-420.5689278,0],[6892.6695842,-420.5689278,-300]],[[6892.6695842,3779.4310722,-300],[6892.6695842,-420.5689278,-300]],[[6892.6695842,-420.5689278,0],[-1316.1383963,-420.5689278,0]],[[-1316.1383963,-420.5689278,0],[-1316.1383963,-420.5689278,-300]],[[6892.6695842,-420.5689278,-300],[-1316.1383963,-420.5689278,-300]]]}"
    }
]
```

### PSET All - Revit Values

This is for demo purposes, as you’d most likely not want to package all the values into one component, but it won’t violate any rules to do so. 

```jsx
[
    {
        "component_version" : "00001",
        "entity_guid" : "2XO9sNxaf0tBWBWE4fj03n",
        "component_guid" : "b326e9b2-fd6c-4f30-a55d-2387bf199292",
        "classification_value" : "ifcslab",
        "name" : "Floor:Floor 1:9633",
        "sequence_name" : "a sequence",
        "sequence_id" : "some number",
        "sequence_value" : "00001",
        "context" : "hok.com/projects/123...",
        "author" : "hok",
        "source_data" : "C:\\+HOK\\OneDrive - HOK\\Downloads 677\\Sample_ECS_IFC.ifc",
        "source_data_id" : "4a44f905-356d-4e5d-a413-e9034c4f6495",
        "source_data_other" :"",
        "classification_reference" : "URI for the Classification Reference.",
        "component_type" : "IFC_Pset_All",
        "component_type_reference" : "https://.....",
        "version" : "1",
        "version_id" : "4a44f905-356d-4e5d-a413-e9034c4f5493",
        "status" : "WIP",
        "active" : "1",
        "author_software" : "Revit 2024",
        "hash1" : "",
        "payload_data_type" : "json",
        "date_created" : "20230518095403.5713569",
        "element_parent_id" : "2XO9sNxaf0tBWBWE4fj28X",
        "element_id" : "2XO9sNxaf0tBWBWE4fj03n",
        "GlobalId" : "2XO9sNxaf0tBWBWE4fj03n",
        "Name" : "Floor:Floor 1:9633",
        "ObjectType" : "Floor:Floor 1",
        "Tag" : "9633",
        "Constraints.Level" : "Level 1",
        "Dimensions.Volume" : 10.34309805544262,
        "Phasing.Phase Created" : "New Construction",
        "multi_reader_full_id" : 0,
        "multi_reader_id" : 0,
        "multi_reader_keyword" : "REVIT_1",
        "multi_reader_type" : "REVIT",
        "Dimensions.Thickness" : "299.99999999999994",
        "Constraints.Height Offset From Level" : 0,
        "Constraints.Related to Mass" : false,
        "Constraints.Room Bounding" : true,
        "Dimensions.Area" : 34.47699351814207,
        "Dimensions.Perimeter" : 24817.615961019987,
        "Pset_SlabCommon.IsExternal" : false,
        "Pset_SlabCommon.LoadBearing" : true,
        "Pset_SlabCommon.Reference" : "Floor 1",
        "Structural.Structural" : true,
        "_uuid" : "b326e9b2-fd6c-4f30-a55d-2387bf199293"
    }
]
```

### Relationship

Relationships are Components just like Data Components.  Here you’ll find a relationship that states that several Entities and Components have a relationship with a building Story Entity and Its Components. 

```jsx
[
    {
        "component_version" : "00001",
        "entity_guid" : "3o5x6W2EXLgWynzp6poG5Q",
        "component_guid" : "3981eb98-92b0-4c72-849c-09ed21addc8c",
        "classification_value" : "ifcrelationship",
        "name" : "relationship1",
        "sequence_name" : "a sequence",
        "sequence_id" : "some number",
        "sequence_value" : "00001",
        "context" : "hok.com/projects/123...",
        "author" : "hok",
        "source_data" : "C:\\+HOK\\OneDrive - HOK\\Downloads 677\\Sample_ECS_IFC.ifc",
        "source_data_id" : "6e28aba5-3195-446c-acad-3187261f78a2",
        "classification_reference" : "URI for the Classification Reference.",
        "component_type" : "member_of_relationship",
        "component_type_reference" : "https://.....",
        "version" : "1",
        "status" : "WIP",
        "active" : "1",
        "author_software" : "Revit 2024",
        "hash1" : "",
        "payload_data_type" : "json",
        "date_created" : "20230518095403.5000419",
        "source_entities" : "2XO9sNxaf0tBWBWE4fj28X",
        "source_components" : "12c5310a-fca8-434f-b36f-494754b157a4",
        "source_component_type" : "BuildingStory",
        "destination_entities" : "2XO9sNxaf0tBWBWF8fj06l,2XO9sNxaf0tBWBWF8fj01x,2XO9sNxaf0tBWBWF8fj3bd,2XO9sNxaf0tBWBWF8fj0Lv,2XO9sNxaf0tBWBWF8fj00m,2webN1ByIyh7t4C_D3A$H_,3Y0ZKiU6kUajwsq5fL5HF4,1nDWbUkpKJE7QGAKbUJydn,3asUQY1AQWm91Ftuc0IpE6,3o5x6W2EXLgWynzp6poG3Q,1Cn$3jXq7CO_Zbm3Dje3S$,2XO9sNxaf0tBWBWE4fj06l,2XO9sNxaf0tBWBWE4fj01x,2XO9sNxaf0tBWBWE4fj0Lv,2XO9sNxaf0tBWBWE4fj00m,2XO9sNxaf0tBWBWE4fj03n,2XO9sNxaf0tBWBWE4fj3bd,2XO9sNxaf0tBWBWE4fj1or,2XO9sNxaf0tBWBWE4fj0DN,2XO9sNxaf0tBWBWE4fj1Zf,2XO9sNxaf0tBWBWE4fj0DI,2XO9sNxaf0tBWBWE4fj0DH,2XO9sNxaf0tBWBWE4fj0DM,2XO9sNxaf0tBWBWE4fj0DK,2XO9sNxaf0tBWBWE4fj0DO,2XO9sNxaf0tBWBWE4fj0DL,2XO9sNxaf0tBWBWE4fj0DJ,2XO9sNxaf0tBWBWE4fj2xR,2XO9sNxaf0tBWBWE4fj2Y0,2XO9sNxaf0tBWBWE4fj2bj,2XO9sNxaf0tBWBWE4fj2c8,2XO9sNxaf0tBWBWE4fj2WU,2XO9sNxaf0tBWBWE4fj2hl,2XO9sNxaf0tBWBWE4fj2gH",
        "destination_components" : "1cb6d448-9b57-48d1-8daf-b03e1c3fea86,32aedccb-4a4b-48fd-9181-0635d6cb281d,80a918b0-8c41-458a-8246-a7fce73706fd,6f72691e-716f-4623-b062-9a451f2638f4,93ec36c0-46cb-40e9-87bc-fbc951e126f9,1b9fe029-4199-40b1-b984-764c805f015c,b3248c7d-cb37-4c9f-8667-74bc0829390d,c6d53d83-1467-48c8-be92-589d18e7cfe0,00b91123-d845-48f0-bcb3-577752fa011f,3219cb50-a445-453d-bc9d-266759397fc7,c4ccb641-c1f2-4634-8c41-22af59107b31,fddf8ac6-3f7e-4f83-9e01-fc08ae1294b3,784f95f0-65cc-4a7f-98e9-c4b66de12ea5,fbfe43dc-74e2-42d7-b89f-a9d2534903b1,14663abb-4f6b-4b22-a66e-3e64fe210596,fc4a6326-e544-4270-bf0f-ced45aa8f6f4,3a123e49-92b3-4bf0-9cdc-d94aaad5403b,947c9c00-cb15-4920-81c6-b2f3ac3975b2,018b6272-03cc-42ef-aabb-6f10e4ddcaad,740e4ad2-eff4-4f22-85c0-cd5db0031114,45293a23-00f0-43ce-b426-21cc4f02b99c,1eada1c7-ca65-4c79-ace0-3e3dcd71c2a2,5515aa0d-7de6-4446-b79d-4eb00c7f0548,cf43a65f-f1e6-4fcf-ba54-366a55b932a5,d83fa667-7a69-40ad-9022-a0c186a187a9,e4f2ed71-1161-4797-8128-46a0301ff6fb,1e39e486-fde2-4e15-ac02-6a8861a2af7e,5eb3b2fb-17b6-476c-89ee-c6e1ddcff4ee,74795de6-009c-4adb-acc7-8ad268ad05fd,d5a6c071-b414-4d54-9fc4-5b07774265f3,34945e88-7045-4d53-ae29-59dfb57dfb7e,5b2a8193-d116-4461-85fd-d3232010ada8,39fca75a-6c7d-4d0e-9edb-30550a893c87,0bf7b19a-a6a7-448f-be4f-06d29a5d16c0",
        "destination_component_type" : ""
    }
]
```

## Collection (Formerly Container)

A collection does the work that files do in other systems.  But instead of containing the data it references the components, and thus components can be members of many collections. 

![Untitled](Untitled%204.png)

```jsx
[
    {
        "component_version" : "00001",
        "entity_guid" : "3o5x6W2EXLgWynzp6poG53",
        "component_guid" : "3981eb98-92b0-4c72-849c-09ed21addc8f",
        "classification_value" : "What is the object",
        "name" : "Collection1",
        "sequence_name" : "a sequence",
        "sequence_id" : "some number",
        "sequence_value" : "00001",
        "context" : "hok.com/projects/123...",
        "author" : "hok",
        "source_data" : "C:\\+HOK\\OneDrive - HOK\\Downloads 677\\Sample_ECS_IFC.ifc",
        "source_data_id" : "6e28aba5-3195-446c-acad-3187261f78a2",
        "classification_reference" : "URI for the Classification Reference.",
        "component_type" : "Collection",
        "component_type_reference" : "https://.....",
        "version" : "1",
        "status" : "WIP",
        "active" : "1",
        "author_software" : "Revit 2024",
        "hash1" : "",
        "payload_data_type" : "json",
        "date_created" : "20230518095403.5000419",
        "collection_components" : "1cb6d448-9b57-48d1-8daf-b03e1c3fea86,32aedccb-4a4b-48fd-9181-0635d6cb281d,80a918b0-8c41-458a-8246-a7fce73706fd,6f72691e-716f-4623-b062-9a451f2638f4,93ec36c0-46cb-40e9-87bc-fbc951e126f9,1b9fe029-4199-40b1-b984-764c805f015c,b3248c7d-cb37-4c9f-8667-74bc0829390d,c6d53d83-1467-48c8-be92-589d18e7cfe0,00b91123-d845-48f0-bcb3-577752fa011f,3219cb50-a445-453d-bc9d-266759397fc7,c4ccb641-c1f2-4634-8c41-22af59107b31,fddf8ac6-3f7e-4f83-9e01-fc08ae1294b3,784f95f0-65cc-4a7f-98e9-c4b66de12ea5,fbfe43dc-74e2-42d7-b89f-a9d2534903b1,14663abb-4f6b-4b22-a66e-3e64fe210596,fc4a6326-e544-4270-bf0f-ced45aa8f6f4,3a123e49-92b3-4bf0-9cdc-d94aaad5403b,947c9c00-cb15-4920-81c6-b2f3ac3975b2,018b6272-03cc-42ef-aabb-6f10e4ddcaad,740e4ad2-eff4-4f22-85c0-cd5db0031114,45293a23-00f0-43ce-b426-21cc4f02b99c,1eada1c7-ca65-4c79-ace0-3e3dcd71c2a2,5515aa0d-7de6-4446-b79d-4eb00c7f0548,cf43a65f-f1e6-4fcf-ba54-366a55b932a5,d83fa667-7a69-40ad-9022-a0c186a187a9,e4f2ed71-1161-4797-8128-46a0301ff6fb,1e39e486-fde2-4e15-ac02-6a8861a2af7e,5eb3b2fb-17b6-476c-89ee-c6e1ddcff4ee,74795de6-009c-4adb-acc7-8ad268ad05fd,d5a6c071-b414-4d54-9fc4-5b07774265f3,34945e88-7045-4d53-ae29-59dfb57dfb7e,5b2a8193-d116-4461-85fd-d3232010ada8,39fca75a-6c7d-4d0e-9edb-30550a893c87,0bf7b19a-a6a7-448f-be4f-06d29a5d16c0"
    }
]
```

## Scene (TBD)

![Untitled](Untitled%205.png)

## Archetype

In a system such as this, it’s going to be important to externally define all the components that are necessary to complete a task, project etc.  An Archetype is a named set of these components.

![Untitled](Untitled%206.png)

## Ledger (WIP)

To quickly capture and enable a history of change the system will define how Ledgers can be used to capture change at a level more granular than is logical than components. 

## Cache (WIP)

It can be images that the raw data needs to be expressed as individual components, but for querying and fast accessing it can be imaged that the system will need a way to cache static data. 

## Data Dictionaries

Much like the BuildingSMART Data Dictionary today describes and identifies the definitions of parameters, Components and Archetypes will need this as well.  Given that the Components are generic and not tied to any specific data ,source, the Data Dictionary schema will also want to be data format agnostic.

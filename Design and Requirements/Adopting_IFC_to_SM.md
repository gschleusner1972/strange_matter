# IFC on Strange Matter

Strange Matter was born out of the needs expressed by both the
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

The first thing you must do when going down this path is begin with explicit definitions for data. This technique takes data that might be defined in one location but now can be define in many places.  IFC has distributed definitions already so its not to dissimilar.    The following is the JSON-LD representation of a Strange Matter  Header.   Because it's necessary for each component to describe itself there is a fair amount of boiler plate.  When looking at storage this is why the columnar formats are interesting as they can compress data like this very easily. 



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

## Payloads

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

### Header Instance Examples

## Step Geometry (~IFC Today)

```json
[
{
"authoring_software":"?",
"payload_hash":"value",
"payload_hash_definition":"na",
"payload_data_type": "step21",
"payload_encoding":"na",
"payload_encryption":"na",
"payload_data": "ISO-10303-21;
    HEADER;
    FILE_DESCRIPTION(('FTC-11 geometry only from the NIST MBE PMI Validation and Conformance Testing Project'),'2;1');
    FILE_NAME('nist_ftc_11_asme1.stp','2015-05-27T17:43:57',(''),(''),'','','');
    FILE_SCHEMA(('CONFIG_CONTROL_DESIGN'));
    ENDSEC;
    DATA;
    #5=APPLICATION_CONTEXT('configuration controlled 3D designs of mechanical parts and assemblies');
    #6=APPLICATION_PROTOCOL_DEFINITION('International Standard','ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf',2004,#5);
    #7=PRODUCT_CONTEXT('',#5,'mechanical');
    #8=PRODUCT('nist_ftc_11_asme1','nist_ftc_11_asme1',$,(#7));
    #9=PRODUCT_RELATED_PRODUCT_CATEGORY('part',$,(#8));
    #10=PRODUCT_DEFINITION_FORMATION('',$,#8);
    #11=PRODUCT_DEFINITION_CONTEXT('part definition',#5,'design');
    #12=PRODUCT_DEFINITION('',$,#10,#11);
    #18=(NAMED_UNIT(*)PLANE_ANGLE_UNIT()SI_UNIT($,.RADIAN.));
    #19=DIMENSIONAL_EXPONENTS(0.0,0.0,0.0,0.0,0.0,0.0,0.0);
    #20=PLANE_ANGLE_MEASURE_WITH_UNIT(PLANE_ANGLE_MEASURE(0.0174532925),#18);
    #24=(CONVERSION_BASED_UNIT('DEGREE',#20)NAMED_UNIT(#19)PLANE_ANGLE_UNIT());
    #28=(NAMED_UNIT(*)SI_UNIT($,.STERADIAN.)SOLID_ANGLE_UNIT());
    #32=(LENGTH_UNIT()NAMED_UNIT(*)SI_UNIT(.MILLI.,.METRE.));
    #34=UNCERTAINTY_MEASURE_WITH_UNIT(LENGTH_MEASURE(0.01),#32,'DISTANCE_ACCURACY_VALUE','');
    #36=(GEOMETRIC_REPRESENTATION_CONTEXT(3)GLOBAL_UNCERTAINTY_ASSIGNED_CONTEXT((#34))GLOBAL_UNIT_ASSIGNED_CONTEXT((#24,#28,#32))REPRESENTATION_CONTEXT('None','None'));
    #37=AXIS2_PLACEMENT_3D('',#38,#39,#40);
    #38=CARTESIAN_POINT('',(0.0,0.0,0.0));
    #39=DIRECTION('',(0.0,0.0,1.0));
    #40=DIRECTION('',(1.0,0.0,0.0));
    #41=SHAPE_REPRESENTATION('',(#37),#36);
    #42=PRODUCT_DEFINITION_SHAPE('','',#12);
    #43=SHAPE_DEFINITION_REPRESENTATION(#42,#41);
    #49=(NAMED_UNIT(*)PLANE_ANGLE_UNIT()SI_UNIT($,.RADIAN.));
    #50=DIMENSIONAL_EXPONENTS(0.0,0.0,0.0,0.0,0.0,0.0,0.0);
    #51=PLANE_ANGLE_MEASURE_WITH_UNIT(PLANE_ANGLE_MEASURE(0.0174532925),#49);
    #55=(CONVERSION_BASED_UNIT('DEGREE',#51)NAMED_UNIT(#50)PLANE_ANGLE_UNIT());
    #59=(NAMED_UNIT(*)SI_UNIT($,.STERADIAN.)SOLID_ANGLE_UNIT());
    #63=(LENGTH_UNIT()NAMED_UNIT(*)SI_UNIT(.MILLI.,.METRE.));
    #65=UNCERTAINTY_MEASURE_WITH_UNIT(LENGTH_MEASURE(0.000001),#63,'DISTANCE_ACCURACY_VALUE','');
    #67=(GEOMETRIC_REPRESENTATION_CONTEXT(3)GLOBAL_UNCERTAINTY_ASSIGNED_CONTEXT((#65))GLOBAL_UNIT_ASSIGNED_CONTEXT((#55,#59,#63))REPRESENTATION_CONTEXT('','3D'));
    #68=CARTESIAN_POINT('',(0.0,0.0,-0.75));
    #69=DIRECTION('',(0.0,0.0,1.0));
    #70=DIRECTION('',(0.0,-1.0,0.0));
    #71=AXIS2_PLACEMENT_3D('',#68,#69,#70);
    #72=CYLINDRICAL_SURFACE('',#71,16.0);
    #73=CARTESIAN_POINT('',(0.0,-16.0,-1.499999999999999));
    #74=VERTEX_POINT('',#73);
    #75=CARTESIAN_POINT('',(0.0,0.0,-1.499999999999999));
    #76=DIRECTION('',(0.0,0.0,1.0));
    #77=DIRECTION('',(0.0,-1.0,0.0));
    #78=AXIS2_PLACEMENT_3D('',#75,#76,#77);
    #79=CIRCLE('',#78,16.0);
    #80=EDGE_CURVE('',#74,#74,#79,.T.);
    #81=ORIENTED_EDGE('',*,*,#80,.F.);
    #82=EDGE_LOOP('',(#81));
    #83=FACE_OUTER_BOUND('',#82,.T.);
    #84=CARTESIAN_POINT('',(0.0,-16.0,0.0));
    #85=VERTEX_POINT('',#84);
    #86=CARTESIAN_POINT('',(0.0,0.0,0.0));
    #87=DIRECTION('',(0.0,0.0,1.0));
    #88=DIRECTION('',(0.0,-1.0,0.0));
    #89=AXIS2_PLACEMENT_3D('',#86,#87,#88);
    #90=CIRCLE('',#89,16.0);
    #91=EDGE_CURVE('',#85,#85,#90,.T.);
    #92=ORIENTED_EDGE('',*,*,#91,.T.);
    #93=EDGE_LOOP('',(#92));
    #94=FACE_BOUND('',#93,.T.);
    #95=ADVANCED_FACE('',(#83,#94),#72,.F.);
    #96=CARTESIAN_POINT('',(0.0,-23.75,-1.5));
    #97=DIRECTION('',(0.0,0.0,-1.0));
    #98=DIRECTION('',(-1.0,0.0,0.0));
    #99=AXIS2_PLACEMENT_3D('',#96,#97,#98);
    #100=PLANE('',#99);
    #101=CARTESIAN_POINT('',(0.0,-31.5,-1.500000000000001));
    #102=VERTEX_POINT('',#101);
    #103=CARTESIAN_POINT('',(0.0,0.0,-1.500000000000001));
    #104=DIRECTION('',(0.0,0.0,1.0));
    #105=DIRECTION('',(0.0,-1.0,0.0));
    #106=AXIS2_PLACEMENT_3D('',#103,#104,#105);
    #107=CIRCLE('',#106,31.5);
    #108=EDGE_CURVE('',#102,#102,#107,.T.);
    #109=ORIENTED_EDGE('',*,*,#108,.F.);
    #110=EDGE_LOOP('',(#109));
    #111=FACE_OUTER_BOUND('',#110,.T.);
    #112=ORIENTED_EDGE('',*,*,#80,.T.);
    #113=EDGE_LOOP('',(#112));
    #114=FACE_BOUND('',#113,.T.);
    #115=ADVANCED_FACE('',(#111,#114),#100,.T.);
    #116=CARTESIAN_POINT('',(0.0,0.0,-0.75));
    #117=DIRECTION('',(0.0,0.0,1.0));
    #118=DIRECTION('',(0.0,-1.0,0.0));
    #119=AXIS2_PLACEMENT_3D('',#116,#117,#118);
    #120=CYLINDRICAL_SURFACE('',#119,31.5);
    #121=CARTESIAN_POINT('',(0.0,-31.5,0.0));
    #122=VERTEX_POINT('',#121);
    #123=CARTESIAN_POINT('',(0.0,0.0,0.0));
    #124=DIRECTION('',(0.0,0.0,1.0));
    #125=DIRECTION('',(0.0,-1.0,0.0));
    #126=AXIS2_PLACEMENT_3D('',#123,#124,#125);
    #127=CIRCLE('',#126,31.5);
    #128=EDGE_CURVE('',#122,#122,#127,.T.);
    #129=ORIENTED_EDGE('',*,*,#128,.F.);
    #130=EDGE_LOOP('',(#129));
    #131=FACE_OUTER_BOUND('',#130,.T.);
    #132=ORIENTED_EDGE('',*,*,#108,.T.);
    #133=EDGE_LOOP('',(#132));
    #134=FACE_BOUND('',#133,.T.);
    #135=ADVANCED_FACE('',(#131,#134),#120,.T.);
    #136=CARTESIAN_POINT('',(-1.293027E-015,4.934325E-016,0.425));
    #137=DIRECTION('',(0.0,0.0,1.0));
    #138=DIRECTION('',(1.0,0.0,0.0));
    #139=AXIS2_PLACEMENT_3D('',#136,#137,#138);
    #140=PLANE('',#139);
    #141=CARTESIAN_POINT('',(-28.561467761918419,3.497771E-015,0.425));
    #142=VERTEX_POINT('',#141);
    #143=CARTESIAN_POINT('',(0.0,0.0,0.425));
    #144=DIRECTION('',(0.0,0.0,-1.0));
    #145=DIRECTION('',(1.0,0.0,0.0));
    #146=AXIS2_PLACEMENT_3D('',#143,#144,#145);
    #147=CIRCLE('',#146,28.561467761918419);
    #148=EDGE_CURVE('',#142,#142,#147,.T.);
    #149=ORIENTED_EDGE('',*,*,#148,.F.);
    #150=EDGE_LOOP('',(#149));
    #151=FACE_OUTER_BOUND('',#150,.T.);
    #152=CARTESIAN_POINT('',(-18.938532238081581,-2.319301E-015,0.425));
    #153=VERTEX_POINT('',#152);
    #154=CARTESIAN_POINT('',(0.0,0.0,0.425));
    #155=DIRECTION('',(0.0,0.0,1.0));
    #156=DIRECTION('',(1.0,0.0,0.0));
    #157=AXIS2_PLACEMENT_3D('',#154,#155,#156);
    #158=CIRCLE('',#157,18.938532238081581);
    #159=EDGE_CURVE('',#153,#153,#158,.T.);
    #160=ORIENTED_EDGE('',*,*,#159,.F.);
    #161=EDGE_LOOP('',(#160));
    #162=FACE_BOUND('',#161,.T.);
    #163=ADVANCED_FACE('',(#151,#162),#140,.T.);
    #164=CARTESIAN_POINT('',(0.0,0.0,0.0));
    #165=DIRECTION('',(0.0,0.0,1.0));
    #166=DIRECTION('',(1.0,0.0,0.0));
    #167=AXIS2_PLACEMENT_3D('',#164,#165,#166);
    #168=TOROIDAL_SURFACE('',#167,30.0,1.5);
    #169=ORIENTED_EDGE('',*,*,#128,.T.);
    #170=EDGE_LOOP('',(#169));
    #171=FACE_OUTER_BOUND('',#170,.T.);
    #172=ORIENTED_EDGE('',*,*,#148,.T.);
    #173=EDGE_LOOP('',(#172));
    #174=FACE_BOUND('',#173,.T.);
    #175=ADVANCED_FACE('',(#171,#174),#168,.T.);
    #176=CARTESIAN_POINT('',(0.0,0.0,0.0));
    #177=DIRECTION('',(0.0,0.0,1.0));
    #178=DIRECTION('',(1.0,0.0,0.0));
    #179=AXIS2_PLACEMENT_3D('',#176,#177,#178);
    #180=TOROIDAL_SURFACE('',#179,17.5,1.5);
    #181=ORIENTED_EDGE('',*,*,#159,.T.);
    #182=EDGE_LOOP('',(#181));
    #183=FACE_OUTER_BOUND('',#182,.T.);
    #184=ORIENTED_EDGE('',*,*,#91,.F.);
    #185=EDGE_LOOP('',(#184));
    #186=FACE_BOUND('',#185,.T.);
    #187=ADVANCED_FACE('',(#183,#186),#180,.T.);
    #188=CLOSED_SHELL('',(#95,#115,#135,#163,#175,#187));
    #189=MANIFOLD_SOLID_BREP('Solid1',#188);
    #190=COLOUR_RGB('Default(1)',0.749019622802734,0.749019622802734,0.584313750267029);
    #191=FILL_AREA_STYLE_COLOUR('Default(1)',#190);
    #192=FILL_AREA_STYLE('Default(1)',(#191));
    #193=SURFACE_STYLE_FILL_AREA(#192);
    #194=SURFACE_SIDE_STYLE('Default(1)',(#193));
    #195=SURFACE_STYLE_USAGE(.BOTH.,#194);
    #196=PRESENTATION_STYLE_ASSIGNMENT((#195));
    #197=STYLED_ITEM('',(#196),#189);
    #198=MECHANICAL_DESIGN_GEOMETRIC_PRESENTATION_REPRESENTATION('',(#197),#36);
    #199=ADVANCED_BREP_SHAPE_REPRESENTATION('ABSR',(#189),#36);
    #200=SHAPE_REPRESENTATION_RELATIONSHIP('SRR','None',#199,#41);
    ENDSEC;
    END-ISO-10303-21;"
    ]
}
]

```

### IDS for a Slab

```json
[
{
"authoring_software":"?",
"payload_hash":"value",
"payload_hash_definition":"na",
"payload_data_type": "xml",
"payload_data_type_definition":"na",
"payload_encoding":"na",
"payload_encryption":"na",
"payload_data": "<ids xmlns="http://standards.buildingsmart.org/IDS" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://standards.buildingsmart.org/IDS/ids_05.xsd">
<info>
    <title>An empty string is considered falsey and will not pass</title>
</info>
<specifications>
    <specification name=""An empty string is considered falsey and will not pass" ifcVersion="IFC2X3 IFC4" minOccurs="1" maxOccurs="unbounded">
        <applicability>
            <entity>
                <name>
                    <simpleValue>IFCSLAB</simpleValue>
                </name>
            </entity>
        </applicability>
        <requirements>
            <property datatype="IfcLogical" minOccurs="1" maxOccurs="1">
                <propertySet>
                    <simpleValue>Foo_Bar</simpleValue>
                </propertySet>
                <name>
                    <simpleValue>Foo</simpleValue>
                </name>
            </property>
        </requirements>
    </specification>
</specifications>
</ids>"
}
]

```

### Site GeoJson

```json
[
{
"authoring_software":"FME",
"payload_hash":"value",
"payload_hash_definition":"na",
"payload_data_type": "geojson",
"payload_data_type_definition":"https://github.com/geojson/schema/blob/main/src/schema/MultiLineString.js",
"payload_encoding":"na",
"payload_encryption":"na",
"payload_data": "{\"type\":\"MultiLineString\",\"coordinates\":[[[-1316.1383963,-420.5689278,0],[-1316.1383963,3779.4310722,0]],[[-1316.1383963,3779.4310722,0],[-1316.1383963,3779.4310722,-300]],[[-1316.1383963,-420.5689278,-300],[-1316.1383963,3779.4310722,-300]],[[-1316.1383963,3779.4310722,0],[6892.6695842,3779.4310722,0]],[[6892.6695842,3779.4310722,0],[6892.6695842,3779.4310722,-300]],[[-1316.1383963,3779.4310722,-300],[6892.6695842,3779.4310722,-300]],[[6892.6695842,3779.4310722,0],[6892.6695842,-420.5689278,0]],[[6892.6695842,-420.5689278,0],[6892.6695842,-420.5689278,-300]],[[6892.6695842,3779.4310722,-300],[6892.6695842,-420.5689278,-300]],[[6892.6695842,-420.5689278,0],[-1316.1383963,-420.5689278,0]],[[-1316.1383963,-420.5689278,0],[-1316.1383963,-420.5689278,-300]],[[6892.6695842,-420.5689278,-300],[-1316.1383963,-420.5689278,-300]]]}"
}
]

```



### Payloads

Payloads is the name given to the data the Component is referencing.  This can be stored “in” the component or referenced. 

### Example Instance Data of an IFC4 Floor converted to Strange Matter



### Geometry

Here is a sample of an IFC4,  IFC Floor converted to GeoJSON data and packaged in a “Geometry” component.  The Geometry Component Definition will most likely want to be more precise than just “Geometry,” but this is a sample. 



### PSET All - Revit Values

This is for demo purposes, as you’d most likely not want to package all the values into one component, but it won’t violate any rules to do so. 



### Relationship

Relationships are Components just like Data Components.  Here you’ll find a relationship that states that several Entities and Components have a relationship with a building Story Entity and Its Components. 



## Collection (Formerly Container)

A collection does the work that files do in other systems.  But instead of containing the data it references the components, and thus components can be members of many collections. 

![Untitled](Untitled%204.png)



![Untitled](Untitled%205.png)

## Archetype

In a system such as this, it’s going to be important to externally define all the components that are necessary to complete a task, project etc.  An Archetype is a named set of these components.

![Untitled](Untitled%206.png)

## Ledger (WIP)

To quickly capture and enable a history of change the system will define how Ledgers can be used to capture change at a level more granular than is logical than components. 

## Cache (WIP)

It can be images that the raw data needs to be expressed as individual components, but for querying and fast accessing it can be imaged that the system will need a way to cache static data. 


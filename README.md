# Strange Matter - Its what Data Craves!
Strange Matter is an open protocol for working with distributed, heterogeneous data used before, during, and after all phases of design and construction of the built-environment.

## The Problem

https://github.com/magnetar-io/strange_matter/assets/33819927/76916606-40db-4f08-983a-4dc39ab00e1f

Strange matter is format, vendor, and tool agnostic.  

It is a way for people, processes, and tools with different requirements working together on design and construction projects to collaborate on data that has distributed ownership, comes from different sources, and that is continuously changing. 

Strange Matter does this by providing a universal abstract concept of entity. That is the thing that people care about (whether it is a particular building, floor, facade, column, duct, asset, or whatever) and for which more or less data may be available to different stakeholders over different periods of time, authored in different pieces of software. 

Actual data in a Strange Matter project is organized in components and relationships.  Components are JSON headers that refer to data payloads, which can be in any format a user or tool generates. Relationships are defined in the same way as components, just without payloads, and can describe any kind of semantic relation between two components. A relationship between a component and entity is done by sharing a relationship with an Entity ID  component. 

A detailed walkthrough the of the reasoning, requirements and key technical components can be found in the wiki.

## More Details
https://github.com/magnetar-io/strange_matter/wiki

## WIP Specification
https://github.com/magnetar-io/strange_matter/wiki/005_Technical_Concepts-(WIP-Specification)


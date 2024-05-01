# InvalidSchemaorgProperty

[**code**](/en/latest/Schema Reference/meta/defs/code): INVALID_SCHEMAORG_PROPERTY

[**level**](/en/latest/Schema Reference/meta/defs/level): warning

[**reason**](/en/latest/Schema Reference/meta/defs/reason): The schema.org ontology contains a fixed set of legal properties which can be applied to objects within the metadata. If schema.org is used as the only @context within your metadata, then all properties will be interpreted as schema.org properties. Using an invalid schema.org property is not considered an error in the psych-DS specification, but it should be understood that such usages result in the property in question not being interpretable by machines.
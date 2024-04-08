# InvalidObjectType

[**code**](/Schema Reference/meta/defs/code): INVALID_OBJECT_TYPE

[**level**](/Schema Reference/meta/defs/level): warning

[**reason**](/Schema Reference/meta/defs/reason): Properties in the schema.org ontology have selective restrictions on which types of objects can be used for their values. including an object with a @type that does not match the selective restrictions of its property is not an error in psych-DS, but it will result in the object in question not being interpretable by machines.
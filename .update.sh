#!/bin/bash
python3 schema_model/tools/convert_to_json.py external_schemas/schemaorg.yaml
mv schema.json external_schemas/schemaorg.json
python3 schema_model/tools/convert_to_json.py schema_model/versions/1.0.0
mv schema.json schema_model/versions/jsons/1.0.0 
cp schema_model/versions/jsons/1.0.0/schema.json schema_model/versions/jsons/latest 
git add .   
git commit -m "updated schema model"
git push origin develop 

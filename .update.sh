#!/bin/bash
python3 schema_model/tools/convert_to_json.py schema_model/versions/$1
mkdir -p schema_model/versions/jsons/$1
mv schema.json schema_model/versions/jsons/$1/schema.json
cp schema_model/versions/jsons/$1/schema.json schema_model/versions/jsons/latest 
git add .   
git commit -m "updated schema model, version $1"
git push origin develop 

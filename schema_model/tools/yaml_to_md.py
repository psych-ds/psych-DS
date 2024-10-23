import yaml
import pathlib
import os
import snakemd
import argparse

docs_dir = './psychDS-docs'


#loops through schema model directory
def explore_dir(this_dir,context={'props':{},'files':{}}):
    #create subdirs for all but the root dir
    if not this_dir.endswith(args.version):
        pathlib.Path('./psychDS-docs/{dir_tail}'.format(dir_tail=this_dir.split('{version}/'.format(version=args.version))[1])).mkdir(exist_ok=True)
    #loop through files/dirs in schema model recursively
    for filename in os.listdir(this_dir):
        if 'DS_Store' in filename:
            continue
        f = os.path.join(this_dir,filename)
        #save "context" dict to keep track of definitions and links
        if os.path.isfile(f):
            context = gen_rst(f,this_dir,context)
        #recursively search subdir
        if os.path.isdir(f):
            explore_dir(f,context)

#when a file is encountered, the yaml needs to be loaded and converted into a markdown,
#which is handled differently depending on the location of the file
def gen_rst(this_file,this_dir,context):
    with open(this_file,'r') as f:
        this_yaml = yaml.safe_load(f)
        #context is a unique case and needs to be handled specifically, 
        #with definitions for properties being stored
        if 'context' in this_file:
            context = generate_context(this_yaml,context)
        else:
            subdir = this_dir.split('{version}/'.format(version=args.version))[1]
            file_stem = this_file.split('/')[-1].split('.')[0]
            this_path = os.path.join('./psychDS-docs',subdir,file_stem)
            pathlib.Path(this_path).mkdir(exist_ok=True)
            #ignore yamls without class structure
            if type(this_yaml) != list:
                for key,val in this_yaml.items():
                    #files in the objects subdir are all handled the same. context is stored
                    if not subdir.startswith('rules'):
                        context = gen_standard_doc(key,val,this_path,context)
                    #errors and rules are handled differently. no context is stored
                    else:
                        if 'errors' in this_path:
                            gen_error_doc(key,val,this_path,context)
                        else:
                            gen_rule_doc(key,val,this_path,context)
        return context
                
#handle conversion of rule doc 
def gen_rule_doc(key,val,path,context):
    print(context['files'])
    doc = snakemd.new_doc()
    doc.add_heading('[{key}]({loc} "{desc}")'.format(key=key,loc='/en/latest/Schema Reference/objects/files/{key}'.format(key=key),desc=context['files'][key]['description']))
    doc.add_raw('### Definition:')
    doc.add_paragraph(context['files'][key]['description'])
    doc.add_raw('### Properties:')
    doc.add_raw('\n'.join(['- [**{prop}**]({loc} "{desc}"): {value}'.format(prop=prop,loc=context['props'][prop]['loc'],desc=context['props'][prop]['description'],value=str(value)) for prop,value in val.items() if prop not in ['code','reason','level','selectors','helpUrl']]))
    #if there's a presence/absence error code, display info
    if 'code' in val:
        doc.add_paragraph('**If file/directory not found**:')
        doc.add_paragraph('[**code**](/en/latest/Schema Reference/meta/defs/code): {code}'.format(code=val['code']))
        doc.add_paragraph('[**level**](/en/latest/Schema Reference/meta/defs/level): {level}'.format(level=val['level']))
        doc.add_paragraph('[**reason**](/en/latest/Schema Reference/meta/defs/reason): {reason}'.format(reason=val['reason']))
    doc.dump(os.path.join(path,key))

#handle conversion of error doc
def gen_error_doc(key,val,path,context):
    doc = snakemd.new_doc()
    doc.add_heading(key)
    doc.add_paragraph('[**code**](/en/latest/Schema Reference/meta/defs/code): {code}'.format(code=val['code']))
    doc.add_paragraph('[**level**](/en/latest/Schema Reference/meta/defs/level): {level}'.format(level=val['level']))
    doc.add_paragraph('[**reason**](/en/latest/Schema Reference/meta/defs/reason): {reason}'.format(reason=val['reason']))
    doc.dump(os.path.join(path,key))

#handle conversion of object doc
def gen_standard_doc(key,val,path,context):
    doc = snakemd.new_doc()
    doc.add_heading(val['display_name'])
    if 'type' in val:
        doc.add_paragraph('Value type: {val_type}'.format(val_type=val['type']))
    if 'file_type' in val:
        context['files'][key] = {
            'loc':os.path.join('/en/latest/Schema Reference',path.split('./psychDS-docs')[1],'{key}'.format(key=key)),
            'description':val['description']
        }
        doc.add_paragraph('File type: {file_type}'.format(file_type=val['file_type']))
    doc.add_raw('Definition: {desc}'.format(desc=val['description']))
    doc.dump(os.path.join(path,key))
    return context

#process context yaml and also grab defs/locations for properties
def generate_context(this_yaml,context):
    pathlib.Path('./psychDS-docs/meta').mkdir(exist_ok=True)
    doc = snakemd.new_doc()
    
    doc.add_heading('Schema Context')
    p1 = doc.add_paragraph(
        this_yaml['context']['description']
    )
    doc.add_heading('Properties:')
    doc.add_unordered_list([
        "[{prop_name}](/en/latest/Schema Reference/meta/defs/{prop_name}): ({value_type}) {description}".format(prop_name=name,value_type=el['type'],description=el['description']) for name, el in this_yaml['context']['properties'].items()
    ])
    doc.dump(os.path.join(docs_dir,'meta/context'))
    pathlib.Path('./psychDS-docs/meta/defs').mkdir(exist_ok=True)

    for name,prop in (dict(sorted(this_yaml['context']['properties'].items()))).items():
        #collect info on props and store in context dic
        context['props'][name] = {
            'description':prop['description'],
            'loc':'/en/latest/Schema Reference/meta/defs/{name}'.format(name=name)
        }
        this_doc = snakemd.new_doc()

        this_doc.add_heading(name)

        p1 = this_doc.add_paragraph("Value type: {type}".format(type=prop['type']))

        p2 = this_doc.add_paragraph("Definition: {desc}".format(desc=prop['description']))

        if 'properties' in prop and name == 'keywords':
            this_doc.add_heading('Official keywords:')
            this_doc.add_unordered_list([
                "**{keyword}**: {description}".format(keyword=keyword,description=el['description']) for keyword,el in prop['properties'].items()
            ])
        
        this_doc.dump(os.path.join(docs_dir,'meta/defs/{name}'.format(name=name)))
    return context

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert version of schema model to markdown")
    parser.add_argument("version",nargs="?",default="latest",help="The version to convert.")
    args = parser.parse_args()

    schema_dir = 'schema_model/versions/{version}'.format(version=args.version)

    pathlib.Path('./psychDS-docs').mkdir(exist_ok=True)

    explore_dir(schema_dir)

import yaml

data = yaml.safe_load(open('nlu\\train.yml', 'r', encoding='utf-8').read())

#print (data)

for command in data['commands']:
    print(command)
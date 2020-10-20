from jinja2 import Environment, FileSystemLoader

def required_field(model, field, question = ''):
  value = ''
  if question:
    value = input('* ' + question + ': ')
  else:
    value = input('* ' + field.title() + ': ')

  if value:
    model[field] = value
  else:
    raise Exception('This field is required!')

def optional_field(model, field, question = ''):
  value = ''
  if question:
    value = input(question + ': ')
  else:
    value = input(field.title() + ': ')

  if value:
    model[field] = value

def get_model():
  print('Fields with a * are required.')
  model = {}

  required_field(model, 'name')
  optional_field(model, 'cr', 'CR')
  optional_field(model, 'gender')
  optional_field(model, 'race')
  optional_field(model, 'class', 'Class(es)')
  required_field(model, 'alignment')
  required_field(model, 'size')
  required_field(model, 'type')
  required_field(model, 'initiative')
  optional_field(model, 'senses')
  required_field(model, 'perception')

  return model

def main():
  model = get_model()

  env = Environment(loader=FileSystemLoader('templates'))
  template = env.get_template('statblock.jinja')
  stat_block = template.render(model)

  filename = model['name'].lower() + '.htm'
  with open(filename, 'w') as f:
    f.write(stat_block)
  print('Stat block ' + filename + ' created')

if __name__ == '__main__':
  main()

from jinja2 import Environment, FileSystemLoader

def required_field(field, model, question = ''):
  value = ''
  if question:
    value = input('* ' + question + ': ')
  else:
    value = input('* ' + field.title() + ': ')

  if value:
    model[field] = value
  else:
    raise Exception('This field is required!')

def optional_field(field, model, question = ''):
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

  required_field('name', model)
  optional_field('cr', model, 'CR')
  optional_field('gender', model)
  optional_field('race', model)
  optional_field('class', model, 'Class(es)')
  required_field('alignment', model)
  required_field('size', model)
  required_field('type', model)

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

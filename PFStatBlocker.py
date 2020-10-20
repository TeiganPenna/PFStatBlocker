from jinja2 import Environment, FileSystemLoader

def require_answer(question):
  answer = input('* ' + question)
  if answer:
    return answer
  raise 'This field is required!'

def get_model():
  print('Fields with a * are required.')
  model = {}
  model['name'] = require_answer('Name: ')

  cr = input('CR: ')
  if cr:
    model['cr'] = 'CR: ' + cr

  gender = input('Gender: ')
  if gender:
    model['gender'] = gender

  race = input('Race: ')
  if race:
    model['race'] = race

  classes = input('Class(es): ')
  if classes:
    model['class'] = classes

  model['alignment'] = require_answer('Alignment: ')
  model['size'] = require_answer('Size: ')
  model['type'] = require_answer('Type: ')

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

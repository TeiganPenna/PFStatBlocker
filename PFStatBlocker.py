from jinja2 import Environment, FileSystemLoader

def require_answer(question):
  answer = input('* ' + question)
  if answer:
    return answer
  raise 'This field is required!'

def get_model():
  model = {}
  model['name'] = require_answer('Name: ').upper()
  model['title'] = model['name'].title()
  cr = input('CR: ')
  if cr:
    model['cr'] = 'CR: ' + cr
  gender = require_answer('Gender: ').title()
  race = require_answer('Race: ').lower()
  classes = require_answer('Class(es): ').lower()
  model['gender_race_class'] = ' '.join([gender, race, classes])
  return model

def main():
  model = get_model()

  env = Environment(loader=FileSystemLoader('templates'))
  template = env.get_template('statblock.txt')
  stat_block = template.render(model)

  filename = model['name'].lower() + '.htm'
  with open(filename, 'w') as f:
    f.write(stat_block)
  print('Stat block ' + filename + ' created')

if __name__ == '__main__':
  main()

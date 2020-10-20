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

  # TODO allow italics, allow multiple attack lines

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
  optional_field(model, 'aura', 'Aura (Range, DC)')
  required_field(model, 'ac', 'AC')
  required_field(model, 'touch_ac', 'Touch AC')
  required_field(model, 'flatfooted_ac', 'Flat-footed AC')
  required_field(model, 'ac_breakdown', 'AC breakdown')
  required_field(model, 'hp', 'HP')
  required_field(model, 'hp_breakdown', 'HP breakdown')
  required_field(model, 'fort', 'Fort save')
  required_field(model, 'ref', 'Reflex save')
  required_field(model, 'will', 'Will save')
  optional_field(model, 'save_bonus', 'Additional save bonuses')
  optional_field(model, 'defensive_abilities', 'Defensive Abilities')
  optional_field(model, 'dr', 'DR')
  optional_field(model, 'immunities')
  optional_field(model, 'resistances')
  optional_field(model, 'sr', 'SR')
  optional_field(model, 'weaknesses')
  required_field(model, 'speed')
  optional_field(model, 'melee', 'Melee attack line')
  optional_field(model, 'ranged', 'Ranged attack line')
  required_field(model, 'space')
  required_field(model, 'reach')
  optional_field(model, 'special_attacks', 'Special attacks')

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

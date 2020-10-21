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
    return True
  return False

def get_ordinal_suffix(n):
  return str(n)+('th' if 4<=n%100<=20 else {1:'st',2:'nd',3:'rd'}.get(n%10, 'th'))

def get_spells(model, spell_type):
  optional_field(model, spell_type + '_0_spells', '0th level spells ' + spell_type)
  for level in range(1, 10):
    if not optional_field(model, spell_type + '_' + str(level) '_spells', get_ordinal_suffix(level) + ' level spells ' + spell_type)
      break
  

def get_model():
  print('Fields with a * are required.')
  model = {}

  # TODO allow italics, allow multiple attack lines, spells

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

  # defense
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

  # offense
  required_field(model, 'speed')
  optional_field(model, 'melee', 'Melee attack line')
  optional_field(model, 'ranged', 'Ranged attack line')
  required_field(model, 'space')
  required_field(model, 'reach')
  optional_field(model, 'special_attacks', 'Special attacks')
  if optional_field(model, 'domain'):
    required_field(model, 'domain_powers', 'Domain Powers')
  if optional_field(model, 'prepared_spell_class', 'Prepared Spell Casting Class')
    required_field(model, 'prepared_caster_level', 'Caster Level')
    required_field(model, 'prepared_concentration', 'Concentration')
    get_spells(model, 'prepared')

  # statistics and gear
  required_field(model, 'str', 'Strength')
  required_field(model, 'dex', 'Dexterity')
  required_field(model, 'con', 'Constitution')
  required_field(model, 'int', 'Intelligence')
  required_field(model, 'wis', 'Wisdom')
  required_field(model, 'cha', 'Charisma')
  required_field(model, 'bab', 'Base Attack')
  required_field(model, 'cmb', 'CMB')
  required_field(model, 'cmd', 'CMD')
  optional_field(model, 'feats')
  optional_field(model, 'skills')
  optional_field(model, 'languages')
  optional_field(model, 'sq', 'Special Qualities')
  optional_field(model, 'combat_gear', 'Combat Gear')
  optional_field(model, 'other_gear', 'Other Gear')

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

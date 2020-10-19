from jinja2 import Environment, FileSystemLoader

def get_template():
  with open('template.txt') as f:
    return Template(f.read())

def main():
  env = Environment(loader=FileSystemLoader('templates'))
  template = env.get_template('statblock.txt')
  stat_block = template.render()
  with open('kanjougas.htm', 'w') as f:
    f.write(stat_block)
  print('Stat block kanjougas.htm created')

if __name__ == '__main__':
  main()

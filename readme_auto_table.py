import re

vars_file = "vars\main.yml"
readme_file = "README.md"

with open(vars_file, "r", encoding='utf-8') as f:
	vars_txt = f.read()

regex_table = '## Actions\n(.+)\n##' # single line flag
regex_vars = '# Setting syntax\s+: (?P<syntax>.+)\n# Description\s+: (?P<desc>.+)\n# Apache default\s+: (?P<apache>.+)\n(?P<armor_name>.+): (?P<armor_value>.+)'

match = re.finditer(regex_vars, vars_txt)
if match:
	for m in match:
		print("{} | {} | {} | {} | {}".format(m.group("syntax"), m.group("desc"), m.group("apache"), m.group("armor_name"), m.group("armor_value")))

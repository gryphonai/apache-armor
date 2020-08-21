import re

vars_file = "vars\main.yml"
readme_file = "README.md"


regex_table = '## Actions\n(.+)\n##' # single line flag
regex_vars = '# Setting syntax\s+: (?P<syntax>.+)\n# Description\s+: (?P<desc>.+)\n# Apache default\s+: (?P<apache>.+)\n(?P<armor>.+): (?P<armor_value>.+)'

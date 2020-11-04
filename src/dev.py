from jinja2 import Environment, Template
from jinja2 import nodes

from jinja2.lexer import describe_token, get_lexer
from jinja2.lexer import describe_token_expr

from jinja2.parser import Parser

from jinja2.tatsu import tatsu_tokenize

import pprint

SOURCE = (
    "{% if kvs %}" 
    "  {% for k, v in kvs %}{{ k }}={{ v }} {% endfor %}"
    "{% endif %}"
    "{% if text %}"
    "  <div>Yes</div>"
    "{% else%}"
    "  <p>No</p>\n"
    "  <p>AND \nNo</p>"
    "{% endif %}"
)


# environment setup
env = Environment(lstrip_blocks=True, trim_blocks=True)

# example output of jinja package
# tmpl = env.from_string(SOURCE)
# out = tmpl.render(kvs=[("a", 1), ("b", 2)])
# print (out)

# example output of jinja lexer
# lexer = get_lexer(env)
# generator = lexer.tokeniter(SOURCE, "test")
# for g in generator:
#     print (g)

# tatsu output
generator = tatsu_tokenize(SOURCE)
# print (next(generator))
for g in generator:
    print (g)






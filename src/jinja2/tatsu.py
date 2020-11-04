from tatsu import parse

import pprint


GRAMMAR = '''
    @@grammar::CALC

    @@whitespace:://


    start = {expression}+ ;


    expression
        =
        | code
        | variable
        | data:/./
        ;

    code
        = block_begin:'{%' { whitespace:' ' | name:/\w+/ | operator:operator }+ block_end:'%}' ;

    operator
        =
        | '+' | '-' | '/' | '//' | '*' | '**' | '~'
        | '[' | ']' | '(' | ')' | '{' | '}'
        | '==' | '!=' | '>' | '>=' | '<' | '<=' | '='
        | '.' | ':' | '|' | ',' | ';'
        ; 

    variable = variable_begin:'{{' /[\ \w]+/ variable_end:'}}' ;
'''

def tatsu_tokenize(source):
    p = parse(GRAMMAR, source)
    for item in p:
        yield item

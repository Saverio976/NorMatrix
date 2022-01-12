LIBC_BANNED_FUNC = [
        'printf',
        'memset',
        'strcpy',
        'strcat',
        'calloc'
]

BAD_FILE_EXTENSION = [
        '.a',
        '.o',
        '.so',
        '.gch',
        '~',
        '#',
        '.d'
]

smart_match = {
        ':ALL:': '.',
        ':NOTHING:': '{0}',
        ':ALPHANUM:': '[0-9a-zA-Z]',
        ':NUM:': '[0-9]',
        ':ALPHA:': '[a-zA-Z]',
        ':NOSPACE:': '\S'
}

OPERATOR_LIST = [
        (' ([+',    '+',    '+])= '),
        (' ([-',    '-',    '-])=> '),
        (' ([/*',   '*',    ':NOTHING:',    '[\[\{\( ]\*{2,}'),
        (' (/*',    '/',    '*/= ',         '<\w+?\/\w+?\.h>'),
        ('< ',      '<',    ':ALL:'),
        (':ALL:',   '>',    ' >='),
        (' ',       '&',    ':ALL:'),
        ('([ ',     '!',    ':ALL:'),
        ('/+*-=! ', '=',    '= '),
        (':ALL:',   '(',    ':ALL:'),
        (':ALL:',   ')',    '}]) ;')
]

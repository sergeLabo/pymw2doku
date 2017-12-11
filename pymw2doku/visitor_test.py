#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from visitor import Visitor


class JSONEncoder(Visitor):
    def __init__(self):
        self.indent = 0

    def escape_str(self, s):
        # note: this is not a good escape function, do not use this in
        # production!
        s = s.replace('\\', '\\\\')
        s = s.replace('"', '\\"')
        return '"' + s + '"'

    def visit_list(self, node):
        self.indent += 1
        s = '[\n' + '  ' * self.indent
        s += (',\n' + '  ' * self.indent).join(self.visit(item)
                                               for item in node)
        self.indent -= 1
        s += '\n' + '  ' * self.indent + ']'
        return s

    def visit_str(self, node):
        return self.escape_str(node)

    def visit_int(self, node):
        return str(node)

    def visit_bool(self, node):
        return 'true' if node else 'false'

    def visit_dict(self, node):
        self.indent += 1
        s = '{\n' + '  ' * self.indent
        s += (',\n' + '  ' * self.indent).join(
            '{}: {}'.format(self.escape_str(key), self.visit(value))
            for key, value in sorted(node.items())
        )
        self.indent -= 1
        s += '\n' + '  ' * self.indent + '}'
        return s


data = [
    'List', 'of', 42, 'items', True, {
        'sub1': 'some string',
        'sub2': {
            'sub2sub1': False,
            'sub2sub2': 123,
        }
    }
]

print(JSONEncoder().visit(data))

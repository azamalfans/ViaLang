
from Object.varObject import VariableObject

class penguraian_parser(object):

    def __init__(self, tokens):

        self.tokens = tokens

        self.token_index = 0

        self.transpiled_code = ""

    def diuraikan_parse(self):

        while self.token_index < len(self.tokens):

            token_type = self.tokens[self.token_index][0]

            token_value = self.tokens[self.token_index][1]

            if token_type == "VAR_DECLARATION" and token_value in ("via", "vv", "var", "wow", "valen", "vr"):
                self.diuraikan_parse_variable_declaration(self.tokens[self.token_index : len(self.tokens)])

            self.token_index += 1

        print(self.transpiled_code)

    def diuraikan_parse_variable_declaration(self, token_stream):
            token_checked = 0

            name     = ""
            operator = ""
            value    = ""

            for token in range(0, len(token_stream)):

                token_type = token_stream[token_checked][0]
                token_value = token_stream[token_checked][1]

                if token == 4 and token_type == "STATEMENT_END": break

                elif token == 1 and token_type == "IDENTIFIER":
                    name = token_value
                elif token == 1 and token_type != "IDENTIFIER":
                    print("ERROR : nama variabel tidak valid '" + token_value +"'" )
                    quit()

                elif token == 2 and token_type == "OPERATOR":
                    operator = token_value
                elif token == 2 and token_type != "OPERATOR":
                    print("ERROR : Operator Penugasan hilang atau tidak valid maka tambahkan '='")
                    quit()

                elif token == 3 and token_type in['STRING', 'INTEGER', 'IDENTIFIER']:
                    value = token_value
                elif token == 3 and token_type not in ['STRING','INTEGER', 'IDENTIFIER']:
                    print("nama variabel tidak valid'" + token_value + "'")
                    quit()

                token_checked += 1
            varObj = VariableObject()
            self.transpiled_code += varObj.transpile(name, operator, value)

            #Menambah token index
            self.token_index += token_checked
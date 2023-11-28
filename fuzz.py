'''
Cady Pridgeon
November 27, 2023
Fuzz testing for some functions in parser.py
'''

import project.KubeSec-master.parser as parser

def fuzzValues():
    input_list = ['test', 1, {2,3}, (4,5)]
    for input in input_list:
        try:
            parser.checkIfValidHelm(input)
        except Exception as e:
            print(f'Input for checkIfValidHelm was invalid.\n Error: {e}\n')
        try:
            parser.checkIfValidK8SYaml(input)
        except Exception as e:
            print(f'Input for checkIfValidK8SYaml was invalid.\n Error: {e}\n')
        try:
            parser.checkIfWeirdYAML(input)
        except Exception as e:
            print(f'Input for checkIfWeirdYAML was invalid.\n Error: {e}\n')
        try:
            parser.checkParseError(input)
        except Exception as e:
            print(f'Input for checkParseError was invalid.\n Error: {e}\n')
        try:
            parser.count_initial_comment_line(input)
        except Exception as e:
            print(f'Input for count_initial_comment_line was invalid.\n Error: {e}\n')
    



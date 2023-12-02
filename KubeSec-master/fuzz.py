'''
Cady Pridgeon
November 27, 2023
Fuzz testing for some functions in parser.py
'''

import parser

def fuzzValues():
    with open('fuzzValues.txt', 'w') as f:
        input_list = [1]
        for input in input_list:
            flag = False
            # print(f'Input: {input}\n')
            
            try:
                parser.checkIfValidHelm(input)
            except Exception as e:
                print(f'Input for checkIfValidHelm was invalid.\n Error: {e}\n')
                f.write(f'Input for checkIfValidHelm was invalid.\n Error: {e}\n')
                flag = True
            try:
                parser.readYAMLAsStr(input)
            except Exception as e:
                print(f'Input for checkIfValidK8SYaml was invalid.\n Error: {e}\n')
                f.write(f'Input for checkIfValidK8SYaml was invalid.\n Error: {e}\n')
                flag = True
            try:
                parser.checkIfWeirdYAML(input)
            except Exception as e:
                print(f'Input for checkIfWeirdYAML was invalid.\n Error: {e}\n')
                f.write(f'Input for checkIfWeirdYAML was invalid.\n Error: {e}\n')
                flag = True
            # try:
            #     parser.checkParseError(input)
            # except Exception as e:
            #     print(f'Input for checkParseError was invalid.\n Error: {e}\n')
            #     flag = True
            # try:
            #     parser.count_initial_comment_line(input)
            # except Exception as e:
            #     print(f'Input for count_initial_comment_line was invalid.\n Error: {e}\n')
            #     flag = True
            # if not flag:
            #     print(f'Input {input} was valid for all functions.\n')

if __name__ == '__main__':
    fuzzValues()
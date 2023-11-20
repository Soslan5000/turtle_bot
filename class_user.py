class User:
    def __init__(self, chat_id):
        self.chat_id = chat_id
        self.orientation = None
        self.commands_list = []
        self.num_index = 0
        self.commands_list_index = -1
        self.in_cicle = False
        self.in_hands_branch = False
        self.in_btns_branch = False
        self.msg_id = 0

    def build_instruction_string(self):
        instruction_string = ''
        for el in self.commands_list:
            if el == '[':
                instruction_string += el
            elif el == ']':
                instruction_string = instruction_string[::-1]
                instruction_string += el
            else:
                instruction_string += str(el)
        return instruction_string

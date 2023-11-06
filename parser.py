import sys
import argparse
import openai
import copy

messages = [
    { "role": "system", "content": "You are helpful arguments analyst" }
]

one_line_help = "use gpt to get parameter one-line suggestions for executing commands, you need input question."

help = "use gpt to get parameter suggestions for executing commands, you need input question."

one_line_prompt_template = """
You are a command parameter analyst.
You need to find parameters that are close to my problem based on the usage and help text provided.
You must recommend what parameters I should choose.
The parameters you choose should be in usage.
You just need to tell me one line of command.


context
---------------
help:
{help}

---------------

Question: {question}

one line command:
"""

prompt_template = """
You are a command parameter analyst.
You'll need to find suggestions that are close to my problem based on the usage and help text provided about the command in context.
You have to suggest which parameters I should choose.


context
---------------
help:
{help}

---------------

Question: {question}

suggestion:
"""

one_line_suggest_template = "One Line Suggest: \n{answer}\n"

question_suggest_template = "Question Suggestion: \n{answer}\n"


def context_help(help: str):
    context = ""
    for line in help.split('\n'):
        if line.startswith('  -s SUGGESTION'):
            continue
        if line.startswith('  -a AI'):
            continue

        context += line + '\n'
    return context


class AIArgumentParser(argparse.ArgumentParser):

    def __init__(self, model_name: str = "gpt-3.5-turbo",  **argument_kwargs):
        self.model_name = model_name
        super(AIArgumentParser, self).__init__(**argument_kwargs)

        self.add_argument("-a", "--ai", type=str, help=help)
        self.add_argument("-s", "--suggestion", type=str, help=help)

    def format_context(self):
        prev_action_groups = copy.deepcopy(self._action_groups)
        for group in self._action_groups:
            group._group_actions = [a for a in group._group_actions if a.dest not in ('ai', 'suggestion')]

        help_text = self.format_help()
        self._action_groups= prev_action_groups
        return help_text

    def suggestion_question(self, query: str = "", one_line: bool = True):
        if not query:
            return 
        
        prompt_tpl = one_line_prompt_template if one_line else prompt_template

        prompt = prompt_tpl.format(
            usage=self.format_usage(),
            help=context_help(self.format_context()),
            question=query
        )
        
        messages.append({"role": "user", "content": prompt})

        chat = openai.ChatCompletion.create( 
            model=self.model_name, messages=messages 
        )

        return chat.choices[0].message.content
    
    def parse_known_args(self, args=None, namespace=None):
        args, argv = super(AIArgumentParser, self).parse_known_args(args, namespace)
        
        query, one_line = (args.ai, True) if args.ai else (args.suggestion, False)
        if query:
            answer = self.suggestion_question(query, one_line)
            suggest_tpl = one_line_suggest_template if one_line else question_suggest_template
            self._print_message(suggest_tpl.format(answer=answer), sys.stdout)

        return args, argv

if __name__ == '__main__':
    parser = AIArgumentParser()

    parser.add_argument('-l', help="show file with list")

    args = parser.parse_args()

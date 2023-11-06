# ai-arg
argparse ai


# Quickstart


```
from ai_arg import AIArgumentParser()

parser = AIArgumentParser()
parser.add_argument('-l', help="show file with list")
```


```
$ python xxx.py -a "list files long format"
One Line Suggest: 
ls -l



$ python xxx.py -a "把目录列为普通文件"
One Line Suggest: 
ls -d

$ python xxx.py -s "list files long format"
Question Suggestion: 
Based on the provided context, you can use the following parameters to list files in long format:
- `-l` or `--l`: This parameter will list files in the long format.
Example: `ls -l`

You can also combine multiple parameters if needed. For example, if you want to list directories as plain files and display them in long format, you can use:
`ls -l -d` or `ls --l --d`

Remember, these suggestions are based on the given context, and there might be other parameters available for the `ls` command depending on the specific implementation.
```

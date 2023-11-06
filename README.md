# ai-arg
argparse ai


# Quickstart


```python
parser = AIArgumentParser(
    prog="ls",
    description="""For each operand that names a file of a type other than directory, ls displays its name as well as any requested, associated information.  For each operand that names a file of type directory, ls
 displays the names of files contained within that directory, as well as any requested, associated information.
 If no operands are given, the contents of the current directory are displayed.  If more than one operand is given, non-directory operands are displayed first; directory and non-directory operands are
 sorted separately and in lexicographical order.""",
    epilog="list directory contents",
)

parser.add_argument('-d', help="Directories are listed as plain files (not searched recursively).")
parser.add_argument('-l', help="(The lowercase letter “ell”.) List files in the long format, as described in the The Long Format subsection below.")
args = parser.parse_args()
```


```python
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

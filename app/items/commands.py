import markdown

def getCommands():
    with open('bin/files/commands.md', 'r') as f:
        return markdown.markdown(f.read())

import subprocess as sub

def fetch(wish):
    p = sub.Popen('remind', stdin = sub.PIPE, \
                        stdout = sub.PIPE, stderr = sub.PIPE)
    output, errors = p.communicate(input = wish)
    return output

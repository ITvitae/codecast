"""Run command cmd yielding output"""


from subprocess import Popen, PIPE  # , CalledProcessError


def run_command(runner, source, history, format_output=False):
    """Run command cmd yielding output"""

    config = {
        '_default': {'arguments': []},
        'lua': {
            'arguments': ['-e']
        },
        'python': {
            'arguments': ['-u', '-c']
        },
        'shell': {
            'arguments': ['-c']
        },
    }

    lang = '_default'

    if runner.startswith('/'):
        lang = runner.split('/')[-1]
    elif runner.startswith('./'):
        lang = runner.split('./', 1)[1].split('/')[-1]
    else:
        lang = runner

    if lang in ('python', 'python3'):
        lang = 'python'
    elif lang in ('sh', 'bash', 'zsh'):
        lang = 'shell'

    if lang == 'shell':  # Might turn out to be required for all?
        source = source.replace("U+000A", '')  # Get rid of ^M?
        source = source.replace("\r\n", ';')  # Replace \r\n with ;
        source = source.replace("\\n", '\n')  # Remove escaping on \n

    command = [runner] + config[lang]['arguments'] + [source]

    try:
        with Popen(
                command,
                stdout=PIPE,
                stderr=PIPE,
                universal_newlines=True
        ) as process:
            for line in process.stdout:
                if format_output:
                    line = f'<div class="stdout">{line}</div>'
                history.append(line)
                yield line
            for line in process.stderr:
                if format_output:
                    line = f'<div class="stderr">{line}</div>'
                history.append(line)
                yield line

        # if process.returncode != 0:
            # raise CalledProcessError(process.returncode, process.args)
    except FileNotFoundError as _e:
        yield f'Error! File Not Found: {_e}'

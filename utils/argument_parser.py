"""
Argument parser for starting the app
"""


from argparse import ArgumentParser

defaults = {
    'port': 5001,
    'debug': False,
    'format_output': False,
    'hide_env_data': False,
}

Parser = ArgumentParser()
Parser.add_argument(
    '-p',
    '--port',
    help='Port the server should listen on.',
    type=int,
    default=defaults['port']
)

Parser.add_argument(
    '-d',
    '--debug',
    help='Run the server in debug mode.',
    action='store_true',
    default=defaults['debug']
)

Parser.add_argument(
    '-f',
    '--format_output',
    help='Apply HTML formatting to stdout and stderr.',
    action='store_true',
    default=defaults['format_output']
)

Parser.add_argument(
    '-H',
    '--hide_env_data',
    help='Do not add USER@HOST in top bar.',
    action='store_true',
    default=defaults['hide_env_data']
)

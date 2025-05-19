"""
Codecast: code caster
"""

from getpass import getuser
from platform import uname

from flask_server import app
from utils.argument_parser import Parser
from utils.generate_start_screen import generate_start_screen
from utils.test_runners import test_runners


def main():
    """Default debug mode"""

    args = Parser.parse_args()

    if args.format_output:
        print(' * Format output: on')
    else:
        print(' * Format output: off')

    app.env_data = 'code🖥cast'
    if not args.hide_env_data:
        app.env_data = f'{getuser()}@{uname().node} - code🖥cast'

    app.program_settings['format_output'] = args.format_output

    app.runners = test_runners()

    app.start_screen = generate_start_screen(
        app.env_data,
        app.runners,
        app.program_settings,
    )

    app.run(
        port=args.port,
        debug=args.debug,
    )


if __name__ == "__main__":
    main()

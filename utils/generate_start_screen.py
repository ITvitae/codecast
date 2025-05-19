"""Return codecast startscreen as html"""


def generate_start_screen(env_data, runners ,program_settings):
    """Return codecast startscreen as html"""

    _settings = ''
    for setting in program_settings:
        _settings = f'{_settings}\n<code class=console_data>'
        _settings = f'{_settings}\n{setting}: {program_settings[setting]}'
        _settings = f'{_settings}\n</code>'

    _runners = ''
    for runner in runners:
        _runners = f'{_runners}\n<code class=console_data>'
        if runners[runner]:
            _runners = f'{_runners}<div class="runner_enabled">'
            _runners = f'{_runners}\n{runner}'
            _runners = f'{_runners}</div>'
        else:
            _runners = f'{_runners}<div class="runner_disabled">'
            _runners = f'{_runners}\n{runner}'
            _runners = f'{_runners}</div>'
        _runners = f'{_runners}\n</code>'

    start_screen = [
        '<div id="title_background">',
        '<p id="title">',
        'code🖥cast',
        '</p>',
        '<a href="https://itvitae.nl" id="logo_link">',
        '<img src="static/images/itvitae.png" ',
        'alt="ITvitae" id="itvitae_logo">',
        '</a>',
        '<br>',
        '<div id="console">'
        f'<code class="console_data">{env_data}</code>',
        '<code class="console_data"></code>',
        '<code class="console_data">[CONFIG]</code>',
        _settings,
        '<code class="console_data"></code>',
        '<code class="console_data">[RUNNERS]</code>',
        _runners,
        '</div>',
        '<div id="console_menu">',
        '<button ',
        'class="console_button"',
        'id="console_button" onclick="toggle_console()" ',
        'title="Toggle console">',
        '⎚',
        '</button>',
        '</div>',
        '</div>',
    ]

    return start_screen

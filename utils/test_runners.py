"""
Test for available runners
Return runner information as a dictionary
"""


from subprocess import run, DEVNULL


def test_runners():
    """
    Test for available runners
    Return runner information as a dictionary
    """

    runners = {}

    langs = get_langs()
    langs = langs + get_others()

    langs = sorted(langs)

    for lang in langs:
        state = False

        # Other (non language) stuff goes here
        if lang == 'html':
            runners.update({lang: True})
            continue

        # Test for languages
        _p = run(
            [
                'which',
                lang,
            ],
            check=False,
            stdout=DEVNULL,
        )
        if _p.returncode == 0:
            state = True
        runners.update({lang: state})

    return runners


def get_langs():
    """Return a list of supported programming languages"""

    return [
        'bash',
        'lua',
        'python',
        'python3',
        'sh',
        'zsh',
    ]


def get_others():
    """Return a list of other supported data structures"""

    return [
        'html',
    ]

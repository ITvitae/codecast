"""
Flask based server
"""


from flask import Flask, request

from utils.run_command import run_command
from utils.stream_template import _stream_template


app = Flask(
    __name__,
    static_folder='web/static',
    template_folder='web/templates',
)
app.program_settings = {
    'format_output': False,
}
app.runners = []
app.env_data = []
app.start_screen = []
app.history = []


@app.route('/', methods=['GET', 'POST'])
@app.route('/<main_font_size>', methods=['GET', 'POST'])
def index(main_font_size=1):
    """Root"""
    runner = ''
    source = ''
    html = False
    left_window_width = '50vw'

    if request.method == 'POST':
        runner = request.form['runner']
        source = request.form['source']
        left_window_width = request.form['left_window_width']

    if not left_window_width:
        left_window_width = '50vw'

    if not runner:
        rows = []
    elif not source:
        rows = []
    elif runner == 'html':
        rows = source.split('\n')
        html = True
    elif runner == '--history--':
        rows = (y for y in app.history)
    else:
        rows = run_command(
            runner,
            source,
            app.history,
            format_output=app.program_settings['format_output']
        )

    if rows == []:
        rows = app.start_screen
        html = True

    return app.response_class(_stream_template(
        app,
        'index.html',
        left_window_width=left_window_width,
        format_output=app.program_settings['format_output'],
        main_font_size=main_font_size,
        rows=rows,
        html=html,
        runners=app.runners,
        env_data=app.env_data,
    ))

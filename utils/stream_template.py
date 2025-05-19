"""
Flask extension
See: https://flask.palletsprojects.com/en/2.1.x/patterns/streaming/
"""


def _stream_template(app, template_name, **context):
    """
    Flask extension
    See: https://flask.palletsprojects.com/en/2.1.x/patterns/streaming/
    """
    app.update_template_context(context)
    template = app.jinja_env.get_template(template_name)
    ret = template.stream(context)
    # rv.enable_buffering(5)
    return ret

from app import create_app
import datetime

app = create_app()


@app.template_filter("datetime")
def format_datetime(value, from_format, to_format):
    return datetime.datetime.strptime(value, from_format).strftime(to_format)
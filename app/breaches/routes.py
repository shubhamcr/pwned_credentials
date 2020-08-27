from . import breaches_bp
from flask import render_template
from .services import breached_websites_service
import datetime


@breaches_bp.route("/breachedWebsites", methods=["GET"])
def breached_websites():
    json_response = breached_websites_service.breached_websites()
    return render_template("breached_websites.html", breached_websites=json_response)
from flask import Blueprint, request, render_template

zillow_routes = Blueprint("zillow_routes", __name__)

@zillow_routes.route("/zillow/form")

def zillow_form():
    print("ZILLOW FORM")
    return render_template( "zillow_form.html")

@zillow_routes.route("/zillow/getdata", methods=["POST", "GET"])

def get_zillow_data():
    request_data = dict(request.form)
    print("FORM DATA:", request_data)
    return request_data
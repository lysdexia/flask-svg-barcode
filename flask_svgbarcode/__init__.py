import barcode
from flask.ext import restful
from flask_restful import reqparse, abort

try:
    from flask import _app_ctx_stack as stack
except ImportError:
    from flask import _request_ctx_stack as stack

def svg_barcode(app, endpoint):
    """
    flask extension providing tissue thin wrapper around pybarcode
    You can find pyBarcode with it's nice licenses and documentation at
        http://pythonhosted.org/pyBarcode/
    You'll be glad you did.
    
    accepts
        app <object> for circular import of curcularity
        endpoint <str> api endpoint for post call ex. "/api/barcode"

    Usage:
        from flask_svg_barcode import svg_barcode
        app=Flask(__name__)
        # initialize with endpoint
        svg_barcode(app, "/api/barcode")

    XML string is returned in json object.
    If you don't like this, feel free to fork it, add an
    @api.representation('application/xml') decorator to the post and convert
    the error messages to xml or whatever turns you on. I'm groovy like that.
    """

    api = restful.Api(app)

    class SVGBarcodeAPI(restful.Resource):

        def barcode_svg(self, barcode_format, barcode_string):
            """
            accepts
                barcode_format <str> one of ['code39', 'ean', 'ean13', 'ean8', 'gs1', 'gtin', 'isbn', 'isbn10', 'isbn13', 'issn', 'jan', 'pzn', 'upc', 'upca']
                barcode_string <str> string constructed according to barcode_format requirements - see google, svp
            """
            try:
                barcode_svg = barcode.get(
                        barcode_format,
                        barcode_string).render(writer_options=None)
            except Exception as error:
                return {
                        "error": 500,
                        "message": str(error)
                        }
            return {"barcode_svg": barcode_svg} 

        def post(self):
            """
            accept
                JSON object {barcode_format: <str>, barcode_string: <str>}
            return
                JSON object {"barcode_svg": <XML svg barcode in format specified in "barcode_string> } 
            on error return
                JSON object {"error": <numeric error code>, "message": <str>}
            """

            parser = reqparse.RequestParser(bundle_errors=True)

            parser.add_argument(
                    "barcode_format",
                    type=str,
                    help="barcode formats supported: %s"%str(
                        barcode.PROVIDED_BARCODES),
                    required=True
                    )

            parser.add_argument(
                    "barcode_string",
                    type=str,
                    help="string to render",
                    required=True
                    )

            args = parser.parse_args()

            data = self.barcode_svg(
                    args["barcode_format"],
                    args["barcode_string"],
                    )
            if "error" in data:
                return data, data["error"]
            return data, 200

    api.add_resource(SVGBarcodeAPI, endpoint)

class SVGBarcode(object):

    def __init__(self, app=None, endpoint=None):
        self.app = app
        if app is not None:
            self.init_app(app, endpoint)

    def init_app(self, app, endpoint):
        if not endpoint:
            endpoint = "/api/barcode"

        if hasattr(app, "teardown_appcontext"):
            app.teardown_appcontext(self.teardown)
        else:
            app.teardown_request(self.teardown)

        svg_barcode(app, endpoint)

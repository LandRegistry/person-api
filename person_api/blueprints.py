# Import every blueprint file
from person_api.views import general
from person_api.views.v1_0 import people as people_v1_0


def register_blueprints(app):
    """Adds all blueprint objects into the app."""
    app.register_blueprint(general.general)
    app.register_blueprint(people_v1_0.people, url_prefix='/v1/people')

    # All done!
    app.logger.info("Blueprints registered")

from flask import Blueprint, abort
from person_api.app import app

import json
import os

people = Blueprint('people', __name__)

data_dir = app.root_path + "/data"


@people.route("/<person_id>", methods=['GET'])
def get_person_details(person_id):
    if os.path.exists("{}/{}.json".format(data_dir, person_id)):
        with open("{}/{}.json".format(data_dir, person_id)) as f:
            person_data = f.read()
        f.closed

        result = json.loads(person_data)

        return json.dumps(result, sort_keys=True, separators=(',', ':')), 200, {"Content-Type": "application/json"}
    else:
        abort(404)

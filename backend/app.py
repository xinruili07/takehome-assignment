from typing import Tuple

from flask import Flask, jsonify, request, Response
import mockdb.mockdb_interface as db

app = Flask(__name__)


def create_response(
    data: dict = None, status: int = 200, message: str = ""
) -> Tuple[Response, int]:
    """Wraps response in a consistent format throughout the API.
    
    Format inspired by https://medium.com/@shazow/how-i-design-json-api-responses-71900f00f2db
    Modifications included:
    - make success a boolean since there's only 2 values
    - make message a single string since we will only use one message per response
    IMPORTANT: data must be a dictionary where:
    - the key is the name of the type of data
    - the value is the data itself

    :param data <str> optional data
    :param status <int> optional status code, defaults to 200
    :param message <str> optional message
    :returns tuple of Flask Response and int, which is what flask expects for a response
    """
    if type(data) is not dict and data is not None:
        raise TypeError("Data should be a dictionary 😞")

    response = {
        "code": status,
        "success": 200 <= status < 300,
        "message": message,
        "result": data,
    }
    return jsonify(response), status


"""
~~~~~~~~~~~~ API ~~~~~~~~~~~~
"""


@app.route("/")
def hello_world():
    return create_response({"content": "hello world!"})


@app.route("/mirror/<name>")
def mirror(name):
    data = {"name": name}
    return create_response(data)

@app.route("/shows/<id>", methods=['DELETE'])
def delete_show(id):
    if db.getById('shows', int(id)) is None:
        return create_response(status=404, message="No show with this id exists")
    db.deleteById('shows', int(id))
    return create_response(message="Show deleted")

# TODO: Implement the rest of the API here!
#Part 2
@app.route("/shows/<id>", methods=['GET'])
def get_show_by_id(id):
    # if the show with the provided id does not exist
    if db.getById('shows', int(id)) is None:
        return create_response(status=404, message="No show with this id exists!")
    return create_response({"shows": db.getById("shows", int(id))})

#Part 3
@app.route("/shows", methods=['POST'])
def add_show():
    # obtain the request.json file from the POST method
    data = request.json
    name = data.get('name', '')
    episodes_seen = data.get('episodes_seen', '')

    # if the name or the number of episodes seen is not provided
    if "name" not in data or name == None:
        return create_response(status=422, message="The name of the show is not provided.")
    if "episodes_seen" not in data or episodes_seen == None:
        return create_response(status=422, message="The number of episodes seen is not provided.")
    #create the show with the required informations
    added_show = db.create("shows", data)
    return create_response(data = added_show, status=201, message="Show added!")
#Part 4
@app.route("/shows/<id>", methods=['PUT'])
def update_show(id):
    # if the show with the provided id does not exist
    if db.getById("shows", int(id)) is None:
        return create_response(status=404, message="No show with this id exists!")
    
    show = db.getById("shows", int(id))
    # received request.json file
    data = request.json
    # obtain the updated name and episodes_seen
    name = data.get("name", "")
    episodes_seen = data.get("episodes_seen", "")
    #update the values from the corresponding show in our database
    show["name"] = name
    show["episodes_seen"] = episodes_seen
    return create_response(data=show, status=201, message="Show updated!")

#Part 6
@app.route("/shows", methods=['GET'])
def return_shows_with_min_episodes():
    # obtain the query argument
    minEpisodes_string = request.args.get("minEpisodes")
    # if no query argument is provided, return all shows
    if minEpisodes_string == None:
        return create_response({"shows": db.get('shows')})
    # convert the string to an integer
    minEpisodes_int = int(minEpisodes_string)
    shows = db.get("shows")

    #initialize an empty list and add relevant shows
    relevant_shows = []
    for show in shows:
        if show["episodes_seen"] >= minEpisodes_int:
            relevant_shows.append(show)
    return create_response(data={"shows": relevant_shows}, message="Shows with more than {} episode(s) seen found!".format(minEpisodes_int))

"""
~~~~~~~~~~~~ END API ~~~~~~~~~~~~
"""
if __name__ == "__main__":
    app.run(port=8080, debug=True)

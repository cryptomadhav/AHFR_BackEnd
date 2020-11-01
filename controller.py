from flask import Flask, jsonify, request
# initialize our Flask application
app= Flask("__name__")
@app.route("/", methods=["GET"])
def message():
    posted_data = request.get_json()
    name = posted_data['name']
    return jsonify(" Hope you are having a good time " +  name + "!!!")
#  main thread of execution to start the server
if __name__=='__main__':
    app.run(debug=True)
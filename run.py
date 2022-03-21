import os  # in order to utilize enviroment vars
from taskmanager import app


# telling our app how/where to run the application
if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP"),
        port=int(os.environ.get("PORT")),
        debug=os.environ.get("DEBUG")
    )

from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
app.app_context().push()
CORS(app)

from routes import usersapi
#db = DB()
#ya = db.users

#user1 = User("abc", "dfg@gmail.com", "admin")
#user2 = User("hij", "klm@gmail.com", "user")

#ya.insert_many([user1.__dict__, user2.__dict__])


if __name__ == "__main__":
    app.run(debug=True)
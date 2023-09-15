Collection Tracker
This program uses Python and a PostgreSQL database to store information on users, their collections and items within those collections.

USERS
Method
Create/POST
URL Input(s): none JSON Input(s): username - req (>3 char), password - req (>8 char), email - opt
Outputs: JSON with id, username, email upon successful creation of new user

Show/GET
URL Input(s): none JSON Input(s): none
Outputs: JSON with id, username, password, email of all users

Index/GET
URL Input(s): id - req JSON Input(s): none
Outputs: JSON with username, email of user matching id

Update/PATCH
URL Input(s): id - req JSON Input(s): username - req, password - req, email - opt
Outputs: JSON True if update was successful, False if update unsuccessful

Delete/DELETE
URL Input(s): id - req JSON Input(s): none
Outputs: JSON True if deletion was successful, False if deletion unsuccessful

COLLECTIONS
Method
Create/POST
URL Input(s): u_id JSON Input(s): collection_name - req
Outputs: JSON username, collection_id, collection_name, user_id

Show/GET
URL Input(s): none JSON Input(s): none
Outputs: JSON username, collection_id, collection_name, user_id for all collections

Index/GET
URL Input(s): id - req JSON Input(s): none
Outputs: JSON username, collection_id, collection_name for collections with id = user_id

Update/PATCH
URL Input(s): id - req JSON Input(s): username - req, password - req, email - opt
Outputs: JSON username, collection_id, collection_name, user_id

Delete/DELETE
URL Input(s): id - req JSON Input(s): none
Outputs: JSON True if deletion was successful, False if deletion unsuccessful

ITEMS
Method
Create/POST
URL Input(s): u_id - req, c_id - req
JSON Input(s): category - req, title - req, rank - req, format - opt, genre - opt, platform - opt, author - opt, max_players - opt
Outputs: JSON username, collection_name, item_id, category, title, rank

Show/GET
URL Input(s): u_id
JSON Input(s): none
Outputs: JSON username, collection_name, item_id, category, title, rank, genre, platform, author, max_players for all items owned by user u_id

Index/GET 
URL Input(s): u_id - req, c_id - req
JSON Input(s): none
Outputs: JSON username, collection_name, item_id, category, title, rank, genre, platform, author, max_players for all items owned by user u_id in collection c_id

Update/PATCH
URL Input(s): id - req
JSON Input(s): category - opt, title - opt, rank - opt, format - opt, genre - opt, platform - opt, author - opt, max_players - opt
Outputs: JSON item_id, category, title, rank, format, genre, platform, author, max_players of updated item id

Delete/DELETE
URL Input(s): id - req
JSON Input(s): none
Outputs: JSON True if deletion was successful, False if deletion unsuccessful

Troubleshooting:
If database tables are empty run: alembic upgrade head from Alembic Folder to rebuild tables in Collection Tracker 
Database.
If Collection Tracker Database does not connect it may need to be renamed/recreated in Postgres to fix connection issue.

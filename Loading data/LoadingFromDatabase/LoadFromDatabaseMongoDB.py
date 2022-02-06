from pymongo import MongoClient

# Create a client object with connection string
client = MongoClient("mongodb+srv://root:heslo@pytest.0icjp.mongodb.net/sample_airbnb?retryWrites=true&w=majority")
# Get database from connection
db = client.sample_airbnb
# Get collection from database
listings = db.listingsAndReviews
# Find results
results = listings.find({"accommodates": 8})

# Work with loaded data as necessary, results are iterable

prices = []

for offer in results:
    prices.append(offer["price"])

   
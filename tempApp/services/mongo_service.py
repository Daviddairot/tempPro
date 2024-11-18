from django.conf import settings

# Access the MongoDB instance from settings
mongo_db = settings.mongo_db

def create_product(data):
    """Create a new product in MongoDB."""
    numbers_collection = mongo_db["tempreture"]
    result = numbers_collection.insert_one(data)
    return result.inserted_id

def get_product(product_id):
    """Retrieve a product by its ID."""
    product_collection = mongo_db["tempreture"]
    return product_collection.find_one({"_id": product_id})

def update_product(product_id, updated_data):
    """Update an existing product."""
    product_collection = mongo_db["tempreture"]
    result = product_collection.update_one(
        {"_id": product_id},
        {"$set": updated_data}
    )
    return result.modified_count

def delete_product(product_id):
    """Delete a product by its ID."""
    product_collection = mongo_db["tempreture"]
    result = product_collection.delete_one({"_id": product_id})
    return result.deleted_count

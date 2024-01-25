from fastavro import writer, parse_schema
from fastavro.validation import validate_many
from selenium.page import HomePage
from json import load
from scrape.base import Base
import os

class GetShoesUnder10(Base) :
    def setUp(self):
        super().setUp()
        self.home_page = HomePage(self.driver)
    #   self.search_page = SearchPage(self.driver)
    #   ...
    def exec(self):
        self.home_page.search_Item("Hey")
# Preparing fake data and loading Item schema

records = [
    {u'name': u'Zapatitos Kalsaitos', u'price' : 19.99},
    {u'name': u'Xaketita Vintage', u'description' : u'Como ronea, como ronea (8)', u'price' : 15.00},
]

item_schema = load(open(f"{os.getcwd()}/py/scrape/models/item.avsc"))
parsed_item_schema = parse_schema(item_schema)


# Step 1. TODO Extract data with Selenium script. Example data is provided in records dict
# Step 2. Data is checked to know if it's an instance of its schema

validate_many(records, parsed_item_schema)

# Writing example data to avro format

with open(f"{os.getcwd()}/py/avro_target/item.avro", 'wb') as out:
    writer(out, parsed_item_schema, records, validator=True)

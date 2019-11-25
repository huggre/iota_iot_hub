import os
clear = lambda: os.system('cls')

from sqlalchemy.sql import func

from app import db


from datetime import date, datetime

# import paho.mqtt.client as mqtt

from app.models import tbl_members
from app.models import tbl_assets
from app.models import tbl_asset_types
from app.models import tbl_tags
#from app.models import tbl_tag_types
from app.models import tbl_sensors
from app.models import tbl_sensor_types
#from app.models import tbl_accounts
from app.models import tbl_transactions
#from app.models import tbl_deposits
#from app.models import tbl_withdrawals
from app.models import tbl_transaction_errors

def add_sensortype(sensor_type_name):

    sensor_type = tbl_sensor_types()
    sensor_type.name = sensor_type_name 

    db.session.add(sensor_type)

    # Commit tagtype to DB
    db.session.commit()

    print("\n Sensor Type: " + sensor_type_name + " added to DB")

def add_assettype(asset_type_name):

    asset_type = tbl_asset_types()
    asset_type.name = asset_type_name 

    db.session.add(asset_type)

    # Commit tagtype to DB
    db.session.commit()

    print("\n Asset Type: " + asset_type_name + " added to DB")

def register_tag(tag_UID):
    # Check if tag UID already exist
    tag = (db.session.query(tbl_tags)
        .filter(tbl_tags.tag_UID == tag_UID)
        .add_columns(tbl_tags.tag_UID.label('tag_UID'))
        .first())

    if tag is None:
        tag = tbl_tags()
        tag.tag_UID = tag_UID
        db.session.add(tag)

        # Commit new transaction to DB
        db.session.commit()

        print("Tag sucessfully created")

    else:
        print("Tag UID already exist")

def add_transaction(sensor_UID, tag_UID, trans_type, value):


clear()

print("""

The db_init.py tools helps you add new tag, sensor and asset types to the IotaGo database.

Common tag types are: RFID Tag etc.
Common sensor types are: RFID Reader etc.
Common asset types are: Parking Lot, Sports Venue etc.

""")

ans=True
while ans:
    print ("""
    1.Register Tag
    2.Add Transaction
    3.Exit/Quit
    """)
    ans=input("What would you like to do? ") 
    if ans=="1":
        tag_UID = input("\n Specify Tag UID:")
        register_tag(tag_UID)
    elif ans=="2":
        sensor_UID input("\n Specify Sensor UID:")
        tag_UID = input("\n Specify Tag UID:")
        trans_type = input("\n Specify Transaction Type ID:")
        value = input("\n Specify Value:")
        add_transaction(sensor_UID, tag_UID, trans_type, deposit_value)
    elif ans=="3":
      exit()
    elif ans !="":
      print("\n Not Valid Choice Try again") 
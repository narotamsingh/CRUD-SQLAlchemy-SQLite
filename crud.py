#!/usr/bin/env python2
"""This python program performed all of CRUD operations with SQLAlchemy
on an SQLite database."""


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem


engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


def Create_Res(Restaurant_Name):
    """It create a new Restaurant"""
    myRestaurant = Restaurant(name=Restaurant_Name)
    session.add(myRestaurant)
    session.commit()


def Add_Item(Restaurant_Name, Item_Name, Item_Des, Item_Course, Item_Price):
    """It add menu item in a Restaurant"""
    Rest = session.query(Restaurant).filter_by(name=Restaurant_Name).one()
    additem = MenuItem(
        name=Item_Name,
        description=Item_Des,
        course=Item_Course,
        price=Item_Price,
        restaurant_id=Rest.id)
    session.add(additem)
    session.commit()


def ReadAll():
    """Print information from database using the query method in SQLAlchemy"""
    items = session.query(Restaurant).all()
    for item in items:
        print "ID:", item.id
        print "Restaurant:", item.name
    print "\n"

    items = session.query(MenuItem).all()
    for item in items:
        print "Item ID:", item.id
        print "Name:", item.name
        print "Description:", item.description
        print "Course:", item.course
        print "Price:", item.price
        print "Restaurant ID:", item.restaurant_id
        print "\n"


def Find(item_name):
    """Find Entry in database using the query method in SQLAlchemy"""
    items = session.query(MenuItem).filter_by(name=item_name)
    for item in items:
        print "Item ID:", item.id
        print "Price:", item.price
        print "Restaurant:", item.restaurant.name
        print "\n"


def Update(item_id):
    """Update Entry in database using the query method in SQLAlchemy"""
    UrbanVeggieBurger = session.query(MenuItem).filter_by(id=item_id).one()
    UrbanVeggieBurger.price = '$2.99'
    session.add(UrbanVeggieBurger)
    session.commit()


def Delete_Item_Name(item_name):
    """Find/delete entry (name) in database using query method in SQLAlchemy"""
    spinach = session.query(MenuItem).filter_by(name=item_name).one()
    session.delete(spinach)
    session.commit()


def Delete_Item_Id(item_id):
    """Find/delete entry (name) in database using query method in SQLAlchemy"""
    spinach = session.query(MenuItem).filter_by(id=item_id).one()
    session.delete(spinach)
    session.commit()


def Delete_Res(item_id):
    """Find/delete entry (id) in database using query method in SQLAlchemy"""
    spinach = session.query(Restaurant).filter_by(id=item_id).one()
    session.delete(spinach)
    session.commit()

if __name__ == '__main__':
    # Create_Res("Pizza Palace")
    # Add_Item("Pizza Palace", "Cheese Pizza",
    #        "Made with all natural ingredients  fresh mozzarella",
    #        "Entree", "$6.99")
    ReadAll()
    # Find('Cheese Pizza')
    # Update(1)
    # Delete_Item_Id(2)
    # Delete_Item_Name('Cheese Pizza')
    # Delete_Res(2)

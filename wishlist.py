from flask import make_response, abort
from config import db
from models import Wish, WishSchema


def read_all():
    wishlist = Wish.query.order_by(Wish.desc).all()
    wish_schema = WishSchema(many=True)
    data = wish_schema.dump(wishlist)
    return data


def read_one(wish_id):
    wish = Wish.query.filter(Wish.wish_id == wish_id).one_or_none()

    if wish is not None:
        wish_schema = WishSchema()
        data = wish_schema.dump(wish)
        return data
    else:
        abort(
            404,
            "Wish not found for Id: {wish_id}".format(wish_id=wish_id),
        )


def create(wish):
    title = wish.get("title")
    desc = wish.get("desc")
    existing_wish = (
        Wish.query.filter(Wish.title == title)
        .filter(Wish.desc == desc)
        .one_or_none()
    )

    if existing_wish is None:
        schema = WishSchema()
        new_wish = Wish(title=title, desc=desc)
        db.session.add(new_wish)
        db.session.commit()
        data = schema.dump(new_wish)
        return data, 201
    else:
        abort(
            409,
            "Wish {title} {desc} exists already".format(
                title=title, desc=desc
            ),
        )


def update(wish_id, wish):
    update_wish = Wish.query.filter(
        Wish.wish_id == wish_id
    ).one_or_none()

    title = wish.get("title")
    desc = wish.get("desc")

    existing_wish = (
        Wish.query.filter(Wish.title == title)
        .filter(Wish.desc == desc)
        .one_or_none()
    )


    if update_wish is None:
        abort(
            404,
            "Wish not found for Id: {wish_id}".format(wish_id=wish_id),
        )
    elif (
        existing_wish is not None and existing_wish.wish_id != wish_id
    ):
        abort(
            409,
            "Wish {title} {desc} exists already".format(
                title=title, desc=desc
            ),
        )
    else:
        schema = WishSchema()
        updt_wish = Wish(title=title, desc=desc, wish_id=wish_id)
        db.session.merge(updt_wish)
        db.session.commit()
        data = schema.dump(update_wish)
        return data, 200


def delete(wish_id):
    wish = Wish.query.filter(Wish.wish_id == wish_id).one_or_none()

    if wish is not None:
        db.session.delete(wish)
        db.session.commit()
        return make_response(
            "Wish {wish_id} deleted".format(wish_id=wish_id), 200
        )
    else:
        abort(
            404,
            "Wish not found for Id: {wish_id}".format(wish_id=wish_id),
        )
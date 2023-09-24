from flask import abort, jsonify

from src.model.user import User


class UserRepository:
    @classmethod
    def get_all_user(cls):
        try:
            users = User.query.all()
            user_list = []

            for user in users:
                if user.deleted_at is None:
                    user_list.append(user.to_dict())

            return jsonify({"users": user_list})
        except Exception as e:
            return jsonify({"error": str(e)})

    @classmethod
    def get_user_by_id(cls, id: int):
        try:
            user = User.query.get_or_404(id)
            if user.deleted_at is not None:
                abort(404)
            return jsonify({"user": user.to_dict()})
        except Exception as e:
            return jsonify({"error": str(e)})

    @classmethod
    def add_user(cls, new_user: User, db):
        try:
            user = User.query.get(new_user.id)
            if user is None:
                db.session.add(new_user)
                db.session.commit()
            return jsonify({"added_user": user.to_dict()})
        except Exception as e:
            return jsonify({"error": str(e)})

    @classmethod
    def edit_user(cls, new_user: User, id: int, db):
        try:
            user = User.query.get_or_404(id)
            if user.deleted_at is not None:
                abort(404)

            if new_user.email:
                user.email = new_user.email
            if new_user.first_name:
                user.first_name = new_user.first_name
            if new_user.last_name:
                user.last_name = new_user.last_name
            if new_user.avatar:
                user.avatar = new_user.avatar
            db.session.commit()

            return jsonify({"updated_user": user.to_dict()})
        except Exception as e:
            return jsonify({"error": str(e)})

    @classmethod
    def soft_delete_user(cls, id: int, db):
        try:
            user = User.query.get_or_404(id)
            user.soft_delete()
            db.session.commit()

            return jsonify({"deleted_user": user.to_dict()})
        except Exception as e:
            return jsonify({"error": str(e)})

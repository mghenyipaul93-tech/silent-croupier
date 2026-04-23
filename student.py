from flask import jsonify, Blueprint

student_bp = Blueprint("student_bp", __name__)

@student_bp.route("/single", methods=["GET"])
async def sing_student():
    return "single student"

@student_bp.route("/add", methods=["POST"])
async def add():
    return "adding student"

@student_bp.route("/delete", methods=["DELETE"])
async def delete_student():
    return "delete student"

@student_bp.route("/list_all", methods=["GET"])
async def list_all():
    return "list student"


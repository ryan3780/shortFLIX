from flask import Blueprint
from service.get_content import all_contents

bp = Blueprint('contents',__name__)

@bp.route('/contents')
def get_contents():
  return all_contents()

from flask import jsonify, session
from model.models import *

def like_contents(content_id, user_email):
    user = User.query.filter_by(email = user_email).first()
    content = Content.query.filter_by(id = content_id).first()
    
    # 이미 좋아요를 클릭한 사람이라면 취소 기능만 가능해야함
    # if content in user.likes_list:
    #   return dislike_content(content_id, user_email)
    
    prev = user.likes_list
    now = [] 
    now.append({
        'id' : content.id,
        'thumbnail' : content.thumbnail,
        'title' : content.title,
        'rating' : content.rating,
        'genre' : content.genre.replace("'",""),
        'running_time' : content.running_time,
        'synop' : content.synop,
        'like':content.like,
        'key_words' : content.key_words,
        'year' : content.year
    })

    if user.likes_list is None:
        content.like += 1
        now[0]['like'] += 1
        db.session.commit()

        user.likes_list = []
        user.likes_list = [] + now
        db.session.commit()
        return '첫 좋아요 입니다.'
   
    content.like += 1
    now[0]['like'] += 1
    db.session.commit()

    user.likes_list = prev + now
    db.session.commit()

    return '좋아요 +1'

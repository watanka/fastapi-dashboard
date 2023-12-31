from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from datetime import datetime

from database import SessionLocal, get_db
from models import Question
from domain.question import question_schema
from domain.question import question_crud

router = APIRouter(
    prefix = '/api/question'
)

@router.get('/list', response_model = list[question_schema.Question])
def question_list(db : Session = Depends(get_db)) :
    _question_list = question_crud.get_question_list(db)
    return _question_list

@router.get('/detail/{question_id}', response_model = question_schema.Question)
def question_detail(question_id : int, db : Session = Depends(get_db)) : 
    question = question_crud.get_question(db, question_id = question_id)
    return question
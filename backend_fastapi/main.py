
from fastapi import FastAPI, Depends, HTTPException, status
import uvicorn
import p_model_type
from different_languages import different_language
import models
from database import engine, SessionLocal
from sqlalchemy.orm import Session
import os
from Split_word import Splitword
from sqlalchemy.exc import DatabaseError


models.Base.metadata.create_all(bind=engine)


app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
@app.get("/")
async def root():
    return {"Hello": "World"}



@app.post("/createpost", status_code=status.HTTP_201_CREATED)
async def tt_speech(details:p_model_type.Post, db: Session= Depends(get_db)):

    new_dict = details.dict()
    name = [details.first_name, details.last_name]
    full_name = " ".join(name)
    new_dict["full_name"] = full_name
    file_name = full_name+str(details.student_id)


    different_language(text=full_name,lang=details.lang_name)
    with open(f"{full_name}.wav", "rb") as file:
        audio_binary = file.read()
    new_dict["audio_binary"] = audio_binary
    if os.path.exists(f"{full_name}.wav"):
        os.remove(f"{full_name}.wav")
    with open(f"{file_name}.wav", "wb") as file:
        file.write(audio_binary)


    new_student_details = models.Student_data(**new_dict)

    try:
        db.add(new_student_details)
        db.commit()
        db.refresh(new_student_details)
    except DatabaseError as e:
        print(e.orig)
        db.rollback()
        

    pro_data = {
    "student_id" : new_student_details.student_id,
    "first_name" : new_student_details.first_name,
    "last_name": new_student_details.last_name,
    "full_name": new_student_details.full_name
    }

    first_name_pro_eng, last_name_pro_eng =Splitword().Phonetics_eng_words(first_name=pro_data["first_name"], last_name=pro_data["last_name"])
    first_name_pro, last_name_pro = Splitword().pronouncing_word(first_name=pro_data["first_name"], last_name=pro_data["last_name"])
    split_first_name, split_last_name = Splitword().seperating_name(first_name=pro_data["first_name"], last_name=pro_data['last_name'])



    pro_data["first_name_p_eng"] = first_name_pro_eng
    pro_data["first_name_p"] = first_name_pro
    pro_data["last_name_p_eng"] = last_name_pro_eng
    pro_data["last_name_p"] = last_name_pro
    pro_data["split_first_name"] = split_first_name
    pro_data["split_last_name"] = split_last_name


    name_list = pro_data["full_name"].split()

    results = db.query(models.Namepronounciation).filter(models.Namepronounciation.name.in_(name_list)).order_by(models.Namepronounciation.votes.desc()).limit(3).all()


    return {"data": pro_data,
            "results": results}


@app.post("/selection", status_code=status.HTTP_201_CREATED)
async def selection(details:p_model_type.Selection, db: Session= Depends(get_db)):
    statement_dict = []
    for i in range(len(details.name)):
        data = {"student_id":details.student_id,
                "name":details.name[i],
                "name_selection":details.name_selection[i],
                "votes":details.votes,
                "show":details.show}
        statement_dict.append(data)


    for stat_dict in statement_dict:
        new_data = models.Namepronounciation(**stat_dict)
        db.add(new_data)
        db.commit()
        db.refresh(new_data)



if __name__ == "__main__":
    uvicorn.run("main:app", port=8080, log_level="info", reload=True)
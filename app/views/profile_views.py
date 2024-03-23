from flask import Flask, render_template, request, redirect, flash, get_flashed_messages
from app.models.user import *
from config import *
from . import views
import os
from flask_login import current_user


@views.route('/profile/<int:id_>', methods=['POST', 'GET'])
def profile_view(id_):
    name_username = users.query.filter_by(id_=id_).first()

    profile_info = profile.query.filter_by(id_user=id_).first()

    user_photo = avatars.query.filter_by(user_id=id_).first()

    if name_username is None:
      return render_template("not_found.html")
    
    is_company=False
    c_id = current_user.get_id()
    company_check = users_employers.query.filter_by(id_=c_id).first()
    invite_st=None

    if company_check:
      is_company=True
      invite_st=check_application(id_=id_)
      print(invite_st)

    if request.method == 'POST':

        if 'photo' in request.files and request.files['photo'].filename:
           
           print(request.files['photo'])
           if user_photo:
             db.session.delete(user_photo)
             os.remove(Config.UPLOAD_FOLDER+user_photo.photo_path)

           photo = request.files['photo']
  

           photo.save(os.path.join(Config.UPLOAD_FOLDER,
                                photo.filename))
          
           datas = avatars(user_id=id_,
                          photo_path=photo.filename)
            
          
           db.session.add(datas)
           db.session.commit()

           return redirect(f'/profile/{id_}')
        
        elif is_company==True:

          datas = Applications(id_req=create_new_id_application(),
                          id_from=c_id,
                          id_to=id_,
                          status='sent')
          
          db.session.add(datas)
          db.session.commit()

          return redirect(f'/profile/{id_}')

        elif 'exp1' in request.form:

          id_ = id_
          description = request.form['descr']
          exp1 = request.form['exp1']
          exp2 = request.form['exp2']
          gr = request.form['gr']
          workac = request.form['workac']
          otherd = request.form['otherd']
          phone = request.form['phone']
          socn = request.form['socn']

          try:

           datas = profile(id_user=id_,
           profile_descr=description,
           work_exp_y=exp1,
           work_exp_p = exp2,
           citizen=gr,
           work_accept=workac,
           other_docs=otherd,
           phone=phone,
           nets=socn
           )

           if profile_info:
            db.session.delete(profile_info)
       
           db.session.add(datas)
           db.session.commit()

           return redirect(f'/profile/{id_}')
          
          except:
           flash('Что-то пошло не так!')
        else:

          flash("Фото не было загружено!")
        
    
    currentuser = 0

    if current_user.get_id() != None:

     currentuser = int(current_user.get_id())

    all_invites = Applications.query.filter_by(id_to=id_).all()
    company_nms = {company.id_from: get_company_name(company.id_from) for company in all_invites}


    return render_template("profile.html", 
                           name_username=name_username, 
                           profile_info=profile_info,
                           user_photo=user_photo,
                           id_=int(id_),
                           currentuser=currentuser,
                           is_company=is_company,
                           invite_st=invite_st,
                           company_nms=company_nms,
                           all_invites=all_invites)


@views.route('/delete_photo/<int:id_>', methods=['POST', 'GET'])
def delete_photo(id_):
  user_photo = avatars.query.filter_by(user_id=id_).first()
  
  if user_photo:
   db.session.delete(user_photo)
   db.session.commit()
   os.remove(Config.UPLOAD_FOLDER+user_photo.photo_path)
  
  return redirect(f'/profile/{id_}')

@views.route('/company/<int:id_>', methods=['POST', 'GET'])
def company_view(id_):
  datas = users_employers.query.filter_by(id_=id_).first()

  invites = Applications.query.filter_by(id_from=id_).all()
  names = {user.id_to: get_name(user.id_to) for user in invites}

  currentuser = 0

  if current_user.get_id() != None:

     currentuser = int(current_user.get_id())

  if datas is None:
      return render_template("not_found.html")

  return render_template("profile_employer.html", 
                         datas=datas,
                         id_=int(id_),
                         invites=invites,
                         names=names,
                         currentuser=currentuser)


@views.route('/approve/<int:id_from>/<int:id_to>', methods=['POST', 'GET'])
def approving_application(id_from, id_to):
  update_app_st(id_from, id_to,'approved')
  
  return redirect(f'/profile/{id_to}')

@views.route('/reject/<int:id_from>/<int:id_to>', methods=['POST', 'GET'])
def rejecting_application(id_from, id_to):
  update_app_st(id_from, id_to,'rejected')
  
  return redirect(f'/profile/{id_to}')

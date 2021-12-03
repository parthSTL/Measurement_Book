from flask import Flask, render_template, url_for, request, redirect
import os
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

def create_the_database(db):
    db.create_all()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///mb.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db=SQLAlchemy(app)

class Representative(db.Model):
    id= db.Column(db.Integer,primary_key=True)
    book_name=db.Column(db.String(200),nullable=False)
    name=db.Column(db.String(200),nullable=False)
    date_created= db.Column(db.DateTime,default=datetime.utcnow) 
class Project_description(db.Model):

    msi=db.Column(db.String(200),nullable=False)
    measurement_book_no=db.Column(db.Integer,nullable=False)
    sheet_no=db.Column(db.Integer,nullable=False)
    pop_type=db.Column(db.String(200),nullable=False)
    zone=db.Column(db.String(200),nullable=False)
    mandal=db.Column(db.String(200),nullable=False)
    gp_name=db.Column(db.String(200),nullable=False)
    ring_id=db.Column(db.String(200),nullable=False)
    span_id=db.Column(db.String(200),primary_key=True,nullable=False)
    measurements = db.relationship('Measurement', backref='project_description')
    plt_locs=db.relationship('Plt_loc',backref='project_description')



measurement_loc=db.Table('measurement_loc',
    db.Column('measurement_id',db.Integer,db.ForeignKey('measurement.id'),primary_key=True),
    db.Column('loc_id',db.Integer,db.ForeignKey('plt_loc.id'),primary_key=True))

class Measurement(db.Model):
    id= db.Column(db.Integer,primary_key=True)
    ch_from=db.Column(db.Integer,nullable=False)
    ch_to=db.Column(db.Integer,nullable=False)
    length=db.Column(db.Integer,nullable=False)
    offset=db.Column(db.Integer,nullable=False)
    depth=db.Column(db.Integer,nullable=False)
    trench_side=db.Column(db.String(200),nullable=False)
    duct_laid=db.Column(db.Integer,nullable=False)
    method_exec=db.Column(db.String(200),nullable=False)
    crossing=db.Column(db.String(200),nullable=False)
    strata_type=db.Column(db.String(200),nullable=False)
    protect_dwc=db.Column(db.Integer,nullable=False)
    protect_gi=db.Column(db.Integer,nullable=False)
    protect_rcc=db.Column(db.Integer,nullable=False)
    protect_pcc=db.Column(db.Integer,nullable=False)
    rcc_chamber=db.Column(db.Integer,nullable=False)
    rcc_marker=db.Column(db.Integer,nullable=False)
    remark=db.Column(db.String(200),nullable=False)
    span_id = db.Column(db.String(200), db.ForeignKey('project_description.span_id'), nullable=False)


class Plt_loc(db.Model):
    id= db.Column(db.Integer,primary_key=True)
    start_lat=db.Column(db.Float,nullable=False)
    start_long=db.Column(db.Float,nullable=False)
    end_lat=db.Column(db.Float,nullable=False)
    end_long=db.Column(db.Float,nullable=False)
    span_id = db.Column(db.String(200), db.ForeignKey('project_description.span_id'), nullable=False)
    measurements=db.relationship('Measurement',secondary=measurement_loc)

@app.route("/",methods=['POST','GET'])
def index():
    if request.method=='POST':
        representative_book_name=request.form['book_name']
        representative_name=request.form['name']
        new_representative=Representative(book_name=representative_book_name,name=representative_name)

        try:
            db.session.add(new_representative)  # Add new_task in database
            db.session.commit()  # Commit the database
            return redirect('/Project_Site') # Redirect to Project_Site webpage
        except:
            return 'There was an issue adding your task'
    else:

        return render_template('index.html')


@app.route("/Project_Site", methods=['POST','GET'])
def project():
    if request.method=='POST':
        project_msi_name=request.form['msi_name']
        project_mb_no=request.form['mb_no']
        project_sheet_no=request.form['sheet_no']
        project_pop_type=request.form['pop_type']
        project_zone=request.form['zone']
        project_mandal=request.form['mandal']
        project_gp_name=request.form['gp_name']
        project_ring_id=request.form['ring_id']
        project_span_id=request.form['span_id']


        new_project_site=Project_description(msi=project_msi_name,measurement_book_no=project_mb_no,
        sheet_no=project_sheet_no,pop_type=project_pop_type,zone=project_zone,
        mandal=project_mandal,gp_name=project_gp_name,
        ring_id=project_ring_id,span_id=project_span_id)
        print(new_project_site.span_id)

        try:
            db.session.add(new_project_site)  # Add new_task in database
            db.session.commit()  # Commit the database
            return redirect('/Measurement/{}'.format(new_project_site.span_id)) # Redirect to Project_Site webpage
        except:
            return 'There was an issue adding your task'
    else:

        return render_template('project.html')

@app.route("/Measurement/<string:span_id>", methods=['POST','GET'])
def measurement(span_id):
    if request.method=='POST':
        measurement_ch_from=request.form['ch_from']
        measurement_ch_to=request.form['ch_to']
        measurement_length=request.form['length']
        measurement_offset=request.form['offset']
        measurement_depth=request.form['depth']
        measurement_trench_side=request.form['trench_side']
        measurement_duct_laid=request.form['duct_laid']
        measurement_method_exec=request.form['method_exec']
        measurement_crossing=request.form['crossing']
        measurement_strata_type=request.form['strata_type']
        measurement_protect_dwc=request.form['protect_dwc']
        measurement_protect_gi=request.form['protect_gi']
        measurement_protect_rcc=request.form['protect_rcc']
        measurement_protect_pcc=request.form['protect_pcc']
        measurement_rcc_chamber=request.form['rcc_chamber']
        measurement_rcc_marker=request.form['rcc_marker']
        measurement_remark=request.form['remark']

        new_measurement=Measurement(ch_from=measurement_ch_from,ch_to=measurement_ch_to, length=measurement_length,
        offset=measurement_offset,depth=measurement_depth, trench_side=measurement_trench_side,duct_laid=measurement_duct_laid,
        method_exec=measurement_method_exec,crossing=measurement_crossing, strata_type=measurement_strata_type,
        protect_dwc=measurement_protect_dwc, protect_gi=measurement_protect_gi,protect_rcc=measurement_protect_rcc,
        protect_pcc=measurement_protect_pcc,rcc_chamber=measurement_rcc_chamber,rcc_marker=measurement_rcc_marker,
        remark=measurement_remark,span_id=span_id)

        # try:
        #     db.session.add(new_measurement)  # Add new_task in database
        #     db.session.commit()  # Commit the database
        #     return redirect('/Coordinates') # Redirect to Measurement webpage
        # except:
        #     return 'There was an issue adding your task'
        db.session.add(new_measurement)
        db.session.commit()
        return redirect('/Measurement/{}'.format(span_id))
    else:

        return render_template('measurement.html',span_id=span_id)
        


@app.route("/Coordinates",methods=['POST','GET'])
def coordinates():
    return render_template('coordinates.html')

# if database does not exist in the current directory, create it!
db_is_new = not os.path.exists('mb.db')
if db_is_new:
    create_the_database(db)

if __name__=='__main__':
    app.run(debug=True, port=8000)
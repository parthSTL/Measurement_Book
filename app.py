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
class Project_description_tfiber_tnd(db.Model):

    msi=db.Column(db.String(200),nullable=False)
    measurement_book_no=db.Column(db.Integer,nullable=False)
    sheet_no=db.Column(db.Integer,nullable=False)
    pop_type=db.Column(db.String(200),nullable=False)
    zone=db.Column(db.String(200),nullable=False)
    mandal=db.Column(db.String(200),nullable=False)
    gp_name=db.Column(db.String(200),nullable=False)
    ring_id=db.Column(db.String(200),nullable=False)
    span_id=db.Column(db.String(200),primary_key=True,nullable=False)
    tfiber_tnd_measurements = db.relationship('TFiber_TnD_Measurement', backref='project_description_tfiber_tnd')
    
class Project_description_tfiber_hdd(db.Model):
    msi=db.Column(db.String(200),nullable=False)
    measurement_book_no=db.Column(db.Integer,nullable=False)
    sheet_no=db.Column(db.Integer,nullable=False)
    pop_type=db.Column(db.String(200),nullable=False)
    zone=db.Column(db.String(200),nullable=False)
    mandal=db.Column(db.String(200),nullable=False)
    gp_name=db.Column(db.String(200),nullable=False)
    ring_id=db.Column(db.String(200),nullable=False)
    span_id=db.Column(db.String(200),primary_key=True,nullable=False)
    abd=db.Column(db.String(200),nullable=False)
    tfiber_hdd_measurements = db.relationship('TFiber_HDD_Measurement', backref='project_description_tfiber_hdd')





class TFiber_TnD_Measurement(db.Model):
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
    span_id = db.Column(db.String(200), db.ForeignKey('project_description_tfiber_tnd.span_id'), nullable=False)
    lat_pt=db.Column(db.Float,nullable=False)
    long_pt=db.Column(db.Float,nullable=False)

class TFiber_HDD_Measurement(db.Model):
    id= db.Column(db.Integer,primary_key=True)
    ch_from=db.Column(db.Integer,nullable=False)
    ch_to=db.Column(db.Integer,nullable=False)
    road_side=db.Column(db.String(200),nullable=False)
    length=db.Column(db.Integer,nullable=False)
    graph_as_built_made=db.Column(db.String(200),nullable=False)
    inter_sec_depth=db.Column(db.Integer,nullable=False)
    bore_reamer_dia=db.Column(db.Integer,nullable=False)
    no_of_duct=db.Column(db.Integer,nullable=False)
    remark=db.Column(db.String(200),nullable=False)
    span_id = db.Column(db.String(200), db.ForeignKey('project_description_tfiber_hdd.span_id'), nullable=False)

# class TFiber_DIT_Measurement(db.Model):
#     id= db.Column(db.Integer,primary_key=True)
#     chainage_from=db.Column(db.Integer,nullable=False)
#     chainage_to=db.Column(db.Integer,nullable=False)
#     chamber_from=db.Column(db.Integer,nullable=False)
#     chamber_to=db.Column(db.Integer,nullable=False)
#     length=db.Column(db.Integer,nullable=False)
#     air_test=db.Column(db.String(200),nullable=False)
#     sponge_test=db.Column(db.String(200),nullable=False)
#     shuttle_test=db.Column(db.String(200),nullable=False)
#     pressure_test_5bar_30_min=db.Column(db.Float,nullable=False)   # Float number
#     pressure_test_10bar_10_min=db.Column(db.Float,nullable=False)   # Float number
#     pressure_test_10min_30_min=db.Column(db.Float,nullable=False)   # Float number
#     drop_in_pressure=db.Column(db.Float,nullable=False)   # Float number
#     test_result=db.Column(db.String(200),nullable=False)
#     coupler_loc=db.Column(db.Float,nullable=False)
#     mb_duct_from=db.Column(db.Float,nullable=False)
#     mb_duct_to=db.Column(db.Float,nullable=False)
#     mb_duct_len=db.Column(db.Float,nullable=False)
#     remark=db.Column(db.String(200),nullable=False)
#     span_id = db.Column(db.String(200), db.ForeignKey('project_description_tfiber_tnd.span_id'), nullable=False)

# class TFiber_DRT_Measurement(db.Model):
#     id= db.Column(db.Integer,primary_key=True)
#     chamber1_lat=db.Column(db.Float,nullable=False)
#     chamber1_long=db.Column(db.Float,nullable=False)
#     chamber1_condition=db.Column(db.String(200),nullable=False)
#     chamber1_route_marker_avail=db.Column(db.String(200),nullable=False)

#     chamber2_lat=db.Column(db.Float,nullable=False)
#     chamber2_long=db.Column(db.Float,nullable=False)
#     chamber2_condition=db.Column(db.String(200),nullable=False)
#     chamber2_route_marker_avail=db.Column(db.String(200),nullable=False)

#     mb_duct_dam_lat=db.Column(db.Float,nullable=False)
#     mb_duct_dam_long=db.Column(db.Float,nullable=False)
#     mb_duct_dam_ch_from=db.Column(db.Integer,nullable=False)
#     mb_duct_dam_ch_to=db.Column(db.Integer,nullable=False)
#     mb_duct_dam_len=db.Column(db.Integer,nullable=False)
#     mb_duct_mis_lat=db.Column(db.Float,nullable=False)
#     mb_duct_mis_long=db.Column(db.Float,nullable=False)
#     mb_duct_mis_ch_from=db.Column(db.Integer,nullable=False)
#     mb_duct_mis_ch_to=db.Column(db.Integer,nullable=False)
#     mb_duct_mis_len=db.Column(db.Integer,nullable=False)
#     remarks=db.Column(db.String(200),nullable=False)
#     span_id = db.Column(db.String(200), db.ForeignKey('project_description_tfiber_tnd.span_id'), nullable=False)

# class TFiber_Blowing_Measurement(db.Model):
#     id= db.Column(db.Integer,primary_key=True)
#     ch_from=db.Column(db.Integer,nullable=False)
#     ch_to=db.Column(db.Integer,nullable=False)
#     chamber_from=db.Column(db.Integer,nullable=False)
#     chamber_to=db.Column(db.Integer,nullable=False)
#     length=db.Column(db.Integer,nullable=False)
#     size_of_ofc=db.Column(db.String(200),nullable=False)
#     ofc_cable_id=db.Column(db.Integer,nullable=False)
#     cable_start=db.Column(db.Integer,nullable=False)
#     cable_end=db.Column(db.Integer,nullable=False)
#     cable_len=db.Column(db.Integer,nullable=False)
#     mh_a_cable_end=db.Column(db.Integer,nullable=False)
#     mh_a_cable_end=db.Column(db.Integer,nullable=False)
#     mh_a_slack_cable_len=db.Column(db.Integer,nullable=False)
#     mh_b_cable_end=db.Column(db.Integer,nullable=False)
#     mh_b_cable_end=db.Column(db.Integer,nullable=False)
#     mh_b_slack_cable_len=db.Column(db.Integer,nullable=False)
#     span_id = db.Column(db.String(200), db.ForeignKey('project_description_tfiber_tnd.span_id'), nullable=False)









@app.route("/",methods=['POST','GET'])
def index():
    if request.method=='POST':
        representative_book_name=request.form['book_name']
        representative_name=request.form['name']
        new_representative=Representative(book_name=representative_book_name,name=representative_name)

        try:
            db.session.add(new_representative)  # Add new_task in database
            db.session.commit()  # Commit the database
            if representative_book_name=='tnd':
                return redirect('/Project_Site_T&D')
            elif representative_book_name=='hdd':
                return redirect('/Project_Site_HDD')
             # Redirect to Project_Site webpage
        except:
            return 'There was an issue adding your task'
    else:

        return render_template('index.html')


@app.route("/Project_Site_T&D", methods=['POST','GET'])
def tfiber_project_tnd():
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


        new_project_site=Project_description_tfiber_tnd(msi=project_msi_name,measurement_book_no=project_mb_no,
        sheet_no=project_sheet_no,pop_type=project_pop_type,zone=project_zone,
        mandal=project_mandal,gp_name=project_gp_name,
        ring_id=project_ring_id,span_id=project_span_id)
        # print(new_project_site.span_id)

        try:
            db.session.add(new_project_site)  # Add new_task in database
            db.session.commit()  # Commit the database
            return redirect('/TFiber_T&D_Measurement/{}'.format(new_project_site.span_id)) # Redirect to Project_Site webpage
        except:
            return 'There was an issue adding your task'
    else:

        return render_template('project_tfiber_tnd.html')

@app.route("/Project_Site_HDD", methods=['POST','GET'])
def tfiber_project_hdd():
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
        project_abd=request.form['abd']


        new_project_site=Project_description_tfiber_hdd(msi=project_msi_name,measurement_book_no=project_mb_no,
        sheet_no=project_sheet_no,pop_type=project_pop_type,zone=project_zone,
        mandal=project_mandal,gp_name=project_gp_name,
        ring_id=project_ring_id,span_id=project_span_id,abd=project_abd)
        # print(new_project_site.span_id)

        try:
            db.session.add(new_project_site)  # Add new_task in database
            db.session.commit()  # Commit the database
            return redirect('/TFiber_HDD_Measurement/{}'.format(new_project_site.span_id)) # Redirect to Project_Site webpage
        except:
            return 'There was an issue adding your task'
    else:

        return render_template('project_tfiber_hdd.html')

@app.route("/TFiber_T&D_Measurement/<string:span_id>", methods=['POST','GET']) # Dynamic part URL for span id
def tfiber_tnd_measurement(span_id):
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
        measurement_lat_pt=request.form['lat_pt']
        measurement_long_pt=request.form['long_pt']

        new_measurement=TFiber_TnD_Measurement(ch_from=measurement_ch_from,ch_to=measurement_ch_to, length=measurement_length,
        offset=measurement_offset,depth=measurement_depth, trench_side=measurement_trench_side,duct_laid=measurement_duct_laid,
        method_exec=measurement_method_exec,crossing=measurement_crossing, strata_type=measurement_strata_type,
        protect_dwc=measurement_protect_dwc, protect_gi=measurement_protect_gi,protect_rcc=measurement_protect_rcc,
        protect_pcc=measurement_protect_pcc,rcc_chamber=measurement_rcc_chamber,rcc_marker=measurement_rcc_marker,
        remark=measurement_remark,span_id=span_id,lat_pt=measurement_lat_pt,long_pt=measurement_long_pt)

        try:
            db.session.add(new_measurement)  # Add new_task in database
            db.session.commit()  # Commit the database
            return redirect('/TFiber_T&D_Measurement/{}'.format(span_id)) # Redirect to Measurement webpage
        except:
            return 'There was an issue adding your task'
        # db.session.add(new_measurement)
        # db.session.commit()
        # return redirect('/TFiber_T&D_Measurement/{}'.format(span_id))
    else:

        return render_template('tfiber_t&d_measurement.html',span_id=span_id)

@app.route("/TFiber_HDD_Measurement/<string:span_id>", methods=['POST','GET'])
def tfiber_hdd_measurement(span_id):
    if request.method=='POST':
        measurement_ch_from=request.form['ch_from']
        measurement_ch_to=request.form['ch_to']
        measurement_length=request.form['length']
        measurement_road_side=request.form['road_side']
        measurement_graph_as_built_made=request.form['graph_as_built_made']
        measurement_inter_sec_depth=request.form['inter_sec_depth']
        measurement_bore_reamer_dia=request.form['bore_reamer_dia']
        measurement_no_of_duct=request.form['no_of_duct']
        
        measurement_remark=request.form['remark']
        measurement_lat_pt=request.form['lat_pt']
        measurement_long_pt=request.form['long_pt']
        
        new_measurement=TFiber_HDD_Measurement(ch_from=measurement_ch_from,
        ch_to=measurement_ch_to,road_side=measurement_road_side,
        length=measurement_length,graph_as_built_made=measurement_graph_as_built_made,
        inter_sec_depth=measurement_inter_sec_depth,bore_reamer_dia=measurement_bore_reamer_dia,
        no_of_duct=measurement_no_of_duct,remark=measurement_remark,
        span_id=span_id)

        try:
            db.session.add(new_measurement)  # Add new_task in database
            db.session.commit()  # Commit the database
            return redirect('/TFiber_HDD_Measurement/{}'.format(span_id)) # Redirect to Measurement webpage
        except:
            return 'There was an issue adding your task'

    return render_template('tfiber_hdd_measurement.html',span_id=span_id)
        




# if database does not exist in the current directory, create it!
db_is_new = not os.path.exists('mb.db')
if db_is_new:
    create_the_database(db)

if __name__=='__main__':
    app.run(debug=True, port=8000)
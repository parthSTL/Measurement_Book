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

class Project_description_tfiber_dit(db.Model):
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
    duct_make_and_model=db.Column(db.String(200),nullable=False)
    tfiber_hdd_measurements = db.relationship('TFiber_DIT_Measurement', backref='project_description_tfiber_dit')

class Project_description_tfiber_drt(db.Model):
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
    tfiber_hdd_measurements = db.relationship('TFiber_DRT_Measurement', backref='project_description_tfiber_drt')

class Project_description_tfiber_blowing(db.Model):
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
    ofc_make_and_size=db.Column(db.String(200),nullable=False)
    tfiber_hdd_measurements = db.relationship('TFiber_Blowing_Measurement', backref='project_description_tfiber_blowing')





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

class TFiber_DIT_Measurement(db.Model):
    id= db.Column(db.Integer,primary_key=True)
    chainage_from=db.Column(db.Integer,nullable=False)
    chainage_to=db.Column(db.Integer,nullable=False)
    chamber_from=db.Column(db.Integer,nullable=False)
    chamber_to=db.Column(db.Integer,nullable=False)
    length=db.Column(db.Integer,nullable=False)
    air_test=db.Column(db.String(200),nullable=False)
    sponge_test=db.Column(db.String(200),nullable=False)
    shuttle_test=db.Column(db.String(200),nullable=False)
    pressure_test_5bar_30_min=db.Column(db.Float,nullable=False)   # Float number
    pressure_test_10bar_10_min=db.Column(db.Float,nullable=False)   # Float number
    pressure_test_10min_30_min=db.Column(db.Float,nullable=False)   # Float number
    drop_in_pressure=db.Column(db.Float,nullable=False)   # Float number
    test_result=db.Column(db.String(200),nullable=False)
    coupler_loc=db.Column(db.Float,nullable=False)
    mb_duct_from=db.Column(db.Float,nullable=False)
    mb_duct_to=db.Column(db.Float,nullable=False)
    mb_duct_len=db.Column(db.Float,nullable=False)
    remark=db.Column(db.String(200),nullable=False)
    span_id = db.Column(db.String(200), db.ForeignKey('project_description_tfiber_dit.span_id'), nullable=False)

class TFiber_DRT_Measurement(db.Model):
    id= db.Column(db.Integer,primary_key=True)
    chamber1_lat=db.Column(db.Float,nullable=False)
    chamber1_long=db.Column(db.Float,nullable=False)
    chamber1_condition=db.Column(db.String(200),nullable=False)
    chamber1_route_marker_avail=db.Column(db.String(200),nullable=False)

    chamber2_lat=db.Column(db.Float,nullable=False)
    chamber2_long=db.Column(db.Float,nullable=False)
    chamber2_condition=db.Column(db.String(200),nullable=False)
    chamber2_route_marker_avail=db.Column(db.String(200),nullable=False)

    ch_from=db.Column(db.Integer,nullable=False)
    ch_to=db.Column(db.Integer,nullable=False)
    duct_len=db.Column(db.Integer,nullable=False)

    mb_duct_dam_lat=db.Column(db.Float,nullable=False)
    mb_duct_dam_long=db.Column(db.Float,nullable=False)
    mb_duct_dam_ch_from=db.Column(db.Integer,nullable=False)
    mb_duct_dam_ch_to=db.Column(db.Integer,nullable=False)
    mb_duct_dam_len=db.Column(db.Integer,nullable=False)
    mb_duct_mis_lat=db.Column(db.Float,nullable=False)
    mb_duct_mis_long=db.Column(db.Float,nullable=False)
    mb_duct_mis_ch_from=db.Column(db.Integer,nullable=False)
    mb_duct_mis_ch_to=db.Column(db.Integer,nullable=False)
    mb_duct_mis_len=db.Column(db.Integer,nullable=False)
    remarks=db.Column(db.String(200),nullable=False)
    span_id = db.Column(db.String(200), db.ForeignKey('project_description_tfiber_drt.span_id'), nullable=False)

class TFiber_Blowing_Measurement(db.Model):
    id= db.Column(db.Integer,primary_key=True)
    ch_from=db.Column(db.Integer,nullable=False)
    ch_to=db.Column(db.Integer,nullable=False)
    chamber_from=db.Column(db.Integer,nullable=False)
    chamber_to=db.Column(db.Integer,nullable=False)
    length=db.Column(db.Integer,nullable=False)
    size_of_ofc=db.Column(db.String(200),nullable=False)
    ofc_cable_id=db.Column(db.Integer,nullable=False)
    cable_start=db.Column(db.Integer,nullable=False)
    cable_end=db.Column(db.Integer,nullable=False)
    cable_len=db.Column(db.Integer,nullable=False)
    mh_a_cable_entry=db.Column(db.Integer,nullable=False)
    mh_a_cable_end=db.Column(db.Integer,nullable=False)
    mh_a_slack_cable_len=db.Column(db.Integer,nullable=False)
    mh_b_cable_entry=db.Column(db.Integer,nullable=False)
    mh_b_cable_end=db.Column(db.Integer,nullable=False)
    mh_b_slack_cable_len=db.Column(db.Integer,nullable=False)
    remarks=db.Column(db.String(200),nullable=False)
    span_id = db.Column(db.String(200), db.ForeignKey('project_description_tfiber_blowing.span_id'), nullable=False)









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
            elif representative_book_name=='dit':
                return redirect('/Project_Site_DIT')
            elif representative_book_name=='drt':
                return redirect('/Project_Site_DRT')
            elif representative_book_name=='blowing':
                return redirect('/Project_Site_Blowing')
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

@app.route("/Project_Site_DIT", methods=['POST','GET'])
def tfiber_project_dit():
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
        project_duct_make_and_model=request.form['duct_make_and_model']


        new_project_site=Project_description_tfiber_dit(msi=project_msi_name,measurement_book_no=project_mb_no,
        sheet_no=project_sheet_no,pop_type=project_pop_type,zone=project_zone,
        mandal=project_mandal,gp_name=project_gp_name,
        ring_id=project_ring_id,span_id=project_span_id,abd=project_abd,duct_make_and_model=project_duct_make_and_model)
        # print(new_project_site.span_id)

        try:
            db.session.add(new_project_site)  # Add new_task in database
            db.session.commit()  # Commit the database
            return redirect('/TFiber_DIT_Measurement/{}'.format(new_project_site.span_id)) # Redirect to Project_Site webpage
        except:
            return 'There was an issue adding your task'
    else:

        return render_template('project_tfiber_dit.html')


@app.route("/Project_Site_DRT", methods=['POST','GET'])
def tfiber_project_drt():
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


        new_project_site=Project_description_tfiber_drt(msi=project_msi_name,measurement_book_no=project_mb_no,
        sheet_no=project_sheet_no,pop_type=project_pop_type,zone=project_zone,
        mandal=project_mandal,gp_name=project_gp_name,
        ring_id=project_ring_id,span_id=project_span_id,abd=project_abd)
        # print(new_project_site.span_id)

        try:
            db.session.add(new_project_site)  # Add new_task in database
            db.session.commit()  # Commit the database
            return redirect('/TFiber_DRT_Measurement/{}'.format(new_project_site.span_id)) # Redirect to Project_Site webpage
        except:
            return 'There was an issue adding your task'
    else:

        return render_template('project_tfiber_drt.html')


@app.route("/Project_Site_Blowing", methods=['POST','GET'])
def tfiber_project_blowing():
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
        project_ofc_make_and_size=request.form['ofc_make_and_size']


        new_project_site=Project_description_tfiber_blowing(msi=project_msi_name,measurement_book_no=project_mb_no,
        sheet_no=project_sheet_no,pop_type=project_pop_type,zone=project_zone,
        mandal=project_mandal,gp_name=project_gp_name,
        ring_id=project_ring_id,span_id=project_span_id,abd=project_abd,ofc_make_and_size=project_ofc_make_and_size)
        # print(new_project_site.span_id)

        try:
            db.session.add(new_project_site)  # Add new_task in database
            db.session.commit()  # Commit the database
            return redirect('/TFiber_Blowing_Measurement/{}'.format(new_project_site.span_id)) # Redirect to Project_Site webpage
        except:
            return 'There was an issue adding your task'
    else:

        return render_template('project_tfiber_blowing.html')




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

@app.route("/TFiber_DIT_Measurement/<string:span_id>", methods=['POST','GET'])
def tfiber_dit_measurement(span_id):
    if request.method=='POST':
        measurement_chainage_from=request.form['chainage_from']
        measurement_chainage_to=request.form['chainage_to']
        measurement_chamber_from=request.form['chamber_from']
        measurement_chamber_to=request.form['chamber_to']
        measurement_length=request.form['length']
        measurement_air_test=request.form['air_test']
        measurement_sponge_test=request.form['sponge_test']
        measurement_shuttle_test=request.form['shuttle_test']
        measurement_pressure_test_5bar_30_min=request.form['pressure_test_5bar_30_min']
        measurement_pressure_test_10bar_10_min=request.form['pressure_test_10bar_10_min']
        measurement_pressure_test_10min_30_min=request.form['pressure_test_10min_30_min']
        measurement_drop_in_pressure=request.form['drop_in_pressure']
        measurement_test_result=request.form['test_result']
        measurement_coupler_loc=request.form['coupler_loc']
        measurement_mb_duct_from=request.form['mb_duct_from']
        measurement_mb_duct_to=request.form['mb_duct_to']
        measurement_mb_duct_len=request.form['mb_duct_len']
        measurement_remark=request.form['remark']
        
        new_measurement=TFiber_DIT_Measurement(chainage_from=measurement_chainage_from,chainage_to=measurement_chainage_to,
        chamber_from=measurement_chamber_from,chamber_to=measurement_chamber_to,length=measurement_length,
        air_test=measurement_air_test,sponge_test=measurement_sponge_test,shuttle_test=measurement_shuttle_test,
        pressure_test_5bar_30_min=measurement_pressure_test_5bar_30_min,pressure_test_10bar_10_min=measurement_pressure_test_10bar_10_min,
        pressure_test_10min_30_min=measurement_pressure_test_10min_30_min,drop_in_pressure=measurement_drop_in_pressure,
        test_result=measurement_test_result,coupler_loc=measurement_coupler_loc,mb_duct_from=measurement_mb_duct_from,
        mb_duct_to=measurement_mb_duct_to,mb_duct_len=measurement_mb_duct_len,remark=measurement_remark,span_id=span_id)

        try:
            db.session.add(new_measurement)  # Add new_task in database
            db.session.commit()  # Commit the database
            return redirect('/TFiber_DIT_Measurement/{}'.format(span_id)) # Redirect to Measurement webpage
        except:
            return 'There was an issue adding your task'

    return render_template('tfiber_dit_measurement.html',span_id=span_id)


@app.route("/TFiber_DRT_Measurement/<string:span_id>", methods=['POST','GET'])
def tfiber_drt_measurement(span_id):
    if request.method=='POST':
        measurement_chamber1_lat=request.form['chamber1_lat']
        measurement_chamber1_long=request.form['chamber1_long']
        measurement_chamber1_condition=request.form['chamber1_condition']
        measurement_chamber1_route_marker_avail=request.form['chamber1_route_marker_avail']
        measurement_chamber2_lat=request.form['chamber2_lat']
        measurement_chamber2_long=request.form['chamber2_long']
        measurement_chamber2_condition=request.form['chamber2_condition']
        measurement_chamber2_route_marker_avail=request.form['chamber2_route_marker_avail']
        measurement_ch_from=request.form['ch_from']
        measurement_ch_to=request.form['ch_to']
        measurement_duct_len=request.form['duct_len']
        measurement_mb_duct_dam_lat=request.form['mb_duct_dam_lat']
        measurement_mb_duct_dam_long=request.form['mb_duct_dam_long']
        measurement_mb_duct_dam_ch_from=request.form['mb_duct_dam_ch_from']
        measurement_mb_duct_dam_ch_to=request.form['mb_duct_dam_ch_to']
        measurement_mb_duct_dam_len=request.form['mb_duct_dam_len']
        measurement_mb_duct_mis_lat=request.form['mb_duct_mis_lat']
        measurement_mb_duct_mis_long=request.form['mb_duct_mis_long']
        measurement_mb_duct_mis_ch_from=request.form['mb_duct_mis_ch_from']
        measurement_mb_duct_mis_ch_to=request.form['mb_duct_mis_ch_to']
        measurement_mb_duct_mis_len=request.form['mb_duct_mis_len']
        measurement_remarks=request.form['remarks']

        new_measurement=TFiber_DRT_Measurement(chamber1_lat=measurement_chamber1_lat,chamber1_long=measurement_chamber1_long,
        chamber1_condition=measurement_chamber1_condition,chamber1_route_marker_avail=measurement_chamber1_route_marker_avail,
        ch_from=measurement_ch_from,ch_to=measurement_ch_to,duct_len=measurement_duct_len,
        chamber2_lat=measurement_chamber2_lat,chamber2_long=measurement_chamber2_long,chamber2_condition=measurement_chamber2_condition,
        chamber2_route_marker_avail=measurement_chamber2_route_marker_avail,mb_duct_dam_lat=measurement_mb_duct_dam_lat,
        mb_duct_dam_long=measurement_mb_duct_dam_long,mb_duct_dam_ch_from=measurement_mb_duct_dam_ch_from,
        mb_duct_dam_ch_to=measurement_mb_duct_dam_ch_to,mb_duct_dam_len=measurement_mb_duct_dam_len,mb_duct_mis_lat=measurement_mb_duct_mis_lat,
        mb_duct_mis_long=measurement_mb_duct_mis_long,mb_duct_mis_ch_from=measurement_mb_duct_mis_ch_from,mb_duct_mis_ch_to=measurement_mb_duct_mis_ch_to,
        mb_duct_mis_len=measurement_mb_duct_mis_len,remarks=measurement_remarks,span_id=span_id)

        try:
            db.session.add(new_measurement)  # Add new_task in database
            db.session.commit()  # Commit the database
            return redirect('/TFiber_DRT_Measurement/{}'.format(span_id)) # Redirect to Measurement webpage
        except:
            return 'There was an issue adding your task'

    return render_template('tfiber_drt_measurement.html',span_id=span_id)


@app.route("/TFiber_Blowing_Measurement/<string:span_id>", methods=['POST','GET'])
def tfiber_blowing_measurement(span_id):
    if request.method=='POST':
        measurement_chamber_from=request.form['chamber_from']
        measurement_chamber_to=request.form['chamber_to']
        measurement_ch_from=request.form['ch_from']
        measurement_ch_to=request.form['ch_to']
        measurement_length=request.form['length']
        measurement_size_of_ofc=request.form['size_of_ofc']
        measurement_ofc_cable_id=request.form['ofc_cable_id']
        measurement_cable_start=request.form['cable_start']
        measurement_cable_end=request.form['cable_end']
        measurement_cable_len=request.form['cable_len']
        measurement_mh_a_cable_end=request.form['mh_a_cable_end']
        measurement_mh_a_cable_entry=request.form['mh_a_cable_entry']
        measurement_mh_a_slack_cable_len=request.form['mh_a_slack_cable_len']
        measurement_mh_b_cable_entry=request.form['mh_b_cable_entry']
        measurement_mh_b_cable_end=request.form['mh_b_cable_end']
        measurement_mh_b_slack_cable_len=request.form['mh_b_slack_cable_len']
        
        measurement_remarks=request.form['remarks']

        new_measurement=TFiber_Blowing_Measurement(chamber_from=measurement_chamber_from,chamber_to=measurement_chamber_to,
        ch_from=measurement_ch_from,ch_to=measurement_ch_to,length=measurement_length,size_of_ofc=measurement_size_of_ofc,
        ofc_cable_id=measurement_ofc_cable_id,cable_start=measurement_cable_start,cable_end=measurement_cable_end,
        cable_len=measurement_cable_len,mh_a_cable_end=measurement_mh_a_cable_end,mh_a_cable_entry=measurement_mh_a_cable_entry,
        mh_a_slack_cable_len=measurement_mh_a_slack_cable_len,mh_b_cable_entry=measurement_mh_b_cable_entry,
        mh_b_cable_end=measurement_mh_b_cable_end,mh_b_slack_cable_len=measurement_mh_b_slack_cable_len,
        remarks=measurement_remarks,span_id=span_id)

        try:
            db.session.add(new_measurement)  # Add new_task in database
            db.session.commit()  # Commit the database
            return redirect('/TFiber_Blowing_Measurement/{}'.format(span_id)) # Redirect to Measurement webpage
        except:
            return 'There was an issue adding your task'

    return render_template('tfiber_blowing_measurement.html',span_id=span_id)
        




# if database does not exist in the current directory, create it!
db_is_new = not os.path.exists('mb.db')
if db_is_new:
    create_the_database(db)

if __name__=='__main__':
    app.run(debug=True, port=8000)
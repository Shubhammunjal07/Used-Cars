from dff import get_carsname, get_company, get_fuel, get_owner, get_sellertype, get_year
from flask import Flask, render_template, request, redirect, url_for
import numpy as np
import pandas as pd

app = Flask(__name__)

@app.route("/")
def index():
     return render_template("index.html")

@app.route("/home/")
def home():
    return render_template("index.html")

@app.route("/visualization")
def visualization() :
    return render_template("visualization.html")

@app.route("/visualize_graph/" , methods=['GET', 'POST'])
def visualize_graph():
    
    if request.method == "POST":
        barplot = request.form.get('barplot', 'off')
        boxplot = request.form.get('boxplot', 'off')
        piechart = request.form.get('piechart', 'off')
        countplot_distplot = request.form.get('countplot_distplot', 'off')
        jointplot = request.form.get('jointplot', 'off')

    # Check which checkbox is on

    if barplot == "on":
        return render_template("barplot.html")

    elif boxplot == "on":
        return render_template("boxplot.html")

    elif piechart == "on":
        return render_template("piechart.html")

    elif countplot_distplot == "on":
        return render_template("count_distplot.html")

    elif jointplot == "on":
        return render_template("jointplot.html")    
    
    else:
        return ('Select anyone switch button')


@app.route("/analysiss")
def analysiss():
    years = get_year
    companys = get_company()
    cars = get_carsname()
    owners = get_owner()
    sellers = get_sellertype()
    fuels = get_fuel()
    return render_template("analysis.html", years=years, companys=companys, cars=cars, owners=owners, sellers=sellers, fuels=fuels)

def filter_data(years,companys, cars, owners, sellers, fuels,kmdriven):
    temp = pd.read_csv("../used_cars.csv", index_col = 0)
    if years:
        temp = temp[temp['year'].apply(lambda x:True if years == int(x) else False)]
    if companys:
        temp = temp[temp['company'].apply(lambda x:True if companys.lower() in str(x).lower() else False)]
    if cars:
        temp = temp[temp['cars_name'].apply(lambda x:True if cars.lower() in str(x).lower() else False)]
    if owners:
        temp = temp[temp['owner'].apply(lambda x:True if owners.lower() in str(x).lower() else False)]
    if sellers:
        temp = temp[temp['seller_type'].apply(lambda x:True if sellers.lower() in str(x).lower() else False)]
    if fuels:
        temp = temp[temp['fuel'].apply(lambda x:True if fuels.lower() in str(x).lower() else False)]
    if kmdriven:
        temp = temp[temp['km_driven'].apply(lambda x:True if int(kmdriven) == int(x) else False)]
    
    return temp.to_html()
    

@app.route("/analysis/", methods=['GET', 'POST'])
def analysis():
    if request.method == "POST":
        years = request.form.get('years')
        companys = request.form.get("companys")
        cars = request.form.get("cars")
        owners = request.form.get("owners")
        sellers = request.form.get("sellers")
        fuels = request.form.get("fuels")
        kmdriven = request.form.get("kmdriven")
        
        return filter_data(years,companys,cars, owners, sellers, fuels, kmdriven)
    return redirect(url_for("index")) 
app.run(host='localhost', port=5000, debug=True)
from app import app, db


@app.route("/")
def status():
    return "OK"


@app.route("/probes/liveness")
def liveness():
    return "Ok"


@app.route("/neo", methods=['POST'])
def neo():
    content_dict = request.json
    print("content is ", content_dict)

    close_approach_date = content_dict["close_approach_date"]

    datetime_object = datetime.strptime(close_approach_date, '%Y-%b-%d %H:%M')

    neo_obj = NEO(id=content_dict["id"],
                  name=content_dict["name"],
                  nasa_jpl_url=content_dict["nasa_jpl_url"],
                  close_approach_date=datetime_object,
                  is_potentially_hazardous_asteroid=content_dict["is_potentially_hazardous_asteroid"])

    db.session.add(neo_obj)
    db.session.commit()

    return "OK"


@app.route("/neo/week", methods=['GET'])
def neo_count_this_week():
    today = date.today()
    start = today - timedelta(days=today.weekday())
    end = start + timedelta(days=6)
    count = NEO.query.filter(start <= NEO.close_approach_date, NEO.close_approach_date <= end).count()
    return {"count": count}


@app.route("/neo/next", methods=['GET'])
def neo_next():
    hazardous = request.args.get("hazardous")
    today = date.today()
    all_next = NEO.query.filter(NEO.close_approach_date > today)
    if hazardous == "true":
        all_next = all_next.filter(NEO.is_potentially_hazardous_asteroid == True)
    next = all_next.first()
    return next.serialize()





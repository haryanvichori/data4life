"""
This file (test_models.py) contains the unit tests for the models.py file.
"""
from datetime import datetime

from datamodels import NEO


def test_new_neo():
    datetime_obj = datetime.strptime("2015-Sep-08 20:28", '%Y-%b-%d %H:%M')
    neo_id = 2465633
    name = "465633 (2009 JR5)"
    nasa_jpl_url = "http://ssd.jpl.nasa.gov/sbdb.cgi?sstr=2465633"
    is_potentially_hazardous_asteroid = True

    neo_obj = NEO(id=neo_id,
                  name=name,
                  nasa_jpl_url=nasa_jpl_url,
                  close_approach_date=datetime_obj,
                  is_potentially_hazardous_asteroid=is_potentially_hazardous_asteroid)
    assert neo_obj.id == 2465633
    assert neo_obj.name == name
    assert neo_obj.nasa_jpl_url == nasa_jpl_url
    assert neo_obj.is_potentially_hazardous_asteroid == is_potentially_hazardous_asteroid

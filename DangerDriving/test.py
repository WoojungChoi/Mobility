import influxdb
import pandas as pd
from dangerdriving import Dangerdriving

def loaddata_influxdb(_database_name, _measurement_name, start_time, end_time, car_id):

    client = influxdb.DataFrameClient(host='125.140.110.217',
                                      port=8999,
                                      username='wjchoi',
                                      password='wjchoi',
                                      database=_database_name)

    _query = 'SELECT DRIVE_SPEED, GPS_LAT, GPS_LONG, time FROM "%s"' % _measurement_name + " WHERE time >= '%s' and time < '%s' and car_id = '%s'" % (start_time, end_time, car_id)
    print(_query)
    _query_result = client.query(_query)

    df = _query_result[_measurement_name]
    df = df.reset_index().rename(columns={"index": "RECORD_TIME"})
    print(len(df), 'data loaded')

    return df.to_dict()



if __name__ == "__main__":

    database = 'SAMPYO_MONIT'
    measurement = 'MAIN2'

    # 차량번호를 입력해주세요.
    car_id = '01225797291'

    # 시작일자 종료일자를 입력해주세요.
    time_s = '2020-04-11T22:10:00Z'
    time_e = '2020-04-13T00:10:00Z'

    # 데이터를 로드한 후 csv 파일(차량번호.csv)로 저장합니다.
    dataset = pd.DataFrame(loaddata_influxdb(database, measurement, time_s, time_e, car_id))

    example = Dangerdriving(dataset=dataset, type='TRUCK')
    AC = example.AC()
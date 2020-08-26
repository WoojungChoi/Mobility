# -*- coding:utf-8 -*-

"""
    Title : dangerdriving.py
    Comment : 급가속 급감속 모듈
    Author : 최우정 / github : https://github.com/woojungchoi
    Last working date : 2020/08/14
"""

import pandas as pd
import json
import sys

class Dangerdriving:
    """
    8대 위험운전 항목
    1)급가속 = AC(Accelerate)
    2)급출발 = QS(Quick Start)
    3)급감속 = DC(Decelerate)
    4)급정지 = SS(Sudden Stop)
    5)급차로변경 = LC(Lane Change)
    6)급앞지르기 = OT(Overtaking)
    7)급회전 = ST(Sharp Turn)
    8)급유턴 = UT(U-Tern)

    운행 데이터의 input 타입 정의

    etc.
    초당 회전각 60도 이상 예외처리
    속도 0이상에서 좌표값이 변경되지 않을 시 터널로 판정하여 예외처리
    운행기록장치에서 GPS 오류코드 수신 시 예외처리
    """

    """vehicle type: TRUCK / BUS / TAXI"""
    def datatypecheck(self):
        typecheck = type(self.dataset)
        if str(typecheck) != '<class \'pandas.core.frame.DataFrame\'>':
            print('error: wrong dataset datetype')
            sys.exit()

    def datatypecheck(self):


    def __init__(self, dataset, type):
        self.dataset = dataset

        #데이터셋 데이터타입 확인
        self.datatypecheck()

        #데이터셋 데이터타입 변환
        

        #데이터셋 시간 datetime 체크
        if (type(dataset[0]['time'])==0):
            print('시간 데이터셋 타입은 datetime이여야 합니다.')

        with open('vehicle_type.json') as json_file:
            vehicle_type = json.load(json_file)

        print(vehicle_type)

        #운행 데이터셋
        self.len = len(dataset)

        #차량 타입
        self.type = type

        #위험항목 저장 리스트
        self.dangerlist = []


    def __gettimedifference(self, sp, ep):
        timediff = (ep - sp).total_seconds()

        return timediff


    '''
    def AC(self):
        s = 0
        outbool = False

        while s < self.len:
            #start point
            sp = (self.dataset[s]['DRIVE_SPEED'], self.dataset[s]['time'])

            e = s + 1
            if e == self.len: break
            #end point
            ep = (self.dataset[e]['DRIVE_SPEED'], self.dataset[e]['time'])


            diff = (ep[0]-sp[0]) / self.__gettimedifference(sp[1], ep[1])

            if diff <= ""


            s+=1











    i = 0
    j = 0
    outbool = False
    status = 'N'

    while i < len(self.dict['RECORD_TIME']) - 1:
        point_s = (self.dict['DRIVE_SPEED'][i], self.dict['RECORD_TIME'][i])

        if j >= len(self.dict['RECORD_TIME']) - 1: break
        if i >= len(self.dict['RECORD_TIME']) - 2: break

        j = i + 1
        # print('i:', i, 'j:', j, '    147')

        while j <= len(self.dict['RECORD_TIME']) - 1:

            point_e = (self.dict['DRIVE_SPEED'][j], self.dict['RECORD_TIME'][j])

            try:
                # 시간차이 = 0 -> 분모 = 0 -> error 발생
                diff = (point_e[0] - point_s[0]) / self.__gettimedifference(point_e[1], point_s[1])
            except:
                j += 1
                # print('i:',i,'j:',j, '    160')
                continue

            """위험운행 조건 시작"""
            if diff <= -8:
                # 감속 O
                if point_e[0] >= 6:
                    # 급감속
                    status = 'D'
                else:
                    # 급정지
                    status = 'S'
            else:
                # 감속 X
                if diff >= 5:
                    # 가속 O
                    if point_s[0] >= 6:
                        # 급가속 O
                        status = 'A'
                    else:
                        # 급가속 X
                        if diff >= 6:
                            # 급출발
                            status = 'Q'
                        else:
                            # 상태 X
                            outbool = True
                else:
                    # 상태 X
                    outbool = True

            """위험운행 조건 끝"""
            if outbool == True:
                if status != 'N':
                    """저장"""
                    self.danger_list.append([i, j - 1, status])
                """초기화"""
                status = 'N'
                i = j
                # print('i:', i, 'j:', j,'    199')
                outbool = False
                break

            """j값 증가 후 iter 반복"""
            j += 1
            # print('i:',i,'j:', j, '    205')

    return dangerlist
    '''


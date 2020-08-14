# -*- coding:utf-8 -*-

"""
    Title : dangerdriving.py
    Comment : 급가속 급감속 모듈
    Author : 최우정 / github : https://github.com/woojungchoi
    Last working date : 2020/08/14
"""

import pandas as pd

class dangerdriving:
    """
    8대 위험운전 항목
    급가속 = AC(Accelerate), 급출발 = QS(Quick Start), 급감속 = DC(Decelerate), 급정지 = SS(Sudden Stop)
    급차로변경 = LC(Lane Change)  급앞지르기 = OT(Overtaking) 급회전 = ST(Sharp Turn) 급유턴 = UT(U-Tern)

    초당 회전각 60도 이상 예외처리
    속도 0이상에서 좌표값이 변경되지 않을 시 터널로 판정하여 예외처리
    운행기록장치에서 GPS 오류코드 수신 시 예외처리

    """

    """vehicle type truck bus taxi"""

    def __init__(self, dataset, type):
        self.dataset= dataset
        self.type = type
        self.dangerlist = []

        if type == 'truck':
            AC = 5
            QS = 6
            DC = 8
            SS = 8
            LC = 6
            OT = 6
            ST_SPEED = 20
            ST_TIME = 4
            UT_SPEED = 15
            UT_TIME = 8

        elif type == 'bus':
            AC = 6
            QS = 8
            DC = 9
            SS = 9
            LC = 8
            OT = 8
            ST_SPEED = 25
            ST_TIME = 4
            UT_SPEED = 20
            UT_TIME = 8

        elif type == 'taxi':
            AC = 8
            QS = 10
            DC = 14
            SS = 14
            LC = 10
            OT = 10
            ST_SPEED = 30
            ST_TIME = 3
            UT_SPEED = 25
            UT_TIME = 6

        else:
            print('잘못된 vehicle type 형식입니다.\n truck bus taxi 중에서 선택해주세요')


    def AC(self):

        i = 0
        j = 0
        outbool = False














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

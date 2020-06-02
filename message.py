def message(code, message, param):
    return dict(code=code, message=message, param=param)

def messageMaker(c, _id = []):
    switcher={
        100 : message(100, 'IC-Authcon', _id),
        101 : message(101, 'IC-Auth', _id),
        102 : message(102, 'IC-Authclose', _id),
        103 : message(103, 'IC-Control_addID', _id),
        104 : message(104, 'IC-Control_addIDass', _id),
        105 : message(105, 'IC-Control_sendKey', _id),
        106 : message(106, 'IC-IDF_sendDD', _id),
        107 : message(107, 'IC-IDF_sendToServer', _id),
        108 : message(108, 'IC-IDF_send', _id),
        200 : message(200, 'IC-AuthconSuccess', _id),
        201 : message(201, 'IC-AuthSuccess', _id),
        202 : message(202, 'IC-AuthClose', _id),
        203 : message(203, 'IC-AuthconFail',_id),
        204 : message(204, 'IC-AuthFail', _id),
        205 : message(205, 'IC-AuthCloseFail', _id),
        206 : message(206, 'IC-Control_addStart', _id),
        207 : message(207, 'IC-Control_IdRequest', _id),
        208 : message(208, 'IC-Control_KeySuccess', _id),
        209 : message(209, 'IC-Control_addFail', _id),
        210 : message(210, 'IC-Control_IDFail', _id),
        211 : message(211, 'IC-Control_KeyFail', _id),
        407 : message(407, 'IC-IDF_OverFlow', _id),
        216 : message(216, 'IC-IDF_Error', _id),
        217 : message(217, 'IC-IDF_ServerDError', _id),
        218 : message(218, 'IC-IDF_ServerError', _id),
        219 : message(219, 'IC-IDF_Success', _id),
        220 : message(220, 'IC-IDF_ServerDSuccess', _id),
        221 : message(221, 'IC-IDF_ServerSuccess', _id)
    }
    return switcher.get(c, None)
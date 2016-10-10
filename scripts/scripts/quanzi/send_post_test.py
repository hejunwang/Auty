# -*- coding: utf-8 -*-
import sys
import os
import requests
from utils.execute_sql_mysql import exec_sql
from utils.sql_info import qz_host,qz_user,qz_pwd,qz_db_name
from utils.get_lottery_session_id import get_lottery_session_id
import json

def send_post_test(accountId):
	s = requests.Session()
	url = 'http://quanzi.caipiao.163.com/circle_sendPosts.html'
	#sql = 'select column_name from information_schema.columns where table_name = \'ts_user_info\''
	#Get userId from mysql db ts_user_info.
	sql = 'select userid from ts_user_info where email = \''+accountId+'\''
	r = exec_sql(sql,qz_host,qz_user,qz_pwd,qz_db_name)
	userId = r[0][0]
	#print 'userId:'+str(userId)
	#print 'userToken:'+str(get_lottery_session_id(accountId))
	data = {
		'userId':userId,
		'category':'4',
		'text':'Tylan python send_post_test',
		'postType':'1',
		'userToken':get_lottery_session_id(accountId),
		'boardId':'12'
	}
	r = s.post(url, data = data)
	#print r.content
	basic_assert(r)

def basic_assert(r):
	jsonResult = json.loads(r.content)
	assert jsonResult['resultDesc'] == u"发帖成功!"
	assert jsonResult['result'] == 100

if __name__ == '__main__':
    send_post_test('runcheck5@163.com')
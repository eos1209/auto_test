'''
@Created by yuhsiang
@Date : 2019/11/18
'''

# 測試帳密 For AB005
Master_Account = 'QAautomation'
Master_Password = '123456'

# 測試帳密 For AB007
# Master_Account = 'QA3'
# Master_Password = 'a123456'

# 測試環境 For AB005 Master Headers
Get_Mater_Headers = {'X-Requested-With': "XMLHttpRequest"}
Post_Master_Headers = {'Content-Type': "application/json", 'X-Requested-With': "XMLHttpRequest"}
Post_headers_upLoadFile = {'X-Requested-With': "XMLHttpRequest"}

# 新增會員-不存在的代理
no_exist_agent = 'DS_a_player'

# 總存取款匯出 決定 以月匯出 還是 以日匯出
# 1:月，#0:日
switch_month_day = 1

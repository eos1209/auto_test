'''
@Created by yuhsiang
@Date : 2019/11/18
'''

# 測試帳密 For AB005
Master_Account = 'QAautomation'
Master_Password = '123456'
Test_Account = 'QAUser'

# 測試環境 For AB005
Master_url = 'http://master.fnjtd.com'
Portal_url = 'http://www.fnjtd.com'

# 測試環境 For AB005 Master Headers
Get_Mater_Headers = {'X-Requested-With': "XMLHttpRequest"}
Post_Master_Headers = {'Content-Type': "application/json", 'X-Requested-With': "XMLHttpRequest"}
Post_headers_upLoadFile = {'X-Requested-With': "XMLHttpRequest"}

# 測試會員
Account = 'DS_player4'
# 測試批次會員
batchAccount = 'QATEST,DS,DS_player4,DS_player8'

# 新增會員-已存在的代理
exist_agent = 'QA_Test_D'
# 新增會員-不存在的代理
no_exist_agent = 'DS_a_player'
# 新增代理商 - 已存在的總代理
exist_Lv3_agent = 'QA_Test_C'
# 新增代理商 - 已存在的股東
exist_Lv2_agent = 'QA_Test_B'
# 新增代理商 - 已存在的大股東
exist_Lv1_agent = 'QA_Test_A'

# 總存取款匯出 決定 以月匯出 還是 以日匯出
# 1:月，#0:日
switch_month_day = 1


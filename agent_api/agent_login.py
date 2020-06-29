'''
@Created by loka
@Date : 2020/06/09
'''
from base.agent_httpReuest import Agent_Http
from data_config.agent_config import agent_Account, agent_Password, Post_Agent_Headers
from data_config.system_config import systemSetting


def agent_login():  # getCookie
    http = Agent_Http()
    data = {'account': agent_Account, 'password': agent_Password}
    response_data = http.post_login(systemSetting().agent_link() + '/Account/login', data, {}, {})
    return response_data[2]


def connectionId():  # getCookie
    http = Agent_Http()
    data = {}
    response_data = http.post(systemSetting().agent_link() + '/signalr/negotiate', data, {}, {})
    return response_data[1]['ConnectionId']

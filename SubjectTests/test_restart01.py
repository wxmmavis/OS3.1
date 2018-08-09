import time,os,logging,configparser,paramiko
import sys
sys.path.append("..")
from tools import *

def case():
    t = tools()
    projectPath = os.path.dirname(os.getcwd())
    configFile = projectPath + '/configure/' + 'testconfig.ini'
    filename = os.path.basename(__file__).split('.')[0]
    t.log(filename)
    logging.info(__file__)
    config = configparser.ConfigParser()
    config.read(configFile, encoding='UTF-8')
    default_ip = config.get('Default', 'default_ip')
    default_pw = config.get('Default', 'default_pw')
    cmd = ["ubus call xapi.system reboot '{}'"]
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(default_ip, 22 , "root", default_pw)
    stdin, stdout, stderr = ssh.exec_command(cmd)

case()
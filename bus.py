#!/usr/local/bin/python2.7
# -*- coding: utf8 -*-
import os
import re
import sys
import codecs
import config
import urllib2
import commands
import traceback
import cx_Oracle
from metaData import *
from datetime import datetime
from xml.dom.minidom import *
from HTMLParser import HTMLParser

os.environ["NLS_LANG"] = ".UTF8"
TAG_RE = re.compile(r'<[^>]+>')
exp = re.compile('charset=(.*?)"')


class Bus:
    def __init__(self):  # В конструкторе инициализируются основные переменные класса
        self.appdate = str(datetime.now())[0:19].replace(" ", "_").replace(":", "-")  # Текущая дата_время
        self.location = "SC_GetChanges_Logs"  # Название папки с логами
        self.process, self.sc_req, self.skuf_req = "", "", ""  # Переменная процесса, номера в сц, номера в скуф
        self.connection, self.cursor = None, None  # Перменные подклюения к БД
        self.arguments = {}  # Универсальный словарь аргументов
        self.logs_directory = os.path.join(os.path.dirname(os.path.realpath(__file__)), self.location)

    @staticmethod
    def send_req(req, timeout):  # Метод отправки запроса через urllib2, принимает инстанс запрос и таймаут
        return urllib2.urlopen(req, timeout=timeout)

    @staticmethod
    def get_values_by_tag_name(raw_xml, tag_name):  # Метод парсинга xml, принимает на вход название тега
        parsed_xml = parseString(raw_xml).getElementsByTagName(tag_name)
        return [i.childNodes[0].nodeValue for i in parsed_xml]

    @staticmethod
    def create_req_instance(request, soap_action=None, url=None):  # Метод создания инстанса запроса к urllib2,
        req = urllib2.Request(url=url, data=request.encode("utf-8"))
        req.add_header('Content-Type', 'text/xml;charset=UTF-8')
        req.add_header('SOAPAction', soap_action)
        return req

    @staticmethod
    def remove_quotes(text):  # Удаление сец символов
        return re.sub("[;'~{}]", '', text).replace('<![CDATA[', '').replace(']]>', '')

    @staticmethod
    def write_process(text, stat, var1, var2=""):  # Унифицированный метод записи строки в файл, принимает строку
        try:                                       # статус процесса, предыдущий текст процесса и traceback, если
            if stat == 0:                          # stat = 1 (логируем ошибку)
                return var1 + text + '\n'
            elif stat == 1:
                return var1 + text + '\n' + var2 + '\n'
        except Exception as err:
            return "error creating process text " + var1 + '\n' + traceback.format_exc()

    @staticmethod
    def stop_if_already_running(script_name):  # Метод для проверки наличия процесса в памяти с именем script_name
        l = commands.getstatusoutput("ps aux | grep -e '%s' | grep -v grep | awk '{print $2}'" % script_name)
        print l[1]
        if l[1]:
            print "Already running"
            sys.exit(1)

    @staticmethod
    def continue_if_running(script_name):  # Метод для проверки наличия процесса в памяти с именем script_name
        l = commands.getstatusoutput("ps aux | grep -e '%s' | grep -v grep | awk '{print $2}'" % script_name)
        print l[1]
        if l[1]:
            return True
        else:
            return False

    @staticmethod
    def return_db_connection():  # Метод по созданию соедения с БД oracle. Параметры подключения берет из config.py
        tns = cx_Oracle.makedsn(config.db_ip, 1521, service_name=config.db_service_name)
        connection = cx_Oracle.connect(config.db_login, config.dp_pass, tns)
        return connection, connection.cursor()

    def log_process(self, text, number=''):  # Метод логирования процесса
        try:
            if not os.path.exists(self.logs_directory):
                os.makedirs(self.logs_directory)
            log = codecs.open(os.path.join(self.logs_directory, number + "_" + self.appdate + "_" + "process_logs.xml"), 'w')
            log.write(text)
            log.close()
        except Exception as err:
            if not os.path.exists(self.logs_directory):
                os.makedirs(self.logs_directory)
            log = codecs.open(os.path.join(self.logs_directory, number + "_" + self.appdate + "_" + "process_logs.xml"), 'w')
            log.write("Log process creation error " + '\n' + str(err))
            log.close()

    def create_db_connection(self):  # Метод для созданию соедения с БД oracle. Параметры подключения берет из config.py
        tns = cx_Oracle.makedsn(config.db_ip, 1521, service_name=config.db_service_name)
        self.connection = cx_Oracle.connect(config.db_login, config.dp_pass, tns)
        self.cursor = self.connection.cursor()

    def send_database_request(self, sql):  # Метод отправки запроса в БД по ранее созданным коннектам
        self.cursor.arraysize = 1000
        self.cursor.execute(sql)
        self.connection.commit()
        return self.cursor

    def logger(self, message, msg_type, operation_name, counter, msg_id):  # Метод логирования soap пакетов
        try:
            try:
                if msg_type == 'RESPONSE' and operation_name != 'GetStats' and operation_name != 'GetEvents':
                    pars = HTMLParser()
                    message = pars.unescape(message)
                    message = unicode(message, 'utf-8')
                if msg_type == 'RESPONSE' and operation_name == 'GetEvents':
                    message = unicode(message, 'utf-8')
                else:
                    message = unicode(message, 'utf-8')
            except:
                pars = HTMLParser()
                message = pars.unescape(message)
            if not os.path.exists(self.logs_directory):
                os.makedirs(self.logs_directory)
            log = codecs.open(os.path.join(self.logs_directory, msg_id + "_" + self.appdate + "_" + operation_name +
                              "_OperationLog.xml"), 'a', encoding='utf8')
            log.write("--------------Start of " + msg_type + " - Transaction Number is " + str(counter) +
                      "--------------------\n" + message)
            log.write("\n--------------End of " + msg_type + "- Transaction Number is " + str(counter) +
                      "--------------------\n")
            log.close()
            return "Success creating LOG " + operation_name + " - " + msg_type + ": "
        except Exception:
            return "Failure creating LOG " + operation_name + " - " + msg_type + ": " + '\n' + traceback.format_exc()

    @staticmethod
    def replace_html_chars(text):  # Метод для удаления html спец символов. Список символов объявлен в metaData.py
        for elem in html_chars:
            text = text.replace(elem, "")
        return text

    @staticmethod
    def func_unicode_or_lob(x):
        if isinstance(x, cx_Oracle.LOB):
            return unicode(x.read(), 'utf-8')
        if isinstance(x, str):
            return unicode(x, 'utf-8')
        return unicode(str(x).replace('None', ''), 'utf-8')

    def fetch_response_from_db(self, cursor):
        var = [ list(map(self.func_unicode_or_lob, x))[0] for x in cursor ]
        return var

    def fetch_response_from_db_v2(self, cursor):
        var = [ list(map(self.func_unicode_or_lob, x)) for x in cursor ]
        return var

    @staticmethod
    def node_val(node):
        return node[0].childNodes[0].nodeValue.rstrip().lstrip()

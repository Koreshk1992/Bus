#!/usr/local/bin/python2.7
# -*- coding: utf8 -*-
import sys
import urllib2
import traceback
from metaData import *
#from pyremedy import ARS, ARSError


def get_changes_error_handler(func_to_handle):  # Функция декоратор, для обработки внештатных ситуация
    def handler(self):
        try:
            func_to_handle(self)
            return func_to_handle
        except urllib2.HTTPError as error:  # Обработчик http ошибок

            self.process = self.write_process(self.logger(str(error.read()), "RESPONSE", self.current_method, 0,
                                              self.event_id), 0, self.process)
            self.process = self.write_process("Error sending", 1, self.process, traceback.format_exc())
            self.send_database_request(insert_error.format(self.remove_quotes(traceback.format_exc()), self.event_id, "GetChangesProcess"))
            self.log_process(self.process, self.event_id)
        except Exception as error:  # Обобщенный обработчик, если ни один из верхнеуровневых не подошел
            self.condition = True
            self.process = self.write_process("Ups, something went wrong, investigation needed..." +
                                              '\n' + str(error) + '\n' + traceback.format_exc(), 0, self.process)
            self.log_process(self.process, self.event_id)
            self.send_database_request(insert_error.format(self.remove_quotes(traceback.format_exc()), self.event_id, "GetChangesProcess"))
    return handler


def main_error_handler(func_to_handle):
    def handler(self):
        try:
            func_to_handle(self)
            return func_to_handle
        except urllib2.HTTPError as error:
            self.process = self.write_process(self.logger(str(error.read()), "RESPONSE", self.current_method, 0,
                                              self.event_id), 0, self.process)
            self.process = self.write_process("Error sending", 1, self.process, traceback.format_exc())
            self.send_database_request(insert_error.format(self.remove_quotes(traceback.format_exc()), self.event_id, "GetTasksFromScProcess"))
            self.log_process(self.process, self.event_id)
            sys.exit(0)       
        except Exception as error:
            self.process = self.write_process("Ups, something went wrong, investigation needed..." +
                                              '\n' + str(error) + '\n' + traceback.format_exc(), 0, self.process)
            self.log_process(self.process, self.event_id)
            self.send_database_request(insert_error.format(self.remove_quotes(traceback.format_exc()), self.event_id, "GetTasksFromScProcess"))
            sys.exit(0)
    return handler


def pass_changes_error_handler(func_to_handle):  # Функция декоратор, для обработки внештатных ситуация
    def handler(self):
        try:
            func_to_handle(self)
            return func_to_handle
        except urllib2.HTTPError as error:  # Обработчик http ошибок
            response = error.read()
            self.process = self.write_process(self.logger(str(response), "RESPONSE", self.current_method, 0,
                                              self.event_id), 0, self.process)
            self.process = self.write_process("Error sending to SC", 1, self.process, traceback.format_exc())
            if u'находится в новом статусе' in unicode(response, 'utf-8'):
                self.process = self.write_process("Already in this status", 0, self.process)
                self.send_database_request(u_status.format(self.remove_quotes(self.process), self.event_id, "PassChangesProcess"))
                self.log_process(self.process, self.event_id)
                self.connection.close()
                sys.exit()
            if u"Закрыт' в статус" in unicode(response, 'utf-8'):
                self.process = self.write_process("Incident closed in SC", 0, self.process)
                self.send_database_request(u_status.format(self.remove_quotes(self.process), self.event_id, "PassChangesProcess"))
                self.log_process(self.process, self.event_id)
                self.connection.close()
                sys.exit()
            self.send_database_request(insert_error.format(self.remove_quotes(traceback.format_exc()), self.event_id, "PassChangesProcess"))
            self.log_process(self.process, self.event_id)
            self.connection.close()
            sys.exit()
        except Exception as error:  # Обобщенный обработчик, если ни один из верхнеуровневых не подошел
            self.process = self.write_process("Ups, something went wrong, investigation needed..." +
                                              '\n' + str(error) + '\n' + traceback.format_exc(), 0, self.process)
            self.log_process(self.process, self.event_id)
            self.send_database_request(insert_error.format(self.remove_quotes(traceback.format_exc()), self.event_id, "PassChangesProcess"))
            self.connection.close()
            sys.exit()
    return handler


def get_workers_error_handler(func_to_handle):  # Функция декоратор, для обработки внештатных ситуация
    def handler(self):
        try:
            func_to_handle(self)
            return func_to_handle
        except urllib2.HTTPError as error:  # Обработчик http ошибок
            self.state = 1
            self.process = self.write_process(self.logger(str(error.read()), "RESPONSE", "Workers", 0, ''), 0, self.process)
            self.process = self.write_process("Error sending to SKUF", 1, self.process, traceback.format_exc())
        except Exception as error:  # Обобщенный обработчик, если ни один из верхнеуровневых не подошел
            self.state = 1
            self.process = self.write_process("Ups, something went wrong, investigation needed..." +
                                              '\n' + str(error) + '\n' + traceback.format_exc(), 0, self.process)
    return handler


def pass_task_error_handler(func_to_handle):  # Функция декоратор, для обработки внештатных ситуация
    def handler(self):
        try:
            func_to_handle(self)
            return func_to_handle
        except urllib2.HTTPError as error:  # Обработчик http ошибок
            self.process = self.write_process(self.logger(str(error.read()), "RESPONSE", "Create", 0,
                                                self.ext_id), 0, self.process)
            self.process = self.write_process("Error sending to SC", 1, self.process, traceback.format_exc())
            self.log_process(self.process, self.ext_id)
            self.send_database_request(insert_error.format(self.remove_quotes(traceback.format_exc()), self.ext_id, "PassTasksProcess"))
            sys.exit()
        except Exception as error:  # Обобщенный обработчик, если ни один из верхнеуровневых не подошел
            self.process = self.write_process("Ups, something went wrong, investigation needed..." +
                                         '\n' + str(error) + '\n' + traceback.format_exc(), 0, self.process)
            self.log_process(self.process, self.ext_id)
            self.send_database_request(insert_error.format(self.remove_quotes(traceback.format_exc()), self.ext_id, "PassTasksProcess"))
            sys.exit()
    return handler


def check_author(self, xml_entry):
    if len(xml_entry.getElementsByTagName('Author')[0].childNodes) == 0:
        return 0
    author = xml_entry.getElementsByTagName('Author')[0].childNodes[0].nodeValue
    if author != u'employee$41110603':# and author != u'superUser$script' and author != u'superUser$eventActionProcessor' and author != self.team_id and author != u'superUser$system':
        return 1
    else:
        return 0


def check_duplicates(self, action_id):
    data = self.send_database_request(g_action_id.format(action_id))
    tmp = [x for x in data]
    if len(tmp):
        return 1
    else:
        return 0

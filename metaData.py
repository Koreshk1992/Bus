#!/usr/bin/python27
# -*- coding: utf8 -*-

# ---------------------------------------------Справочники------------------------------------------------------------ #
User = {0: "591e281d-cb3d-47fa-bf5c-8e11678106e8:employee$48562304",   # sc_agent@rtlabs.ru
        1: "591e281d-cb3d-47fa-bf5c-8e11678106e8:employee$48562305",   # sc_mon@rtlabs.ru
        2: "591e281d-cb3d-47fa-bf5c-8e11678106e8:employee$48562306",   # sc_pd@rtlabs.ru
        3: "591e281d-cb3d-47fa-bf5c-8e11678106e8:team$2282601",        # smev@gosuslugi.ru
        4: "591e281d-cb3d-47fa-bf5c-8e11678106e8:employee$3763605",    # support@gosuslugi.ru
        5: "591e281d-cb3d-47fa-bf5c-8e11678106e8:employee$41110603",   # skuf-sc@gosuslugi.ru
        6: "591e281d-cb3d-47fa-bf5c-8e11678106e8:team$2282602",        # esia_sc@gosuslugi.ru
        7: "591e281d-cb3d-47fa-bf5c-8e11678106e8:employee$8344601",    # reports@gosuslugi.ru
        8: "591e281d-cb3d-47fa-bf5c-8e11678106e8:employee$8355749",    # support-egov@rtlabs.ru
        9: "591e281d-cb3d-47fa-bf5c-8e11678106e8:team$50901501",       # top10_sc@rtlabs.ru
        10: "591e281d-cb3d-47fa-bf5c-8e11678106e8:team$593501",        # ПАО Ростелеком
        11: "591e281d-cb3d-47fa-bf5c-8e11678106e8:team$27244701",      # АО Рт Лабс
        12: "591e281d-cb3d-47fa-bf5c-8e11678106e8:team$41895102",      # ФГИС ДО
        13: "591e281d-cb3d-47fa-bf5c-8e11678106e8:team$9430801",       # ЕПГУ
        14: "591e281d-cb3d-47fa-bf5c-8e11678106e8:team$131164001",     # ГУЦ
        15: "591e281d-cb3d-47fa-bf5c-8e11678106e8:employee$644104"}    # ОИВ

main_lc = {"registered": ["assignResponEmpl", "refused", "resolved", "suspended",],
           "assignResponOrg": ["assignResponEmpl", "secondLine", "suspended", "refused"],
           "assignResponEmpl": ["secondLine", "refused", "resolved"],
           "secondLine": ["analysis", "transferred", "refused", "resolved"],
           "transferred": ["assignResponOrg", "suspended", "refused", "escalated"],
           "suspended": ["registered", "assignResponOrg", "assignResponEmpl", "secondLine", "transferred", "standby",
                         "provideInfo", "refused", "resolved", "escalated" ],
           "standby": ["secondLine", "suspended", "provideInfo", "refused", "escalated"],
           "provideInfo": ["assignResponOrg", "secondLine", "transferred", "suspended", "refused", "escalated"],
           "neutralize": ["resolved", "resumed", "escalated"],
           "resolved": ["resumed", "closed"],
           "refused": ["resumed", "closed"],
           "resumed": ["registered", "assignResponOrg", "resolved", "refused", "escalated"],
           "escalated": ["assignResponOrg", "transferred", "suspended", "refused"]}

simple_status = {'Assigned': 'registered',
                 'Work In Progress': 'registered',
                 'In Progress': 'registered',
                 'Pending': 'resumed',
                 'Resolved': 'resolved',
                 'Closed': 'closed',
                 }

impactCode = {'Critical': "impact$8478601",
              'High': "impact$7203",
              'Medium': "impact$7202",
              'Low': "impact$7201"}

skuf_priority = {"impact$8478601": "0",
                 "impact$7203": "1",
                 "impact$7202": "2",
                 "impact$7201": "3"}

assignment_mapping = {'0': "Дежурные ИЭП",
                      '1': "Дежурные ИЭП",
                      '2': "Дежурные ИЭП",
                      '3': "Проект  СМЭВ",
                      '4': "Дежурные ИЭП",
                      '5': "Группа внутренней автоматизации и мониторинга",
                      '6': "Группа ЕСИА",
                      '7': "Аналитическая группа",
                      '8': "Дежурные ИЭП",
                      '9': "Дежурные ИЭП",
                      '10': "Проект  СМЭВ",
                      '11': "Проект  СМЭВ",
                      '12': "Группа ФГИС ДО",
                      '13': "Группа ПГУ",
                      '14': "Начальник смены ЦПП",
                      }

Service = {u"ЕПГУ":       "serviceCall$epguCall",    u"РПГУ":         "serviceCall$rpguCall",
           u"ИПШ":        "serviceCall$ipshCall",    u"МП Госуслуги": "serviceCall$smuCall",
           u"Инфомат":    "serviceCall$smfciodCall", u"Концентратор": "serviceCall$hubCall",
           u"ГЭПС":       "serviceCall$gapsCall",    u"СМЭВ":         "serviceCall$smavCall",
           u"СЦ":         "serviceCall$scCall",      u"СГК":          "serviceCall$sgkCall",
           u"ТРМВ":       "serviceCall$trmvCall",    u"РСМЭВ":        "serviceCall$rsmavCall",
           u"СКиМ":       "serviceCall$skimCall",    u"ЕСИА":         "serviceCall$esiaCall",
           u"ГУЦ":        "serviceCall$gucCall",     u"ФРГУ":         "serviceCall$frguCall",
           u"ФТЦ":        "serviceCall$ftcCall",     u"ФГИС ДО":      "serviceCall$fgisdoCall",
           u"РОИ":        "serviceCall$roiCall",     u"ПАИС ФЦОД":    "serviceCall$fcodCall",
           u"ПАИС НПРОД": "serviceCall$nprodCall",   u"ПГП":          "serviceCall$pgpCall",
           u"УВиРИ":      "serviceCall$uviriCall",   u"ФГИС ФАП":     "serviceCall$fgisfapCall",
           u"ЭС ЦТО":     "serviceCall$asctoCall",   u"ПАИС":         "serviceCall$paisCall",
           u"ЕСНСИ":      "serviceCall$esnsiCall",   u"СМЭВ 3.0":     "serviceCall$smevThreeCall",
           u"ЕПГУ 3.0":   "serviceCall$epguCall"}

html_chars = ["&quot;", "&amp;", "&lt;", "&gt;", "&nbsp;", "&iexcl;", "&cent;", "&pound;",
              "&curren;", "&yen;", "&brvbar;", "&sect;", "&uml;", "&copy;", "&ordf;", "&laquo;",
              "&not;", "&shy;", "&reg;", "&macr;", "&deg;", "&plusmn;", "&sup2;", "&sup3;", "&acute;",
              "&micro;", "&para;", "&middot;", "&cedil;", "&sup1;", "&ordm;", "&raquo;", "&frac14;",
              "&frac12;", "&frac34;", "&iquest;", "&Agrave;", "&Aacute;", "&Acirc;", "&Atilde;", "&Auml;",
              "&Aring;", "&AElig;", "&Ccedil;", "&Egrave;", "&Eacute;", "&Ecirc;", "&Euml;",
              "&Igrave;", "&Iacute;", "&Icirc;", "&Iuml;", "&ETH;", "&Ntilde;", "&Ograve;", "&Oacute;",
              "&Ocirc;", "&Otilde;", "&Ouml;", "&times;", "&Oslash;", "&Ugrave;", "&Uacute;", "&Ucirc;",
              "&Uuml;", "&Yacute;", "&THORN;", "&szlig;", "&agrave;", "&aacute;", "&acirc;", "&atilde;",
              "&auml;", "&aring;", "&aelig;", "&ccedil;", "&egrave;", "&eacute;", "&ecirc;", "&euml;",
              "&igrave;", "&iacute;", "&icirc;", "&iuml;", "&eth;", "&ntilde;", "&ograve;", "&oacute;",
              "&ocirc;", "&otilde;", "&ouml;", "&divide;", "&oslash;", "&ugrave;", "&uacute;", "&ucirc;",
              "&uuml;", "&yacute;", "&thorn;", "&yuml;", "&euro;"]


service_mapping = {u"ЕСИА": "units$78478006",
                   u"СМЭВ 3.0": "units$106025103",
                   u"СМЭВ": "units$78478007",
                   u"Регламентная процедура ЕСИА": "units$2075401",
                   u"ФТЦ": "units$78478003",
                   u"РСМЭВ.01": "units$78478008",
                   u"РСМЭВ.01": "units$78478008",
                   u"РСМЭВ.02": "units$78478008",
                   u"РСМЭВ.03": "units$78478008",
                   u"РСМЭВ.04": "units$78478008",
                   u"РСМЭВ.05": "units$78478008",
                   u"РСМЭВ.06": "units$78478008",
                   u"РСМЭВ.07": "units$78478008",
                   u"РСМЭВ.08": "units$78478008",
                   u"РСМЭВ.09": "units$78478008",
                   u"РСМЭВ.10": "units$78478008",
                   u"РСМЭВ.11": "units$78478008",
                   u"РСМЭВ.12": "units$78478008",
                   u"РСМЭВ.13": "units$78478008",
                   u"РСМЭВ.14": "units$78478008",
                   u"РСМЭВ.15": "units$78478008",
                   u"РСМЭВ.16": "units$78478008",
                   u"РСМЭВ.17": "units$78478008",
                   u"РСМЭВ.18": "units$78478008",
                   u"РСМЭВ.19": "units$78478008",
                   u"РСМЭВ.20": "units$78478008",
                   u"РСМЭВ.21": "units$78478008",
                   u"РСМЭВ.22": "units$78478008",
                   u"РСМЭВ.23": "units$78478008",
                   u"РСМЭВ.24": "units$78478008",
                   u"РСМЭВ.25": "units$78478008",
                   u"РСМЭВ.26": "units$78478008",
                   u"РСМЭВ.27": "units$78478008",
                   u"РСМЭВ.28": "units$78478008",
                   u"РСМЭВ.29": "units$78478008",
                   u"РСМЭВ.30": "units$78478008",
                   u"РСМЭВ.31": "units$78478008",
                   u"РСМЭВ.32": "units$78478008",
                   u"РСМЭВ.33": "units$78478008",
                   u"РСМЭВ.34": "units$78478008",
                   u"РСМЭВ.35": "units$78478008",
                   u"РСМЭВ.36": "units$78478008",
                   u"РСМЭВ.37": "units$78478008",
                   u"РСМЭВ.38": "units$78478008",
                   u"РСМЭВ.39": "units$78478008",
                   u"РСМЭВ.40": "units$78478008",
                   u"РСМЭВ.41": "units$78478008",
                   u"РСМЭВ.42": "units$78478008",
                   u"РСМЭВ.43": "units$78478008",
                   u"РСМЭВ.44": "units$78478008",
                   u"РСМЭВ.45": "units$78478008",
                   u"РСМЭВ.46": "units$78478008",
                   u"РСМЭВ.47": "units$78478008",
                   u"РСМЭВ.48": "units$78478008",
                   u"РСМЭВ.49": "units$78478008",
                   u"РСМЭВ.50": "units$78478008",
                   u"РСМЭВ.51": "units$78478008",
                   u"РСМЭВ.52": "units$78478008",
                   u"РСМЭВ.53": "units$78478008",
                   u"РСМЭВ.54": "units$78478008",
                   u"РСМЭВ.55": "units$78478008",
                   u"РСМЭВ.56": "units$78478008",
                   u"РСМЭВ.57": "units$78478008",
                   u"РСМЭВ.58": "units$78478008",
                   u"РСМЭВ.59": "units$78478008",
                   u"РСМЭВ.60": "units$78478008",
                   u"РСМЭВ.61": "units$78478008",
                   u"РСМЭВ.62": "units$78478008",
                   u"РСМЭВ.63": "units$78478008",
                   u"РСМЭВ.64": "units$78478008",
                   u"РСМЭВ.65": "units$78478008",
                   u"РСМЭВ.66": "units$78478008",
                   u"РСМЭВ.67": "units$78478008",
                   u"РСМЭВ.68": "units$78478008",
                   u"РСМЭВ.69": "units$78478008",
                   u"РСМЭВ.70": "units$78478008",
                   u"РСМЭВ.71": "units$78478008",
                   u"РСМЭВ.72": "units$78478008",
                   u"РСМЭВ.73": "units$78478008",
                   u"РСМЭВ.74": "units$78478008",
                   u"РСМЭВ.75": "units$78478008",
                   u"РСМЭВ.76": "units$78478008",
                   u"РСМЭВ.77": "units$78478008",
                   u"РСМЭВ.78": "units$78478008",
                   u"РСМЭВ.79": "units$78478008",
                   u"РСМЭВ.82": "units$78478008",
                   u"РСМЭВ.83": "units$78478008",
                   u"РСМЭВ.86": "units$78478008",
                   u"РСМЭВ.87": "units$78478008",
                   u"РСМЭВ.89": "units$78478008",
                   u"РСМЭВ.92": "units$78478008",
                   u"ЕСНСИ": "units$78478013",
                   u"ГЭПС": "units$78478014",
                   u"ЕПГУ": "units$78478015",
                   u"ИПШ": "units$78478016",
                   u"Концентратор": "units$78478017",
                   u"МП Госуслуги": "units$78478018",
                   u"РОИ": "units$78478020",
                   u"ПГП": "units$78478024",
                   u"Инфомат": "units$78478026",
                   u"НПРОД": "units$78478028",
                   u"ПАИС": "units$78478029",
                   u"ФГИС ДО": "units$78478031",
                   u"ФРГУ": "units$78478033",
                   u"ФЦОД": "units$78478035",
                   u"ЭС ЦТО": "units$78478037",
                   u"ГОСБАР": "units$85466103",
                   u"Открытая платформа": "units$85466104",
                   u"ТЕСИА": "units$85466105",
                   u"ТСМЭВ": "units$85466106",
                   u"ТФГИС ДО": "units$85466107",
                   u"ТИПШ": "units$85466108",
                   u"ЕСНСИ 2.0": "units$85466108",
                   u"СР СМЭВ 3": "units$106025103",
                   u"ТСМЭВ 3": "units$106025105",
                   u"ТГЭПС": "units$106029601",
                   u"ГУЦ": "units$78478022",
                   u"ТРМВ": "units$78478012",
                   u"СГК": "units$78478011",
                   u"СЦ": "units$78478010"
                   }

available_stats = ['resolved', 'closed']

forbiden_tickets = set([u'serviceCall$14163455', u'serviceCall$12758097', u'serviceCall$13836936', u'serviceCall$12480766'])

allowed_meta_classes = ["serviceCall$NewInc", "serviceCall$Consultation"]

ServiceMapping = {"serviceCall$NewInc": "СМЭВ:Incident"}

reason_mapping = {u"Rejected to Agency": "resolution$105920001",
                  u"Requested information (user)": "resolution$38991304",
                  u"Request": "resolution$38991304",
                  u"Infrastructure Change": "resolution$38991304",
                  u"On the side of a credit institution": "resolution$38991304",
                  u"Sent by the Office to the supplier": "resolution$38991304",
                  u"Notification by phone": "resolution$38991304",
                  u"Necessary modifications": "resolution$38991304",
                  u"No Further Action Required": "closureCode$19701",
                  u"Resolved subcontractor": "closureCode$19701",
                  u"Notify the user of the decision": "closureCode$19701",
                  u"User is notified": "closureCode$19701",
                  u"Priority UP": "closureCode$48073501",
                  u"ScResolution": "closureCode$19701",
                  u"": "resolution$38991304",
                  None: "resolution$38991304",
                  "None": "resolution$38991304",
                  u"ScProvideInfo": "resolution$38991304"}

recovery_mapping = {u"None": "RepairParams$105950701",
                    u"Оповестить о восстановлении": "RepairParams$105946601",
                    u"Оповещен о восстановлении": "RepairParams$105946601",
                    u"Восстановление подтверждено": "RepairParams$105946602"}

recovery_mapping_reversed = {"RepairParams$105950701": "-",
                             "RepairParams$105946601": u"Оповещен о восстановлении",
                             "RepairParams$105946602": u"Восстановление подтверждено"}
# -------------------------------------------------------------------------------------------------------------------- #


# ---------------------------------------------SQL Запросы------------------------------------------------------------ #
# SC_Main
g_exist_tickets = "select DISTINCT(SC_Number) from RTL_SC_Common_GetTicketsFromSC union all select DISTINCT(SC_TicketNumber) from HPD_HELP_DESK" \
                  " union all select DISTINCT(SC_Ticket_Number) from TMS_Task"
# SC_GetChanges
g_action_id = "select Request_ID from RTL_SC_Common_GetChangesFromSC where ActionID = '{0}'"
g_skuf_tickets = """select TO_CHAR(num)
from
(
select SC_TicketNumber as num from HPD_HELP_DESK where SC_TicketNumber is not null and integrationtype = 5
union all
select DISTINCT(SC_Number) as num from RTL_SC_Common_GetTicketsFromSC where mode_X = 'Create'
union all
select SC_Ticket_Number as num from TMS_TASK where SC_Ticket_Number is not null
)"""
# SC_PassChanges
g_events = "select ATTRNAME, ATTRVALUE, SKUF_NUMBER, SC_NUMBER, NOTES, CREATE_DATE, REASON from RTL_SC_COMMON_SENDCHANGESTOSC where REQUEST_ID = '{0}'"
g_events_by_inc = "select REQUEST_ID from RTL_SC_COMMON_SENDCHANGESTOSC where status = 0 and SC_Number is not null and SKUF_Number = '{0}' order by CREATE_DATE asc"
g_chunks = "select DISTINCT(SKUF_Number) from RTL_SC_COMMON_SENDCHANGESTOSC where status = 0 and SC_Number is not null"
insert_error = """INSERT INTO RTL_SC_Common_Errors_Storage
(REQUEST_ID, SUBMITTER, Create_Date, Assigned_TO, Last_Modified_By, Modified_Date, Status, Short_Description, Error_Req_ID, STDOUT)
VALUES
(ARADMIN.RTL_SC_COMMON_ERRORS_SEQ.nextval, 'sc.integrator', (SELECT (SYSDATE - TO_DATE('01-01-1970 00:00:00', 'DD-MM-YYYY HH24:MI:SS')) * 24 * 60 * 60 FROM DUAL)-10800,
'sc.integrator', 'Ситуационный Центр', (SELECT (SYSDATE - TO_DATE('01-01-1970 00:00:00', 'DD-MM-YYYY HH24:MI:SS')) * 24 * 60 * 60 FROM DUAL)-10800,
1, '{2}', '{1}', '{0}')"""

u_status = "update RTL_SC_COMMON_SENDCHANGESTOSC set STATUS = 1, STDOUT = '{0}' where REQUEST_ID = '{1}'"
# SC_GetOrgs
g_skuf_orgs = "select Team_Name, Team_UUID, RequestID from RTL_SC_WorkersMnemonic"
# SC_PassTask
g_inc_created = "select SC_Number from RTL_SC_COMMON_SENTTICKETSTOSC_ where Short_Description = '{0}'"
g_inc_details = "select DESCRIPTION, DETAILED_DECRIPTION, SERVICECI, SUBMIT_DATE, CASE " \
                    "when PRIORITY = 0 THEN 'Critical' " \
                    "when PRIORITY = 1 THEN 'High' " \
                    "when PRIORITY = 2 THEN 'Medium' " \
                    "when PRIORITY = 3 THEN 'Low' " \
                    "END," \
          " INCIDENT_NUMBER from HPD_HELP_DESK WHERE INCIDENT_NUMBER = '{0}'"
g_inc_details_oiv = "select Summary, Notes, SERVICECI, Create_Date, CASE " \
                    "when PRIORITY = 0 THEN 'Critical' " \
                    "when PRIORITY = 1 THEN 'High' " \
                    "when PRIORITY = 2 THEN 'Medium' " \
                    "when PRIORITY = 3 THEN 'Low' " \
                    "END," \
                    " Task_ID, SC_TeamUUID, SC_ParentTicket_Number, ServiceCI from TMS_TASK WHERE Task_ID = '{0}'"
i_created_ticket = """INSERT INTO RTL_SC_COMMON_SENTTICKETSTOSC_
(Short_Description,STATUS,Submitter,Modified_Date,Last_Modified_By,Create_Date,Request_ID,SC_Number )
VALUES ('{0}',0,'kirill.lenchenkov',
(SELECT (SYSDATE - TO_DATE('01-01-1970 00:00:00', 'DD-MM-YYYY HH24:MI:SS')) * 24 * 60 * 60 FROM DUAL),
'kirill.lenchenkov',
(SELECT (SYSDATE - TO_DATE('01-01-1970 00:00:00', 'DD-MM-YYYY HH24:MI:SS')) * 24 * 60 * 60 FROM DUAL),
ARADMIN.RTL_SC_SentTicketsToSC_SEQ.nextval,'{1}')"""
g_unprocessed = "select SKUF_Number,Request_ID from RTL_SC_Common_SendTicketsToSC where SC_Number is NULL order by Request_ID asc"
# SC_GetNumber
u_nums_hpd = "update hpd_help_desk set sc_ticketnumber_for_user = '{number}'" \
              " where SC_TicketNumber = '{sc_number}'"
u_nums_tms = "update tms_task set sc_ticket_num_User = '{number}'" \
              " where SC_Ticket_Number = '{sc_number}'"
g_nums = "select * from (select SC_TicketNumber as num, 'HPD:Help Desk' as form_name from hpd_help_desk where sc_ticketnumber_for_user is null" \
              " and SC_TicketNumber is not null and SUBMIT_DATE > 1476748800 union all select SC_Ticket_Number" \
              " as num, 'TMS:Task' as form_name from TMS_TASK where sc_ticket_num_User is null and SC_Ticket_Number is not null)"

# -------------------------------------------------------------------------------------------------------------------- #


# ---------------------------------------------Soap Запросы----------------------------------------------------------- #
# SC_MAIN ------------------------------------------------------------------------------------------------------------ #
create_skuf_incident = u"""<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:urn="urn:RTL:SC_Common:GetTicketsFromSC">
   <soapenv:Header>
      <urn:AuthenticationInfo>
         <urn:userName>{user}</urn:userName>
         <urn:password>{pwd}</urn:password>
      </urn:AuthenticationInfo>
   </soapenv:Header>
   <soapenv:Body>
      <urn:CreateRequest>
           <urn:Mode>{mode}</urn:Mode>
         <urn:SC_Number>{number}</urn:SC_Number>
         <urn:Description><![CDATA[{topic}]]></urn:Description>
         <urn:Detailed_Description><![CDATA[{descr}]]></urn:Detailed_Description>
         <urn:Priority>{priority}</urn:Priority>
         <urn:ServiceCI>{service}</urn:ServiceCI>
         <urn:AssignedGroup>{group}</urn:AssignedGroup>
         <urn:IncidentType>{inc_type}</urn:IncidentType>
         <urn:UserEmail>{email}</urn:UserEmail>
         <urn:UserOrg>{org}</urn:UserOrg>
         <urn:STDOUT>{stdout}</urn:STDOUT>
      </urn:CreateRequest>
   </soapenv:Body>
</soapenv:Envelope>"""

add_attach_full = u"""<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:urn="urn:RTL:SC_Common:GetChangesFromSC">
   <soapenv:Header>
      <urn:AuthenticationInfo>
         <urn:userName>{login}</urn:userName>
         <urn:password>{passwd}</urn:password>
      </urn:AuthenticationInfo>
   </soapenv:Header>
   <soapenv:Body>
      <urn:SendChanges>
         <urn:Att1_attachmentName>{name1}</urn:Att1_attachmentName>
         <urn:Att1_attachmentData>{b64_1}</urn:Att1_attachmentData>
         <urn:Att1_attachmentOrigSize>1</urn:Att1_attachmentOrigSize>
         <urn:SC_Number>{sc_num}</urn:SC_Number>
         <urn:AttrName>AddAttachEvent</urn:AttrName>
         <urn:Att2_attachmentName>{name2}</urn:Att2_attachmentName>
         <urn:Att2_attachmentData>{b64_2}</urn:Att2_attachmentData>
         <urn:Att2_attachmentOrigSize>1</urn:Att2_attachmentOrigSize>
         <urn:Att3_attachmentName>{name3}</urn:Att3_attachmentName>
         <urn:Att3_attachmentData>{b64_2}</urn:Att3_attachmentData>
         <urn:Att3_attachmentOrigSize>1</urn:Att3_attachmentOrigSize>
         <urn:Mode>True</urn:Mode>
         <urn:ActionID>{ID}</urn:ActionID>
      </urn:SendChanges>
   </soapenv:Body>
</soapenv:Envelope>"""

add_attach_1 = u"""<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:urn="urn:RTL:SC_Common:GetChangesFromSC">
   <soapenv:Header>
      <urn:AuthenticationInfo>
         <urn:userName>{login}</urn:userName>
         <urn:password>{passwd}</urn:password>
      </urn:AuthenticationInfo>
   </soapenv:Header>
   <soapenv:Body>
      <urn:SendChanges>
         <urn:Att1_attachmentName>{name1}</urn:Att1_attachmentName>
         <urn:Att1_attachmentData>{b64_1}</urn:Att1_attachmentData>
         <urn:Att1_attachmentOrigSize>1</urn:Att1_attachmentOrigSize>
         <urn:SC_Number>{sc_num}</urn:SC_Number>
         <urn:AttrName>AddAttachEvent</urn:AttrName>
         <urn:Mode>True</urn:Mode>
         <urn:ActionID>{ID}</urn:ActionID>
      </urn:SendChanges>
   </soapenv:Body>
</soapenv:Envelope>"""

add_attach_2 = u"""<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:urn="urn:RTL:SC_Common:GetChangesFromSC">
   <soapenv:Header>
      <urn:AuthenticationInfo>
         <urn:userName>{login}</urn:userName>
         <urn:password>{passwd}</urn:password>
      </urn:AuthenticationInfo>
   </soapenv:Header>
   <soapenv:Body>
      <urn:SendChanges>
         <urn:Att1_attachmentName>{name1}</urn:Att1_attachmentName>
         <urn:Att1_attachmentData>{b64_1}</urn:Att1_attachmentData>
         <urn:Att1_attachmentOrigSize>1</urn:Att1_attachmentOrigSize>
         <urn:SC_Number>{sc_num}</urn:SC_Number>
         <urn:AttrName>AddAttachEvent</urn:AttrName>
         <urn:Att2_attachmentName>{name2}</urn:Att2_attachmentName>
         <urn:Att2_attachmentData>{b64_2}</urn:Att2_attachmentData>
         <urn:Att2_attachmentOrigSize>1</urn:Att2_attachmentOrigSize>
         <urn:Mode>True</urn:Mode>
         <urn:ActionID>{ID}</urn:ActionID>
      </urn:SendChanges>
   </soapenv:Body>
</soapenv:Envelope>"""

send_comment = u"""<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:urn="urn:RTL:SC_Common:GetChangesFromSC">
   <soapenv:Header>
      <urn:AuthenticationInfo>
         <urn:userName>{login}</urn:userName>
         <urn:password>{passwd}</urn:password>
      </urn:AuthenticationInfo>
   </soapenv:Header>
   <soapenv:Body>
      <urn:SendChanges>
         <urn:SC_Number>{sc_num}</urn:SC_Number>
         <urn:AttrName>{name}</urn:AttrName>
        <urn:AttrValue><![CDATA[{value}]]></urn:AttrValue>
         <urn:Mode>{mode}</urn:Mode>
         <urn:ActionID>{ID}</urn:ActionID>
      </urn:SendChanges>
   </soapenv:Body>
</soapenv:Envelope>"""
# -------------------------------------------------------------------------------------------------------------------- #

# SC_Workers --------------------------------------------------------------------------------------------------------- #

sc_req = """<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:ser="http://naumen.ru/soap/server">
   <soapenv:Header/>
   <soapenv:Body>
      <ser:FindRequest>
         <ser:accessKey>591e281d-cb3d-47fa-bf5c-8e11678106e8</ser:accessKey>
          <ser:fqn>team</ser:fqn>
      </ser:FindRequest>
   </soapenv:Body>
</soapenv:Envelope>"""

# -------------------------------------------------------------------------------------------------------------------- #

# SC_GetChanges ------------------------------------------------------------------------------------------------------ #

send_change = u"""<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:urn="urn:RTL:SC_Common:GetChangesFromSC">
   <soapenv:Header>
      <urn:AuthenticationInfo>
         <urn:userName>{login}</urn:userName>
         <urn:password>{passwd}</urn:password>
      </urn:AuthenticationInfo>
   </soapenv:Header>
   <soapenv:Body>
      <urn:SendChanges>
         <urn:SC_Number>{sc_num}</urn:SC_Number>
         <urn:AttrName>{name}</urn:AttrName>
        <urn:AttrValue><![CDATA[{value}]]></urn:AttrValue>
         <urn:Mode>{mode}</urn:Mode>
         <urn:ActionID>{ID}</urn:ActionID>
      </urn:SendChanges>
   </soapenv:Body>
</soapenv:Envelope>"""

# -------------------------------------------------------------------------------------------------------------------- #

# SC_PassChanges ----------------------------------------------------------------------------------------------------- #

single_event = u"""<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:ns="urn://sc.voskhod.ru/soap-adapter-service/types/1.0" xmlns:ns1="urn://sc.voskhod.ru/soap-adapter-service/basic/1.0">
   <soapenv:Header/>
   <soapenv:Body>
      <ns:SendEventsRequest>
         <ns1:Header>
      <ns1:AccessKey>591e281d-cb3d-47fa-bf5c-8e11678106e8</ns1:AccessKey>
            <ns1:VisitorId>employee$41110603</ns1:VisitorId>
         </ns1:Header>
         <ns:Tasks>
            <ns:Task id="{sc_num}">
               <ns1:ChangeAttributeEvent>
                  <ns1:Id>{uuid}</ns1:Id>
                  <ns1:Date>{date}</ns1:Date>
                  <ns1:Name>{event}</ns1:Name>
                  <ns1:Value><![CDATA[{value}]]></ns1:Value>
               </ns1:ChangeAttributeEvent>
            </ns:Task>
         </ns:Tasks>
      </ns:SendEventsRequest>
   </soapenv:Body>
</soapenv:Envelope>"""

double_event = u"""<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:ns="urn://sc.voskhod.ru/soap-adapter-service/types/1.0" xmlns:ns1="urn://sc.voskhod.ru/soap-adapter-service/basic/1.0">
   <soapenv:Header/>
   <soapenv:Body>
      <ns:SendEventsRequest>
         <ns1:Header>
      <ns1:AccessKey>591e281d-cb3d-47fa-bf5c-8e11678106e8</ns1:AccessKey>
            <ns1:VisitorId>employee$41110603</ns1:VisitorId>
         </ns1:Header>
         <ns:Tasks>
            <ns:Task id="{sc_num}">
               <ns1:ChangeAttributeEvent>
                  <ns1:Id>{uuid}</ns1:Id>
                  <ns1:Date>{date}</ns1:Date>
                  <ns1:Name>{event}</ns1:Name>
                  <ns1:Value><![CDATA[{value}]]></ns1:Value>
               </ns1:ChangeAttributeEvent>
               <ns1:ChangeAttributeEvent>
                  <ns1:Id>{uuid2}</ns1:Id>
                  <ns1:Date>{date}</ns1:Date>
                  <ns1:Name>{event2}</ns1:Name>
                  <ns1:Value><![CDATA[{value2}]]></ns1:Value>
               </ns1:ChangeAttributeEvent>
            </ns:Task>
         </ns:Tasks>
      </ns:SendEventsRequest>
   </soapenv:Body>
</soapenv:Envelope>"""

tripple_event = u"""<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:ns="urn://sc.voskhod.ru/soap-adapter-service/types/1.0" xmlns:ns1="urn://sc.voskhod.ru/soap-adapter-service/basic/1.0">
   <soapenv:Header/>
   <soapenv:Body>
      <ns:SendEventsRequest>
         <ns1:Header>
            <ns1:AccessKey>591e281d-cb3d-47fa-bf5c-8e11678106e8</ns1:AccessKey>
            <ns1:VisitorId>employee$41110603</ns1:VisitorId>
         </ns1:Header>
         <ns:Tasks>
            <ns:Task id="{sc_num}">
               <ns1:ChangeAttributeEvent>
                  <ns1:Id>{uuid}</ns1:Id>
                  <ns1:Date>{date}</ns1:Date>
                  <ns1:Name>{event}</ns1:Name>
                  <ns1:Value>{value}</ns1:Value>
               </ns1:ChangeAttributeEvent>
               <ns1:ChangeAttributeEvent>
                  <ns1:Id>{uuid2}</ns1:Id>
                  <ns1:Date>{date}</ns1:Date>
                  <ns1:Name>{event2}</ns1:Name>
                  <ns1:Value>{value2}</ns1:Value>
               </ns1:ChangeAttributeEvent>
               <ns1:ChangeAttributeEvent>
                  <ns1:Id>{uuid3}</ns1:Id>
                  <ns1:Date>{date}</ns1:Date>
                  <ns1:Name>{event3}</ns1:Name>
                  <ns1:Value>{value3}</ns1:Value>
               </ns1:ChangeAttributeEvent>
            </ns:Task>
         </ns:Tasks>
      </ns:SendEventsRequest>
   </soapenv:Body>
</soapenv:Envelope>"""

get_attach_hpd = u"""<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:urn="urn:RTL:SC_Common:SendChanges_ToSC_GetComments">
   <soapenv:Header>
      <urn:AuthenticationInfo>
         <urn:userName>{user}</urn:userName>
         <urn:password>{pwd}</urn:password>
      </urn:AuthenticationInfo>
   </soapenv:Header>
   <soapenv:Body>
      <urn:GetComment>
         <urn:req_id>{id}</urn:req_id>
      </urn:GetComment>
   </soapenv:Body>
</soapenv:Envelope>"""

add_attach_sc = u"""<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:ns="urn://sc.voskhod.ru/soap-adapter-service/types/1.0" xmlns:ns1="urn://sc.voskhod.ru/soap-adapter-service/basic/1.0">
   <soapenv:Header/>
   <soapenv:Body>
      <ns:SendEventsRequest>
         <ns1:Header>
            <ns1:AccessKey>591e281d-cb3d-47fa-bf5c-8e11678106e8</ns1:AccessKey>
            <ns1:VisitorId>employee$41110603</ns1:VisitorId>
         </ns1:Header>
         <ns:Tasks>
            <ns:Task id="{sc_num}">
               <ns1:AddFileEvent>
                  <ns1:Id>{uuid}</ns1:Id>
                  <ns1:Date>{date}</ns1:Date>
                  <ns1:BinaryContent>{base64}</ns1:BinaryContent>
                  <ns1:Title>{name}</ns1:Title>
                  <ns1:MimeType>{extension}</ns1:MimeType>
               </ns1:AddFileEvent>
            </ns:Task>
         </ns:Tasks>
      </ns:SendEventsRequest>
   </soapenv:Body>
</soapenv:Envelope>"""

add_comment_sc = u"""<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:ns="urn://sc.voskhod.ru/soap-adapter-service/types/1.0" xmlns:ns1="urn://sc.voskhod.ru/soap-adapter-service/basic/1.0">
   <soapenv:Header/>
   <soapenv:Body>
      <ns:SendEventsRequest>
         <ns1:Header>
        <ns1:AccessKey>591e281d-cb3d-47fa-bf5c-8e11678106e8</ns1:AccessKey>
            <ns1:VisitorId>employee$41110603</ns1:VisitorId>
         </ns1:Header>
         <ns:Tasks>
            <ns:Task id="{sc_num}">
               <ns1:AddCommentEvent>
                  <ns1:Id>{uuid}</ns1:Id>
                  <ns1:Date>{date}</ns1:Date>
                  <ns1:Text>{comment}</ns1:Text>
                  <ns1:Private>false</ns1:Private>
               </ns1:AddCommentEvent>
            </ns:Task>
         </ns:Tasks>
      </ns:SendEventsRequest>
   </soapenv:Body>
</soapenv:Envelope>"""

# -------------------------------------------------------------------------------------------------------------------- #

# SC_PassTask -------------------------------------------------------------------------------------------------------- #

set_sc_number_request = u"""<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:urn="urn:RTL:SC_Common:SendTicketsToSC:SetNumber">
   <soapenv:Header>
      <urn:AuthenticationInfo>
         <urn:userName>{login}</urn:userName>
         <urn:password>{pwd}</urn:password>
      </urn:AuthenticationInfo>
   </soapenv:Header>
   <soapenv:Body>
      <urn:SetNumberSC>
         <urn:SC_Number>{number}</urn:SC_Number>
         <urn:Request_ID>{id}</urn:Request_ID>
      </urn:SetNumberSC>
   </soapenv:Body>
</soapenv:Envelope>"""

create_sc_inc = u"""<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:ns="urn://sc.voskhod.ru/soap-adapter-service/types/1.0" xmlns:ns1="urn://sc.voskhod.ru/soap-adapter-service/basic/1.0">
   <soapenv:Header/>
   <soapenv:Body>
      <ns:CreateTasksRequest>
         <ns1:Header>
            <ns1:AccessKey>591e281d-cb3d-47fa-bf5c-8e11678106e8</ns1:AccessKey>
            <ns1:VisitorId>employee$644104</ns1:VisitorId>
         </ns1:Header>
         <ns:Tasks>
            <ns:Task id="{uuid}">
               <ns1:Attributes>
		{part}
               </ns1:Attributes>
            </ns:Task>
         </ns:Tasks>
      </ns:CreateTasksRequest>
   </soapenv:Body>
</soapenv:Envelope>"""

req_part = u"""<ns1:Attribute>
                  <ns1:Name>{Name}</ns1:Name>
                  <ns1:Value><![CDATA[{Value}]]></ns1:Value>
               </ns1:Attribute>"""

# COMMON ------------------------------------------------------------------------------------------------------------- #
get_tasks_sc = """<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"
xmlns:ns="urn://sc.voskhod.ru/soap-adapter-service/types/1.0"
xmlns:ns1="urn://sc.voskhod.ru/soap-adapter-service/basic/1.0">
   <soapenv:Header/>
   <soapenv:Body>
      <ns:GetTasksListRequest>
         <ns1:Header>
            <ns1:AccessKey>591e281d-cb3d-47fa-bf5c-8e11678106e8</ns1:AccessKey>
            <ns1:VisitorId>{0}</ns1:VisitorId>
         </ns1:Header>
         <ns:role>{1}</ns:role>
         <ns:changed>{2}</ns:changed>
         <ns:skipOwnChanges>{3}</ns:skipOwnChanges>
      </ns:GetTasksListRequest>
   </soapenv:Body>
</soapenv:Envelope>"""

get_task_events = """<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:ns="urn://sc.voskhod.ru/soap-adapter-service/types/1.0" xmlns:ns1="urn://sc.voskhod.ru/soap-adapter-service/basic/1.0">
   <soapenv:Header/>
   <soapenv:Body>
      <ns:GetTaskEventListRequest>
         <ns1:Header>
           <ns1:AccessKey>591e281d-cb3d-47fa-bf5c-8e11678106e8</ns1:AccessKey>
            <ns1:VisitorId>{0}</ns1:VisitorId>
         </ns1:Header>
         <!--Optional:-->
         <ns:skipOwnChanges>false</ns:skipOwnChanges>
         <ns:Tasks>
            <!--1 or more repetitions:-->
            <ns1:Tasks>{1}</ns1:Tasks>
         </ns:Tasks>
      </ns:GetTaskEventListRequest>
   </soapenv:Body>
</soapenv:Envelope>"""

add_attach_to_ticket = u"""<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:urn="urn:RTL:SC:IntegrationWB">
   <soapenv:Header>
      <urn:AuthenticationInfo>
         <urn:userName>{login}</urn:userName>
         <urn:password>{passwd}</urn:password>
      </urn:AuthenticationInfo>
   </soapenv:Header>
   <soapenv:Body>
      <urn:AddAttach>
         <urn:SC_TicketNum>{sc_num}</urn:SC_TicketNum>
         <urn:Mode>attach</urn:Mode>
         <urn:Attachment_attachmentName>{name1}</urn:Attachment_attachmentName>
         <urn:Attachment_attachmentData>{b64_1}</urn:Attachment_attachmentData>
         <urn:Attachment_attachmentOrigSize>111</urn:Attachment_attachmentOrigSize>
         <urn:tr_Status>0</urn:tr_Status>
         <urn:User>{user}</urn:User>
         <urn:Script_STDOUT>Success</urn:Script_STDOUT>
         <urn:Attachment2_attachmentName>{name2}</urn:Attachment2_attachmentName>
         <urn:Attachment2_attachmentData>{b64_2}</urn:Attachment2_attachmentData>
         <urn:Attachment2_attachmentOrigSize>111</urn:Attachment2_attachmentOrigSize>
         <urn:Attachment3_attachmentName>{name3}</urn:Attachment3_attachmentName>
         <urn:Attachment3_attachmentData>{b64_3}</urn:Attachment3_attachmentData>
         <urn:Attachment3_attachmentOrigSize>111</urn:Attachment3_attachmentOrigSize>
         <urn:Submiter>script</urn:Submiter>
      </urn:AddAttach>
   </soapenv:Body>
</soapenv:Envelope>"""

get_task_statuses = """<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:ser="http://naumen.ru/soap/server">
  <soapenv:Header/>
   <soapenv:Body>
      <ser:GetRequest>
         <ser:accessKey>591e281d-cb3d-47fa-bf5c-8e11678106e8</ser:accessKey>
           <ser:uuid>{0}</ser:uuid>
      </ser:GetRequest>
   </soapenv:Body>
</soapenv:Envelope>"""

ackChanges = """<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:ns="urn://sc.voskhod.ru/soap-adapter-service/types/1.0" xmlns:ns1="urn://sc.voskhod.ru/soap-adapter-service/basic/1.0">
   <soapenv:Header/>
   <soapenv:Body>
      <ns:AckEventPackageRequest>
         <ns1:Header>
            <ns1:AccessKey>591e281d-cb3d-47fa-bf5c-8e11678106e8</ns1:AccessKey>
            <ns1:VisitorId>{1}</ns1:VisitorId>
         </ns1:Header>
         <ns:packageId>{0}</ns:packageId>
      </ns:AckEventPackageRequest>
   </soapenv:Body>
</soapenv:Envelope>"""

create_worker = u"""<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:urn="urn:RTL:SC_Common:Workers">
   <soapenv:Header>
      <urn:AuthenticationInfo>
         <urn:userName>{login}</urn:userName>
         <urn:password>{pwd}</urn:password>
      </urn:AuthenticationInfo>
   </soapenv:Header>
   <soapenv:Body>
      <urn:Create>
         <urn:Team_Name>{name}</urn:Team_Name>
         <urn:Team_UUID>{id}</urn:Team_UUID>
      </urn:Create>
   </soapenv:Body>
</soapenv:Envelope>"""

change_worker = u"""<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:urn="urn:RTL:SC_Common:Workers">
   <soapenv:Header>
      <urn:AuthenticationInfo>
         <urn:userName>{login}</urn:userName>
         <urn:password>{pwd}</urn:password>
      </urn:AuthenticationInfo>
   </soapenv:Header>
   <soapenv:Body>
      <urn:SetOrDelete>
         <urn:Action>{action}</urn:Action>
         <urn:ID>{id}</urn:ID>
	 <urn:Name>{name}</urn:Name>
      </urn:SetOrDelete>
   </soapenv:Body>
</soapenv:Envelope>"""

get_req_stats = u"""<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:ns="urn://sc.voskhod.ru/soap-adapter-service/types/1.0" xmlns:ns1="urn://sc.voskhod.ru/soap-adapter-service/basic/1.0">
   <soapenv:Header/>
   <soapenv:Body>
      <ns:GetCurrentTaskStatusesRequest>
         <ns1:Header>
            <ns1:AccessKey>591e281d-cb3d-47fa-bf5c-8e11678106e8</ns1:AccessKey>
            <ns1:VisitorId>team$2282601</ns1:VisitorId>
         </ns1:Header>
         <ns:Tasks>
            <!--1 or more repetitions:-->
            <ns1:Tasks>{0}</ns1:Tasks>
         </ns:Tasks>
      </ns:GetCurrentTaskStatusesRequest>
   </soapenv:Body>
</soapenv:Envelope>"""

# -------------------------------------------------------------------------------------------------------------------- #

# import os
# lstper = os.environ.get('periodos')
# lstperiodos=lstper.split(',')
# periodos="','".join(lstperiodos)
# #"2231,2232,2233"
# print(f"Periodo a ejecutar: {periodos}")
# #"'2233'"
# per = os.environ.get('perActual')
# print(f"Periodo actual: {per}")
# periodoActual=per
# grados="PREG','PPE"

import os
from dotenv import load_dotenv
load_dotenv()
periodo=os.getenv('PERIODO_ACTUAL')

#Semanales
# PS_FLASH_FOR_CU_VW=f"SELECT SEQUENCE_NO,LAM_WEIGHT,LAM_TYPE,CRSE_ID,STRM,DESCR2 FROM SYSADM.PS_FLASH_FOR_CU_VW WHERE STRM IN ('{periodos}')"
# PS_FLASH_MOD_AL_VW=f"SELECT INSTITUTION, ACAD_CAREER, STRM, SESSION_CODE, XLATLONGNAME, TO_CHAR(SESS_BEGIN_DT, 'YYYY-MM-DD') SESS_BEGIN_DT,TO_CHAR(SESS_END_DT, 'YYYY-MM-DD') SESS_END_DT FROM SYSADM.PS_FLASH_MOD_AL_VW WHERE INSTITUTION='UNUTP' AND ACAD_CAREER IN ('{grados}') AND STRM IN ('{periodos}')"
# PS_FLASH_CIC_MS_VW=f"SELECT INSTITUTION, ACAD_CAREER, STRM, DESCR, DESCRSHORT,TO_CHAR(TERM_BEGIN_DT, 'YYYY-MM-DD') TERM_BEGIN_DT, TO_CHAR(TERM_END_DT, 'YYYY-MM-DD') TERM_END_DT,WEEKS_OF_INSTRUCT, ACAD_YEAR, HOLIDAY_SCHEDULE FROM SYSADM.PS_FLASH_CIC_MS_VW WHERE INSTITUTION='UNUTP' AND ACAD_CAREER IN ('{grados}') AND STRM IN ('{periodos}')"
# PS_UTP_DOC_AL_VW=f"SELECT STRM,CRSE_ID, CLASS_NBR,LVF_COD_EMPL,INSTR_ROLE,EMPLID,LAST_NAME,SECOND_LAST_NAME,FIRST_NAME,EMAIL_ADDR,PHONE,EMPLID1 FROM SYSADM.PS_UTP_DOC_AL_VW WHERE STRM IN ('{periodos}')"
# PS_FLASH_BEN_AL_VW=f"SELECT EMPLID,STRM,LVF_TIP_BEN,XLATLONGNAME,LVF_ID_CPTO,DESCR, LVF_COD_BEN,DESCR1 FROM SYSADM.PS_FLASH_BEN_AL_VW WHERE STRM IN ('{periodos}')"
# PS_FLASH_DT_ALU_VW="select EMPLID, NATIONAL_ID, LVF_COD_UTP, NAME from SYSADM.PS_FLASH_DT_ALU_VW"
# PS_EMAIL_ADDR_VW="SELECT EMPLID,E_ADDR_TYPE, EMAIL_ADDR, PREF_EMAIL_FLAG FROM SYSADM.PS_EMAIL_ADDR_VW WHERE PREF_EMAIL_FLAG='Y'"
# PS_FLASH_TEL_AL_VW="SELECT EMPLID, PHONE_TYPE, COUNTRY_CODE, PHONE, EXTENSION,PREF_PHONE_FLAG FROM SYSADM.PS_FLASH_TEL_AL_VW WHERE PREF_PHONE_FLAG='Y'"
# PS_FLASH_ROL_EXAM_VW=f"SELECT C.EMPLID AS EMPLID, LV.LVF_COD_UTP AS LVF_COD_UTP, A.CAMPUS_EVENT_NBR AS CAMPUS_EVENT_NBR, D.DESCR AS DESCRIP_EVENTO,D.CAMPUS_EVENT_TYPE AS CAMPUS_EVENT_TYPE,E.DESCR AS DESCR_TIPO_EVENTO,A.EVENT_MTG_NBR AS EVENT_MTG_NBR,A.FACILITY_ID AS FACILITY_ID,TO_CHAR(A.MEETING_DT, 'YYYY-MM-DD') AS MEETING_DT,CASE TO_CHAR(add_months(A.MEETING_TIME_START,840), 'YYYY-MM-DD HH24:MI:SS') WHEN '1970-01-01 00:00:00' THEN '1970-01-01 00:01:00' ELSE TO_CHAR(add_months(A.MEETING_TIME_START,840), 'YYYY-MM-DD HH24:MI:SS') END MEETING_TIME_START,CASE TO_CHAR(add_months(A.MEETING_TIME_END,840), 'YYYY-MM-DD HH24:MI:SS') WHEN '1970-01-01 00:00:00' THEN '1970-01-01 23:59:00' ELSE TO_CHAR(add_months(A.MEETING_TIME_END,840), 'YYYY-MM-DD HH24:MI:SS') END MEETING_TIME_END,A.CAMPUS_MTG_TYPE AS CAMPUS_MTG_TYPE,J2.DESCR AS DESCRIPCION_REUNION,LV.EMPLID AS DOCENTE_EMPLID,HH.ACAD_CAREER AS ACAD_CAREER,HH.STRM AS STRM,AMB.DESCR1 AS AMB_DIRC,AMB.BLDG_CD AS BLDG_CD,AMB.ROOM AS ROOM,J2.CLASS_NBR AS CLASS_NBR,x.instruction_mode FROM SYSADM.PS_EVENT_MTG A  LEFT JOIN SYSADM.PS_CAMPUS_EVENT D ON D.CAMPUS_EVENT_NBR = A.CAMPUS_EVENT_NBR  LEFT JOIN SYSADM.PS_LVF_SP_AMB_VW amb ON amb.facility_id = A.facility_id  LEFT JOIN SYSADM.PS_CAMPUS_MTG_SEL C ON C.CAMPUS_EVENT_NBR = A.CAMPUS_EVENT_NBR AND C.EVENT_MTG_NBR = A.EVENT_MTG_NBR  LEFT JOIN SYSADM.PS_LVF_COD_ALU_TBL LV ON LV.INSTITUTION = D.INSTITUTION AND LV.EMPLID = C.EMPLID LEFT JOIN SYSADM.PS_EVENT_TYPE_TBL E ON D.CAMPUS_EVENT_TYPE=E.CAMPUS_EVENT_TYPE LEFT JOIN SYSADM.PS_LVFPE15SRE15_H2 HH ON HH.CAMPUS_EVENT_NBR = A.CAMPUS_EVENT_NBR AND A.EVENT_MTG_NBR = HH.EVENT_MTG_NBR  LEFT JOIN SYSADM.PS_LVF_MTG_CLAS_TB J1 ON J1.CAMPUS_EVENT_NBR=C.CAMPUS_EVENT_NBR AND J1.CAMPUS_EVENT_ATND=C.CAMPUS_EVENT_ATND AND J1.EVENT_MTG_NBR=C.EVENT_MTG_NBR  LEFT JOIN SYSADM.PS_CLASS_TBL J2 ON  J2.STRM=HH.STRM AND J2.CLASS_NBR=J1.CLASS_NBR  LEFT JOIN SYSADM.PS_LVF_CLASS_TBL x on X.STRM=J2.STRM AND X.CLASS_SECTION=J2.CLASS_SECTION AND X.CRSE_ID=J2.CRSE_ID AND X.CRSE_OFFER_NBR=J2.CRSE_OFFER_NBR AND X.SESSION_CODE  = J2.SESSION_CODE WHERE  A.CAMPUS_MTG_TYPE='EXFN'  AND HH.STRM='{periodoActual}'  AND HH.ACAD_CAREER in ('{grados}') AND x.instruction_mode!='VT'"

#Diarios

PS_UTP_GRP_HIB2TBL = "SELECT INSTITUTION, STRM, UTP_GRP_CLA_HIB, CLASS_NBR, SCC_ROW_ADD_OPRID,  TO_CHAR(SCC_ROW_ADD_DTTM, 'YYYY-MM-DD hh24:mi:ss')  SCC_ROW_ADD_DTTM , SCC_ROW_UPD_OPRID, TO_CHAR(SCC_ROW_UPD_DTTM, 'YYYY-MM-DD hh24:mi:ss') SCC_ROW_UPD_DTTM  FROM  apolo13.PS_UTP_GRP_HIB2TBL"

PS_CLASS_TBL = f"SELECT CRSE_ID, CRSE_OFFER_NBR, STRM, SESSION_CODE, CLASS_SECTION, INSTITUTION, ACAD_GROUP, SUBJECT, CATALOG_NBR, ACAD_CAREER, DESCR, CLASS_NBR, SSR_COMPONENT, ENRL_STAT, CLASS_STAT, CLASS_TYPE, ASSOCIATED_CLASS, WAITLIST_DAEMON, AUTO_ENRL_WAITLIST, STDNT_SPEC_PERM, AUTO_ENROLL_SECT_1, AUTO_ENROLL_SECT_2, RESECTION, SCHEDULE_PRINT, CONSENT, ENRL_CAP, WAIT_CAP, MIN_ENRL, ENRL_TOT, WAIT_TOT, CRS_TOPIC_ID, PRINT_TOPIC, ACAD_ORG, NEXT_STDNT_POSITIN, EMPLID, CAMPUS, LOCATION, CAMPUS_EVENT_NBR, INSTRUCTION_MODE, EQUIV_CRSE_ID, OVRD_CRSE_EQUIV_ID, ROOM_CAP_REQUEST,  TO_CHAR(START_DT, 'YYYY-MM-DD') , TO_CHAR(END_DT, 'YYYY-MM-DD'), CANCEL_DT, PRIM_INSTR_SECT, COMBINED_SECTION, HOLIDAY_SCHEDULE, EXAM_SEAT_SPACING, DYN_DT_INCLUDE, DYN_DT_CALC_REQ, ATTEND_GENERATE, ATTEND_SYNC_REQD, FEES_EXIST,  CNCL_IF_STUD_ENRLD, RCV_FROM_ITEM_TYPE, AP_BUS_UNIT, AP_LEDGER, AP_ACCOUNT, AP_DEPTID, AP_PROJ_ID, AP_PRODUCT, AP_FUND_CODE, AP_PROG_CODE, AP_CLASS_FLD, AP_AFFILIATE, AP_OP_UNIT, AP_ALTACCT, AP_BUD_REF,  AP_CF1, AP_CF2, AP_CF3, AP_AFF_INT1, AP_AFF_INT2, WRITEOFF_BUS_UNIT, WRITEOFF_LEDGER, WRITEOFF_ACCOUNT, WRITEOFF_DEPTID, WRITEOFF_PROJ_ID, WRITEOFF_PRODUCT, WRITEOFF_FUND_CODE, WRITEOFF_PROG_CODE,  WRITEOFF_CLASS_FLD, WRITEOFF_AFFILIATE, WRITEOFF_OP_UNIT, WRITEOFF_ALTACCT, WRITEOFF_BUD_REF, WRITEOFF_CF1, WRITEOFF_CF2, WRITEOFF_CF3, WRITEOFF_AFF_INT1, WRITEOFF_AFF_INT2, EXT_WRITEOFF, GL_INTERFACE_REQ, LMS_FILE_TYPE, LMS_GROUP_ID, LMS_URL, LMS_CLASS_EXT_DTTM, LMS_ENRL_EXT_DTTM, LMS_PROVIDER, SSR_DROP_CONSENT  FROM apolo13.ps_class_tbl WHERE STRM='{periodo}'  "
PS_CLASS_MTG_PAT=f"""SELECT 
CRSE_ID, CRSE_OFFER_NBR, STRM, SESSION_CODE, CLASS_SECTION, CLASS_MTG_NBR,
FACILITY_ID, 
 TO_CHAR(NOW()   , 'YYYY') || TO_CHAR(MEETING_TIME_START, '-MM-DD hh24:mi:ss') MEETING_TIME_START, 
 TO_CHAR(NOW()   , 'YYYY') || TO_CHAR(MEETING_TIME_END, '-MM-DD hh24:mi:ss')  MEETING_TIME_END,
MON, TUES, WED,
THURS, FRI, SAT, SUN, 
TO_CHAR(START_DT, 'YYYY-MM-DD') START_DT, 
TO_CHAR(END_DT, 'YYYY-MM-DD') END_DT, 
CRS_TOPIC_ID, DESCR,
STND_MTG_PAT, PRINT_TOPIC_ON_XCR
FROM apolo13.PS_CLASS_MTG_PAT WHERE STRM='{periodo}'
"""

PS_CLASS_INSTR=f"""
SELECT CRSE_ID, CRSE_OFFER_NBR, STRM, SESSION_CODE, CLASS_SECTION, CLASS_MTG_NBR, INSTR_ASSIGN_SEQ, EMPLID, INSTR_ROLE, GRADE_RSTR_ACCESS, CONTACT_MINUTES, SCHED_PRINT_INSTR, INSTR_LOAD_FACTOR, EMPL_RCD, ASSIGN_TYPE, 
WEEK_WORKLOAD_HRS, ASSIGNMENT_PCT, AUTO_CALC_WRKLD FROM apolo13.PS_CLASS_INSTR  WHERE STRM='{periodo}' 
"""
PS_CRSE_CATALOG = """
SELECT CRSE_ID,TO_CHAR(EFFDT, 'YYYY-MM-DD') , EFF_STATUS, DESCR, EQUIV_CRSE_ID, CONSENT, ALLOW_MULT_ENROLL, UNITS_MINIMUM, UNITS_MAXIMUM, UNITS_ACAD_PROG,
UNITS_FINAID_PROG, CRSE_REPEATABLE, UNITS_REPEAT_LIMIT, CRSE_REPEAT_LIMIT, GRADING_BASIS, GRADE_ROSTER_PRINT, SSR_COMPONENT, 
COURSE_TITLE_LONG, LST_MULT_TRM_CRS, CRSE_CONTACT_HRS, RQMNT_DESIGNTN, CRSE_COUNT, INSTRUCTOR_EDIT, FEES_EXIST, 
COMPONENT_PRIMARY, ENRL_UN_LD_CLC_TYP, SSR_DROP_CONSENT, SCC_ROW_ADD_OPRID, TO_CHAR(SCC_ROW_ADD_DTTM, 'YYYY-MM-DD hh24:mi:ss') SCC_ROW_ADD_DTTM, SCC_ROW_UPD_OPRID,
TO_CHAR(SCC_ROW_UPD_DTTM, 'YYYY-MM-DD hh24:mi:ss') SCC_ROW_UPD_DTTM, DESCRLONG
FROM apolo13.PS_CRSE_CATALOG
"""

PS_LVF_EMPL_AS400 = """
SELECT EMPLID, EMPL_RCD, TO_CHAR(EFFDT, 'YYYY-MM-DD')  EFFDT, EFFSEQ, LVF_COD_EMPL, FLAG1, LVF_COD_EMPL1, FLAG2, LVF_COD_EMPL2, FLAG3, LVF_COD_AD FROM apolo13.PS_LVF_EMPL_AS400
"""


PS_HOLIDAY_DATE = """
SELECT HOLIDAY_SCHEDULE, TO_CHAR(HOLIDAY, 'YYYY-MM-DD')  HOLIDAY, DESCR, HOLIDAY_HRS, HOLIDAY_TYPE,
TO_CHAR(HOL_TIME_START, 'YYYY-MM-DD hh24:mi:ss') HOL_TIME_START, 
TO_CHAR(HOL_TIME_END, 'YYYY-MM-DD hh24:mi:ss') HOL_TIME_END FROM apolo13.PS_HOLIDAY_DATE
"""

# PS_UTP_HIS_DALU_VW=f"select INSTITUTION,ACAD_CAREER,EMPLID,ACAD_PROG,DESCR ACAD_PROG_DESC,ACAD_PLAN,CAMPUS,DESCR1 CAMPUS_DESC,STRM from SYSADM.PS_UTP_HIS_DALU_VW WHERE STRM IN ('{periodos}')"
# PS_UTP_EMP_P_MA_VW=f"Select DISTINCT EMPLID,STRM from SYSADM.PS_UTP_EMP_P_MA_VW WHERE STRM IN ('{periodos}')



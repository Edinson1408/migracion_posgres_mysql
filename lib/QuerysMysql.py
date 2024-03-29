# import os
# lstper = os.environ.get('periodos')
# lstperiodos=lstper.split(',')
# periodos="','".join(lstperiodos)
# #"2231,2232,2233"
# periodos=periodos
# print(f"Periodos a ejecutar: {periodos}")


#Semanales
# DELETE_AMZ_FLASH_FOR_CU_TBL=f"DELETE FROM AMZ_FLASH_FOR_CU_TBL WHERE STRM IN  ('{periodos}')"
# INSERT_AMZ_FLASH_FOR_CU_TBL="INSERT INTO AMZ_FLASH_FOR_CU_TBL(SEQUENCE_NO,LAM_WEIGHT,LAM_TYPE,CRSE_ID,STRM,DESCR2) VALUES(%s,%s,%s,%s,%s,%s)"

# DELETE_AMZ_FLASH_MOD_AL_TBL=f"DELETE FROM AMZ_FLASH_MOD_AL_TBL WHERE STRM IN  ('{periodos}')"
# INSERT_AMZ_FLASH_MOD_AL_TBL="INSERT INTO AMZ_FLASH_MOD_AL_TBL(INSTITUTION,ACAD_CAREER,STRM,SESSION_CODE,XLATLONGNAME,SESS_BEGIN_DT,SESS_END_DT) VALUES(%s,%s,%s,%s,%s,%s,%s)"

# DELETE_AMZ_FLASH_CIC_MS_TBL=f"DELETE FROM AMZ_FLASH_CIC_MS_TBL WHERE STRM IN ('{periodos}')"
# INSERT_AMZ_FLASH_CIC_MS_TBL="INSERT INTO AMZ_FLASH_CIC_MS_TBL(INSTITUTION,ACAD_CAREER,STRM,DESCR,DESCRSHORT,TERM_BEGIN_DT,TERM_END_DT,WEEKS_OF_INSTRUCT,ACAD_YEAR,HOLIDAY_SCHEDULE)VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

# DELETE_AMZ_UTP_DOC_AL_TBL=f"DELETE FROM AMZ_UTP_DOC_AL_TBL WHERE STRM IN ('{periodos}')"
# INSERT_AMZ_UTP_DOC_AL_TBL="INSERT INTO AMZ_UTP_DOC_AL_TBL(STRM,CRSE_ID,CLASS_NBR,LVF_COD_EMPL,INSTR_ROLE,EMPLID,LAST_NAME,SECOND_LAST_NAME,FIRST_NAME,EMAIL_ADDR,PHONE,EMPLID1) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

# DELETE_AMZ_FLASH_BEN_AL_TBL=f"DELETE FROM AMZ_FLASH_BEN_AL_TBL WHERE STRM IN ('{periodos}')"
# INSERT_AMZ_FLASH_BEN_AL_TBL="INSERT INTO AMZ_FLASH_BEN_AL_TBL (EMPLID,STRM,LVF_TIP_BEN,XLATLONGNAME,LVF_ID_CPTO,DESCR,LVF_COD_BEN,DESCR1)VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"

# DELETE_AMZ_FLASH_DT_ALU_TBL="TRUNCATE AMZ_FLASH_DT_ALU_TBL"
# INSERT_AMZ_FLASH_DT_ALU_TBL="INSERT INTO AMZ_FLASH_DT_ALU_TBL(EMPLID,NATIONAL_ID,LVF_COD_UTP,NAME) VALUES(%s,%s,%s,%s)"

# DELETE_AMZ_EMAIL_ADDR_TBL="TRUNCATE AMZ_EMAIL_ADDR_TBL"
# INSERT_AMZ_EMAIL_ADDR_TBL="INSERT INTO AMZ_EMAIL_ADDR_TBL(EMPLID,E_ADDR_TYPE,EMAIL_ADDR,PREF_EMAIL_FLAG)VALUES(%s,%s,%s,%s)"

# DELETE_AMZ_FLASH_TEL_AL_TBL="TRUNCATE AMZ_FLASH_TEL_AL_TBL"
# INSERT_AMZ_FLASH_TEL_AL_TBL="INSERT INTO AMZ_FLASH_TEL_AL_TBL(EMPLID,PHONE_TYPE,COUNTRY_CODE,PHONE,EXTENSION,PREF_PHONE_FLAG)VALUES(%s,%s,%s,%s,%s,%s)"

# DELETE_AMZ_FLASH_ROL_EXAM_TBL="TRUNCATE AMZ_FLASH_ROL_EXAM_TBL"
# INSERT_AMZ_FLASH_ROL_EXAM_TBL="INSERT INTO AMZ_FLASH_ROL_EXAM_TBL(EMPLID,LVF_COD_UTP,CAMPUS_EVENT_NBR,DESCRIP_EVENTO,CAMPUS_EVENT_TYPE,DESCR_TIPO_EVENTO,EVENT_MTG_NBR,FACILITY_ID,MEETING_DT,MEETING_TIME_START,MEETING_TIME_END,CAMPUS_MTG_TYPE,DESCRIPCION_REUNION,DOCENTE_EMPLID,ACAD_CAREER,STRM,AMB_DIRC,BLDG_CD,ROOM,CLASS_NBR)VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

#Diarios
TRUNCATE_IRL_PS_UTP_GRP_HIB2TBL="TRUNCATE IRL_PS_UTP_GRP_HIB2TBL"
INSERT_IRL_PS_UTP_GRP_HIB2TBL="INSERT INTO IRL_PS_UTP_GRP_HIB2TBL(INSTITUTION, STRM, UTP_GRP_CLA_HIB, CLASS_NBR, SCC_ROW_ADD_OPRID, SCC_ROW_ADD_DTTM, SCC_ROW_UPD_OPRID, SCC_ROW_UPD_DTTM) VALUES(%s, %s,%s, %s,%s, %s,%s,%s)"

TRUNCATE_IRL_PS_CLASS_TBL="TRUNCATE IRL_PS_CLASS_TBL"
INSERT_IRL_PS_CLASS_TBL="Insert into IRL_PS_CLASS_TBL (CRSE_ID,CRSE_OFFER_NBR,STRM,SESSION_CODE,CLASS_SECTION,INSTITUTION,ACAD_GROUP,SUBJECT,CATALOG_NBR,ACAD_CAREER, DESCR,CLASS_NBR,SSR_COMPONENT,ENRL_STAT,CLASS_STAT,CLASS_TYPE,ASSOCIATED_CLASS,WAITLIST_DAEMON,AUTO_ENRL_WAITLIST,STDNT_SPEC_PERM,AUTO_ENROLL_SECT_1, AUTO_ENROLL_SECT_2,RESECTION,SCHEDULE_PRINT,CONSENT,ENRL_CAP,WAIT_CAP,MIN_ENRL,ENRL_TOT,WAIT_TOT,CRS_TOPIC_ID,PRINT_TOPIC,ACAD_ORG,NEXT_STDNT_POSITIN, EMPLID,CAMPUS,LOCATION,CAMPUS_EVENT_NBR,INSTRUCTION_MODE,EQUIV_CRSE_ID,OVRD_CRSE_EQUIV_ID,ROOM_CAP_REQUEST,START_DT,END_DT,CANCEL_DT,PRIM_INSTR_SECT,COMBINED_SECTION, HOLIDAY_SCHEDULE,EXAM_SEAT_SPACING,DYN_DT_INCLUDE,DYN_DT_CALC_REQ,ATTEND_GENERATE,ATTEND_SYNC_REQD,FEES_EXIST,CNCL_IF_STUD_ENRLD,RCV_FROM_ITEM_TYPE,AP_BUS_UNIT,AP_LEDGER, AP_ACCOUNT,AP_DEPTID,AP_PROJ_ID,AP_PRODUCT,AP_FUND_CODE,AP_PROG_CODE,AP_CLASS_FLD,AP_AFFILIATE,AP_OP_UNIT,AP_ALTACCT,AP_BUD_REF,AP_CF1,AP_CF2,AP_CF3,AP_AFF_INT1,AP_AFF_INT2, WRITEOFF_BUS_UNIT,WRITEOFF_LEDGER,WRITEOFF_ACCOUNT,WRITEOFF_DEPTID,WRITEOFF_PROJ_ID,WRITEOFF_PRODUCT,WRITEOFF_FUND_CODE,WRITEOFF_PROG_CODE,WRITEOFF_CLASS_FLD, WRITEOFF_AFFILIATE,WRITEOFF_OP_UNIT,WRITEOFF_ALTACCT,WRITEOFF_BUD_REF,WRITEOFF_CF1,WRITEOFF_CF2,WRITEOFF_CF3,WRITEOFF_AFF_INT1,WRITEOFF_AFF_INT2,EXT_WRITEOFF, GL_INTERFACE_REQ,LMS_FILE_TYPE,LMS_GROUP_ID,LMS_URL,LMS_CLASS_EXT_DTTM,LMS_ENRL_EXT_DTTM,LMS_PROVIDER,SSR_DROP_CONSENT)  values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) "

TRUNCATE_IRL_PS_CLASS_MTG_PAT="TRUNCATE IRL_PS_CLASS_MTG_PAT"
INSERT_IRL_PS_CLASS_MTG_PAT="""Insert into IRL_PS_CLASS_MTG_PAT (CRSE_ID,CRSE_OFFER_NBR,STRM,
SESSION_CODE,CLASS_SECTION,CLASS_MTG_NBR,FACILITY_ID, MEETING_TIME_START,MEETING_TIME_END,MON,TUES,WED,THURS,
FRI,SAT,SUN,START_DT,END_DT, CRS_TOPIC_ID,DESCR,STND_MTG_PAT,PRINT_TOPIC_ON_XCR) 
values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) """

TRUNCATE_IRL_PS_CLASS_INSTR="TRUNCATE IRL_PS_CLASS_INSTR"
INSERT_IRL_PS_CLASS_INSTR="""
Insert into IRL_PS_CLASS_INSTR (CRSE_ID,CRSE_OFFER_NBR,STRM,SESSION_CODE,CLASS_SECTION,CLASS_MTG_NBR,INSTR_ASSIGN_SEQ,EMPLID,INSTR_ROLE,GRADE_RSTR_ACCESS,CONTACT_MINUTES,SCHED_PRINT_INSTR,INSTR_LOAD_FACTOR,EMPL_RCD,ASSIGN_TYPE,WEEK_WORKLOAD_HRS,
ASSIGNMENT_PCT,AUTO_CALC_WRKLD) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) """



TRUNCATE_IRL_PS_CRSE_CATALOG="TRUNCATE IRL_PS_CRSE_CATALOG"
INSERT_IRL_PS_CRSE_CATALOG="""
Insert into IRL_PS_CRSE_CATALOG (CRSE_ID, EFFDT, EFF_STATUS, DESCR, EQUIV_CRSE_ID, CONSENT, ALLOW_MULT_ENROLL, UNITS_MINIMUM, UNITS_MAXIMUM, UNITS_ACAD_PROG,
 UNITS_FINAID_PROG, CRSE_REPEATABLE, UNITS_REPEAT_LIMIT, CRSE_REPEAT_LIMIT, GRADING_BASIS, GRADE_ROSTER_PRINT, SSR_COMPONENT, COURSE_TITLE_LONG, LST_MULT_TRM_CRS, CRSE_CONTACT_HRS, 
 RQMNT_DESIGNTN, CRSE_COUNT, INSTRUCTOR_EDIT, FEES_EXIST, COMPONENT_PRIMARY, ENRL_UN_LD_CLC_TYP, SSR_DROP_CONSENT, SCC_ROW_ADD_OPRID, SCC_ROW_ADD_DTTM,SCC_ROW_UPD_OPRID, 
 SCC_ROW_UPD_DTTM, DESCRLONG) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) """


TRUNCATE_IRL_PS_LVF_EMPL_AS400="TRUNCATE IRL_PS_LVF_EMPL_AS400"
INSERT_IRL_PS_LVF_EMPL_AS400="""
Insert into IRL_PS_LVF_EMPL_AS400 (
    EMPLID, EMPL_RCD, EFFDT, EFFSEQ, LVF_COD_EMPL, FLAG1, LVF_COD_EMPL1, FLAG2, LVF_COD_EMPL2, FLAG3, LVF_COD_AD
) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) """


TRUNCATE_IRL_PS_HOLIDAY_DATE="TRUNCATE IRL_PS_HOLIDAY_DATE"
INSERT_IRL_PS_HOLIDAY_DATE="""
Insert into IRL_PS_HOLIDAY_DATE (
    HOLIDAY_SCHEDULE, HOLIDAY, DESCR, HOLIDAY_HRS, HOLIDAY_TYPE, HOL_TIME_START, HOL_TIME_END
) values (%s,%s,%s,%s,%s,%s,%s) """


TRUNCATE_IRL_PS_TERM_TBL="TRUNCATE IRL_PS_TERM_TBL"
INSERT_IRL_PS_TERM_TBL="""
Insert into IRL_PS_TERM_TBL (
    INSTITUTION, ACAD_CAREER, STRM, DESCR, DESCRSHORT, TERM_BEGIN_DT, TERM_END_DT, SESSION_CODE, WEEKS_OF_INSTRUCT, TERM_CATEGORY, ACAD_YEAR
) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) """


TRUNCATE_IRL_PS_UTP_PARAM_VARIO="TRUNCATE IRL_PS_UTP_PARAM_VARIO"
INSERT_IRL_PS_UTP_PARAM_VARIO="""
                            Insert into IRL_PS_UTP_PARAM_VARIO (
                                UTP_COD_VISTA, DESCR_FPGO, UTP_NOMBRE_PARAM, UTP_VALOR_PARAM
                            ) values (%s,%s,%s,%s) """


# DELETE_AMZ_FLASH_UTP_HIS_DALU_TBL=f"DELETE FROM AMZ_FLASH_UTP_HIS_DALU_TBL WHERE STRM IN ('{periodos}')"
# INSERT_AMZ_FLASH_UTP_HIS_DALU_TBL="INSERT INTO AMZ_FLASH_UTP_HIS_DALU_TBL(INSTITUTION,ACAD_CAREER,EMPLID,ACAD_PROG,ACAD_PROG_DESC,ACAD_PLAN,CAMPUS,CAMPUS_DESC,STRM)VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)"

# DELETE_AMZ_FLASH_UTP_CIC_ALL_TBL=f"DELETE FROM AMZ_FLASH_UTP_CIC_ALL_TBL WHERE STRM IN ('{periodos}')"
# INSERT_AMZ_FLASH_UTP_CIC_ALL_TBL="INSERT INTO AMZ_FLASH_UTP_CIC_ALL_TBL(EMPLID,STRM)VALUES(%s,%s)"



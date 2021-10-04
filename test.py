# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 22:40:30 2021

@author: richa
"""


import yfinance as yf
import numpy as np
import pandas
import yahoo_finance

# =============================================================================
# hist = yf.download('ATCO-A.ST VOLV-B.ST ERIC-B.ST NDA-SE.ST SAND.ST HEXA-B.ST EVO.ST EQT.ST'\
#                     ' ASSA-B.ST SEB-A.ST SHB-A.ST SWED-A.ST ESSITY-B.ST EPI-A.ST SEB-A.ST' \
#                     ' SHB-A.ST	SWED-A.ST ESSITY-B.ST TELIA.ST ABB.ST AZN.ST	LATO-B.ST NIBE-B.ST' \
#                     ' ALFA.ST SWMA.ST SKF-B.ST KINV-B.ST	SCA-B.ST SINCH.ST SKA-B.ST BOL.ST ELUX-B.ST' \
#                     ' TEL2-B.ST BALD-B.ST INDT.ST LUND-B.ST LIFCO-B.ST GETI-B.ST HUSQ-B.ST CAST.ST' \
#                     ' SAGA-B.ST TREL-B.ST	SECU-B.ST AAK.ST SWEC-B.ST HOLM-B.ST	AXFO.ST	BEIJ-B.ST ALIV-SDB.ST' \
#                     ' SOBI.ST	EKTA-B.ST THULE.ST FABG.ST DOM.ST	WALL-B.ST	ADDT-B.ST KIND-SDB.ST BILL.ST TIETOS.ST' \
#                     ' INTRUM.ST	SAAB-B.ST NENT-B.ST TIGO-SDB.ST HPOL-B.ST SBB-B.ST PEAB-B.ST AFRY.ST VITR.ST' \
#                     ' WIHL.ST	HUFV-A.ST BRAV.ST	BURE.ST	SECT-B.ST JM.ST	ATRLJ-B.ST CLNK-B.ST MYCR.ST	KLED.ST' \
#                     ' LOOMIS.ST NOLA-B.ST ALIF-B.ST	BHG.ST ARJO-B.ST NYF.ST MIPS.ST INSTAL.ST PNDX-B.ST' \
#                     ' CATE.ST	STE-R.ST LUG.ST	TROAX.ST LAGR-B.ST NCC-B.ST LIAB.ST MTRS.ST EPRO-B.ST' \
#                     ' MCOV-B.ST HMS.ST SSAB-A.ST BILI-A.ST GRNG.ST SYSR.ST MTG-B.ST BOOZT.ST KARO.ST NOBI.ST' \
#                     ' CAMX.ST VNV.ST RATO-B.ST CINT.ST VIT-B.ST PLAZ-B.ST BONAV-B.ST BETCO.ST RESURS.ST ONCO.ST' \
#                     ' DIOS.ST	BIOT.ST	BETS-B.ST	IVSO.ST	FING-B.ST SKIS-B.ST ACAD.ST BEIA-B.ST ATT.ST BIOG-B.ST INWI.ST' \
#                     ' CEVI.ST	DUST.ST	XVIVO.ST ALIG.ST CLA-B.ST AMBEA.ST	 CRED-A.ST SHOT.ST COIC.ST MEKO.ST BIOA-B.ST' \
#                     ' COOR.ST HNSA.ST NOBINA.ST OEM-B.ST	 CALTX.ST AQ.ST	GARO.ST	MSON-B.ST KNOW.ST COLL.ST SVOL-B.ST' \
#                     ' LEO.ST LIME.ST EOLU-B.ST G5EN.ST CTM.ST EMBRAC-B.ST NOKIA-SEK.ST PCELL.ST PDX.ST HTRO.ST ADAPT.ST' \
#                     ' HOFI.ST SAVE.ST TOBII.ST READ.ST CLAS-B.ST HM-B.ST ICA.ST LUNE.ST SAS.ST AZA.ST FAG.ST SF.ST' \
#                     ' INVE-B.ST INDU-C.ST LUMI.ST' \
#                     , start='2017-01-01', end='2021-10-03')
# =============================================================================

adj_close_price = hist['Adj Close']
open_price = hist['Open']

cl_cl = (np.log(adj_close_price / adj_close_price.shift(-1)))
cl_cl = cl_cl.shift(periods = 1)
cl_cl = cl_cl.drop(cl_cl.index[0])

#calculate 20 day rolling vol
cl_cl_vol = cl_cl.rolling(20).std()
cl_cl_vol = cl_cl_vol.drop(cl_cl_vol.index[range(19)])

#at what vol is the 90th percentile
percentile90 = cl_cl_vol.rolling(window=10).quantile(0.9)
percentile90 = percentile90.drop(percentile90.index[range(9)])

op_cl = (np.log(open_price / adj_close_price.shift(-1)))
op_cl = op_cl.shift(periods = 1)
op_cl = op_cl.drop(op_cl.index[0])


op_cl['AAK.ST'].plot(figsize=(16,9))


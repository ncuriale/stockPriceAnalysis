def TSX_mod():
    
    ext='.TO'
    
    names=['AF','AAB','AAV','ABT','ABX','ACB','ACD','AZ','ACQ','AD','ADN','ADV','AEF',
 'AEM','AEZ','AEZS','AFN','AGI','AGT','AGU','AI','AIF','AIM','AJX','AKG',
 'ALB','ALC','ALS','AMI','ANX','AOI','APS','AQA','AQN','AR','ARE','ARG',
 'ARX','ASO','ASP','ASR','ATA','ATH','ATP','ATZ','AUMN','AVK','AVO','AVP',
 'AXR','AXY','AYA','AYM','AZZ','BAA','BAR','BB','BCB','BCE','BCI','BIR',
 'BK','BKI','BLDP','BLU','BLX','BMO','BNC','BND','BNE','BNP','BNS','BOS',
 'BR','BRB','BRE','BRY','BSC','BSX','BTE','BTO','BUI','BX','BXE','CAE',
 'CAL','CARA','CAS','CBD','CBH','CBL','CBN','CCA','CCM','CCO','CCX','CCZ',
 'CDH','CDZ','CEE','CET','CEU','CEW','CF','CFW','CFX','CG','CGG','CGI',
 'CGL','CGO','CGR','CGX','CHH','CHR','CHW','CIA','CIC','CIE','CIF','CIGI',
 'CIX','CJ','CJT','CKE','CLF','CLG','CLR','CLS','CM','CMG','CMH','CMR',
 'CNE','CNQ','CNR','CNT','COM','COP','COW','CP','CPD','CPG','CPI','CR',
 'CRH','CRP','CS','CSD','CSM','CSU','CSY','CTC','CTU','CTX','CUS','CVD',
 'CVE','CVG','CWB','CWI','CWW','CXF','CXN','CXR','CYB','CYH','DBO','DCM',
 'DDC','DEE','DEN','DF','DGC','DGS','DIV','DLR','DMM','DNT','DOL','DOO',
 'DPM','DQD','DRM','DRWI','DRX','DS','DSG','DW','DXG','DXP','E','ECA','ECI',
 'ECO','ECS','EDR','EDT','EDV','EFH','EFL','EFR','EFX','EGL','EGZ','EIF',
 'ELD','ELF','ELR','ELV','ENB','ENDP','ENT','EPI','EPS','ERF','ESI','ESM',
 'ESP','ET','ETG','ETP','ETX','EUR','EVT','EXE','FAI','FAR','FC','FCR',
 'FCY', 'FDL','FDY','FGB','FHB','FHD','FIE','FIG','FLB','FLI','FM','FN',
 'FNV', 'FQC','FR','FRC','FRU','FRX','FSD','FSR','FST','FSV','FSY','FSZ',
 'FT', 'FTN','FTP','FTS','FTU','FUD','FUM','FUT','FVI','FVL','FXM','G','GBF',
 'GBT', 'GCL','GCM','GCT','GDC','GDI','GDL','GDS','GEN','GEO','GGD','GIL',
 'GMO', 'GMP','GMX','GPR','GPS','GQM','GRL','GS','GSC','GSY','GTE','GTX',
 'GWR', 'GXE','GZT','H','HAC','HAD','HAL','HAZ','HBC','HBM','HBP','HBU',
 'HCG', 'HCN','HE','HED','HEE','HEF','HEP','HGC','HGM','HID','HII','HIX',
 'HLC', 'HLF','HMA','HND','HNZ','HOG','HOU','HPF','HPR','HRA','HRT','HSH',
 'HSM', 'HTD','HTH','HUG','HUL','HUN','HYD','HYG','HYI','HZD','I','IAE',
 'IAG', 'IAM','ICE','ICP','IFA','IGG','IGM','III','ILV','IMG','IMO','IMP',
 'IMV', 'INE','INQ','INV','IPL','IPO','IRG','ITC','ITH','ITP','ITX','JAG',
 'JE', 'JOY','K','KBL','KEL','KER','KEY','KFS','KLS','KOR','KRN','L','LAC',
 'LAM', 'LB','LCS','LEX','LGC','LN','LNF','LNR','LUC','LUG','LYD','MAG',
 'MAR', 'MAX','MBN','MBT','MBX','MCB','MDF','MDI','ME','MEE','MEG','MFC',
 'MFT', 'MG','MGA','MIC','MIN','MKB','MKC','MKP','MMM','MND','MPC','MPVD',
 'MRC', 'MRD','MRE','MSI','MSL','MSV','MTL','MUB','MUS','MUX','MX','MXF',
 'NAL', 'NB','NCA','NEPT','NFI','NG','NGD','NII','NKO','NML','NMX','NOA',
 'NPI', 'NPK','NPS','NRE','NSU','NUS','NVC','NVLN','NWC','NXC','NXJ','OGC',
 'OMI', 'ONC','OR','ORA','ORL','ORT','OSB','OSK','OTC','OTEX','P','PAAS',
 'PATH', 'PAY','PBD','PBH','PBI','PBL','PCY','PDC','PDL','PDN','PEG','PEN',
 'PEU', 'PEY','PFH.F','PFL','PG','PGD','PGF','PGL','PGLC','PHR','PHX','PID',
 'PIH', 'PIN','PKI','PLC','PLG','PLI','PME','PMM','PMN','PMT','PMTS','PNE',
 'POT', 'POW','PPL','PPR','PPS','PPY','PRA','PRK','PRP','PRU','PSA','PSB',
 'PSD', 'PSI','PSK','PTB','PTM','PTS','PUR','PVG','PWT','PXS','PXT','PXU.F',
 'PZA', 'PZC','QCP','QRM','QRT','QSR','QUS','R','RBA','RBS','RCD','RDI',
 'RDL', 'RET','RFP','RGX','RHI','RHP','RHS','RIC','RIG','RLE','RMP','RMX',
 'RPD', 'RQE','RQI','RRX','RSI','RTG','RUD','RUE','RUS','RVX','RWC','RWW',
 'RXD', 'RY','S','SAM','SAP','SBB','SBC','SBI','SBR','SCB','SCC','SCL','SCP',
 'SCY', 'SDY','SEA','SEC','SES','SEV','SFD','SGF','SGY','SHA','SHC','SHE',
 'SHOP', 'SII','SIS','SLF','SLR','SLW','SMC','SMT','SNC','SOY','SPB','SPE',
 'SSL', 'SSO','ST','STB','STN','SU','SUM','SVB','SVC','SVY','SW','SWH','SXI',
 'T', 'TA', 'TAO', 'TBL','TCS','TCW','TD','TDB','TDG','TEI','TEL','TET','TGL',
 'THO', 'THU', 'TLO', 'TLV','TMD','TMI','TML','TMQ','TMR','TNP','TOG','TOS',
 'TOT', 'TOU', 'TPE', 'TPH','TPL','TRI','TRIL','TRP','TRQ','TRZ','TSL','TTP',
 'TV', 'TVE', 'TVK', 'TXF','TXG','TZS','TZZ','UEX','UFS','UNC','UNS','URE',
 'USA', 'USB', 'VA', 'VB','VCB','VCM','VDY','VEH','VET','VGZ','VII','VIU',
 'VLE', 'VMO', 'VNR', 'VRX','VSB','VSC','VSG','VUN','WCN','WFC','WFT','WG',
 'WIN', 'WM', 'WPRT', 'WPX','WRG','WRN','WXM','X','XAL','XCD','XDC','XEB',
 'XEC', 'XEM', 'XEN', 'XFI','XHB','XID','XIN','XIT','XLB','XMC','XMD','XMY',
 'XSC', 'XSI', 'XST', 'XTC','Y','YMI','ZAG','ZAR','ZBK','ZGI','ZID','ZLC',
 'ZMT', 'ZRE', 'ZSP', 'ZST', 'ZUE', 'ZZZ']

    for i in range(len(names)):
        names[i]=names[i]+ext

    return names
         
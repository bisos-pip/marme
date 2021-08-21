# -*- coding: utf-8 -*-
"""\
* *[Summary]* ::  A /library/ to identify *this* ICM Pkg in the general context of icmPkgs
"""

####+BEGIN: bx:icm:python:top-of-file :partof "bystar" :copyleft "halaal+minimal"
"""
*  This file:/acct/smb/com/dev-py/LUE/Sync/pypi/pkgs/unisos/marme/dev/unisos/marme/icmsPkgThis.py :: [[elisp:(org-cycle)][| ]]
 is part of The Libre-Halaal ByStar Digital Ecosystem. http://www.by-star.net
 *CopyLeft*  This Software is a Libre-Halaal Poly-Existential. See http://www.freeprotocols.org
 A Python Interactively Command Module (PyICM). Part Of ByStar.
 Best Developed With COMEEGA-Emacs And Best Used With Blee-ICM-Players.
 Warning: All edits wityhin Dynamic Blocks may be lost.
"""
####+END:

"""
*  [[elisp:(org-cycle)][| *Lib-Module-INFO:* |]] :: Author, Copyleft and Version Information
"""

####+BEGIN: bx:global:lib:name-py :style "fileName"
__libName__ = "icmsPkgThis"
####+END:

####+BEGIN: bx:global:timestamp:version-py :style "date"
__version__ = "201805150812"
####+END:

####+BEGIN: bx:global:icm:status-py :status "Production"
__status__ = "Production"
####+END:

__credits__ = [""]

####+BEGIN: bx:dblock:global:file-insert-cond :cond "./blee.el" :file "/libre/ByStar/InitialTemplates/update/sw/icm/py/icmInfo-mbNedaGpl.py"
icmInfo = {
    'authors':         ["[[http://mohsen.1.banan.byname.net][Mohsen Banan]]"],
    'copyright':       "Copyright 2017, [[http://www.neda.com][Neda Communications, Inc.]]",
    'licenses':        ["[[https://www.gnu.org/licenses/agpl-3.0.en.html][Affero GPL]]", "Libre-Halaal Services License", "Neda Commercial License"],
    'maintainers':     ["[[http://mohsen.1.banan.byname.net][Mohsen Banan]]",],
    'contacts':        ["[[http://mohsen.1.banan.byname.net/contact]]",],
    'partOf':          ["[[http://www.by-star.net][Libre-Halaal ByStar Digital Ecosystem]]",]
}
####+END:

####+BEGIN: bx:icm:python:topControls 
"""
*  [[elisp:(org-cycle)][|/Controls/| ]] :: [[elisp:(org-show-subtree)][|=]]  [[elisp:(show-all)][Show-All]]  [[elisp:(org-shifttab)][Overview]]  [[elisp:(progn (org-shifttab) (org-content))][Content]] | [[file:Panel.org][Panel]] | [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] | [[elisp:(bx:org:run-me)][Run]] | [[elisp:(bx:org:run-me-eml)][RunEml]] | [[elisp:(delete-other-windows)][(1)]] | [[elisp:(progn (save-buffer) (kill-buffer))][S&Q]]  [[elisp:(save-buffer)][Save]]  [[elisp:(kill-buffer)][Quit]] [[elisp:(org-cycle)][| ]]
** /Version Control/ ::  [[elisp:(call-interactively (quote cvs-update))][cvs-update]]  [[elisp:(vc-update)][vc-update]] | [[elisp:(bx:org:agenda:this-file-otherWin)][Agenda-List]]  [[elisp:(bx:org:todo:this-file-otherWin)][ToDo-List]]
"""
####+END:

####+BEGIN: bx:dblock:global:file-insert-cond :cond "./blee.el" :file "/libre/ByStar/InitialTemplates/software/plusOrg/dblock/inserts/pyWorkBench.org"
"""
* 
*  /Python Workbench/ ::  [[elisp:(org-cycle)][| ]]  [[elisp:(python-check (format "pyclbr %s" (bx:buf-fname))))][pyclbr]] || [[elisp:(python-check (format "pyflakes %s" (bx:buf-fname)))][pyflakes]] | [[elisp:(python-check (format "pychecker %s" (bx:buf-fname))))][pychecker (executes)]] | [[elisp:(python-check (format "pep8 %s" (bx:buf-fname))))][pep8]] | [[elisp:(python-check (format "flake8 %s" (bx:buf-fname))))][flake8]] | [[elisp:(python-check (format "pylint %s" (bx:buf-fname))))][pylint]]  [[elisp:(org-cycle)][| ]]
"""
####+END:

####+BEGIN: bx:icm:python:section :title "ContentsList"
"""
*  [[elisp:(beginning-of-buffer)][Top]] ################ [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *ContentsList*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:

####+BEGIN: bx:dblock:python:icmItem :itemType "=Imports=" :itemTitle "*IMPORTS*"
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || =Imports=      :: *IMPORTS*  [[elisp:(org-cycle)][| ]]
"""
####+END:

import os
#import collections
#import enum


####+BEGIN: bx:dblock:global:file-insert :file "/libre/ByStar/InitialTemplates/update/sw/icm/py/importUcfIcmG.py"
from unisos import ucf
from unisos import icm

icm.unusedSuppressForEval(ucf.__file__)  # in case icm and ucf are not used

G = icm.IcmGlobalContext()
G.icmLibsAppend = __file__
G.icmCmndsLibsAppend = __file__

####+END:


import sys
import os

import collections

from unisos import ucf
from unisos import icm

from blee.icmPlayer import bleep

from bisos.currents import bxCurrentsConfig

from unisos.x822Msg import msgOut
#from bxMsg import msgIn
#from bxMsg import msgLib

from unisos.marme import marmeAcctsLib
from unisos.marme import marmeSendLib
from unisos.marme import marmeTrackingLib

import re

import email
import mailbox

import flufl.bounce

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.MIMEBase import MIMEBase



####+BEGIN: bx:dblock:python:section :title "Library Description (Overview)"
"""
*  [[elisp:(beginning-of-buffer)][Top]] ################ [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *Library Description (Overview)*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:

####+BEGIN: bx:icm:python:cmnd:classHead :cmndName "marmePkgThis_libOverview" :comment "" :parsMand "" :parsOpt "" :argsMin "0" :argsMax "3" :asFunc "" :interactiveP ""
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || ICM-Cmnd       :: /marmePkgThis_libOverview/ parsMand= parsOpt= argsMin=0 argsMax=3 asFunc= interactive=  [[elisp:(org-cycle)][| ]]
"""
class marmePkgThis_libOverview(icm.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 0, 'Max': 3,}

    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
        interactive=False,        # Can also be called non-interactively
        argsList=[],         # or Args-Input
    ):
        cmndOutcome = self.getOpOutcome()
        if interactive:
            if not self.cmndLineValidate(outcome=cmndOutcome):
                return cmndOutcome
            effectiveArgsList = G.icmRunArgsGet().cmndArgs
        else:
            effectiveArgsList = argsList

        callParamsDict = {}
        if not icm.cmndCallParamsValidate(callParamsDict, interactive, outcome=cmndOutcome):
            return cmndOutcome

        cmndArgsSpecDict = self.cmndArgsSpec()
        if not self.cmndArgsValidate(effectiveArgsList, cmndArgsSpecDict, outcome=cmndOutcome):
            return cmndOutcome
####+END:

        moduleDescription="""
*       [[elisp:(org-show-subtree)][|=]]  [[elisp:(org-cycle)][| *Description:* | ]]
**  [[elisp:(org-cycle)][| ]]  [Xref]          :: *[Related/Xrefs:]*  <<Xref-Here->>  -- External Documents  [[elisp:(org-cycle)][| ]]

**  [[elisp:(org-cycle)][| ]]	Model and Terminology 					   :Overview:
This module is part of BISOS and its primary documentation is in  http://www.by-star.net/PLPC/180047
**      [End-Of-Description]
"""
        
        moduleUsage="""
*       [[elisp:(org-show-subtree)][|=]]  [[elisp:(org-cycle)][| *Usage:* | ]]

**      How-Tos:
**      [End-Of-Usage]
"""
        
        moduleStatus="""
*       [[elisp:(org-show-subtree)][|=]]  [[elisp:(org-cycle)][| *Status:* | ]]
**  [[elisp:(org-cycle)][| ]]  [Info]          :: *[Current-Info:]* Status/Maintenance -- General TODO List [[elisp:(org-cycle)][| ]]
** TODO [[elisp:(org-cycle)][| ]]  Current         :: Just getting started [[elisp:(org-cycle)][| ]]
**      [End-Of-Status]
"""
####+BEGIN: bx:dblock:global:file-insert-cond :cond "./blee.el" :file "/libre/ByStar/InitialTemplates/update/sw/icm/py/moduleOverview.py"
        icm.unusedSuppressForEval(moduleUsage, moduleStatus)
        actions = self.cmndArgsGet("0&2", cmndArgsSpecDict, effectiveArgsList)
        if actions[0] == "all":
            cmndArgsSpec = cmndArgsSpecDict.argPositionFind("0&2")
            argChoices = cmndArgsSpec.argChoicesGet()
            argChoices.pop(0)
            actions = argChoices
        for each in actions:
            print each
            if interactive:
                #print( str( __doc__ ) )  # This is the Summary: from the top doc-string
                #version(interactive=True)
                exec("""print({})""".format(each))
                
        return(format(str(__doc__)+moduleDescription))

    """
**  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Method-anyOrNone :: /cmndArgsSpec/ retType=bool argsList=nil deco=default  [[elisp:(org-cycle)][| ]]
"""
    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmndArgsSpec(self):
        """
***** Cmnd Args Specification
"""
        cmndArgsSpecDict = icm.CmndArgsSpecDict()
        cmndArgsSpecDict.argsDictAdd(
            argPosition="0&2",
            argName="actions",
            argDefault='all',
            argChoices=['all', 'moduleDescription', 'moduleUsage', 'moduleStatus'],
            argDescription="Output relevant information",
        )

        return cmndArgsSpecDict
####+END:
        

"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Enum         ::  DsnType    [[elisp:(org-cycle)][| ]]
"""
DsnType = ucf.Enum(
    deliveryReport='deliveryReport',
    receiptNotification='receiptNotification',
    ndrNoCoRecipients='ndrNoCoRecipients',
    ndrWithCoRecipients='ndrWithCoRecipients',
    tmpNonDeliveryReport='tmpNonDeliveryReport',
    notADsn='notADsn',
)


"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func         ::  msgDsnTypeDetect    [[elisp:(org-cycle)][| ]]
"""
@icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
def msgDsnTypeDetect(
    inMsg,
    failedMsg,
    tempFailedRecipients,
    permFailedRecipients,
    coRecipients,        
):        
    """ 
** Returns a DsnType.
"""
    if tempFailedRecipients:
        return DsnType.tmpNonDeliveryReport
 
    elif permFailedRecipients:
        if coRecipients:
            return DsnType.ndrWithCoRecipients
        else:
            return DsnType.ndrNoCoRecipients

    # Delivery Report Needs To Be Detected

    # Receipt Notification Needs To Be Detected
    
    elif inMsg['subject'] == "Delivery delay notification":
        return DsnType.tmpNonDeliveryReport
        
    else:
        return DsnType.notADsn

"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func         ::  dsnTypeShortReport    [[elisp:(org-cycle)][| ]]
"""
@icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
def dsnTypeShortReport(
        inMsg,
        typeStr,
):
    icm.ANN_note("""{typeStr:15}:: {msgId}""".format(
        typeStr=typeStr, msgId=str(inMsg['message-id']),))

    
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func         ::  dsnTypeLongReport    [[elisp:(org-cycle)][| ]]
"""    
@icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
def dsnTypeLongReport(
        inMsg,
        typeStr,
):
    icm.ANN_note("""{typeStr:20}:: {msgId} -- {date} -- {subject}""".format(
        typeStr=typeStr, msgId=str(inMsg['message-id']),
        date=str(inMsg['date']), subject=str(inMsg['subject']),
        ))
    

"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func         ::  dsnTypeReports    [[elisp:(org-cycle)][| ]]
"""
@icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
def dsnTypeReports(
    inMsg,
    dsnType,
    reportType,
):

    def dsnTypeStrReport(
            inMsg,
            typeStr,
            reportType,
    ):
        if reportType == "short":
            dsnTypeShortReport(inMsg, typeStr,)
        elif reportType == "long":
            dsnTypeLongReport(inMsg, typeStr,)
        else:
            icm.EH_critical_oops()

    if dsnType == DsnType.deliveryReport:
        dsnTypeStrReport(inMsg, "Delivery Report", reportType,)
        
    elif dsnType == DsnType.receiptNotification:
        dsnTypeStrReport(inMsg, "Receipt Notification", reportType,)
    
    elif dsnType == DsnType.ndrNoCoRecipients:
        dsnTypeStrReport(inMsg, "ndrNoCoRecipients", reportType,)

    elif dsnType == DsnType.ndrWithCoRecipients:
        dsnTypeStrReport(inMsg, "ndrWithCoRecipients", reportType,)
 
    elif dsnType == DsnType.tmpNonDeliveryReport:
        dsnTypeStrReport(inMsg, "tmpNonDeliveryReport", reportType,)        

    elif dsnType == DsnType.notADsn:
        dsnTypeStrReport(inMsg, "Not A DSN", reportType,)        

    else:
        icm.EH_critical_oops()



"""
*  [[elisp:(beginning-of-buffer)][Top]] ################ [[elisp:(delete-other-windows)][(1)]]      *Support Functions For MsgProcs*
"""

"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func         ::  fromNonDeliveryReportGetFailedMsg    [[elisp:(org-cycle)][| ]]
"""
@icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
def fromNonDeliveryReportGetFailedMsg(
    nonDeliveryReportMsg,        
    tempFailedRecipients,
    permFailedRecipients,
):
    """ 
** returns the extracted failed message from the non-delivery-report. Or None.
"""

    if not (tempFailedRecipients or permFailedRecipients):
        # This is NOT a nonDeliveryReport
        return None

    #
    # Get the failed message as an attachement
    # 
    for part in nonDeliveryReportMsg.walk():
        if part.get_content_type() == 'message/rfc822':
            failedMsgList = part.get_payload()
            if failedMsgList:
                #for failedMsg in failedMsgList:
                nuOfFailedMsgs = len(failedMsgList)
                if nuOfFailedMsgs != 1:
                    icm.EH_problem_info("More Then One -- Expected One")
                    return None
                else:
                    return failedMsgList[0]

    #
    # So,the failed message was not included and is part of the body.
    #
    
    #scre = re.compile(b'mail to the following recipients could not be delivered')
    scre = re.compile(b'-- The header and top 20 lines of the message follows --')

    msg = nonDeliveryReportMsg
    failedMsgStr = ""
    found = False
    for line in msg.get_payload(decode=True).splitlines():
        if scre.search(line):
            found = "gotIt"
            continue
        if found == "gotIt":  # This consumes an empty line
            found = True
            continue
        if found == True:
            failedMsgStr = failedMsgStr + line + '\n'

    if found:
        return email.message_from_string(failedMsgStr)
    else:
        return None

"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func         ::  fromFailedMsgGetCoRecipients    [[elisp:(org-cycle)][| ]]
"""
@icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
def fromFailedMsgGetCoRecipients(
    failedMsg,
    tempFailedRecipients,
    permFailedRecipients,
):
    """ 
** Return list of CoRecipients or None
"""
    if not (tempFailedRecipients or permFailedRecipients):
        # This is NOT a nonDeliveryReport
        return None

    if not failedMsg:
        icm.EH_critical_unassigedError("UnFound FailedMsg")
        return None
   
    allRecipients= None

    tos = failedMsg.get_all('to', [])
    ccs = failedMsg.get_all('cc', [])
    resent_tos = failedMsg.get_all('resent-to', [])
    resent_ccs = failedMsg.get_all('resent-cc', [])
    allRecipients = email.utils.getaddresses(tos + ccs + resent_tos + resent_ccs)
                
    if not allRecipients:
        icm.EH_problem_unassignedError("allRecipients is None")
        return None

    allRecipientsSet = set()
    for thisRecipient in allRecipients:
        allRecipientsSet.add(thisRecipient[1])

    failedRecipients = tempFailedRecipients | permFailedRecipients
        
    coRecipientsSet = allRecipientsSet - failedRecipients

    if coRecipientsSet:
        return coRecipientsSet
    else:
        return None


"""
*  [[elisp:(beginning-of-buffer)][Top]] ################ [[elisp:(delete-other-windows)][(1)]]      *Msg ReFiling*
"""
    

"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func         ::  msgMoveToFolder    [[elisp:(org-cycle)][| ]]
"""
@icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
def msgMoveToFolder(
        destFolder,
        srcMaildir,        
        srcMbox,
        srcKey,
        srcMsg,
):
    """ 
** Given a srcMbox and a srcMsg, move it to the specified  destination.
"""
    srcMailBase = os.path.dirname(srcMaildir)

    destMbox = mailbox.Maildir(
            os.path.join(srcMailBase, destFolder),
            factory=None,  # important!! default does not work
    )

    # Write copy to disk before removing original.
    # If there's a crash, you might duplicate a message, but
    # that's better than losing a message completely.
    destMbox.lock()
    destMbox.add(srcMsg)
    destMbox.flush()
    destMbox.unlock()

    # Remove original message
    srcMbox.lock()
    srcMbox.discard(srcKey)
    srcMbox.flush()
    srcMbox.unlock()

    destMbox.close()


####+BEGIN: bx:icm:python:section :title "Unused Facilities -- Temporary Junk Yard"
"""
*  [[elisp:(beginning-of-buffer)][Top]] ################ [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *Unused Facilities -- Temporary Junk Yard*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:
"""
*       /Empty/  [[elisp:(org-cycle)][| ]]
"""

####+BEGIN: bx:icm:python:section :title "End Of Editable Text"
"""
*  [[elisp:(beginning-of-buffer)][Top]] ################ [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *End Of Editable Text*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:

####+BEGIN: bx:dblock:global:file-insert-cond :cond "./blee.el" :file "/libre/ByStar/InitialTemplates/software/plusOrg/dblock/inserts/endOfFileControls.org"
#+STARTUP: showall
####+END:

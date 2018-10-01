# -*- coding: utf-8 -*-
"""\
* TODO *[Summary]* ::  A /library/ with ICM Cmnds to support ByStar facilities
"""

####+BEGIN: bx:icm:python:top-of-file :partof "bystar" :copyleft "halaal+minimal"
"""
*  This file:/de/bx/nne/dev-py/pypi/pkgs/unisos/marme/dev/unisos/marme/new-marmeSendLib.py :: [[elisp:(org-cycle)][| ]]
** is part of The Libre-Halaal ByStar Digital Ecosystem. http://www.by-star.net
** *CopyLeft*  This Software is a Libre-Halaal Poly-Existential. See http://www.freeprotocols.org
** A Python Interactively Command Module (PyICM). Part Of ByStar.
** Best Developed With COMEEGA-Emacs And Best Used With Blee-ICM-Players.
** Warning: All edits wityhin Dynamic Blocks may be lost.
"""
####+END:


"""
*  [[elisp:(org-cycle)][| *Lib-Module-INFO:* |]] :: Author, Copyleft and Version Information
"""

####+BEGIN: bx:global:lib:name-py :style "fileName"
__libName__ = "new-marmeSendLib"
####+END:

####+BEGIN: bx:global:timestamp:version-py :style "date"
__version__ = "201712252535"
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
*  [[elisp:(org-cycle)][|/Controls/| ]] :: [[elisp:(org-show-subtree)][|=]] [[elisp:(show-all)][Show-All]]  [[elisp:(org-shifttab)][Overview]]  [[elisp:(progn (org-shifttab) (org-content))][Content]] | [[file:Panel.org][Panel]] | [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] | [[elisp:(bx:org:run-me)][Run]] | [[elisp:(bx:org:run-me-eml)][RunEml]] | [[elisp:(delete-other-windows)][(1)]] | [[elisp:(progn (save-buffer) (kill-buffer))][S&Q]]  [[elisp:(save-buffer)][Save]]  [[elisp:(kill-buffer)][Quit]] [[elisp:(org-cycle)][| ]]
** /Version Control/ ::  [[elisp:(call-interactively (quote cvs-update))][cvs-update]]  [[elisp:(vc-update)][vc-update]] | [[elisp:(bx:org:agenda:this-file-otherWin)][Agenda-List]]  [[elisp:(bx:org:todo:this-file-otherWin)][ToDo-List]]
"""
####+END:

"""
* 
####+BEGIN: bx:dblock:global:file-insert-cond :cond "./blee.el" :file "/libre/ByStar/InitialTemplates/software/plusOrg/dblock/inserts/pythonWb.org"
*  /Python Workbench/ ::  [[elisp:(org-cycle)][| ]]  [[elisp:(python-check (format "pyclbr %s" (bx:buf-fname))))][pyclbr]] || [[elisp:(python-check (format "pyflakes %s" (bx:buf-fname)))][pyflakes]] | [[elisp:(python-check (format "pychecker %s" (bx:buf-fname))))][pychecker (executes)]] | [[elisp:(python-check (format "pep8 %s" (bx:buf-fname))))][pep8]] | [[elisp:(python-check (format "flake8 %s" (bx:buf-fname))))][flake8]] | [[elisp:(python-check (format "pylint %s" (bx:buf-fname))))][pylint]]  [[elisp:(org-cycle)][| ]]
####+END:
"""


####+BEGIN: bx:icm:python:section :title "ContentsList"
"""
*  [[elisp:(beginning-of-buffer)][Top]] ################ [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *ContentsList*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:

####+BEGIN: bx:dblock:python:func :funcName "insertPathForImports" :funcType "FrameWrk" :retType "none" :deco "" :argsList "path"
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func-FrameWrk  :: /insertPathForImports/ retType=none argsList=(path)  [[elisp:(org-cycle)][| ]]
"""
def insertPathForImports(
    path,
):
####+END:
    """
** Extends Python imports path with  ../lib/python
"""
    import os
    import sys
    absolutePath = os.path.abspath(path)    
    if os.path.isdir(absolutePath):
        sys.path.insert(1, absolutePath)

insertPathForImports("../lib/python/")



####+BEGIN: bx:dblock:python:icmItem :itemType "=Imports=" :itemTitle "*IMPORTS*"
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || =Imports=      :: *IMPORTS*  [[elisp:(org-cycle)][| ]]
"""
####+END:

import os
import collections
import enum

# NOTYET, should become a dblock with its own subItem
from unisos import ucf
from unisos import icm

G = icm.IcmGlobalContext()
G.icmLibsAppend = __file__
G.icmCmndsLibsAppend = __file__
# NOTYET DBLOCK Ends -- Rest of bisos libs follow;

import marmeAcctsLib

#import shlex
#import subprocess

#from datetime import datetime

#import re
#import pprint

import email
#import mailbox
#import smtplib

#import flufl.bounce

from unisos.x822Msg import msgOut
from unisos.x822Msg import msgIn


####+BEGIN: bx:dblock:python:section :title "Library Description (Overview)"
"""
*  [[elisp:(beginning-of-buffer)][Top]] ################ [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *Library Description (Overview)*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:

####+BEGIN: bx:dblock:python:icm:cmnd:classHead :modPrefix "new" :cmndName "bxpBaseDir_LibOverview" :parsMand "" :parsOpt "" :argsMin "0" :argsMax "3" :asFunc "" :interactiveP ""
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || ICM-Cmnd       :: /bxpBaseDir_LibOverview/ parsMand= parsOpt= argsMin=0 argsMax=3 asFunc= interactive=  [[elisp:(org-cycle)][| ]]
"""
class marmeSendLib_LibOverview(icm.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 0, 'Max': 3,}

    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
        interactive=False,        # Can also be called non-interactively
        argsList=None,         # or Args-Input
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
        cmndArgsSpec = {"0&-1": ['moduleDescription', 'moduleUsage', 'moduleStatus']}
        cmndArgsValid = cmndArgsSpec["0&-1"]
        for each in effectiveArgsList:
            if each in cmndArgsValid:
                print each
                if interactive:
                    #print( str( __doc__ ) )  # This is the Summary: from the top doc-string
                    #version(interactive=True)
                    exec("""print({})""".format(each))
                
        return(format(str(__doc__)+moduleDescription))

####+BEGIN: bx:dblock:python:section :title "Support Functions For MsgProcs"
"""
*  [[elisp:(beginning-of-buffer)][Top]] ################ [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *Support Functions For MsgProcs*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:

"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Class-IIF    ::  sendCompleteMessage    [[elisp:(org-cycle)][| ]]
"""
class sendCompleteMessage(icm.Cmnd):
    """
** Submit a message using inFile =purely=. 
"""
    
    cmndParamsMandatory = ['inFile']
    cmndParamsOptional = []        
    cmndArgsLen = {'Min': 0, 'Max': 0,}

####+BEGIN: bx:dblock:python:icm:cmnd:parsValidate :par "inFile" :asFunc "msg"
    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
        interactive=False,        # Can also be called non-interactively
        inFile=None,         # or Cmnd-Input
        msg=None,         # asFunc when interactive==False
    ):
        cmndOutcome = self.getOpOutcome()
        if interactive:
            if not self.cmndLineValidate(outcome=cmndOutcome):
                return cmndOutcome

        callParamsDict = {'inFile': inFile, }
        if not icm.cmndCallParamsValidate(callParamsDict, interactive, outcome=cmndOutcome):
            return cmndOutcome
        inFile = callParamsDict['inFile']
####+END:
        
        G = icm.IcmGlobalContext()

        if not msg:
            if inFile:
                msg = msgIn.getMsgFromFile(inFile)
            else:
                # Stdin then
                msg = msgIn.getMsgFromStdin()

        icm.LOG_here(msgOut.strLogMessage(
            "Msg As Input:", msg,))

        print G.icmRunArgsGet().runMode

        outcome = msgOut.sendingRunControlSet(msg, G.icmRunArgsGet().runMode)
        if outcome.isProblematic(): return(icm.EH_badOutcome(outcome))
        
        bx822Set_setMandatoryFields(msg)
        
        outcome = bx822Get_sendingFieldsPipelineLoad(msg)
        if outcome.isProblematic(): return(icm.EH_badOutcome(outcome))
        
        if outcome.results != "INCOMPLETE":
            icm.LOG_here("Complete Message Being Sent")
            return (
                msgOut.sendBasedOnHeadersInfo(msg)
            )

        icm.LOG_here("Incomplete Message -- using qmail+dryrun")

        msgOut.injectionParams(
            msg,
            injectionProgram=msgOut.InjectionProgram.qmail,
            sendingRunControl=msgOut.SendingRunControl.dryRun,        
        )

        return msgOut.sendBasedOnHeadersInfo(msg)

"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func         ::  bx822Set_sendWithEnabledAcct    [[elisp:(org-cycle)][| ]]
"""
def bx822Set_sendWithEnabledAcct(
        msg,
        sendingMethod,
):
    """
** Setup BX-Send-WithControlProfile and BX-Send-WithAcctName to enabledAcct
"""
    if sendingMethod == msgOut.SendingMethod.inject:
        return True
    elif sendingMethod == msgOut.SendingMethod.submit:
        if not 'BX-Send-WithControlProfile' in msg:
            msg['BX-Send-WithControlProfile'] = marmeAcctsLib.enabledControlProfileObtain()
        if not 'BX-Send-WithAcctName' in msg:
            msg['BX-Send-WithAcctName'] = marmeAcctsLib.enabledInMailAcctObtain()
        return True
    else:
        return False
    

"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func         ::  bx822Set_setMandatoryFields    [[elisp:(org-cycle)][| ]]
"""
def bx822Set_setMandatoryFields(
    msg,
):
    """
** Mail Sending Agent's Final Setups: Date, Message-ID, User-Agent, if needed
"""
    if not 'Date' in msg:
        msg['Date'] = email.utils.formatdate(localtime = 1)

    if not 'Message-ID' in msg:
        msg['Message-ID'] = email.utils.make_msgid()

    if not 'User-Agent' in msg:
        msg['User-Agent'] = "Marme/VersionNu"

        
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func         ::  bx822Get_sendingFieldsPipelineLoad    [[elisp:(org-cycle)][| ]]
"""
def bx822Get_sendingFieldsPipelineLoad(
    msg,
):
    """
** Look for BX-Send-WithAcctName or BX-Send-WithBaseDir, and based on those prep the Bx822 fields.
"""
    opOutcome = icm.OpOutcome()
    if 'BX-Send-WithAcctName' in msg:
        controlProfile = msg['BX-Send-WithControlProfile']
        outMailAcct = msg['BX-Send-WithAcctName']        
        return (
            msgSendingPipelineLoadFromAcct(
                msg,
                controlProfile,
                outMailAcct,
            ))
    elif 'BX-Send-WithBaseDir' in msg:
        acctBaseDir = msg['BX-Send-WithBaseDir']
        return (
            msgSendingPipelineLoadFromAcctBaseDir(
                msg,
                acctBaseDir,
            ))
    else:
        return opOutcome.set(opResults='INCOMPLETE')


"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func         ::  msgSendingPipelineLoadFromAcct    [[elisp:(org-cycle)][| ]]
"""    
def msgSendingPipelineLoadFromAcct(
        msg,
        controlProfile,
        outMailAcct,
):
    """
** Just call with obtained base for acct.
    """
    acctBaseDir = marmeAcctsLib.outMailAcctDirGet(controlProfile, outMailAcct)
    return (
        msgSendingPipelineLoadFromAcctBaseDir(
            msg,
            acctBaseDir,
        ))

"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func         ::  msgSendingPipelineLoadFromAcctBaseDir    [[elisp:(org-cycle)][| ]]
"""
def msgSendingPipelineLoadFromAcctBaseDir(
        msg,
        acctBaseDir,
):
    """
** Read File Params for mailAcct and set X822-MSP params accordingly
    """
    opOutcome = icm.OpOutcome()
    #print acctBaseDir
    #G = icm.IcmGlobalContext()

    outcome = icm.FP_readTreeAtBaseDir().cmnd(
        interactive=False,
        FPsDir=os.path.join(acctBaseDir, 'access'),
    )
    fp_access_dict = outcome.results

    outcome = icm.FP_readTreeAtBaseDir().cmnd(
        interactive=False,
        FPsDir=os.path.join(acctBaseDir, 'controllerInfo'),
    )
    #fp_controllerInfo_dict = outcome.results
    
    outcome = icm.FP_readTreeAtBaseDir().cmnd(
        interactive=False,
        FPsDir=os.path.join(acctBaseDir, 'submission'),
    )
    fp_submission_dict = outcome.results

    envelopeAddr = fp_submission_dict["envelopeAddr"].parValueGet()
    
    msgOut.envelopeAddrSet(
        msg,
        mailBoxAddr=envelopeAddr,  # Mandatory
    )

    sendingMethod = fp_submission_dict["sendingMethod"].parValueGet()

    if msgOut.sendingMethodSet(msg, sendingMethod).isProblematic():
        return icm.EH_badLastOutcome()

    if sendingMethod == msgOut.SendingMethod.inject:
        return opOutcome

    #
    # So, It is a submission 
    #
    # NOTYET, below should be split and use
    #  msgOut.submitParamsNOT()
    #

    try:
        mtaRemHost = fp_access_dict["mtaRemHost"].parValueGet()
    except  KeyError:
        return icm.eh_problem_usageError(opOutcome, "Missing BX-MTA-Rem-Host")

    try:
        userName = fp_access_dict["userName"].parValueGet()
    except  KeyError:
        return icm.eh_problem_usageError(opOutcome, "Missing BX-MTA-Rem-User")

    try:
        userPasswd = fp_access_dict["userPasswd"].parValueGet()
    except  KeyError:
        return icm.eh_problem_usageError(opOutcome, "Missing BX-MTA-Rem-Passwd")

    try:
        remProtocol = fp_access_dict["mtaRemProtocol"].parValueGet()        
    except  KeyError:
        return icm.eh_problem_usageError(opOutcome, "Missing BX-MTA-Rem-Protocol")
    
    try:
        remPortNu = fp_access_dict["mtaRemPortNu"].parValueGet()
    except  KeyError:
        remPortNu = None

    msgOut.submitParams(
        msg,
        mtaRemProtocol=remProtocol,          # smtp
        mtaRemHost=mtaRemHost,              # Remote Host To Submit to (could be localhost)
        mtaRemPort=remPortNu,
        mtaRemUser=userName,        
        mtaRemPasswd=userPasswd,
        mtaRemCerts=None,
    )
    
    return opOutcome
    
    

####+BEGIN: bx:icm:python:section :title "End Of Editable Text"
"""
*  [[elisp:(beginning-of-buffer)][Top]] ################ [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *End Of Editable Text*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:

####+BEGIN: bx:dblock:global:file-insert-cond :cond "./blee.el" :file "/libre/ByStar/InitialTemplates/software/plusOrg/dblock/inserts/endOfFileControls.org"
#+STARTUP: showall
####+END:

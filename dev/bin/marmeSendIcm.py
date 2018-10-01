#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""\
* TODO *[Summary]* :: An =ICM=: a basic mail sending script
"""

####+BEGIN: bx:icm:python:top-of-file :partof "bystar" :copyleft "halaal+minimal"
"""
*  This file:/de/bx/nne/dev-py/pypi/pkgs/unisos/marme/dev/bin/marmeSendIcm.py :: [[elisp:(org-cycle)][| ]]
 is part of The Libre-Halaal ByStar Digital Ecosystem. http://www.by-star.net
 *CopyLeft*  This Software is a Libre-Halaal Poly-Existential. See http://www.freeprotocols.org
 A Python Interactively Command Module (PyICM). Part Of ByStar.
 Best Developed With COMEEGA-Emacs And Best Used With Blee-ICM-Players.
 Warning: All edits wityhin Dynamic Blocks may be lost.
"""
####+END:

"""
*  [[elisp:(org-cycle)][| *ICM-INFO:* |]] :: Author, Copyleft and Version Information
"""
####+BEGIN: bx:icm:python:name :style "fileName"
__icmName__ = "marmeSendIcm"
####+END:

####+BEGIN: bx:global:timestamp:version-py :style "date"
__version__ = "201712253236"
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

####+BEGIN: bx:icm:python:topControls :partof "bystar" :copyleft "halaal+minimal"
"""
*  [[elisp:(org-cycle)][|/Controls/| ]] :: [[elisp:(org-show-subtree)][|=]] [[elisp:(show-all)][Show-All]]  [[elisp:(org-shifttab)][Overview]]  [[elisp:(progn (org-shifttab) (org-content))][Content]] | [[file:Panel.org][Panel]] | [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] | [[elisp:(bx:org:run-me)][Run]] | [[elisp:(bx:org:run-me-eml)][RunEml]] | [[elisp:(delete-other-windows)][(1)]] | [[elisp:(progn (save-buffer) (kill-buffer))][S&Q]]  [[elisp:(save-buffer)][Save]]  [[elisp:(kill-buffer)][Quit]] [[elisp:(org-cycle)][| ]]
** /Version Control/ ::  [[elisp:(call-interactively (quote cvs-update))][cvs-update]]  [[elisp:(vc-update)][vc-update]] | [[elisp:(bx:org:agenda:this-file-otherWin)][Agenda-List]]  [[elisp:(bx:org:todo:this-file-otherWin)][ToDo-List]]
"""
####+END:

####+BEGIN: bx:icm:python:section :title "ContentsList"
"""
*  [[elisp:(beginning-of-buffer)][Top]] ################ [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *ContentsList*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:

####+BEGIN: bx:icm:python:icmItem :itemType "=Imports=" :itemTitle "*IMPORTS*"
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || =Imports=      :: *IMPORTS*  [[elisp:(org-cycle)][| ]]
"""
####+END:

import sys
import os

import email
#import mailbox
#import smtplib

#import flufl.bounce

from email.mime.text import MIMEText
#from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email import Encoders


import collections

from unisos import ucf
from unisos import icm

from blee.icmPlayer import bleep

from unisos.x822Msg import msgOut
from unisos.x822Msg import msgIn
#from unisos.x822Msg import msgLib

from unisos.marme import marmeAcctsLib
from unisos.marme import marmeSendLib

g_importedCmnds = {        # Enumerate modules from which CMNDs become invokable
    'bleep': bleep.__file__,    
    'marmeAcctsLib': marmeAcctsLib.__file__,
    'marmeSendLib': marmeSendLib.__file__,    
}


####+BEGIN: bx:icm:python:section :title "= =Framework::= ICM  Description (Overview) ="
"""
*  [[elisp:(beginning-of-buffer)][Top]] ################ [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *= =Framework::= ICM  Description (Overview) =*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:


####+BEGIN: bx:icm:python:cmnd:classHead :modPrefix "new" :cmndName "icmOverview" :parsMand "" :parsOpt "" :argsMin "0" :argsMax "3" :asFunc "" :interactiveP ""
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || ICM-Cmnd       :: /icmOverview/ parsMand= parsOpt= argsMin=0 argsMax=3 asFunc= interactive=  [[elisp:(org-cycle)][| ]]
"""
class icmOverview(icm.Cmnd):
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
*** See BISOS Documentation for ICM's model and terminology
**      [End-Of-Description]
"""
        
        moduleUsage="""
*       [[elisp:(org-show-subtree)][|=]]  [[elisp:(org-cycle)][| *Usage:* | ]]

**      How-Tos:
*** TODO Edit icmInfo to identify author, etc
*** TODO Select ICM type in g_icmChars
*** TODO Enhance g_argsExtraSpecify for your parameters
*** TODO Add your Commands
*** TODO Enhance Examples Cmnd
**      [End-Of-Usage]
"""
        
        moduleStatus="""
*       [[elisp:(org-show-subtree)][|=]]  [[elisp:(org-cycle)][| *Status:* | ]]
**  [[elisp:(org-cycle)][| ]]  [Info]          :: *[Current-Info:]* Status/Maintenance -- General TODO List [[elisp:(org-cycle)][| ]]
** TODO [[elisp:(org-cycle)][| ]]  Current         :: Just getting started [[elisp:(org-cycle)][| ]]
**      [End-Of-Status]
"""

####+BEGIN: bx:dblock:global:file-insert-cond :cond "./blee.el" :file "/libre/ByStar/InitialTemplates/update/sw/icm/py/moduleOverview.py"
        cmndArgsSpec = {"0&-1": ['moduleDescription', 'moduleUsage', 'moduleStatus']}
        cmndArgsValid = cmndArgsSpec["0&-1"]
        icm.unusedSuppressForEval(moduleDescription, moduleUsage, moduleStatus)
        for each in effectiveArgsList:
            if each in cmndArgsValid:
                if interactive:
                    exec("""print({})""".format(each))
                
        return(format(str(__doc__)+moduleDescription))
####+END:


        
####+BEGIN: bx:icm:python:section :title "= =Framework::= ICM Hooks ="
"""
*  [[elisp:(beginning-of-buffer)][Top]] ################ [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *= =Framework::= ICM Hooks =*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:

####+BEGIN: bx:icm:python:func :funcName "g_icmChars" :comment "ICM Characteristics Spec" :funcType "FrameWrk" :retType "Void" :deco "" :argsList ""
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func-FrameWrk  :: /g_icmChars/ =ICM Characteristics Spec= retType=Void argsList=nil  [[elisp:(org-cycle)][| ]]
"""
def g_icmChars(
):
####+END:
    icmInfo['panel'] = "{}-Panel.org".format(__icmName__)
    icmInfo['groupingType'] = "IcmGroupingType-pkged"
    icmInfo['cmndParts'] = "IcmCmndParts[common] IcmCmndParts[param]"
    
g_icmChars()


####+BEGIN: bx:icm:python:func :funcName "g_icmPreCmnds" :funcType "FrameWrk" :retType "Void" :deco "default" :argsList ""
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func-FrameWrk  :: /g_icmPreCmnds/ retType=Void argsList=nil deco=default  [[elisp:(org-cycle)][| ]]
"""
@icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
def g_icmPreCmnds(
):
####+END:
    """ PreHook """
    pass


####+BEGIN: bx:icm:python:func :funcName "g_icmPostCmnds" :funcType "FrameWrk" :retType "Void" :deco "default" :argsList ""
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func-FrameWrk  :: /g_icmPostCmnds/ retType=Void argsList=nil deco=default  [[elisp:(org-cycle)][| ]]
"""
@icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
def g_icmPostCmnds(
):
####+END:
    """ PostHook """
    pass


####+BEGIN: bx:icm:python:section :title "= =Framework::= Options, Arguments and Examples Specifications ="
"""
*  [[elisp:(beginning-of-buffer)][Top]] ################ [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *= =Framework::= Options, Arguments and Examples Specifications =*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:


####+BEGIN: bx:icm:python:func :funcName "g_argsExtraSpecify" :comment "FrameWrk: ArgsSpec" :funcType "FrameWrk" :retType "Void" :deco "" :argsList "parser"
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func-FrameWrk  :: /g_argsExtraSpecify/ =FrameWrk: ArgsSpec= retType=Void argsList=(parser)  [[elisp:(org-cycle)][| ]]
"""
def g_argsExtraSpecify(
    parser,
):
####+END:
    """Module Specific Command Line Parameters.
    g_argsExtraSpecify is passed to G_main and is executed before argsSetup (can not be decorated)
    """
    G = icm.IcmGlobalContext()
    icmParams = icm.ICM_ParamDict()

    marmeAcctsLib.commonParamsSpecify(icmParams)    

    icmParams.parDictAdd(
        parName='moduleVersion',
        parDescription="Module Version",
        parDataType=None,
        parDefault=None,
        parChoices=list(),
        parScope=icm.ICM_ParamScope.TargetParam,
        argparseShortOpt=None,
        argparseLongOpt='--version',
    )

    
    icmParams.parDictAdd(
        parName='inFile',
        parDescription="Input File",
        parDataType=None,
        # ../control/outMail/common/template/bynameUtf8.mail
        parDefault=os.path.join(
            marmeAcctsLib.outMailCommonDirGet(marmeAcctsLib.enabledControlProfileObtain()),
            "template/bynameUtf8.mail"
        ),            
        parChoices=["someFile", "UserInput"],
        parScope=icm.ICM_ParamScope.TargetParam,
        argparseShortOpt=None,
        argparseLongOpt='--inFile',
        )
    
    icmParams.parDictAdd(
        parName='fromLine',
        parDescription="From Line",
        parDataType=None,
        parDefault="someFrom@example.com",
        parChoices=["from@example.com", "UserInput"],
        parScope=icm.ICM_ParamScope.TargetParam,
        argparseShortOpt=None,
        argparseLongOpt='--fromLine',
        )
    
    icmParams.parDictAdd(
        parName='toLine',
        parDescription="To Line",
        parDataType=None,
        parDefault="someTo@example.com",
        parChoices=["to@example.com", "UserInput"],
        parScope=icm.ICM_ParamScope.TargetParam,
        argparseShortOpt=None,
        argparseLongOpt='--toLine',
    )
    
    bleep.commonParamsSpecify(icmParams)    
       
    icm.argsparseBasedOnIcmParams(parser, icmParams)

    # So that it can be processed later as well.
    G.icmParamDictSet(icmParams)
    
    return


####+BEGIN: bx:icm:python:cmnd:classHead :modPrefix "new" :cmndName "examples" :cmndType "ICM-Cmnd-FWrk"  :comment "FrameWrk: ICM Examples" :parsMand "" :parsOpt "" :argsMin "0" :argsMax "0" :asFunc "" :interactiveP ""
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || ICM-Cmnd-FWrk  :: /examples/ =FrameWrk: ICM Examples= parsMand= parsOpt= argsMin=0 argsMax=0 asFunc= interactive=  [[elisp:(org-cycle)][| ]]
"""
class examples(icm.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 0, 'Max': 0,}

    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
        interactive=False,        # Can also be called non-interactively
    ):
        cmndOutcome = self.getOpOutcome()
        if interactive:
            if not self.cmndLineValidate(outcome=cmndOutcome):
                return cmndOutcome

        callParamsDict = {}
        if not icm.cmndCallParamsValidate(callParamsDict, interactive, outcome=cmndOutcome):
            return cmndOutcome
####+END:

        icm.ex_gCommon()

        bleep.examples_icmBasic()

        """
**  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Examples   ::  General Dev and Testing IIFs [[elisp:(org-cycle)][| ]]
"""
        icm.cmndExampleMenuChapter('*General Dev and Testing IIFs*')   

        cmndName = "unitTest" ; cmndArgs = "" ; cps = collections.OrderedDict()        
        icm.ex_gCmndMenuItem(cmndName, cps, cmndArgs, verbosity='none')

        
        """
**  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Examples   ::  Default Mail From Complete File [[elisp:(org-cycle)][| ]]
"""

        enabledControlProfile = marmeAcctsLib.enabledControlProfileObtain()
        enabledOutMailAcct = marmeAcctsLib.enabledOutMailAcctObtain()
        
        icm.cmndExampleMenuChapter("""*Mail From Complete File -- Default ControlProfile={controlProfile} Acct={mailAcct}*""".format(
                controlProfile=marmeAcctsLib.enabledControlProfileObtain(), mailAcct=enabledOutMailAcct,))

        cmndName = "sendCompleteMessage" ; cmndArgs = "" ;

        icm.cmndExampleMenuSection("""*Mail File fromValid/toValid -- Default ControlProfile={controlProfile} Acct={mailAcct}*""".format(
                controlProfile=marmeAcctsLib.enabledControlProfileObtain(), mailAcct=marmeAcctsLib.enabledOutMailAcctObtain()))

        inFileExample = '''{fileName}'''.format(
            fileName=os.path.join(marmeAcctsLib.outMailCommonDirGet(enabledControlProfile),
                                  "template/plain/fromValid/toValid/default.mail"))

        cps = collections.OrderedDict() ; cps['inFile'] = inFileExample
        icm.ex_gCmndMenuItem(cmndName, cps, cmndArgs, verbosity='none')

        cps = collections.OrderedDict() ; cps['runMode'] = "runDebug" ; cps['inFile'] = inFileExample
        icm.ex_gCmndMenuItem(cmndName, cps, cmndArgs, verbosity='little')

        cps = collections.OrderedDict() ; cps['runMode'] = "runDebug" ; cps['inFile'] = inFileExample
        icm.ex_gCmndMenuItem(cmndName, cps, cmndArgs, icmWrapper="echo", verbosity='little')

        cps = collections.OrderedDict() ; cps['runMode'] = "dryRun" ; cps['inFile'] = inFileExample 
        icm.ex_gCmndMenuItem(cmndName, cps, cmndArgs, verbosity='little')

        icm.cmndExampleMenuSection("""*Mail File fromValid/toBad -- Default ControlProfile={controlProfile} Acct={mailAcct}*""".format(
                controlProfile=marmeAcctsLib.enabledControlProfileObtain(), mailAcct=marmeAcctsLib.enabledOutMailAcctObtain(),))

        inFileExample = '''{fileName}'''.format(
            fileName=os.path.join(marmeAcctsLib.outMailCommonDirGet(marmeAcctsLib.enabledControlProfileObtain()),
                                  "template/plain/fromValid/toBad/default.mail"))

        cps = collections.OrderedDict() ; cps['inFile'] = inFileExample
        icm.ex_gCmndMenuItem(cmndName, cps, cmndArgs, verbosity='none')

        cps = collections.OrderedDict() ; cps['runMode'] = "runDebug" ; cps['inFile'] = inFileExample
        icm.ex_gCmndMenuItem(cmndName, cps, cmndArgs, verbosity='little')

        cps = collections.OrderedDict() ; cps['runMode'] = "runDebug" ; cps['inFile'] = inFileExample
        icm.ex_gCmndMenuItem(cmndName, cps, cmndArgs, icmWrapper="echo", verbosity='little')

        cps = collections.OrderedDict() ; cps['runMode'] = "dryRun" ; cps['inFile'] = inFileExample 
        icm.ex_gCmndMenuItem(cmndName, cps, cmndArgs, verbosity='little')
        
        """
**  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Examples   ::  Mail From Partial File -- Qmail Inject [[elisp:(org-cycle)][| ]]
"""
        
        icm.cmndExampleMenuChapter('*Mail From Partial File -- Qmail Inject*')

        inFileExample = '''{fileName}'''.format(
            fileName=os.path.join(
                marmeAcctsLib.outMailCommonDirGet(enabledControlProfile),
                "template/bynameUtf8.mail"
            ))

        cmndName = "sendFromPartialFileWithPars" ; cmndArgs = "" ; cps = collections.OrderedDict()        
        cps['submissionMethod'] = "inject" ; cps['inFile'] = inFileExample
        cps['runMode']="dryRun"
        icm.ex_gCmndMenuItem(cmndName, cps, cmndArgs, verbosity='none')

        """
**  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Examples   ::  Basic Mail Sending  [[elisp:(org-cycle)][| ]]
"""
        
        
        icm.cmndExampleMenuChapter('*Basic Mail Sending*')

        cmndName = "msgSend_basic" ; cmndArgs = "" ; cps = collections.OrderedDict()        
        cps['fromLine']="office@mohsen.1.banan.byname.net" ; cps['toLine']="test@mohsen.banan.1.byname.net"
        icm.ex_gCmndMenuItem(cmndName, cps, cmndArgs, verbosity='none')

        cmndName = "msgSend_basic" ; cmndArgs = "" ; cps = collections.OrderedDict()
        cps['verbosity']="20" ; cps['runMode']="runDebug"        
        cps['fromLine']="office@mohsen.1.banan.byname.net" ; cps['toLine']="test@mohsen.banan.1.byname.net"
        icm.ex_gCmndMenuItem(cmndName, cps, cmndArgs, verbosity='none')

        cmndName = "msgSend_basic" ; cmndArgs = "" ; cps = collections.OrderedDict()
        cps['verbosity']="20" ; cps['runMode']="dryRun"        
        cps['fromLine']="office@mohsen.1.banan.byname.net" ; cps['toLine']="test@mohsen.banan.1.byname.net"
        icm.ex_gCmndMenuItem(cmndName, cps, cmndArgs, verbosity='none')
        

        cmndName = "msgSend_tracked" ; cmndArgs = "" ; cps = collections.OrderedDict()        
        cps['fromLine']="office@mohsen.1.banan.byname.net" ; cps['toLine']="test@mohsen.banan.1.byname.net"
        icm.ex_gCmndMenuItem(cmndName, cps, cmndArgs, verbosity='none')

        
        """
**  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Examples   ::  From  marmeAcctsLib.py   [[elisp:(org-cycle)][| ]]
"""

        marmeAcctsLib.examples_controlProfileManage()

        marmeAcctsLib.examples_enabledOutMailAcctConfig()        
   
        marmeAcctsLib.examples_outMailAcctAccessPars()
        
        return(cmndOutcome)


####+BEGIN: bx:icm:python:section :title "ICM Commands"
"""
*  [[elisp:(beginning-of-buffer)][Top]] ################ [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *ICM Commands*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:

####+BEGIN: bx:icm:python:cmnd:classHead :modPrefix "new" :cmndName "unitTest" :parsMand "" :parsOpt "" :argsMin "0" :argsMax "1" :asFunc "" :interactiveP ""
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || ICM-Cmnd       :: /unitTest/ parsMand= parsOpt= argsMin=0 argsMax=1 asFunc= interactive=  [[elisp:(org-cycle)][| ]]
"""
class unitTest(icm.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 0, 'Max': 1,}

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

        myName=self.myName()
        thisOutcome = icm.OpOutcome(invokerName=myName)

        print G.icmInfo

        for eachArg in effectiveArgsList:
            icm.ANN_here("{}".format(eachArg))

        print (icm.__file__)
        print sys.path

        import imp
        print(imp.find_module('unisos/icm'))

        @ucf.runOnceOnly
        def echo(str):
            print str
            
        echo("first")
        echo("second")  # Should not run
    
        return thisOutcome
    
    def cmndDocStr(self): return """
** Place holder for ICM's experimental or test code.  [[elisp:(org-cycle)][| ]]
*** You can use this Cmnd for rapid prototyping and testing of newly developed functions.
"""



"""
*  [[elisp:(beginning-of-buffer)][Top]] ################ [[elisp:(delete-other-windows)][(1)]]      *Support Functions For MsgProcs*
"""


####+BEGIN: bx:icm:python:cmnd:classHead :cmndName "sendFromPartialFileWithPars" :comment "" :parsMand "" :parsOpt "outMailAcct inFile sendingMethod" :argsMin "0" :argsMax "0" :asFunc "msg" :interactiveP ""
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || ICM-Cmnd       :: /sendFromPartialFileWithPars/ parsMand= parsOpt=outMailAcct inFile sendingMethod argsMin=0 argsMax=0 asFunc=msg interactive=  [[elisp:(org-cycle)][| ]]
"""
class sendFromPartialFileWithPars(icm.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ 'outMailAcct', 'inFile', 'sendingMethod', ]
    cmndArgsLen = {'Min': 0, 'Max': 0,}

    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
        interactive=False,        # Can also be called non-interactively
        outMailAcct=None,         # or Cmnd-Input
        inFile=None,         # or Cmnd-Input
        sendingMethod=None,         # or Cmnd-Input
        msg=None,         # asFunc when interactive==False
    ):
        cmndOutcome = self.getOpOutcome()
        if interactive:
            if not self.cmndLineValidate(outcome=cmndOutcome):
                return cmndOutcome

        callParamsDict = {'outMailAcct': outMailAcct, 'inFile': inFile, 'sendingMethod': sendingMethod, }
        if not icm.cmndCallParamsValidate(callParamsDict, interactive, outcome=cmndOutcome):
            return cmndOutcome
        outMailAcct = callParamsDict['outMailAcct']
        inFile = callParamsDict['inFile']
        sendingMethod = callParamsDict['sendingMethod']
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

        if not sendingMethod:
            sendingMethod = msgOut.SendingMethod.submit
        if msgOut.sendingMethodSet(msg, sendingMethod).isProblematic():
            return msgOut.sendingMethodSet(msg, sendingMethod)

        print G.usageParams.runMode
        
        if msgOut.sendingRunControlSet(msg, G.usageParams.runMode).isProblematic():
            return msgOut.sendingRunControlSet(msg, G.usageParams.runMode)
        

        envelopeAddr = msg['From']
        recipientsList = msg['To']
        
        msgOut.envelopeAddrSet(
            msg,
            mailBoxAddr=envelopeAddr,  # Mandatory
        )

        msgOut.crossRefInfo(
            msg,
            crossRefInfo="XrefForStatusNotifications"  # Mandatory
        )
        msgOut.nonDeliveryNotificationRequetsForTo(
            msg,
            recipientsList=recipientsList,        
            notifyTo=envelopeAddr,
        )
        msgOut.nonDeliveryNotificationActions(
            msg,
            coRecipientsList=recipientsList,
        )
        msgOut.deliveryNotificationRequetsForTo(
            msg,
            recipientsList=recipientsList,
            notifyTo=envelopeAddr,
        )
        msgOut.dispositionNotificationRequetsForTo(
            msg,
            recipientsList=recipientsList,
            notifyTo=envelopeAddr,
        )

        if msgOut.sendingMethodSet(msg, sendingMethod).isProblematic():
            return icm.EH_badLastOutcome()
            
        if not marmeSendLib.bx822Set_sendWithEnabledAcct(msg, sendingMethod):
            return icm.EH_badOutcome(cmndOutcome)

        cmndOutcome = marmeSendLib.sendCompleteMessage().cmnd(
            interactive=False,
            msg=msg,
        )

        return cmndOutcome

    def cmndDocStr(self): return """
** Submit a message using inFile and pars: outMailAcct, submissionMethod. 
** Augment with delivery/non-delivery requests and track.
"""


####+BEGIN: bx:icm:python:cmnd:classHead :modPrefix "new" :cmndName "msgSend_basic" :comment "" :parsMand "fromLine toLine" :parsOpt "sendingMethod" :argsMin "0" :argsMax "0" :asFunc "" :interactiveP ""
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || ICM-Cmnd       :: /msgSend_basic/ parsMand=fromLine toLine parsOpt=sendingMethod argsMin=0 argsMax=0 asFunc= interactive=  [[elisp:(org-cycle)][| ]]
"""
class msgSend_basic(icm.Cmnd):
    cmndParamsMandatory = [ 'fromLine', 'toLine', ]
    cmndParamsOptional = [ 'sendingMethod', ]
    cmndArgsLen = {'Min': 0, 'Max': 0,}

    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
        interactive=False,        # Can also be called non-interactively
        fromLine=None,         # or Cmnd-Input
        toLine=None,         # or Cmnd-Input
        sendingMethod=None,         # or Cmnd-Input
    ):
        cmndOutcome = self.getOpOutcome()
        if interactive:
            if not self.cmndLineValidate(outcome=cmndOutcome):
                return cmndOutcome

        callParamsDict = {'fromLine': fromLine, 'toLine': toLine, 'sendingMethod': sendingMethod, }
        if not icm.cmndCallParamsValidate(callParamsDict, interactive, outcome=cmndOutcome):
            return cmndOutcome
        fromLine = callParamsDict['fromLine']
        toLine = callParamsDict['toLine']
        sendingMethod = callParamsDict['sendingMethod']
####+END:

        if not sendingMethod:
            sendingMethod = msgOut.SendingMethod.submit

        msg = MIMEMultipart()

        msg['From'] = fromLine
        msg['To'] = toLine

        msg['Subject'] = """Example Of A Simple And Untracked Message"""

        msg.preamble = 'Multipart massage.\n'

        part = MIMEText(
            """ 
This is a simple example message with a simple attachment
being sent using the current enabled controlledProfile and mailAcct.

On the sending end, use mailAcctsManage.py with 
-i enabledControlProfileSet and -i enabledMailAcctSet
to select the outgoing profile. The current settings are:
    ControlProfile={controlProfile}  -- MailAcct={mailAcct}

This message is then submitted for sending with sendCompleteMessage().cmnd(msg)

Please find example of an attached file\n
            """.format(
                controlProfile=marmeAcctsLib.enabledControlProfileObtain(),
                mailAcct=marmeAcctsLib.enabledInMailAcctObtain()
            )
        )
        msg.attach(part)

        part = MIMEBase('application', "octet-stream")
        part.set_payload(open("/etc/resolv.conf", "rb").read())
        Encoders.encode_base64(part)

        part.add_header('Content-Disposition', 'attachment; filename="/etc/resolv.conf"')

        msg.attach(part)

        if msgOut.sendingMethodSet(msg, sendingMethod).isProblematic():
            return icm.EH_badLastOutcome()
            
        if not marmeSendLib.bx822Set_sendWithEnabledAcct(msg, sendingMethod):
            return icm.EH_badOutcome(cmndOutcome)

        cmndOutcome = marmeSendLib.sendCompleteMessage().cmnd(
            interactive=False,
            msg=msg,
        )
        
        return cmndOutcome

####+BEGIN: bx:icm:python:cmnd:classHead :modPrefix "new" :cmndName "msgSend_tracked" :comment "" :parsMand "fromLine toLine" :parsOpt "sendingMethod" :argsMin "0" :argsMax "0" :asFunc "" :interactiveP ""    
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || ICM-Cmnd       :: /msgSend_tracked/ parsMand=fromLine toLine parsOpt=sendingMethod argsMin=0 argsMax=0 asFunc= interactive=  [[elisp:(org-cycle)][| ]]
"""
class msgSend_tracked(icm.Cmnd):
    cmndParamsMandatory = [ 'fromLine', 'toLine', ]
    cmndParamsOptional = [ 'sendingMethod', ]
    cmndArgsLen = {'Min': 0, 'Max': 0,}

    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
        interactive=False,        # Can also be called non-interactively
        fromLine=None,         # or Cmnd-Input
        toLine=None,         # or Cmnd-Input
        sendingMethod=None,         # or Cmnd-Input
    ):
        cmndOutcome = self.getOpOutcome()
        if interactive:
            if not self.cmndLineValidate(outcome=cmndOutcome):
                return cmndOutcome

        callParamsDict = {'fromLine': fromLine, 'toLine': toLine, 'sendingMethod': sendingMethod, }
        if not icm.cmndCallParamsValidate(callParamsDict, interactive, outcome=cmndOutcome):
            return cmndOutcome
        fromLine = callParamsDict['fromLine']
        toLine = callParamsDict['toLine']
        sendingMethod = callParamsDict['sendingMethod']
####+END:
        #G = icm.IcmGlobalContext()

        if not sendingMethod:
            sendingMethod = msgOut.SendingMethod.submit

        msg = email.message.Message()  #msg = MIMEText() # MIMEMultipart() 

        msg['From'] = fromLine
        msg['To'] = toLine

        msg['Subject'] = """Example Of A Simple And Tracked Message"""

        envelopeAddr = fromLine

        if msgOut.sendingMethodSet(msg, sendingMethod).isProblematic():
            return msgOut.sendingMethodSet(msg, sendingMethod)
        
        msg.add_header('Content-Type', 'text')
        msg.set_payload(
            """ 
This is a simple example message with a simple attachment
being sent using the current enabled controlledProfile and mailAcct.

On the sending end, use mailAcctsManage.py with 
-i enabledControlProfileSet and -i enabledMailAcctSet
to select the outgoing profile. The current settings are:
    ControlProfile={controlProfile}  -- MailAcct={mailAcct}

This message is then submitted for sending with sendCompleteMessage().cmnd(msg)

            """.format(
                controlProfile=marmeAcctsLib.enabledControlProfileObtain(),
                mailAcct=marmeAcctsLib.enabledInMailAcctObtain()
            )
        )


        #
        ###########################
        #
        # Above is the real content of the email.
        #
        # We now augment the message with:
        #   - explicit envelope address -- To be used for Delivery-Status-Notifications (DSN)
        #   - The email is be tagged for crossReferencing when DSN is received (e.g. with peepid)    
        #   - Request that non-delivery-reports be acted upon and sent to co-recipients
        #   - Explicit delivery-reports are requested
        #   - Explicit read-receipts are requested
        #   - Injection/Submission parameters are specified
        # The message is then sent out
        #

        msgOut.envelopeAddrSet(
            msg,
            mailBoxAddr=envelopeAddr,  # Mandatory
        )

        #
        # peepId will be used to crossRef StatusNotifications
        #
        msgOut.crossRefInfo(
            msg,
            crossRefInfo="XrefForStatusNotifications"  # Mandatory
        )

        #
        # Delivery Status Notifications will be sent to notifyTo=envelopeAddr
        #
        msgOut.nonDeliveryNotificationRequetsForTo(
            msg,
            notifyTo=envelopeAddr,
        )

        #
        # In case of Non-Delivery, coRecipientsList will be informed
        #
        msgOut.nonDeliveryNotificationActions(
            msg,
            coRecipientsList=[toLine],        
        )

        #
        # Explicit Delivery Report is requested
        #
        msgOut.deliveryNotificationRequetsForTo(
            msg,
            recipientsList=[toLine],
            notifyTo=envelopeAddr,
        )

        #
        # Explicit Read Receipt is requested
        #    
        msgOut.dispositionNotificationRequetsForTo(
            msg,
            recipientsList=[toLine],        
            notifyTo=envelopeAddr,
        )

        if msgOut.sendingMethodSet(msg, sendingMethod).isProblematic():
            return icm.EH_badLastOutcome()
            
        if not marmeSendLib.bx822Set_sendWithEnabledAcct(msg, sendingMethod):
            return icm.EH_badOutcome(cmndOutcome)

        cmndOutcome = marmeSendLib.sendCompleteMessage().cmnd(
            
            interactive=False,
            msg=msg,
        )
        
        return

    

####+BEGIN: bx:icm:python:section :title "Supporting Classes And Functions"
"""
*  [[elisp:(beginning-of-buffer)][Top]] ################ [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *Supporting Classes And Functions*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:
"""
*       /Empty/  [[elisp:(org-cycle)][| ]]
"""
    
####+BEGIN: bx:icm:python:section :title "Common/Generic Facilities -- Library Candidates"
"""
*  [[elisp:(beginning-of-buffer)][Top]] ################ [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *Common/Generic Facilities -- Library Candidates*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:
"""
*       /Empty/  [[elisp:(org-cycle)][| ]]
"""

    
####+BEGIN: bx:icm:python:section :title "= =Framework::=   G_main -- Instead Of ICM Dispatcher ="
"""
*  [[elisp:(beginning-of-buffer)][Top]] ################ [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *= =Framework::=   G_main -- Instead Of ICM Dispatcher =*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:

####+BEGIN: bx:icm:python:func :funcName "G_main" :funcType "FrameWrk" :retType "Void" :deco "" :argsList ""
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func-FrameWrk  :: /G_main/ retType=Void argsList=nil  [[elisp:(org-cycle)][| ]]
"""
def G_main():
####+END:
    """ 
** Replaces ICM dispatcher for other command line args parsings.
"""
    pass

####+BEGIN: bx:icm:python:subSection :title "= =Framework::= g_ Settings -- ICMs Imports ="
"""
*  [[elisp:(beginning-of-buffer)][Top]] ================ [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]          *= =Framework::= g_ Settings -- ICMs Imports =*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:


g_examples = examples  # or None 
g_mainEntry = None  # or G_main

####+BEGIN: bx:dblock:global:file-insert :file "/libre/ByStar/InitialTemplates/update/sw/icm/py/icm2.G_main.py"
"""
*  [[elisp:(beginning-of-buffer)][Top]] # /Dblk-Begin/ # [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *= =Framework::= ICM main() =*
"""

def classedCmndsDict():
    """
** Should be done here, can not be done in icm library because of the evals.
"""
    callDict = dict()
    for eachCmnd in icm.cmndList_mainsMethods().cmnd(
            interactive=False,
            importedCmnds=g_importedCmnds,
            mainFileName=__file__,
    ):
        try:
            callDict[eachCmnd] = eval("{}".format(eachCmnd))
            continue
        except NameError:
            pass

        for mod in g_importedCmnds:
            try:
                eval("{mod}.{cmnd}".format(mod=mod, cmnd=eachCmnd))
            except AttributeError:
                continue
            try:                
                callDict[eachCmnd] = eval("{mod}.{cmnd}".format(mod=mod, cmnd=eachCmnd))
                break
            except NameError:
                pass
    return callDict

icmInfo['icmName'] = __icmName__
icmInfo['version'] = __version__
icmInfo['status'] = __status__
icmInfo['credits'] = __credits__

G = icm.IcmGlobalContext()
G.icmInfo = icmInfo

def g_icmMain():
    """This ICM's specific information is passed to G_mainWithClass"""
    sys.exit(
        icm.G_mainWithClass(
            inArgv=sys.argv[1:],                 # Mandatory
            extraArgs=g_argsExtraSpecify,        # Mandatory
            G_examples=g_examples,               # Mandatory            
            classedCmndsDict=classedCmndsDict(),   # Mandatory
            mainEntry=g_mainEntry,
            g_icmPreCmnds=g_icmPreCmnds,
            g_icmPostCmnds=g_icmPostCmnds,
        )
    )

g_icmMain()

"""
*  [[elisp:(beginning-of-buffer)][Top]] ## /Dblk-End/ ## [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *= =Framework::= ICM main() =*
"""

####+END:

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

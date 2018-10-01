# -*- coding: utf-8 -*-
"""\
* TODO *[Summary]* ::  A /library/ with ICM Cmnds to support ByStar facilities
"""

####+BEGIN: bx:icm:python:top-of-file :partof "bystar" :copyleft "halaal+minimal"
"""
*  This file:/de/bx/nne/dev-py/pypi/pkgs/unisos/marme/dev/unisos/marme/new-marmeAcctsLib.py :: [[elisp:(org-cycle)][| ]]
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
__libName__ = "new-marmeAcctsLib"
####+END:

####+BEGIN: bx:global:timestamp:version-py :style "date"
__version__ = "201712251031"
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

from unisos.common import icmsPkgLib

from unisos.marme import icmsPkgThis

####+BEGIN: bx:dblock:python:section :title "Library Description (Overview)"
"""
*  [[elisp:(beginning-of-buffer)][Top]] ################ [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *Library Description (Overview)*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:

####+BEGIN: bx:dblock:python:icm:cmnd:classHead :modPrefix "new" :cmndName "marmeAcctsLib_LibOverview" :parsMand "" :parsOpt "" :argsMin "0" :argsMax "3" :asFunc "" :interactiveP ""
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || ICM-Cmnd       :: /marmeAcctsLib_LibOverview/ parsMand= parsOpt= argsMin=0 argsMax=3 asFunc= interactive=  [[elisp:(org-cycle)][| ]]
"""
class marmeAcctsLib_LibOverview(icm.Cmnd):
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


"""
*  [[elisp:(beginning-of-buffer)][Top]] ################ [[elisp:(delete-other-windows)][(1)]]      *Base Directory Locations*
"""

"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func         ::  mailAcctsBaseDirGet    [[elisp:(org-cycle)][| ]]
"""

def mailAcctsBaseDirGet():
    return(
        icmsPkgLib.pkgBaseDir_obtain()
    )


"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func         ::  controlBaseDirGet    [[elisp:(org-cycle)][| ]]
"""
def controlBaseDirGet():
    return(
        icmsPkgLib.controlBaseDir_obtain(
            icmsPkgInfoBaseDir=icmsPkgThis.icmsPkgBase_dir()
        )
    )


"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func         ::  varBaseDirGet    [[elisp:(org-cycle)][| ]]
"""
def varBaseDirGet():
    return(
        icmsPkgLib.varBaseDir_obtain(
            icmsPkgInfoBaseDir=icmsPkgThis.icmsPkgBase_dir()
        )
    )

    
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func         ::  configBaseDirGet    [[elisp:(org-cycle)][| ]]
"""
def configBaseDirGet():
    return(
        icmsPkgLib.varConfigBaseDir_obtain(
            icmsPkgInfoBaseDir=icmsPkgThis.icmsPkgBase_dir()            
        )
    )

    
    
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func         ::  tmpBaseDirGet    [[elisp:(org-cycle)][| ]]
"""
def tmpBaseDirGet():
    return(
        icmsPkgLib.tmpBaseDir_obtain(
            icmsPkgInfoBaseDir=icmsPkgThis.icmsPkgBase_dir()            
        )
    )

"""
*  [[elisp:(beginning-of-buffer)][Top]] ################ [[elisp:(delete-other-windows)][(1)]]      *Control From  FP Obtain*
"""


"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func         ::  enabledControlProfileObtain    [[elisp:(org-cycle)][| ]]
"""
def enabledControlProfileObtain():
    """Returns as a string fp value read."""
    return icm.FILE_ParamValueReadFrom(
        parRoot=os.path.join(
            controlBaseDirGet(),
            "common",
            "selections",
            "fp",
        ),
        parName="enabledControlProfile",
    )

"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func         ::  availableControlProfilesObtain    [[elisp:(org-cycle)][| ]]
"""
def availableControlProfilesObtain():
    """
Returns a list
"""
    availablesList = list()
    controlBaseDir = controlBaseDirGet()
    for each in  os.listdir(controlBaseDir):
        if each == "CVS":
            continue
        if each == "common":
            continue
        eachFullPath = os.path.join(controlBaseDir, each)
        if not os.path.isdir(eachFullPath):
            continue
        availablesList.append(each)
    return availablesList


"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func         ::  enabledMailAcctObtainObsoleted    [[elisp:(org-cycle)][| ]]
"""
def enabledMailAcctObtainObsoleted():
    """
** Called obtain to leave Get for the IIF"""
    return icm.FILE_ParamValueReadFrom(
        parRoot=os.path.join(
            controlBaseDirGet(),
            "common",
            "selections",
            "fp",
        ),
        parName="enabledMailAcct",          
    )

"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func         ::  enabledInMailAcctObtain    [[elisp:(org-cycle)][| ]]
"""
def enabledInMailAcctObtain():
    """
** Called obtain to leave Get for the IIF"""
    return icm.FILE_ParamValueReadFrom(
        parRoot=os.path.join(
            controlBaseDirGet(),
            "common",
            "selections",
            "fp",
        ),
        parName="enabledInMailAcct",          
    )

"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func         ::  availableInMailAcctObtain    [[elisp:(org-cycle)][| ]]
"""
def availableInMailAcctObtain():
    """
Returns a list
"""
    availablesList = list()
    baseDir = os.path.join(
           controlProfileBaseDirGet(enabledControlProfileObtain(),),
            "inMail",
    )

    for each in  os.listdir(baseDir):
        if each == "CVS":
            continue
        if each == "common":
            continue
        eachFullPath = os.path.join(baseDir, each)
        if not os.path.isdir(eachFullPath):
            continue
        availablesList.append(each)
    return availablesList


"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func         ::  enabledOutMailAcctObtain    [[elisp:(org-cycle)][| ]]
"""
def enabledOutMailAcctObtain():
    """
** Called obtain to leave Get for the IIF"""
    return icm.FILE_ParamValueReadFrom(
        parRoot=os.path.join(
            controlBaseDirGet(),
            "common",
            "selections",
            "fp",
        ),
        parName="enabledOutMailAcct",          
    )


"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func         ::  availableOutMailAcctObtain    [[elisp:(org-cycle)][| ]]
"""
def availableOutMailAcctObtain():
    """
Returns a list
"""
    availablesList = list()
    baseDir = os.path.join(
           controlProfileBaseDirGet(enabledControlProfileObtain(),),
            "outMail",
    )

    for each in  os.listdir(baseDir):
        if each == "CVS":
            continue
        if each == "common":
            continue
        eachFullPath = os.path.join(baseDir, each)
        if not os.path.isdir(eachFullPath):
            continue
        availablesList.append(each)
    return availablesList



"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func         ::  enabledMailBoxObtain    [[elisp:(org-cycle)][| ]]
"""
def enabledMailBoxObtain():
    """
** Called obtain to leave Get for the IIF"""
    return icm.FILE_ParamValueReadFrom(
        parRoot=os.path.join(
            controlBaseDirGet(),
            "common",
            "selections",
            "fp",
        ),
        parName="enabledMailBox",          
    )


"""
*  [[elisp:(beginning-of-buffer)][Top]] ################ [[elisp:(delete-other-windows)][(1)]]      *Control Base Directory From FP Get*
"""

"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func         ::  controlProfileBaseDirGet    [[elisp:(org-cycle)][| ]]
"""
def controlProfileBaseDirGet (controlProfile):
    """
** Joins controlBaseDirGet() and enabledControlProfileObtain()
"""
    if not controlProfile:
        controlProfile = enabledControlProfileObtain()
    return os.path.abspath(
        os.path.join(
            controlBaseDirGet(),
            controlProfile,
    ))

"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func         ::  outMailAcctDirGet    [[elisp:(org-cycle)][| ]]
"""

def outMailAcctDirGet(controlProfile, outMailAcct):
    return os.path.abspath(
        os.path.join(
           controlProfileBaseDirGet(controlProfile),
            "outMail",
            outMailAcct,
            "fp",
    ))


"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func         ::  outMailCommonDirGet    [[elisp:(org-cycle)][| ]]
"""
def outMailCommonDirGet(controlProfile):
    if not controlProfile:
        controlProfile = enabledControlProfileObtain()
    return os.path.abspath(
        os.path.join(
            controlProfileBaseDirGet(controlProfile),
            "outMail",
            "common",
            #"fp",         # NOTYET, Needs to be revisited
    ))


"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func         ::  inMailAcctDirGet    [[elisp:(org-cycle)][| ]]
"""
def inMailAcctDirGet(controlProfile, inMailAcct):
    if not controlProfile:
        controlProfile = enabledControlProfileObtain()
    return os.path.abspath(
        os.path.join(
            controlProfileBaseDirGet(controlProfile),             
            "inMail",
            inMailAcct,
            "fp",

    ))


"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func         ::  inMailCommonDirGet    [[elisp:(org-cycle)][| ]]
"""
def inMailCommonDirGet(controlProfile,):
    if not controlProfile:
        controlProfile = enabledControlProfileObtain()
    return (
        os.path.abspath(
            os.path.join(
                controlProfileBaseDirGet(controlProfile,),
                "inMail"
                "common"
                "fp"            
            )))


"""
*  [[elisp:(beginning-of-buffer)][Top]] ################ [[elisp:(delete-other-windows)][(1)]]      *VAR Base Directory Get*
"""


"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func         ::  getPathForAcctMaildir    [[elisp:(org-cycle)][| ]]
"""
def getPathForAcctMaildir(
    controlProfile,
    mailAcct,
):
    """
** NOTYET, controlProfile is not being used.
"""
    return (
        os.path.join(
            varBaseDirGet(),
            "inMail",
            controlProfile,
            mailAcct,
            "maildir"
        ))

"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func         ::  getPathForAcctMbox    [[elisp:(org-cycle)][| ]]
"""
def getPathForAcctMbox(
    controlProfile,     
    mailAcct,
    mbox,
):
    #if not controlProfile:
        #controlProfile = enabledControlProfileObtain()

    if not mailAcct:
        mailAcct = enabledInMailAcctObtain()

    if not mbox:
        mbox = enabledMailBoxObtain()

    return (
        os.path.join(
            varBaseDirGet(),
            "inMail",
            controlProfile,            
            mailAcct,
            "maildir",
            mbox,
        ))

"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func         ::  getPathForInMailConfig    [[elisp:(org-cycle)][| ]]
"""
def getPathForInMailConfig(
    controlProfile,     
    inMailAcct,
):

    return (
        os.path.join(
            configBaseDirGet(),
            "inMail",
            controlProfile,            
            inMailAcct,
        ))

"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func         ::  getPathForOutMailConfig    [[elisp:(org-cycle)][| ]]
"""
def getPathForOutMailConfig(
    controlProfile,     
    outMailAcct,
):

    return (
        os.path.join(
            configBaseDirGet(),
            "outMail",
            controlProfile,            
            outMailAcct,
        ))



"""
*  [[elisp:(beginning-of-buffer)][Top]] ################ [[elisp:(delete-other-windows)][(1)]]      *Common Arguments Specification*
"""

"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func         ::  commonParamsSpecify    [[elisp:(org-cycle)][| ]]
"""
def commonParamsSpecify(
        icmParams,
):
    enabledControlProfile = enabledControlProfileObtain()    
    enabledInMailAcct = enabledInMailAcctObtain()
    enabledOutMailAcct = enabledOutMailAcctObtain()        

    icmParams.parDictAdd(
        parName='controlProfile',
        parDescription="Base for Domain/Site/Source of incoming Mail",
        parDataType=None,
        parDefault="{default}".format(default=enabledControlProfile),
        parChoices=["someOptionalPar", "UserInput"],
        parScope=icm.ICM_ParamScope.TargetParam,
        argparseShortOpt=None,
        argparseLongOpt='--controlProfile',
    )

    icmParams.parDictAdd(
        parName='inMailAcct',
        parDescription="Base for Domain/Site/Source of incoming Mail",
        parDataType=None,
        parDefault="{default}".format(default=enabledInMailAcct),
        parChoices=["someOptionalPar", "UserInput"],
        parScope=icm.ICM_ParamScope.TargetParam,
        argparseShortOpt=None,
        argparseLongOpt='--inMailAcct',
    )
    
    icmParams.parDictAdd(
        parName='outMailAcct',
        parDescription="Base for Domain/Site/Source of incoming Mail",
        parDataType=None,
        parDefault="{default}".format(default=enabledOutMailAcct),
        parChoices=["someOptionalPar", "UserInput"],
        parScope=icm.ICM_ParamScope.TargetParam,
        argparseShortOpt=None,
        argparseLongOpt='--outMailAcct',
    )
    
    icmParams.parDictAdd(
        parName='firstName',
        parDescription="Base for Domain/Site/Source of incoming Mail",
        parDataType=None,
        parDefault=None,
        parChoices=["someOptionalPar", "UserInput"],
        parScope=icm.ICM_ParamScope.TargetParam,
        argparseShortOpt=None,
        argparseLongOpt='--firstName',
    )
    
    icmParams.parDictAdd(
        parName='lastName',
        parDescription="Base for Domain/Site/Source of incoming Mail",
        parDataType=None,
        parDefault=None,
        parChoices=["someOptionalPar", "UserInput"],
        parScope=icm.ICM_ParamScope.TargetParam,
        argparseShortOpt=None,
        argparseLongOpt='--lastName',
    )

    icmParams.parDictAdd(
        parName='userName',
        parDescription="Base for Domain/Site/Source of incoming Mail",
        parDataType=None,
        parDefault=None,
        parChoices=["someOptionalPar", "UserInput"],
        parScope=icm.ICM_ParamScope.TargetParam,
        argparseShortOpt=None,
        argparseLongOpt='--userName',
    )

    icmParams.parDictAdd(
        parName='userPasswd',
        parDescription="Base for Domain/Site/Source of incoming Mail",
        parDataType=None,
        parDefault=None,
        parChoices=["someOptionalPar", "UserInput"],
        parScope=icm.ICM_ParamScope.TargetParam,
        argparseShortOpt=None,
        argparseLongOpt='--userPasswd',
    )
    
    icmParams.parDictAdd(
        parName='mtaRemHost',
        parDescription="Base for Domain/Site/Source of incoming Mail",
        parDataType=None,
        parDefault=None,
        parChoices=["someOptionalPar", "UserInput"],
        parScope=icm.ICM_ParamScope.TargetParam,
        argparseShortOpt=None,
        argparseLongOpt='--mtaRemHost',
    )

    icmParams.parDictAdd(
        parName='mtaRemProtocol',
        parDescription="Base for Domain/Site/Source of incoming Mail",
        parDataType=None,
        parDefault=None,
        parChoices=["someOptionalPar", "UserInput"],
        parScope=icm.ICM_ParamScope.TargetParam,
        argparseShortOpt=None,
        argparseLongOpt='--mtaRemProtocol',
    )
    
    
    # icmParams.parDictAdd(
    #     parName='imapServer',
    #     parDescription="Base for Domain/Site/Source of incoming Mail",
    #     parDataType=None,
    #     parDefault=None,
    #     parChoices=["someOptionalPar", "UserInput"],
    #     parScope=icm.ICM_ParamScope.TargetParam,
    #     argparseShortOpt=None,
    #     argparseLongOpt='--imapServer',
    # )

    icmParams.parDictAdd(
        parName='inMailAcctMboxesPath',
        parDescription="Base Directory Of Maildir where msgs are retrieved to.",
        parDataType=None,
        parDefault=None,        
        #parDefault="../var/inMail/{default}/maildir/".format(default=enabledMailAcct),
        parChoices=["someFile", "UserInput"],
        parScope=icm.ICM_ParamScope.TargetParam,
        argparseShortOpt=None,
        argparseLongOpt='--inMailAcctMboxesPath',
    )
    
    icmParams.parDictAdd(
        parName='inMbox',
        parDescription="Name of MailBox to be joined with inMailAcctMboxesPath.",
        parDataType=None,
        parDefault=None,
        parChoices=["envelope", "Tmp"],
        parScope=icm.ICM_ParamScope.TargetParam,
        argparseShortOpt=None,
        argparseLongOpt='--inMbox',
    )

    icmParams.parDictAdd(
        parName='mboxesList',
        parDescription="Name of MailBox to be joined with inMailAcctMboxesPath.",
        parDataType=None,
        parDefault=None,
        parChoices=["envelope", "Tmp"],
        parScope=icm.ICM_ParamScope.TargetParam,
        argparseShortOpt=None,
        argparseLongOpt='--mboxesList',
    )

    icmParams.parDictAdd(
        parName='ssl',
        parDescription="Name of MailBox to be joined with inMailAcctMboxesPath.",
        parDataType=None,
        parDefault=None,
        parChoices=["no", "on"],
        parScope=icm.ICM_ParamScope.TargetParam,
        argparseShortOpt=None,
        argparseLongOpt='--ssl',
    )
    
    icmParams.parDictAdd(
        parName='sendingMethod',
        parDescription="sending method for outgoing email",
        parDataType=None,
        parDefault=None,
        parChoices=["inject", "authSmtp"],
        parScope=icm.ICM_ParamScope.TargetParam,
        argparseShortOpt=None,
        argparseLongOpt='--sendingMethod',
    )

    icmParams.parDictAdd(
        parName='envelopeAddr',
        parDescription="Envelope Address Of Outgoing Email",
        parDataType=None,
        parDefault=None,
        parChoices=["envelop@example.com"],
        parScope=icm.ICM_ParamScope.TargetParam,
        argparseShortOpt=None,
        argparseLongOpt='--envelopeAddr',
    )

    # icmParams.parDictAdd(
    #     parName='parGroup',
    #     parDescription="Temporary till args dblock processing gets fixed",
    #     parDataType=None,
    #     parDefault=None,
    #     parChoices=["access", ],
    #     parScope=icm.ICM_ParamScope.TargetParam,
    #     argparseShortOpt=None,
    #     argparseLongOpt='--parGroup',
    # )
    


"""
*  [[elisp:(beginning-of-buffer)][Top]] ################ [[elisp:(delete-other-windows)][(1)]]      *Common Examples Sections*
"""
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func         ::  examples_controlProfileManage    [[elisp:(org-cycle)][| ]]
"""
def examples_controlProfileManage():
    """."""
    icm.cmndExampleMenuChapter('* =Selection=  Control Profiles -- /{}/ --*'.format(enabledControlProfileObtain()))

    thisCmndAction= " -i enabledControlProfileGet"
    icm.cmndExampleMenuItem(
        format(""  + thisCmndAction),
        verbosity='none'
    )

    cmndAction = "  -i enabledControlProfileSet"

    for each in availableControlProfilesObtain():
        cmndArgs = " {controlProfile}".format(controlProfile=each)
        menuLine = """{cmndAction} {cmndArgs}""".format(cmndAction=cmndAction, cmndArgs=cmndArgs)
        icm.cmndExampleMenuItem(menuLine, verbosity='none')
    return


"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func         ::  examples_enabledInMailAcctConfig    [[elisp:(org-cycle)][| ]]
"""    
def examples_enabledInMailAcctConfig():
    """
** Select Enabled Mail Account Config. Read/Writeen to control/common/selections/fp
"""
    icm.cmndExampleMenuChapter('* =Selection=  InMailAccts -- /{controlProfile}+{mailAcct}/ --*'.format(
        controlProfile=enabledControlProfileObtain(), mailAcct=enabledInMailAcctObtain()))

    thisCmndAction= " -i enabledInMailAcctGet"
    icm.cmndExampleMenuItem(
        format(""  + thisCmndAction),
        verbosity='none'
    )

    cmndAction = "  -i enabledInMailAcctSet"


    for each in availableInMailAcctObtain():
        cmndArgs = " {}".format(each)
        menuLine = """{cmndAction} {cmndArgs}""".format(cmndAction=cmndAction, cmndArgs=cmndArgs)
        icm.cmndExampleMenuItem(menuLine, verbosity='none')
    return



"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func         ::  examples_enabledOutMailAcctConfig    [[elisp:(org-cycle)][| ]]
"""
def examples_enabledOutMailAcctConfig():
    """
** Select Enabled Mail Account Config. Read/Writeen to control/common/selections/fp
"""
    icm.cmndExampleMenuChapter('* =Selection=  OutMailAccts -- /{controlProfile}+{mailAcct}/ --*'.format(
        controlProfile=enabledControlProfileObtain(), mailAcct=enabledOutMailAcctObtain()))

    thisCmndAction= " -i enabledOutMailAcctGet"
    icm.cmndExampleMenuItem(
        format(""  + thisCmndAction),
        verbosity='none'
    )

    cmndAction = "  -i enabledOutMailAcctSet"

    for each in availableOutMailAcctObtain():
        cmndArgs = " {}".format(each)
        menuLine = """{cmndAction} {cmndArgs}""".format(cmndAction=cmndAction, cmndArgs=cmndArgs)
        icm.cmndExampleMenuItem(menuLine, verbosity='none')
    return
    

"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func         ::  examples_select_mailBox    [[elisp:(org-cycle)][| ]]
"""
def examples_select_mailBox():
    """."""
    icm.cmndExampleMenuChapter('* =Selection=  MailBox -- /{controlProfile}+{mailAcct}+{mBox}/ --*'.format(
        controlProfile=enabledControlProfileObtain(),
        mailAcct=enabledInMailAcctObtain(),
        mBox=enabledMailBoxGet().cmnd().results,
        ))

    thisCmndAction= " -i enabledMailBoxGet"
    icm.cmndExampleMenuItem(
        format(""  + thisCmndAction),
        verbosity='none'
    )

    cmndAction = "  -i enabledMailBoxSet"
    
    # ../../marme.control
    cmndArgs = " Inbox"
    menuLine = """{cmndAction} {cmndArgs}""".format(cmndAction=cmndAction, cmndArgs=cmndArgs)
    icm.cmndExampleMenuItem(menuLine, verbosity='none')
    
    
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func         ::  examples_inMailAcctAccessPars    [[elisp:(org-cycle)][| ]]
"""
def examples_inMailAcctAccessPars():
    """
** Auxiliary examples to be commonly used.
"""
    icm.cmndExampleMenuChapter('* =FP Values=  inMail Controls -- /{controlProfile}+{mailAcct}/ --*'.format(
        controlProfile=enabledControlProfileObtain(), mailAcct=enabledInMailAcctObtain()))
    

    cmndAction = " -i inMailAcctParsGet" ; cmndArgs = ""
    menuLine = """{cmndAction} {cmndArgs}""".format(cmndAction=cmndAction, cmndArgs=cmndArgs)
    icm.cmndExampleMenuItem(menuLine, verbosity='none')

    menuLine = """"""
    icm.cmndExampleMenuItem(menuLine, icmName="marmeAcctsManage.py", verbosity='none')    


"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func         ::  examples_inMailAcctAccessParsFull    [[elisp:(org-cycle)][| ]]
"""    
def examples_inMailAcctAccessParsFull():
    """
** Auxiliary examples to be commonly used.
"""
    icm.cmndExampleMenuChapter('* =FP Values=  inMail Controls -- /{controlProfile}+{mailAcct}/ --*'.format(
        controlProfile=enabledControlProfileObtain(), mailAcct=enabledInMailAcctObtain()))

    cmndAction = " -i inMailAcctParsGet" ; cmndArgs = ""
    menuLine = """{cmndAction} {cmndArgs}""".format(cmndAction=cmndAction, cmndArgs=cmndArgs)
    icm.cmndExampleMenuItem(menuLine, verbosity='none')

    icm.cmndExampleMenuSection('*inMail /Access/ ParsSet -- /defaulMailAcct={}/ --*'.format(enabledInMailAcctObtain()))    

    cmndAction = " -i inMailAcctAccessParsSet" ; cmndArgs = ""
    menuLine = """--userName="UserName" --userPasswd="UserPasswd" --imapServer="ImapServer" {cmndAction} {cmndArgs}""".format(cmndAction=cmndAction, cmndArgs=cmndArgs)
    icm.cmndExampleMenuItem(menuLine, icmWrapper="echo", verbosity='none')
    
    cmndAction = " -i inMailAcctAccessParsSet" ; cmndArgs = ""
    menuLine = """--userName="UserName" {cmndAction} {cmndArgs}""".format(cmndAction=cmndAction, cmndArgs=cmndArgs)
    icm.cmndExampleMenuItem(menuLine, icmWrapper="echo", verbosity='none')

    icm.cmndExampleMenuSection('*inMail /ControllerInfo/ ParsSet -- /defaulMailAcct={}/ --*'.format(enabledInMailAcctObtain()))    

    cmndAction = " -i inMailAcctControllerInfoParsSet" ; cmndArgs = ""
    menuLine = """--firstName="FirstName" --lastName="LastName" {cmndAction} {cmndArgs}""".format(cmndAction=cmndAction, cmndArgs=cmndArgs)
    icm.cmndExampleMenuItem(menuLine, icmWrapper="echo", verbosity='none')
    
    cmndAction = " -i inMailAcctControllerInfoParsSet" ; cmndArgs = ""
    menuLine = """--firstName="FirstName" {cmndAction} {cmndArgs}""".format(cmndAction=cmndAction, cmndArgs=cmndArgs)
    icm.cmndExampleMenuItem(menuLine, icmWrapper="echo", verbosity='none')

    icm.cmndExampleMenuSection('*inMail /Retrieval/ ParsSet -- /defaulMailAcct={}/ --*'.format(enabledInMailAcctObtain()))    

    cmndAction = " -i inMailAcctRetrievalParsSet" ; cmndArgs = ""
    menuLine = """--inMailAcctMboxesPath="MaildirPath" --mboxesList="" --ssl="on" {cmndAction} {cmndArgs}""".format(cmndAction=cmndAction, cmndArgs=cmndArgs)
    icm.cmndExampleMenuItem(menuLine, icmWrapper="echo", verbosity='none')

    
    cmndAction = " -i inMailAcctRetrievalParsSet" ; cmndArgs = ""
    mailDirPath = getPathForAcctMaildir(enabledControlProfileObtain(), enabledInMailAcctObtain())
    menuLine = """--inMailAcctMboxesPath={mailDirPath} {cmndAction} {cmndArgs}""".format(
        mailDirPath=mailDirPath, cmndAction=cmndAction, cmndArgs=cmndArgs)
    icm.cmndExampleMenuItem(menuLine, icmWrapper="", verbosity='none')

    cmndAction = " -i inMailAcctRetrievalParsSet" ; cmndArgs = ""
    menuLine = """--ssl=on {cmndAction} {cmndArgs}""".format(cmndAction=cmndAction, cmndArgs=cmndArgs)
    icm.cmndExampleMenuItem(menuLine, icmWrapper="", verbosity='none')
    
    
    cmndAction = " -i inMailAcctRetrievalParsSet" ; cmndArgs = ""
    menuLine = """--mboxesList="Inbox" --ssl="on" {cmndAction} {cmndArgs}""".format(cmndAction=cmndAction, cmndArgs=cmndArgs)
    icm.cmndExampleMenuItem(menuLine, icmWrapper="echo", verbosity='none')
    
    
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func         ::  examples_outMailAcctAccessPars    [[elisp:(org-cycle)][| ]]
"""
def examples_outMailAcctAccessPars():
    """."""
    icm.cmndExampleMenuChapter('* =FP Values=  outMail Controls -- /{controlProfile}+{mailAcct}/ --*'.format(
        controlProfile=enabledControlProfileObtain(), mailAcct=enabledOutMailAcctObtain()))
    

    cmndName = "outMailAcctParsGet" ; cmndArgs = "" ; cps = collections.OrderedDict()        
    icm.ex_gCmndMenuItem(cmndName, cps, cmndArgs, verbosity='none')

    menuLine = """"""
    icm.cmndExampleMenuItem(menuLine, icmName="marmeAcctsManage.py", verbosity='none')    

"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func         ::  examples_outMailAcctAccessParsFull    [[elisp:(org-cycle)][| ]]
"""    
def examples_outMailAcctAccessParsFull():
    """."""
    icm.cmndExampleMenuChapter('* =FP Values=  outMail Controls -- /{controlProfile}+{mailAcct}/ --*'.format(
        controlProfile=enabledControlProfileObtain(), mailAcct=enabledOutMailAcctObtain()))

    cmndName = "outMailAcctParsGet" ; cmndArgs = "" ; cps = collections.OrderedDict()        
    icm.ex_gCmndMenuItem(cmndName, cps, cmndArgs, verbosity='none')

    icm.cmndExampleMenuSection('*outMail /Access/ ParsSet -- /enabledMailAcct={controlProfile}+{mailAcct}/ --*'.format(
        controlProfile=enabledControlProfileObtain(), mailAcct=enabledOutMailAcctObtain()))        

    cmndName = "outMailAcctParsSet" ; cmndArgs = "access" ; cps = collections.OrderedDict()        
    cps['userName']="TBS" ; cps['userPasswd']="TBS" ; cps['mtaRemHost']="TBS" ; cps['mtaRemProtocol']="smtp_ssl/smtp_tls/smtp"     
    icm.ex_gCmndMenuItem(cmndName, cps, cmndArgs, icmWrapper="echo", verbosity='none')

    icm.cmndExampleMenuSection('*outMail /ControllerInfo/ ParsSet -- /enabledMailAcct={controlProfile}+{mailAcct}/ --*'.format(
        controlProfile=enabledControlProfileObtain(), mailAcct=enabledOutMailAcctObtain()))        

    cmndName = "outMailAcctParsSet" ; cmndArgs = "controllerInfo" ; cps = collections.OrderedDict()        
    cps['firstName']="TBS" ; cps['lastName']="TBS"
    icm.ex_gCmndMenuItem(cmndName, cps, cmndArgs, icmWrapper="echo", verbosity='none')

    icm.cmndExampleMenuSection('*outMail /Submission/ ParsSet -- /enabledMailAcct={controlProfile}+{mailAcct}/ --*'.format(
        controlProfile=enabledControlProfileObtain(), mailAcct=enabledOutMailAcctObtain()))                

    cmndName = "outMailAcctParsSet" ; cmndArgs = "submission" ; cps = collections.OrderedDict()        
    cps['sendingMethod']="inject/submit" ; cps['envelopeAddr']="TBS"
    icm.ex_gCmndMenuItem(cmndName, cps, cmndArgs, icmWrapper="echo", verbosity='none')

    

"""
*  [[elisp:(beginning-of-buffer)][Top]] ################ [[elisp:(delete-other-windows)][(1)]]      *File Parameters Get/Set -- Commands*
"""

    
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func         ::  FP_readTreeAtBaseDir_CmndOutput    [[elisp:(org-cycle)][| ]]
"""
def FP_readTreeAtBaseDir_CmndOutput(
        interactive,
        fpBaseDir,
        cmndOutcome,
):
    """Invokes FP_readTreeAtBaseDir.cmnd as interactive-output only."""
    #
    # Interactive-Output + Chained-Outcome Command Invokation
    #
    FP_readTreeAtBaseDir = icm.FP_readTreeAtBaseDir()
    FP_readTreeAtBaseDir.cmndLineInputOverRide = True
    FP_readTreeAtBaseDir.cmndOutcome = cmndOutcome
        
    return FP_readTreeAtBaseDir.cmnd(
        interactive=interactive,
        FPsDir=fpBaseDir,
    )

"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Class-IIF    ::  enabledControlProfileGet    [[elisp:(org-cycle)][| ]]
"""
class enabledControlProfileGet(icm.Cmnd):
    """
** Output the current from -- NOTYET -- Should write at {varBase}/selections/fp
    """

    cmndParamsMandatory = []
    cmndParamsOptional = []       
    cmndArgsLen = {'Min': 0, 'Max': 0,}

####+BEGIN: bx:dblock:python:icm:cmnd:parsValidate :par ""
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
    
        enabledMailAcct = enabledControlProfileObtain()
 
        if interactive:
            icm.ANN_write(enabledMailAcct)

        return cmndOutcome.set(
            opError=icm.OpError.Success,
            opResults=enabledMailAcct,
        )

"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Class-IIF    ::  enabledControlProfileSet    [[elisp:(org-cycle)][| ]]
"""    
class enabledControlProfileSet(icm.Cmnd):
    """
** Write as a FP the enabledControlProfile.
"""

    cmndParamsMandatory = []
    cmndParamsOptional = []       
    cmndArgsLen = {'Min': 1, 'Max': 1,}
    
####+BEGIN: bx:dblock:python:icm:cmnd:parsValidate :par ""
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

        G = icm.IcmGlobalContext()        

        icmRunArgs = G.icmRunArgsGet()
        for each in icmRunArgs.cmndArgs:
            icm.FILE_ParamWriteToPath(
                parNameFullPath=os.path.join(
                    controlBaseDirGet(),
                    "common",
                    "selections",
                    "fp",
                    "enabledControlProfile",
                ),
                parValue=each,
            )

        return cmndOutcome.set(
            opError=icm.OpError.Success,
            opResults=each,
        )

"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Class-IIF    ::  enabledMailAcctGet    [[elisp:(org-cycle)][| ]]
"""
class enabledInMailAcctGet(icm.Cmnd):
    """
** Output the current enabledMailAcct
    """

    cmndParamsMandatory = []
    cmndParamsOptional = []       
    cmndArgsLen = {'Min': 0, 'Max': 0,}

####+BEGIN: bx:dblock:python:icm:cmnd:parsValidate :par ""
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
    
        enabledInMailAcct = enabledInMailAcctObtain()
 
        if interactive:
            icm.ANN_write(enabledInMailAcct)

        return cmndOutcome.set(
            opError=icm.OpError.Success,
            opResults=enabledInMailAcct,
        )

"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Class-IIF    ::  enabledMailAcctSet    [[elisp:(org-cycle)][| ]]
"""
class enabledInMailAcctSet(icm.Cmnd):
    """
** Write as a FP  the enabledMailAcct.
"""
    cmndParamsMandatory = []
    cmndParamsOptional = []       
    cmndArgsLen = {'Min': 1, 'Max': 1,}
    
####+BEGIN: bx:dblock:python:icm:cmnd:parsValidate :par ""
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

        G = icm.IcmGlobalContext()        

        icmRunArgs = G.icmRunArgsGet()
        for each in icmRunArgs.cmndArgs:
            icm.FILE_ParamWriteToPath(
                parNameFullPath=os.path.join(
                    controlBaseDirGet(),
                    "common",
                    "selections",
                    "fp",
                    "enabledInMailAcct",
                ),
                parValue=each,
            )

        return cmndOutcome.set(
            opError=icm.OpError.Success,
            opResults=each,
        )



"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Class-IIF    ::  enabledMailAcctGet    [[elisp:(org-cycle)][| ]]
"""
class enabledOutMailAcctGet(icm.Cmnd):
    """
** Output the current enabledMailAcct
    """

    cmndParamsMandatory = []
    cmndParamsOptional = []       
    cmndArgsLen = {'Min': 0, 'Max': 0,}

####+BEGIN: bx:dblock:python:icm:cmnd:parsValidate :par ""
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
    
        enabledOutMailAcct = enabledOutMailAcctObtain()
 
        if interactive:
            icm.ANN_write(enabledOutMailAcct)

        return cmndOutcome.set(
            opError=icm.OpError.Success,
            opResults=enabledOutMailAcct,
        )

"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Class-IIF    ::  enabledMailAcctSet    [[elisp:(org-cycle)][| ]]
"""
class enabledOutMailAcctSet(icm.Cmnd):
    """
** Write as a FP  the enabledMailAcct.
"""
    cmndParamsMandatory = []
    cmndParamsOptional = []       
    cmndArgsLen = {'Min': 1, 'Max': 1,}
    
####+BEGIN: bx:dblock:python:icm:cmnd:parsValidate :par ""
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

        G = icm.IcmGlobalContext()        

        icmRunArgs = G.icmRunArgsGet()
        for each in icmRunArgs.cmndArgs:
            icm.FILE_ParamWriteToPath(
                parNameFullPath=os.path.join(
                    controlBaseDirGet(),
                    "common",
                    "selections",
                    "fp",
                    "enabledOutMailAcct",
                ),
                parValue=each,
            )

        return cmndOutcome.set(
            opError=icm.OpError.Success,
            opResults=each,
        )


    

"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Class-IIF    ::  enabledMailBoxGet    [[elisp:(org-cycle)][| ]]
"""
class enabledMailBoxGet(icm.Cmnd):
    """
** Output the current enabledMailBox
    """

    cmndParamsMandatory = []
    cmndParamsOptional = []       
    cmndArgsLen = {'Min': 0, 'Max': 0,}

####+BEGIN: bx:dblock:python:icm:cmnd:parsValidate :par ""
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
    
        enabledMailBox = enabledMailBoxObtain()
 
        if interactive:
            icm.ANN_write(enabledMailBox)

        return cmndOutcome.set(
            opError=icm.OpError.Success,
            opResults=enabledMailBox,
        )
    

"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Class-IIF    ::  enabledMailBoxSet    [[elisp:(org-cycle)][| ]]
"""
class enabledMailBoxSet(icm.Cmnd):
    """
** Write as a FP  the enabledMailBox.
"""
    cmndParamsMandatory = []
    cmndParamsOptional = []       
    cmndArgsLen = {'Min': 1, 'Max': 1,}
    
####+BEGIN: bx:dblock:python:icm:cmnd:parsValidate :par ""
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

        G = icm.IcmGlobalContext()        

        icmRunArgs = G.icmRunArgsGet()
        for each in icmRunArgs.cmndArgs:
            icm.FILE_ParamWriteToPath(
                parNameFullPath=os.path.join(
                    controlBaseDirGet(),
                    "common",
                    "selections",
                    "fp",
                    "enabledMailBox",
                ),
                parValue=each,
            )

        return cmndOutcome.set(
            opError=icm.OpError.Success,
            opResults=each,
        )
    

"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Class-IIF    ::  inMailAcctAccessParsGet    [[elisp:(org-cycle)][| ]]
"""
class inMailAcctParsGet(icm.Cmnd):
    """."""

    cmndParamsMandatory = []
    cmndParamsOptional = ['controlProfile', 'inMailAcct']       
    cmndArgsLen = {'Min': 0, 'Max': 3,}
    cmndArgsSpec = {0: ['access', 'controllerInfo', 'retrieval']}

####+BEGIN: bx:dblock:python:icm:cmnd:parsValidate :par "controlProfile inMailAcct" :args "parTypes"
    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
        interactive=False,        # Can also be called non-interactively
        controlProfile=None,         # or Cmnd-Input
        inMailAcct=None,         # or Cmnd-Input
        parTypes=None,         # or Args-Input
    ):
        cmndOutcome = self.getOpOutcome()
        if interactive:
            if not self.cmndLineValidate(outcome=cmndOutcome):
                return cmndOutcome

        callParamsDict = {'controlProfile': controlProfile, 'inMailAcct': inMailAcct, }
        if not icm.cmndCallParamsValidate(callParamsDict, interactive, outcome=cmndOutcome):
            return cmndOutcome
        controlProfile = callParamsDict['controlProfile']
        inMailAcct = callParamsDict['inMailAcct']
####+END:

        G = icm.IcmGlobalContext()

        validParTypes = self.__class__.cmndArgsSpec[0]

        if not parTypes:
            parTypes = G.icmRunArgsGet().cmndArgs
        if not parTypes:
            parTypes = validParTypes
            
        for each in parTypes:
            if each in validParTypes:
                fpBaseDir = os.path.join(
                    inMailAcctDirGet(controlProfile, inMailAcct),
                    each,
                )
                FP_readTreeAtBaseDir_CmndOutput(
                    interactive=interactive,
                    fpBaseDir=fpBaseDir,
                    cmndOutcome=cmndOutcome,
                )
            else:
                icm.EH_problem_usageError("")
                continue

        return cmndOutcome
    
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Class-IIF    ::  inMailAcctAccessParsSet    [[elisp:(org-cycle)][| ]]
"""    
class inMailAcctAccessParsSet(icm.Cmnd):
    """."""

    cmndParamsMandatory = []
    cmndParamsOptional = ['controlProfile', 'inMailAcct', 'userName', 'userPasswd', 'imapServer']       
    cmndArgsLen = {'Min': 0, 'Max': 0,}

####+BEGIN: bx:dblock:python:icm:cmnd:parsValidate :par "controlProfile inMailAcct userName userPasswd imapServer"
    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
        interactive=False,        # Can also be called non-interactively
        controlProfile=None,         # or Cmnd-Input
        inMailAcct=None,         # or Cmnd-Input
        userName=None,         # or Cmnd-Input
        userPasswd=None,         # or Cmnd-Input
        imapServer=None,         # or Cmnd-Input
    ):
        cmndOutcome = self.getOpOutcome()
        if interactive:
            if not self.cmndLineValidate(outcome=cmndOutcome):
                return cmndOutcome

        callParamsDict = {'controlProfile': controlProfile, 'inMailAcct': inMailAcct, 'userName': userName, 'userPasswd': userPasswd, 'imapServer': imapServer, }
        if not icm.cmndCallParamsValidate(callParamsDict, interactive, outcome=cmndOutcome):
            return cmndOutcome
        controlProfile = callParamsDict['controlProfile']
        inMailAcct = callParamsDict['inMailAcct']
        userName = callParamsDict['userName']
        userPasswd = callParamsDict['userPasswd']
        imapServer = callParamsDict['imapServer']
####+END:

        G = icm.IcmGlobalContext()        

        inMailAcctDir = os.path.join(
            inMailAcctDirGet(inMailAcct),
            "access",
        )

        if userName:
            icm.FILE_ParamWriteToPath(
                parNameFullPath=os.path.join(inMailAcctDir, "userName"),
                parValue=userName,
            )

        if userPasswd:            
            icm.FILE_ParamWriteToPath(
                parNameFullPath=os.path.join(inMailAcctDir, "userPasswd"),
                parValue=userPasswd,
            )
            
        if imapServer:
            icm.FILE_ParamWriteToPath(
                parNameFullPath=os.path.join(inMailAcctDir, "imapServer"),
                parValue=imapServer,
            )
        
        if interactive:
            icm.ANN_here(inMailAcctDir)

        return cmndOutcome.set(
            opError=icm.OpError.Success,
            opResults=inMailAcctDir,
        )


"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Class-IIF    ::  inMailAcctControllerInfoParsSet    [[elisp:(org-cycle)][| ]]
"""
class inMailAcctControllerInfoParsSet(icm.Cmnd):
    """."""

    cmndParamsMandatory = []
    cmndParamsOptional = ['controlProfile', 'inMailAcct', 'firstName', 'lastName']
    cmndArgsLen = {'Min': 0, 'Max': 0,}

####+BEGIN: bx:dblock:python:icm:cmnd:parsValidate :par "controlProfile inMailAcct firstName lastName"
    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
        interactive=False,        # Can also be called non-interactively
        controlProfile=None,         # or Cmnd-Input
        inMailAcct=None,         # or Cmnd-Input
        firstName=None,         # or Cmnd-Input
        lastName=None,         # or Cmnd-Input
    ):
        cmndOutcome = self.getOpOutcome()
        if interactive:
            if not self.cmndLineValidate(outcome=cmndOutcome):
                return cmndOutcome

        callParamsDict = {'controlProfile': controlProfile, 'inMailAcct': inMailAcct, 'firstName': firstName, 'lastName': lastName, }
        if not icm.cmndCallParamsValidate(callParamsDict, interactive, outcome=cmndOutcome):
            return cmndOutcome
        controlProfile = callParamsDict['controlProfile']
        inMailAcct = callParamsDict['inMailAcct']
        firstName = callParamsDict['firstName']
        lastName = callParamsDict['lastName']
####+END:

        G = icm.IcmGlobalContext()        

        inMailAcctDir = os.path.join(
            inMailAcctDirGet(inMailAcct),
            "controllerInfo",
        )

        if firstName:
            icm.FILE_ParamWriteToPath(
                parNameFullPath=os.path.join(inMailAcctDir, "firstName"),
                parValue=firstName,
            )

        if lastName:
            icm.FILE_ParamWriteToPath(
                parNameFullPath=os.path.join(inMailAcctDir, "lastName"),
                parValue=lastName,
            )
        
        if interactive:
            icm.ANN_here(inMailAcctDir)

        return cmndOutcome.set(
            opError=icm.OpError.Success,
            opResults=inMailAcctDir,
        )


"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Class-IIF    ::  inMailAcctRetrievalParsSet    [[elisp:(org-cycle)][| ]]
"""
class inMailAcctRetrievalParsSet(icm.Cmnd):
    """."""

    cmndParamsMandatory = []
    cmndParamsOptional = ['controlProfile', 'inMailAcct', 'inMailAcctMboxesPath', 'mboxesList', 'ssl']       
    cmndArgsLen = {'Min': 0, 'Max': 0,}

####+BEGIN: bx:dblock:python:icm:cmnd:parsValidate :par "controlProfile inMailAcct inMailAcctMboxesPath mboxesList ssl"
    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
        interactive=False,        # Can also be called non-interactively
        controlProfile=None,         # or Cmnd-Input
        inMailAcct=None,         # or Cmnd-Input
        inMailAcctMboxesPath=None,         # or Cmnd-Input
        mboxesList=None,         # or Cmnd-Input
        ssl=None,         # or Cmnd-Input
    ):
        cmndOutcome = self.getOpOutcome()
        if interactive:
            if not self.cmndLineValidate(outcome=cmndOutcome):
                return cmndOutcome

        callParamsDict = {'controlProfile': controlProfile, 'inMailAcct': inMailAcct, 'inMailAcctMboxesPath': inMailAcctMboxesPath, 'mboxesList': mboxesList, 'ssl': ssl, }
        if not icm.cmndCallParamsValidate(callParamsDict, interactive, outcome=cmndOutcome):
            return cmndOutcome
        controlProfile = callParamsDict['controlProfile']
        inMailAcct = callParamsDict['inMailAcct']
        inMailAcctMboxesPath = callParamsDict['inMailAcctMboxesPath']
        mboxesList = callParamsDict['mboxesList']
        ssl = callParamsDict['ssl']
####+END:

        G = icm.IcmGlobalContext()        

        inMailAcctDir = os.path.join(
            inMailAcctDirGet(controlProfile, inMailAcct),
        "retrieval",
        )

        if inMailAcctMboxesPath: (           
            icm.FILE_ParamWriteToPath(
                parNameFullPath=os.path.join(inMailAcctDir, "inMailAcctMboxesPath"),
                parValue=os.path.abspath(
                    inMailAcctMboxesPath,
                )))

        if mboxesList: (           
            icm.FILE_ParamWriteToPath(
                parNameFullPath=os.path.join(inMailAcctDir, "mboxesList"),
                parValue=mboxesList,
                ))

        if ssl: (
            icm.FILE_ParamWriteToPath(
                parNameFullPath=os.path.join(inMailAcctDir, "ssl"),
                parValue=ssl,
            ))
            
        if interactive:
            icm.ANN_here(inMailAcctDir)

        return (
            cmndOutcome.set(
                opError=icm.OpError.Success,
                opResults=inMailAcctDir,
            ))
    
    
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Class-IIF    ::  outMailAcctParsGet    [[elisp:(org-cycle)][| ]]
"""
class outMailAcctParsGet(icm.Cmnd):
    """."""

    cmndParamsMandatory = []
    cmndParamsOptional = ['controlProfile', 'outMailAcct']       
    cmndArgsLen = {'Min': 0, 'Max': 0,}
    cmndArgsSpec = {0: ['access', 'controllerInfo', 'submission']}

####+BEGIN: bx:dblock:python:icm:cmnd:parsValidate :par "controlProfile outMailAcct" :args "parTypes"
    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
        interactive=False,        # Can also be called non-interactively
        controlProfile=None,         # or Cmnd-Input
        outMailAcct=None,         # or Cmnd-Input
        parTypes=None,         # or Args-Input
    ):
        cmndOutcome = self.getOpOutcome()
        if interactive:
            if not self.cmndLineValidate(outcome=cmndOutcome):
                return cmndOutcome

        callParamsDict = {'controlProfile': controlProfile, 'outMailAcct': outMailAcct, }
        if not icm.cmndCallParamsValidate(callParamsDict, interactive, outcome=cmndOutcome):
            return cmndOutcome
        controlProfile = callParamsDict['controlProfile']
        outMailAcct = callParamsDict['outMailAcct']
####+END:

        G = icm.IcmGlobalContext()

        validParTypes = self.__class__.cmndArgsSpec[0]

        if not parTypes:
            parTypes = G.icmRunArgsGet().cmndArgs
        if not parTypes:
            parTypes = validParTypes
            
        for each in parTypes:
            if each in validParTypes:
                fpBaseDir = os.path.join(
                    outMailAcctDirGet(controlProfile, outMailAcct),
                    each,
                )
                FP_readTreeAtBaseDir_CmndOutput(
                    interactive=interactive,
                    fpBaseDir=fpBaseDir,
                    cmndOutcome=cmndOutcome,
                )
            else:
                icm.EH_problem_usageError("")
                continue

        return cmndOutcome
    
    
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Class-IIF    ::  outMailAcctAccessParsSet    [[elisp:(org-cycle)][| ]]
"""    
class outMailAcctParsSet(icm.Cmnd):
    """."""

    cmndParamsMandatory = []
    cmndParamsOptional = [
        'controlProfile', 'outMailAcct',
        'userName', 'userPasswd', 'mtaRemHost', 'mtaRemProtocol',
        'firstName', 'lastName',
        'sendingMethod', 'envelopeAddr',
    ]       
    cmndArgsLen = {'Min': 1, 'Max': 1,}
    cmndArgsSpec = {0: ['access', 'controllerInfo', 'submission']}


####+BEGIN: bx:dblock:python:icm:cmnd:parsValidate :par "controlProfile outMailAcct userName userPasswd mtaRemHost mtaRemProtocol firstName lastName sendingMethod envelopeAddr" :args "parGroup"
    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
        interactive=False,        # Can also be called non-interactively
        controlProfile=None,         # or Cmnd-Input
        outMailAcct=None,         # or Cmnd-Input
        userName=None,         # or Cmnd-Input
        userPasswd=None,         # or Cmnd-Input
        mtaRemHost=None,         # or Cmnd-Input
        mtaRemProtocol=None,         # or Cmnd-Input
        firstName=None,         # or Cmnd-Input
        lastName=None,         # or Cmnd-Input
        sendingMethod=None,         # or Cmnd-Input
        envelopeAddr=None,         # or Cmnd-Input
        parGroup=None,         # or Args-Input
    ):
        cmndOutcome = self.getOpOutcome()
        if interactive:
            if not self.cmndLineValidate(outcome=cmndOutcome):
                return cmndOutcome

        callParamsDict = {'controlProfile': controlProfile, 'outMailAcct': outMailAcct, 'userName': userName, 'userPasswd': userPasswd, 'mtaRemHost': mtaRemHost, 'mtaRemProtocol': mtaRemProtocol, 'firstName': firstName, 'lastName': lastName, 'sendingMethod': sendingMethod, 'envelopeAddr': envelopeAddr, }
        if not icm.cmndCallParamsValidate(callParamsDict, interactive, outcome=cmndOutcome):
            return cmndOutcome
        controlProfile = callParamsDict['controlProfile']
        outMailAcct = callParamsDict['outMailAcct']
        userName = callParamsDict['userName']
        userPasswd = callParamsDict['userPasswd']
        mtaRemHost = callParamsDict['mtaRemHost']
        mtaRemProtocol = callParamsDict['mtaRemProtocol']
        firstName = callParamsDict['firstName']
        lastName = callParamsDict['lastName']
        sendingMethod = callParamsDict['sendingMethod']
        envelopeAddr = callParamsDict['envelopeAddr']
####+END:

        G = icm.IcmGlobalContext()

        validParGroups = self.__class__.cmndArgsSpec[0]

        if not parGroup:
            parGroup = G.icmRunArgsGet().cmndArgs[0]

        if not parGroup in validParGroups:
            return icm.EH_problem_usageError("mis-match")

        outMailAcctDir = os.path.join(
            outMailAcctDirGet(controlProfile, outMailAcct),
        )

        if parGroup == "access":
            if userName:
                icm.FILE_ParamWriteToPath(
                    parNameFullPath=os.path.join(outMailAcctDir, parGroup, "userName"),
                    parValue=userName,
                )

            if userPasswd:                        
                icm.FILE_ParamWriteToPath(
                    parNameFullPath=os.path.join(outMailAcctDir, parGroup, "userPasswd"),
                    parValue=userPasswd,
                )

            if mtaRemHost:
                icm.FILE_ParamWriteToPath(
                    parNameFullPath=os.path.join(outMailAcctDir, parGroup, "mtaRemHost"),
                    parValue=mtaRemHost,
                )
                
            if mtaRemProtocol:
                icm.FILE_ParamWriteToPath(
                    parNameFullPath=os.path.join(outMailAcctDir, parGroup, "mtaRemProtocol"),
                    parValue=mtaRemProtocol,
                )
                
        elif parGroup == "controllerInfo":
            if firstName:                        
                icm.FILE_ParamWriteToPath(
                    parNameFullPath=os.path.join(outMailAcctDir, parGroup, "firstName"),
                    parValue=firstName,
                )

            if lastName:
                icm.FILE_ParamWriteToPath(
                    parNameFullPath=os.path.join(outMailAcctDir, parGroup, "lastName"),
                    parValue=lastName,
                )

        elif parGroup == "submission":
            if sendingMethod:                        
                icm.FILE_ParamWriteToPath(
                    parNameFullPath=os.path.join(outMailAcctDir, parGroup, "sendingMethod"),
                    parValue=sendingMethod,
                )

            if envelopeAddr:
                icm.FILE_ParamWriteToPath(
                    parNameFullPath=os.path.join(outMailAcctDir, parGroup, "envelopeAddr"),
                    parValue=envelopeAddr,
                )
            
        else:
            return icm.EH_problem_usageError("OOPS")
        
        if interactive:
            icm.ANN_here(outMailAcctDir)

        return cmndOutcome.set(
            opError=icm.OpError.Success,
            opResults=outMailAcctDir,
        )
    
    

####+BEGIN: bx:icm:python:section :title "End Of Editable Text"
"""
*  [[elisp:(beginning-of-buffer)][Top]] ################ [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *End Of Editable Text*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:

####+BEGIN: bx:dblock:global:file-insert-cond :cond "./blee.el" :file "/libre/ByStar/InitialTemplates/software/plusOrg/dblock/inserts/endOfFileControls.org"
#+STARTUP: showall
####+END:

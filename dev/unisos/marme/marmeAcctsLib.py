# -*- coding: utf-8 -*-
"""\
* *[Summary]* ::  A /library/ with ICM Cmnds to support managment of Marme related mail profiles
"""

####+BEGIN: bx:icm:python:top-of-file :partof "bystar" :copyleft "halaal+minimal"
"""
*  This file:/acct/smb/com/dev-py/LUE/Sync/pypi/pkgs/unisos/marme/dev/unisos/marme/marmeAcctsLib.py :: [[elisp:(org-cycle)][| ]]
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
__libName__ = "marmeAcctsLib"
####+END:

####+BEGIN: bx:global:timestamp:version-py :style "date"
__version__ = "201805285653"
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


####+BEGIN: bx:dblock:python:icmItem :itemType "=Imports=" :itemTitle "*IMPORTS*"
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || =Imports=      :: *IMPORTS*  [[elisp:(org-cycle)][| ]]
"""
####+END:

import os
import collections
#import enum


####+BEGIN: bx:dblock:global:file-insert :file "/libre/ByStar/InitialTemplates/update/sw/icm/py/importUcfIcmG.py"
from unisos import ucf
from unisos import icm

icm.unusedSuppressForEval(ucf.__file__)  # in case icm and ucf are not used

G = icm.IcmGlobalContext()
G.icmLibsAppend = __file__
G.icmCmndsLibsAppend = __file__

####+END:

from unisos.common import icmsPkgLib

from unisos.marme import marmePkgThis

from bisos.common import serviceObject
from bisos.currents import bxCurrentsConfig

####+BEGIN: bx:dblock:python:section :title "Library Description (Overview)"
"""
*  [[elisp:(beginning-of-buffer)][Top]] ################ [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *Library Description (Overview)*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:

####+BEGIN: bx:icm:python:cmnd:classHead :cmndName "marmeAcctsLib_libOverview" :parsMand "" :parsOpt "" :argsMin "0" :argsMax "3" :asFunc "" :interactiveP ""
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || ICM-Cmnd       :: /marmeAcctsLib_libOverview/ parsMand= parsOpt= argsMin=0 argsMax=3 asFunc= interactive=  [[elisp:(org-cycle)][| ]]
"""
class marmeAcctsLib_libOverview(icm.Cmnd):
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
*       [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(org-cycle)][| *Description:* | ]]
**  [[elisp:(org-cycle)][| ]]  [Xref]          :: *[Related/Xrefs:]*  <<Xref-Here->>  -- External Documents  [[elisp:(org-cycle)][| ]]

**  [[elisp:(org-cycle)][| ]]	Model and Terminology 					   :Overview:
This module is part of BISOS and its primary documentation is in  http://www.by-star.net/PLPC/180047
**  [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]]	ICMs Pkg Inputs And Configuration Patterns 		   :Overview:

    The following modules work collaboratively
     + icmNamePkgThis.py            :: this module which is the main interface for the pkg
     + icmNamePkgConfig.py          :: the file that locates config and data dirs
     + unisos.common.icmsPkgLib.py  :: the lib that implements icmPkg polices

    An ICM-Pkg typically has the following accompanying directories:
     - icmName-config     :: Where fp params for the pkg are (Read/Write)
     - icmName-base       :: Where data and inputs are (Read only)
     - pkgControl         :: bxoIdSr params that control Instance Execution

***   [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]]	General Execution Configuration Vs Instance Execution Configuration

    Execution configuration is performed in 2 layers:

    1) General Execution  Parameters  :: These are specified in icmName- dir
	 1.1) icmName-config
	 1.2) icmName-base

    2) Instance Execution Configuration Parameters :: These are specified in control base

***   [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]]	Organization Of icmNamePkgConfig.py

    The organization of icmNamePkgConfig.py usually follows the pattern below:
    
      * Interface to obtain 
	** icmName-config -- configBaseDirGet
        ** icmName-base  -- inputsBaseDirGet

      * Interface to obtain icmPkg General Execution params
	** control
	** var
	** tmp
	** log

      * Interface to obtain icmPkg Instance Execution params
**      [End-Of-Description]
"""
        
        moduleUsage="""
*       [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]]  [[elisp:(org-cycle)][| *Usage:* | ]]

**      How-Tos:
**      [End-Of-Usage]
"""
        
        moduleStatus="""
*       [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]]  [[elisp:(org-cycle)][| *Status:* | ]]
**  [[elisp:(org-cycle)][| ]]  [Info]          :: *[Current-Info:]* Status/Maintenance -- General TODO List [[elisp:(org-cycle)][| ]]
** DONE [[elisp:(org-cycle)][| ]]  Current         :: [2018-05-30 Wed] BxoIdSr Updates and cleanups completed  [[elisp:(org-cycle)][| ]]
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

####+BEGIN: bx:icm:python:section :title "Common Module Conventions (BxoIdSr)"
"""
*  [[elisp:(beginning-of-buffer)][Top]] ################ [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *Common Module Conventions (BxoIdSr)*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:

####+BEGIN: bx:dblock:global:file-insert :file "/libre/ByStar/InitialTemplates/update/sw/icm/py/curGetBxOSr.py"
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func-BxoIdSr   :: /curGet_{bxoId,sr}/ retType=str argsList=nil  [[elisp:(org-cycle)][| ]]
"""

def curGet_bxoId(): return bxCurrentsConfig.bxoId_fpObtain(configBaseDir=None)
def curGet_sr(): return bxCurrentsConfig.sr_fpObtain(configBaseDir=None)
def cmndParsCurBxoSr(cps): cps['bxoId'] = curGet_bxoId(); cps['sr'] = curGet_sr()

####+END:

####+BEGIN: bx:icm:python:section :title "Obtain ICM-Package Anchor For General Execution"
"""
*  [[elisp:(beginning-of-buffer)][Top]] ################ [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *Obtain ICM-Package Anchor For General Execution*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:


####+BEGIN: bx:icm:python:func :funcName "pkgAnchor_configDir_obtain" :funcType "anyOrNone" :retType "str(path)" :deco "" :argsList ""
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func-anyOrNone :: /pkgAnchor_configDir_obtain/ retType=str(path) argsList=nil  [[elisp:(org-cycle)][| ]]
"""
def pkgAnchor_configDir_obtain():
####+END:
    return marmePkgThis.pkgBase_configDir()


####+BEGIN: bx:icm:python:func :funcName "pkgAnchor_baseDir_obtain" :funcType "anyOrNone" :retType "str(path)" :deco "" :argsList ""
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func-anyOrNone :: /pkgAnchor_baseDir_obtain/ retType=str(path) argsList=nil  [[elisp:(org-cycle)][| ]]
"""
def pkgAnchor_baseDir_obtain():
####+END:
    return (
            marmePkgThis.pkgBase_baseDir()
    )


####+BEGIN: bx:icm:python:func :funcName "inputsBaseDirGet" :funcType "anyOrNone" :retType "str(path)" :deco "" :argsList ""
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func-anyOrNone :: /inputsBaseDirGet/ retType=str(path) argsList=nil  [[elisp:(org-cycle)][| ]]
"""
def inputsBaseDirGet():
####+END:
    return (
        icmsPkgLib.pkgInputsBaseDir_obtain(
            pkgAnchor_baseDir_obtain()
        )
    )


####+BEGIN: bx:icm:python:section :title "Obtain ICM-Package Canonical General Execution Bases"
"""
*  [[elisp:(beginning-of-buffer)][Top]] ################ [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *Obtain ICM-Package Canonical General Execution Bases*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:

####+BEGIN: bx:icm:python:func :funcName "mailAcctsBaseDirGet" :funcType "anyOrNone" :retType "bool" :deco "" :argsList "bxoId=None sr=None"
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func-anyOrNone :: /mailAcctsBaseDirGet/ retType=bool argsList=(bxoId=None sr=None)  [[elisp:(org-cycle)][| ]]
"""
def mailAcctsBaseDirGet(
    bxoId=None,
    sr=None,
):
####+END:
    return(
        icmsPkgLib.pkgBaseDir_obtain(bxoId=bxoId, sr=sr,)
    )



####+BEGIN: bx:icm:python:func :funcName "configBaseDirGet" :funcType "anyOrNone" :retType "bool" :deco "" :argsList "bxoId=None sr=None"
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func-anyOrNone :: /configBaseDirGet/ retType=bool argsList=(bxoId=None sr=None)  [[elisp:(org-cycle)][| ]]
"""
def configBaseDirGet(
    bxoId=None,
    sr=None,
):
####+END:
    return(
        os.path.join(
            icmsPkgLib.varConfigBaseDir_obtain(
                icmsPkgInfoBaseDir=pkgAnchor_configDir_obtain(),
                bxoId=bxoId,
                sr=sr,
            ),
            "marme"   # NOTYET -- icmsPkgName
        )
    )



####+BEGIN: bx:icm:python:func :funcName "controlBaseDirGet" :funcType "anyOrNone" :retType "bool" :deco "" :argsList "bxoId=None sr=None"
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func-anyOrNone :: /controlBaseDirGet/ retType=bool argsList=(bxoId=None sr=None)  [[elisp:(org-cycle)][| ]]
"""
def controlBaseDirGet(
    bxoId=None,
    sr=None,
):
####+END:
    retVal = icmsPkgLib.controlBaseDir_obtain(
        icmsPkgInfoBaseDir=pkgAnchor_configDir_obtain(),
        bxoId=bxoId,
        sr=sr,
    )

    return (
        os.path.join(
            retVal,
            "control",
        )
    )


####+BEGIN: bx:icm:python:func :funcName "varBaseDirGet" :funcType "anyOrNone" :retType "bool" :deco "" :argsList "bxoId=None sr=None"
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func-anyOrNone :: /varBaseDirGet/ retType=bool argsList=(bxoId=None sr=None)  [[elisp:(org-cycle)][| ]]
"""
def varBaseDirGet(
    bxoId=None,
    sr=None,
):
####+END:
    return(
        os.path.join(
            icmsPkgLib.varBaseDir_obtain(
                icmsPkgInfoBaseDir=pkgAnchor_configDir_obtain(),
                bxoId=bxoId,
                sr=sr,            
            ),
            "marme"   # NOTYET -- icmsPkgName
        )
    )

    
####+BEGIN: bx:icm:python:func :funcName "tmpBaseDirGet" :funcType "anyOrNone" :retType "bool" :deco "" :argsList "bxoId=None sr=None"
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func-anyOrNone :: /tmpBaseDirGet/ retType=bool argsList=(bxoId=None sr=None)  [[elisp:(org-cycle)][| ]]
"""
def tmpBaseDirGet(
    bxoId=None,
    sr=None,
):
####+END:
    return(
        icmsPkgLib.tmpBaseDir_obtain(
            icmsPkgInfoBaseDir=pkgAnchor_configDir_obtain(),
            bxoId=bxoId,
            sr=sr,
        )
    )

    
####+BEGIN: bx:icm:python:func :funcName "logBaseDirGet" :funcType "anyOrNone" :retType "bool" :deco "" :argsList "bxoId=None sr=None"
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func-anyOrNone :: /logBaseDirGet/ retType=bool argsList=(bxoId=None sr=None)  [[elisp:(org-cycle)][| ]]
"""
def logBaseDirGet(
    bxoId=None,
    sr=None,
):
####+END:
    return(
        icmsPkgLib.logBaseDir_obtain(
            icmsPkgInfoBaseDir=pkgAnchor_configDir_obtain(),
            bxoId=bxoId,
            sr=sr,
        )
    )


"""
*  [[elisp:(beginning-of-buffer)][Top]] ################ [[elisp:(delete-other-windows)][(1)]]      *Control From  FP Obtain*
"""

    
####+BEGIN: bx:icm:python:func :funcName "enabledControlProfileObtain" :funcType "anyOrNone" :retType "bool" :deco "" :argsList "bxoId=None sr=None"
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func-anyOrNone :: /enabledControlProfileObtain/ retType=bool argsList=(bxoId=None sr=None)  [[elisp:(org-cycle)][| ]]
"""
def enabledControlProfileObtain(
    bxoId=None,
    sr=None,
):
####+END:
    """Returns as a string fp value read."""
    return icm.FILE_ParamValueReadFrom(
        parRoot=os.path.join(
            controlBaseDirGet(bxoId=bxoId, sr=sr,),
            "common",
            "selections",
            "fp",
        ),
        parName="enabledControlProfile",
    )

####+BEGIN: bx:icm:python:func :funcName "availableControlProfilesObtain" :funcType "anyOrNone" :retType "bool" :deco "" :argsList "bxoId=None sr=None"
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func-anyOrNone :: /availableControlProfilesObtain/ retType=bool argsList=(bxoId=None sr=None)  [[elisp:(org-cycle)][| ]]
"""
def availableControlProfilesObtain(
    bxoId=None,
    sr=None,
):
####+END:
    """
Returns a list
"""
    availablesList = list()
    controlBaseDir = controlBaseDirGet(bxoId=bxoId, sr=sr,)
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

####+BEGIN: bx:icm:python:func :funcName "enabledInMailAcctObtain" :funcType "anyOrNone" :retType "bool" :deco "" :argsList "bxoId=None sr=None"
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func-anyOrNone :: /enabledInMailAcctObtain/ retType=bool argsList=(bxoId=None sr=None)  [[elisp:(org-cycle)][| ]]
"""
def enabledInMailAcctObtain(
    bxoId=None,
    sr=None,
):
####+END:
    """
** Called obtain to leave Get for the IIF"""
    return icm.FILE_ParamValueReadFrom(
        parRoot=os.path.join(
            controlBaseDirGet(bxoId=bxoId, sr=sr,),
            "common",
            "selections",
            "fp",
        ),
        parName="enabledInMailAcct",          
    )

####+BEGIN: bx:icm:python:func :funcName "availableInMailAcctObtain" :funcType "anyOrNone" :retType "bool" :deco "" :argsList "bxoId=None sr=None"
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func-anyOrNone :: /availableInMailAcctObtain/ retType=bool argsList=(bxoId=None sr=None)  [[elisp:(org-cycle)][| ]]
"""
def availableInMailAcctObtain(
    bxoId=None,
    sr=None,
):
####+END:
    """
Returns a list
"""
    availablesList = list()
    baseDir = os.path.join(
           controlProfileBaseDirGet(
               enabledControlProfileObtain(bxoId=bxoId, sr=sr,),
               bxoId=bxoId,
               sr=sr,
           ),
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

####+BEGIN: bx:icm:python:func :funcName "enabledOutMailAcctObtain" :funcType "anyOrNone" :retType "bool" :deco "" :argsList "bxoId=None sr=None"
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func-anyOrNone :: /enabledOutMailAcctObtain/ retType=bool argsList=(bxoId=None sr=None)  [[elisp:(org-cycle)][| ]]
"""
def enabledOutMailAcctObtain(
    bxoId=None,
    sr=None,
):
####+END:
    """
** Called obtain to leave Get for the IIF"""
    return icm.FILE_ParamValueReadFrom(
        parRoot=os.path.join(
            controlBaseDirGet(bxoId=bxoId, sr=sr,),
            "common",
            "selections",
            "fp",
        ),
        parName="enabledOutMailAcct",          
    )

####+BEGIN: bx:icm:python:func :funcName "availableOutMailAcctObtain" :funcType "anyOrNone" :retType "bool" :deco "" :argsList "bxoId=None sr=None"
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func-anyOrNone :: /availableOutMailAcctObtain/ retType=bool argsList=(bxoId=None sr=None)  [[elisp:(org-cycle)][| ]]
"""
def availableOutMailAcctObtain(
    bxoId=None,
    sr=None,
):
####+END:
    """
Returns a list
"""
    availablesList = list()
    baseDir = os.path.join(
        controlProfileBaseDirGet(
            enabledControlProfileObtain(bxoId=bxoId, sr=sr,),
            bxoId=bxoId,
            sr=sr,
        ),
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


####+BEGIN: bx:icm:python:func :funcName "enabledMailBoxObtain" :funcType "anyOrNone" :retType "bool" :deco "" :argsList "bxoId=None sr=None"
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func-anyOrNone :: /enabledMailBoxObtain/ retType=bool argsList=(bxoId=None sr=None)  [[elisp:(org-cycle)][| ]]
"""
def enabledMailBoxObtain(
    bxoId=None,
    sr=None,
):
####+END:
    """
** Called obtain to leave Get for the IIF"""
    return icm.FILE_ParamValueReadFrom(
        parRoot=os.path.join(
            controlBaseDirGet(bxoId=bxoId, sr=sr,),
            "common",
            "selections",
            "fp",
        ),
        parName="enabledMailBox",          
    )


"""
*  [[elisp:(beginning-of-buffer)][Top]] ################ [[elisp:(delete-other-windows)][(1)]]      *Control Base Directory From FP Get*
"""

####+BEGIN: bx:icm:python:func :funcName "controlProfileBaseDirGet" :funcType "anyOrNone" :retType "bool" :deco "" :argsList "controlProfile bxoId=None sr=None"
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func-anyOrNone :: /controlProfileBaseDirGet/ retType=bool argsList=(controlProfile bxoId=None sr=None)  [[elisp:(org-cycle)][| ]]
"""
def controlProfileBaseDirGet(
    controlProfile,
    bxoId=None,
    sr=None,
):
####+END:
    """
** Joins controlBaseDirGet() and enabledControlProfileObtain()
"""
    if not controlProfile:
        controlProfile = enabledControlProfileObtain(bxoId=bxoId, sr=sr,)

    return os.path.abspath(
        os.path.join(
            controlBaseDirGet(bxoId=bxoId, sr=sr,),
            controlProfile,
    ))



####+BEGIN: bx:icm:python:func :funcName "outMailAcctDirGet" :funcType "anyOrNone" :retType "bool" :deco "" :argsList "controlProfile outMailAcct bxoId=None sr=None"
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func-anyOrNone :: /outMailAcctDirGet/ retType=bool argsList=(controlProfile outMailAcct bxoId=None sr=None)  [[elisp:(org-cycle)][| ]]
"""
def outMailAcctDirGet(
    controlProfile,
    outMailAcct,
    bxoId=None,
    sr=None,
):
####+END:
    return os.path.abspath(
        os.path.join(
           controlProfileBaseDirGet(controlProfile, bxoId=bxoId, sr=sr,),
            "outMail",
            outMailAcct,
            "fp",
    ))


####+BEGIN: bx:icm:python:func :funcName "outMailCommonDirGet" :funcType "anyOrNone" :retType "bool" :deco "" :argsList "controlProfile bxoId=None sr=None"
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func-anyOrNone :: /outMailCommonDirGet/ retType=bool argsList=(controlProfile bxoId=None sr=None)  [[elisp:(org-cycle)][| ]]
"""
def outMailCommonDirGet(
    controlProfile,
    bxoId=None,
    sr=None,
):
####+END:
    if not controlProfile:
        controlProfile = enabledControlProfileObtain(bxoId=bxoId, sr=sr,)
    return os.path.abspath(
        os.path.join(
            controlProfileBaseDirGet(controlProfile, bxoId=bxoId, sr=sr,),
            "outMail",
            "common",
            #"fp",         # NOTYET, Needs to be revisited
    ))

####+BEGIN: bx:icm:python:func :funcName "inMailAcctDirGet" :funcType "anyOrNone" :retType "bool" :deco "" :argsList "controlProfile inMailAcct bxoId=None sr=None"
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func-anyOrNone :: /inMailAcctDirGet/ retType=bool argsList=(controlProfile inMailAcct bxoId=None sr=None)  [[elisp:(org-cycle)][| ]]
"""
def inMailAcctDirGet(
    controlProfile,
    inMailAcct,
    bxoId=None,
    sr=None,
):
####+END:
    if not controlProfile:
        controlProfile = enabledControlProfileObtain(bxoId=bxoId, sr=sr,)
    return os.path.abspath(
        os.path.join(
            controlProfileBaseDirGet(controlProfile, bxoId=bxoId, sr=sr,),             
            "inMail",
            inMailAcct,
            "fp",
    ))

####+BEGIN: bx:icm:python:func :funcName "inMailCommonDirGet" :funcType "anyOrNone" :retType "bool" :deco "" :argsList "controlProfile bxoId=None sr=None"
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func-anyOrNone :: /inMailCommonDirGet/ retType=bool argsList=(controlProfile bxoId=None sr=None)  [[elisp:(org-cycle)][| ]]
"""
def inMailCommonDirGet(
    controlProfile,
    bxoId=None,
    sr=None,
):
####+END:
    if not controlProfile:
        controlProfile = enabledControlProfileObtain(bxoId=bxoId, sr=sr,)
    return (
        os.path.abspath(
            os.path.join(
                controlProfileBaseDirGet(controlProfile, bxoId=bxoId, sr=sr,),
                "inMail"
                "common"
                "fp"            
            )))


"""
*  [[elisp:(beginning-of-buffer)][Top]] ################ [[elisp:(delete-other-windows)][(1)]]      *VAR Base Directory Get*
"""

####+BEGIN: bx:icm:python:func :funcName "getPathForAcctMaildir" :funcType "anyOrNone" :retType "bool" :deco "" :argsList "controlProfile mailAcct bxoId=None sr=None"
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func-anyOrNone :: /getPathForAcctMaildir/ retType=bool argsList=(controlProfile mailAcct bxoId=None sr=None)  [[elisp:(org-cycle)][| ]]
"""
def getPathForAcctMaildir(
    controlProfile,
    mailAcct,
    bxoId=None,
    sr=None,
):
####+END:
    """
** NOTYET, controlProfile is not being used.
"""
    return (
        os.path.join(
            varBaseDirGet(bxoId=bxoId, sr=sr,),
            "inMail",
            controlProfile,
            mailAcct,
            "maildir"
        ))

####+BEGIN: bx:icm:python:func :funcName "getPathForAcctMbox" :funcType "anyOrNone" :retType "bool" :deco "" :argsList "controlProfile mailAcct mbox bxoId=None sr=None"
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func-anyOrNone :: /getPathForAcctMbox/ retType=bool argsList=(controlProfile mailAcct mbox bxoId=None sr=None)  [[elisp:(org-cycle)][| ]]
"""
def getPathForAcctMbox(
    controlProfile,
    mailAcct,
    mbox,
    bxoId=None,
    sr=None,
):
####+END:
    #if not controlProfile:
        #controlProfile = enabledControlProfileObtain(bxoId=bxoId, sr=sr,)

    if not mailAcct:
        mailAcct = enabledInMailAcctObtain(bxoId=bxoId, sr=sr,)

    if not mbox:
        mbox = enabledMailBoxObtain(bxoId=bxoId, sr=sr,)

    return (
        os.path.join(
            varBaseDirGet(bxoId=bxoId, sr=sr,),
            "inMail",
            controlProfile,            
            mailAcct,
            "maildir",
            mbox,
        ))

####+BEGIN: bx:icm:python:func :funcName "getPathForInMailConfig" :funcType "anyOrNone" :retType "bool" :deco "" :argsList "controlProfile inMailAcct bxoId=None sr=None"
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func-anyOrNone :: /getPathForInMailConfig/ retType=bool argsList=(controlProfile inMailAcct bxoId=None sr=None)  [[elisp:(org-cycle)][| ]]
"""
def getPathForInMailConfig(
    controlProfile,
    inMailAcct,
    bxoId=None,
    sr=None,
):
####+END:
    return (
        os.path.join(
            configBaseDirGet(bxoId=bxoId, sr=sr,),
            "inMail",
            controlProfile,            
            inMailAcct,
        ))

####+BEGIN: bx:icm:python:func :funcName "getPathForOutMailConfig" :funcType "anyOrNone" :retType "bool" :deco "" :argsList "controlProfile outMailAcct bxoId=None sr=None"
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func-anyOrNone :: /getPathForOutMailConfig/ retType=bool argsList=(controlProfile outMailAcct bxoId=None sr=None)  [[elisp:(org-cycle)][| ]]
"""
def getPathForOutMailConfig(
    controlProfile,
    outMailAcct,
    bxoId=None,
    sr=None,
):
####+END:
    return (
        os.path.join(
            configBaseDirGet(bxoId=bxoId, sr=sr,),
            "outMail",
            controlProfile,            
            outMailAcct,
        ))


####+BEGIN: bx:icm:python:subSection :title "Common Arguments Specification"
"""
*  [[elisp:(beginning-of-buffer)][Top]] ================ [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]          *Common Arguments Specification*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:

####+BEGIN: bx:icm:python:func :funcName "commonParamsSpecify" :funcType "anyOrNone" :retType "bool" :deco "" :argsList "icmParams"
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func-anyOrNone :: /commonParamsSpecify/ retType=bool argsList=(icmParams)  [[elisp:(org-cycle)][| ]]
"""
def commonParamsSpecify(
    icmParams,
):
####+END:
    
    enabledControlProfile = enabledControlProfileObtain(curGet_bxoId(), curGet_sr())    
    enabledInMailAcct = enabledInMailAcctObtain(curGet_bxoId(), curGet_sr())
    enabledOutMailAcct = enabledOutMailAcctObtain(curGet_bxoId(), curGet_sr())        

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

    serviceObject.commonParamsSpecify(icmParams)

    

"""
*  [[elisp:(beginning-of-buffer)][Top]] ################ [[elisp:(delete-other-windows)][(1)]]      *Common Examples Sections*
"""

####+BEGIN: bx:icm:python:func :funcName "examples_bxoSrPkgInfoParsGet" :funcType "anyOrNone" :retType "bool" :deco "" :argsList ""
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func-anyOrNone :: /examples_bxoSrPkgInfoParsGet/ retType=bool argsList=nil  [[elisp:(org-cycle)][| ]]
"""
def examples_bxoSrPkgInfoParsGet():
####+END:
    """."""
    
    def cpsInit(): return collections.OrderedDict()
    def menuItem(verbosity): icm.ex_gCmndMenuItem(cmndName, cps, cmndArgs, verbosity=verbosity) # 'little' or 'none'
    def execLineEx(cmndStr): icm.ex_gExecMenuItem(execLine=cmndStr)
    
    icm.cmndExampleMenuChapter('* =Info=  BxoSr PkgInfoParsGet*')

    cmndName = "bxoSrPkgInfoParsGet" ; cmndArgs = ""
    cps=cpsInit(); cmndParsCurBxoSr(cps); menuItem(verbosity='none')

    return

####+BEGIN: bx:icm:python:func :funcName "examples_controlProfileManage" :funcType "anyOrNone" :retType "bool" :deco "" :argsList ""
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func-anyOrNone :: /examples_controlProfileManage/ retType=bool argsList=nil  [[elisp:(org-cycle)][| ]]
"""
def examples_controlProfileManage():
####+END:
    """.
"""
    def cpsInit(): return collections.OrderedDict()
    def menuItem(verbosity): icm.ex_gCmndMenuItem(cmndName, cps, cmndArgs, verbosity=verbosity) # 'little' or 'none'
    def execLineEx(cmndStr): icm.ex_gExecMenuItem(execLine=cmndStr)
    
    icm.cmndExampleMenuChapter('* =Selection=  Control Profiles -- /{}/ --*'.format(
        enabledControlProfileObtain(curGet_bxoId(), curGet_sr()))
    )
    cmndName = "enabledControlProfileGet" ; cmndArgs = ""
    cps=cpsInit(); cmndParsCurBxoSr(cps); menuItem(verbosity='none')

    cmndName = "enabledControlProfileSet"

    for each in availableControlProfilesObtain(curGet_bxoId(), curGet_sr()):
        cmndArgs = " {controlProfile}".format(controlProfile=each)
        cps=cpsInit(); cmndParsCurBxoSr(cps); menuItem(verbosity='little')

    return


####+BEGIN: bx:icm:python:func :funcName "examples_enabledInMailAcctConfig" :funcType "anyOrNone" :retType "bool" :deco "" :argsList ""
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func-anyOrNone :: /examples_enabledInMailAcctConfig/ retType=bool argsList=nil  [[elisp:(org-cycle)][| ]]
"""
def examples_enabledInMailAcctConfig():
####+END:
    """
** Select Enabled Mail Account Config. Read/Writeen to control/common/selections/fp
"""
    def cpsInit(): return collections.OrderedDict()
    def menuItem(verbosity): icm.ex_gCmndMenuItem(cmndName, cps, cmndArgs, verbosity=verbosity) # 'little' or 'none'
    def execLineEx(cmndStr): icm.ex_gExecMenuItem(execLine=cmndStr)
 
    icm.cmndExampleMenuChapter('* =Selection=  InMailAccts -- /{controlProfile}+{mailAcct}/ --*'.format(
        controlProfile=enabledControlProfileObtain(curGet_bxoId(), curGet_sr()),
        mailAcct=enabledInMailAcctObtain(curGet_bxoId(), curGet_sr()))
    )

    cmndName = "enabledInMailAcctGet" ; cmndArgs = ""
    cps=cpsInit(); cmndParsCurBxoSr(cps); menuItem(verbosity='none')

    cmndName = "enabledInMailAcctSet"

    for each in availableInMailAcctObtain(curGet_bxoId(), curGet_sr()):
        cmndArgs = " {}".format(each)
        cps=cpsInit(); cmndParsCurBxoSr(cps); menuItem(verbosity='little')        

    return

####+BEGIN: bx:icm:python:func :funcName "examples_enabledOutMailAcctConfig" :funcType "anyOrNone" :retType "bool" :deco "" :argsList ""
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func-anyOrNone :: /examples_enabledOutMailAcctConfig/ retType=bool argsList=nil  [[elisp:(org-cycle)][| ]]
"""
def examples_enabledOutMailAcctConfig():
####+END:
    """
** Select Enabled Mail Account Config. Read/Writeen to control/common/selections/fp
"""
    def cpsInit(): return collections.OrderedDict()
    def menuItem(verbosity): icm.ex_gCmndMenuItem(cmndName, cps, cmndArgs, verbosity=verbosity) # 'little' or 'none'
    def execLineEx(cmndStr): icm.ex_gExecMenuItem(execLine=cmndStr)

    icm.cmndExampleMenuChapter('* =Selection=  OutMailAccts -- /{controlProfile}+{mailAcct}/ --*'.format(
        controlProfile=enabledControlProfileObtain(curGet_bxoId(), curGet_sr()),
        mailAcct=enabledOutMailAcctObtain(curGet_bxoId(), curGet_sr())))

    cmndName = "enabledOutMailAcctGet" ; cmndArgs = ""
    cps=cpsInit(); cmndParsCurBxoSr(cps); menuItem(verbosity='none')

    cmndName = "enabledOutMailAcctSet"    

    for each in availableOutMailAcctObtain(curGet_bxoId(), curGet_sr()):
        cmndArgs = " {}".format(each)
        cps=cpsInit(); cmndParsCurBxoSr(cps); menuItem(verbosity='little')        

    return
    
####+BEGIN: bx:icm:python:func :funcName "examples_select_mailBox" :funcType "anyOrNone" :retType "bool" :deco "" :argsList ""
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func-anyOrNone :: /examples_select_mailBox/ retType=bool argsList=nil  [[elisp:(org-cycle)][| ]]
"""
def examples_select_mailBox():
####+END:
    """."""
    def cpsInit(): return collections.OrderedDict()
    def menuItem(verbosity): icm.ex_gCmndMenuItem(cmndName, cps, cmndArgs, verbosity=verbosity) # 'little' or 'none'
    def execLineEx(cmndStr): icm.ex_gExecMenuItem(execLine=cmndStr)

    icm.cmndExampleMenuChapter('* =Selection=  MailBox -- /{controlProfile}+{mailAcct}+{mBox}/ --*'.format(
        controlProfile=enabledControlProfileObtain(curGet_bxoId(), curGet_sr()),
        mailAcct=enabledInMailAcctObtain(curGet_bxoId(), curGet_sr()),
        mBox=enabledMailBoxGet().cmnd(bxoId=curGet_bxoId(), sr=curGet_sr()).results,
        )
    )

    cmndName = "enabledMailBoxGet" ; cmndArgs = ""
    cps=cpsInit(); cmndParsCurBxoSr(cps); menuItem(verbosity='none')

    cmndName = "enabledMailBoxSet" ; cmndArgs = "Inbox"
    cps=cpsInit(); cmndParsCurBxoSr(cps); menuItem(verbosity='none')
    
    
    
####+BEGIN: bx:icm:python:func :funcName "examples_inMailAcctAccessPars" :funcType "anyOrNone" :retType "bool" :deco "" :argsList ""
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func-anyOrNone :: /examples_inMailAcctAccessPars/ retType=bool argsList=nil  [[elisp:(org-cycle)][| ]]
"""
def examples_inMailAcctAccessPars():
####+END:
    """
** Auxiliary examples to be commonly used.
"""
    def cpsInit(): return collections.OrderedDict()
    def menuItem(verbosity): icm.ex_gCmndMenuItem(cmndName, cps, cmndArgs, verbosity=verbosity) # 'little' or 'none'
    def execLineEx(cmndStr): icm.ex_gExecMenuItem(execLine=cmndStr)
    
    icm.cmndExampleMenuChapter('* =FP Values=  inMail Controls -- /{controlProfile}+{mailAcct}/ --*'.format(
        controlProfile=enabledControlProfileObtain(curGet_bxoId(), curGet_sr()),
        mailAcct=enabledInMailAcctObtain(curGet_bxoId(), curGet_sr()))
    )
    cmndName = "inMailAcctParsGet" ; cmndArgs = ""
    cps=cpsInit(); cmndParsCurBxoSr(cps); menuItem(verbosity='none')

    menuLine = """"""
    icm.cmndExampleMenuItem(menuLine, icmName="marmeAcctsManage.py", verbosity='none')
    

####+BEGIN: bx:icm:python:func :funcName "examples_inMailAcctAccessParsFull" :funcType "anyOrNone" :retType "bool" :deco "" :argsList ""
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func-anyOrNone :: /examples_inMailAcctAccessParsFull/ retType=bool argsList=nil  [[elisp:(org-cycle)][| ]]
"""
def examples_inMailAcctAccessParsFull():
####+END:
    """
** Auxiliary examples to be commonly used.
"""
    def cpsInit(): return collections.OrderedDict()
    def menuItem(verbosity): icm.ex_gCmndMenuItem(cmndName, cps, cmndArgs, verbosity=verbosity) # 'little' or 'none'
    def execLineEx(cmndStr): icm.ex_gExecMenuItem(execLine=cmndStr)
    
    icm.cmndExampleMenuChapter('* =FP Values=  inMail Controls -- /{controlProfile}+{mailAcct}/ --*'.format(
        controlProfile=enabledControlProfileObtain(curGet_bxoId(), curGet_sr()),
        mailAcct=enabledInMailAcctObtain(curGet_bxoId(), curGet_sr()))
    )
    cmndName = "inMailAcctParsGet" ; cmndArgs = ""
    cps=cpsInit(); cmndParsCurBxoSr(cps); menuItem(verbosity='none')

    icm.cmndExampleMenuSection('*inMail /Access/ ParsSet -- /defaulMailAcct={}/ --*'.format(
        enabledInMailAcctObtain(curGet_bxoId(), curGet_sr()))
    )
    cmndName = "inMailAcctAccessParsSet" ; cmndArgs = "" ;
    cps=cpsInit() ; cmndParsCurBxoSr(cps)
    cps['userName'] = "UserName" ; cps['userPasswd'] = "UserPasswd" ; cps['imapServer'] = "ImapServer"
    icm.ex_gCmndMenuItem(cmndName, cps, cmndArgs, verbosity='none',
                         comment='none', icmWrapper="echo", icmName=None)
    
    icm.cmndExampleMenuSection('*inMail /ControllerInfo/ ParsSet -- /defaulMailAcct={}/ --*'.format(
        enabledInMailAcctObtain(curGet_bxoId(), curGet_sr()))
    )
    cmndName = "inMailAcctControllerInfoParsSet" ; cmndArgs = "" 
    cps=cpsInit() ; cmndParsCurBxoSr(cps)
    cps['firstName'] = "FirstName" ; cps['lastName'] = "LastName"
    icm.ex_gCmndMenuItem(cmndName, cps, cmndArgs, verbosity='none',
                         comment='none', icmWrapper="echo", icmName=None)
    
    icm.cmndExampleMenuSection('*inMail /Retrieval/ ParsSet -- /defaulMailAcct={}/ --*'.format(
        enabledInMailAcctObtain(curGet_bxoId(), curGet_sr()))
    )
    cmndName = "inMailAcctRetrievalParsSet" ; cmndArgs = "" 
    cps=cpsInit() ; cmndParsCurBxoSr(cps)
    cps['inMailAcctMboxesPath'] = "MaildirPath"; cps['mboxesList'] = ""; cps['ssl'] = "on"
    icm.ex_gCmndMenuItem(cmndName, cps, cmndArgs, verbosity='none',
                         comment='none', icmWrapper="echo", icmName=None)

    cmndName = "inMailAcctRetrievalParsSet" ; cmndArgs = "" 
    cps=cpsInit() ; cmndParsCurBxoSr(cps)
    mailDirPath = getPathForAcctMaildir(
        enabledControlProfileObtain(
            curGet_bxoId(),
            curGet_sr()
        ),
        enabledInMailAcctObtain(
            curGet_bxoId(),
            curGet_sr()
        ),
        bxoId=curGet_bxoId(),
        sr=curGet_sr(),
    )
    cps['inMailAcctMboxesPath'] = mailDirPath
    icm.ex_gCmndMenuItem(cmndName, cps, cmndArgs, verbosity='none',
                         comment='none', icmWrapper="", icmName=None)

    cmndName = "inMailAcctRetrievalParsSet" ; cmndArgs = "" 
    cps=cpsInit() ; cmndParsCurBxoSr(cps)
    cps['mboxesList'] = "Inbox"; cps['ssl'] = "on"
    icm.ex_gCmndMenuItem(cmndName, cps, cmndArgs, verbosity='none',
                         comment='none', icmWrapper="echo", icmName=None)
    
    
####+BEGIN: bx:icm:python:func :funcName "examples_outMailAcctAccessPars" :funcType "anyOrNone" :retType "bool" :deco "" :argsList ""
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func-anyOrNone :: /examples_outMailAcctAccessPars/ retType=bool argsList=nil  [[elisp:(org-cycle)][| ]]
"""
def examples_outMailAcctAccessPars():
####+END:
    """.
"""
    def cpsInit(): return collections.OrderedDict()
    def menuItem(verbosity): icm.ex_gCmndMenuItem(cmndName, cps, cmndArgs, verbosity=verbosity) # 'little' or 'none'
    def execLineEx(cmndStr): icm.ex_gExecMenuItem(execLine=cmndStr)

    icm.cmndExampleMenuChapter('* =FP Values=  outMail Controls -- /{controlProfile}+{mailAcct}/ --*'.format(
        controlProfile=enabledControlProfileObtain(curGet_bxoId(), curGet_sr()),
        mailAcct=enabledOutMailAcctObtain(curGet_bxoId(), curGet_sr()))
    )
    cmndName = "outMailAcctParsGet" ; cmndArgs = "" ; cps = collections.OrderedDict()
    cmndParsCurBxoSr(cps)
    icm.ex_gCmndMenuItem(cmndName, cps, cmndArgs, verbosity='none')

    menuLine = """"""
    icm.cmndExampleMenuItem(menuLine, icmName="marmeAcctsManage.py", verbosity='none')    

    
####+BEGIN: bx:icm:python:func :funcName "examples_outMailAcctAccessParsFull" :funcType "anyOrNone" :retType "bool" :deco "" :argsList ""
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func-anyOrNone :: /examples_outMailAcctAccessParsFull/ retType=bool argsList=nil  [[elisp:(org-cycle)][| ]]
"""
def examples_outMailAcctAccessParsFull():
####+END:
    """.
"""
    def cpsInit(): return collections.OrderedDict()
    def menuItem(verbosity): icm.ex_gCmndMenuItem(cmndName, cps, cmndArgs, verbosity=verbosity) # 'little' or 'none'
    def execLineEx(cmndStr): icm.ex_gExecMenuItem(execLine=cmndStr)

    icm.cmndExampleMenuChapter('* =FP Values=  outMail Controls -- /{controlProfile}+{mailAcct}/ --*'.format(
        controlProfile=enabledControlProfileObtain(curGet_bxoId(), curGet_sr()),
        mailAcct=enabledOutMailAcctObtain(curGet_bxoId(), curGet_sr()))
    )
    cmndName = "outMailAcctParsGet" ; cmndArgs = "" ; cps = collections.OrderedDict()
    cmndParsCurBxoSr(cps)
    icm.ex_gCmndMenuItem(cmndName, cps, cmndArgs, verbosity='none')

    icm.cmndExampleMenuSection('*outMail /Access/ ParsSet -- /enabledMailAcct={controlProfile}+{mailAcct}/ --*'.format(
        controlProfile=enabledControlProfileObtain(curGet_bxoId(), curGet_sr()),
        mailAcct=enabledOutMailAcctObtain(curGet_bxoId(), curGet_sr()))
    )

    cmndName = "outMailAcctParsSet" ; cmndArgs = "access" ; cps = collections.OrderedDict()
    cmndParsCurBxoSr(cps)
    cps['userName']="TBS" ; cps['userPasswd']="TBS" ; cps['mtaRemHost']="TBS" ; cps['mtaRemProtocol']="smtp_ssl/smtp_tls/smtp"     
    icm.ex_gCmndMenuItem(cmndName, cps, cmndArgs, icmWrapper="echo", verbosity='none')

    icm.cmndExampleMenuSection('*outMail /ControllerInfo/ ParsSet -- /enabledMailAcct={controlProfile}+{mailAcct}/ --*'.format(
        controlProfile=enabledControlProfileObtain(curGet_bxoId(), curGet_sr()),
        mailAcct=enabledOutMailAcctObtain(curGet_bxoId(), curGet_sr()))
    )

    cmndName = "outMailAcctParsSet" ; cmndArgs = "controllerInfo" ; cps = collections.OrderedDict()
    cmndParsCurBxoSr(cps)    
    cps['firstName']="TBS" ; cps['lastName']="TBS"
    icm.ex_gCmndMenuItem(cmndName, cps, cmndArgs, icmWrapper="echo", verbosity='none')

    icm.cmndExampleMenuSection('*outMail /Submission/ ParsSet -- /enabledMailAcct={controlProfile}+{mailAcct}/ --*'.format(
        controlProfile=enabledControlProfileObtain(curGet_bxoId(), curGet_sr()),
        mailAcct=enabledOutMailAcctObtain(curGet_bxoId(), curGet_sr()))
    )

    cmndName = "outMailAcctParsSet" ; cmndArgs = "submission" ; cps = collections.OrderedDict()
    cmndParsCurBxoSr(cps)    
    cps['sendingMethod']="inject/submit" ; cps['envelopeAddr']="TBS"
    icm.ex_gCmndMenuItem(cmndName, cps, cmndArgs, icmWrapper="echo", verbosity='none')

    

"""
*  [[elisp:(beginning-of-buffer)][Top]] ################ [[elisp:(delete-other-windows)][(1)]]      *File Parameters Get/Set -- Commands*
"""

####+BEGIN: bx:icm:python:func :funcName "FP_readTreeAtBaseDir_CmndOutput" :funcType "anyOrNone" :retType "bool" :deco "" :argsList "interactive fpBaseDir cmndOutcome"
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func-anyOrNone :: /FP_readTreeAtBaseDir_CmndOutput/ retType=bool argsList=(interactive fpBaseDir cmndOutcome)  [[elisp:(org-cycle)][| ]]
"""
def FP_readTreeAtBaseDir_CmndOutput(
    interactive,
    fpBaseDir,
    cmndOutcome,
):
####+END:
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



####+BEGIN: bx:icm:python:cmnd:classHead :cmndName "bxoSrPkgInfoParsGet" :comment "" :parsMand "bxoId sr" :parsOpt "" :argsMin "0" :argsMax "0" :asFunc "" :interactiveP ""
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || ICM-Cmnd       :: /bxoSrPkgInfoParsGet/ parsMand=bxoId sr parsOpt= argsMin=0 argsMax=0 asFunc= interactive=  [[elisp:(org-cycle)][| ]]
"""
class bxoSrPkgInfoParsGet(icm.Cmnd):
    cmndParamsMandatory = [ 'bxoId', 'sr', ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 0, 'Max': 0,}

    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
        interactive=False,        # Can also be called non-interactively
        bxoId=None,         # or Cmnd-Input
        sr=None,         # or Cmnd-Input
    ):
        cmndOutcome = self.getOpOutcome()
        if interactive:
            if not self.cmndLineValidate(outcome=cmndOutcome):
                return cmndOutcome

        callParamsDict = {'bxoId': bxoId, 'sr': sr, }
        if not icm.cmndCallParamsValidate(callParamsDict, interactive, outcome=cmndOutcome):
            return cmndOutcome
        bxoId = callParamsDict['bxoId']
        sr = callParamsDict['sr']

####+END:
 
        if interactive:
            icm.ANN_write("controlBaseDir={}".format(
                controlBaseDirGet(bxoId=bxoId, sr=sr)
            ))
            icm.ANN_write("varBaseDir={}".format(
                varBaseDirGet(bxoId=bxoId, sr=sr)
            ))
            icm.ANN_write("configBaseDir={}".format(
                configBaseDirGet(bxoId=bxoId, sr=sr)
            ))
            icm.ANN_write("tmpBaseDir={}".format(
                tmpBaseDirGet(bxoId=bxoId, sr=sr)
            ))
            icm.ANN_write("logBaseDir={}".format(
                logBaseDirGet(bxoId=bxoId, sr=sr)
            ))


        return cmndOutcome.set(
            opError=icm.OpError.Success,
            opResults=None,
        )



####+BEGIN: bx:icm:python:cmnd:classHead :cmndName "enabledControlProfileGet" :comment "" :parsMand "" :parsOpt "bxoId sr" :argsMin "0" :argsMax "0" :asFunc "" :interactiveP ""
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || ICM-Cmnd       :: /enabledControlProfileGet/ parsMand= parsOpt=bxoId sr argsMin=0 argsMax=0 asFunc= interactive=  [[elisp:(org-cycle)][| ]]
"""
class enabledControlProfileGet(icm.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ 'bxoId', 'sr', ]
    cmndArgsLen = {'Min': 0, 'Max': 0,}

    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
        interactive=False,        # Can also be called non-interactively
        bxoId=None,         # or Cmnd-Input
        sr=None,         # or Cmnd-Input
    ):
        cmndOutcome = self.getOpOutcome()
        if interactive:
            if not self.cmndLineValidate(outcome=cmndOutcome):
                return cmndOutcome

        callParamsDict = {'bxoId': bxoId, 'sr': sr, }
        if not icm.cmndCallParamsValidate(callParamsDict, interactive, outcome=cmndOutcome):
            return cmndOutcome
        bxoId = callParamsDict['bxoId']
        sr = callParamsDict['sr']

####+END:
    
        enabledMailAcct = enabledControlProfileObtain(bxoId=bxoId, sr=sr,)
 
        if interactive:
            icm.ANN_write(enabledMailAcct)

        return cmndOutcome.set(
            opError=icm.OpError.Success,
            opResults=enabledMailAcct,
        )


####+BEGIN: bx:icm:python:method :methodName "cmndDocStr" :methodType "anyOrNone" :retType "bool" :deco "default" :argsList ""
    """
**  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Method-anyOrNone :: /cmndDocStr/ retType=bool argsList=nil deco=default  [[elisp:(org-cycle)][| ]]
"""
    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmndDocStr(self):
####+END:        
        return """
***** TODO [[elisp:(org-cycle)][| *CmndDesc:* | ]]  Output the current from -- NOTYET -- Should write at {varBase}/selections/fp
"""

####+BEGIN: bx:icm:python:cmnd:classHead :cmndName "enabledControlProfileSet" :comment "" :parsMand "" :parsOpt "bxoId sr" :argsMin "1" :argsMax "1" :asFunc "" :interactiveP ""
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || ICM-Cmnd       :: /enabledControlProfileSet/ parsMand= parsOpt=bxoId sr argsMin=1 argsMax=1 asFunc= interactive=  [[elisp:(org-cycle)][| ]]
"""
class enabledControlProfileSet(icm.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ 'bxoId', 'sr', ]
    cmndArgsLen = {'Min': 1, 'Max': 1,}

    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
        interactive=False,        # Can also be called non-interactively
        bxoId=None,         # or Cmnd-Input
        sr=None,         # or Cmnd-Input
        argsList=[],         # or Args-Input
    ):
        cmndOutcome = self.getOpOutcome()
        if interactive:
            if not self.cmndLineValidate(outcome=cmndOutcome):
                return cmndOutcome
            effectiveArgsList = G.icmRunArgsGet().cmndArgs
        else:
            effectiveArgsList = argsList

        callParamsDict = {'bxoId': bxoId, 'sr': sr, }
        if not icm.cmndCallParamsValidate(callParamsDict, interactive, outcome=cmndOutcome):
            return cmndOutcome
        bxoId = callParamsDict['bxoId']
        sr = callParamsDict['sr']

        cmndArgsSpecDict = self.cmndArgsSpec()
        if not self.cmndArgsValidate(effectiveArgsList, cmndArgsSpecDict, outcome=cmndOutcome):
            return cmndOutcome
####+END:

        icmRunArgs = G.icmRunArgsGet()
        for each in icmRunArgs.cmndArgs:
            icm.FILE_ParamWriteToPath(
                parNameFullPath=os.path.join(
                    controlBaseDirGet(bxoId=bxoId, sr=sr,),   # NOTYET
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


####+BEGIN: bx:icm:python:method :methodName "cmndDocStr" :methodType "anyOrNone" :retType "bool" :deco "default" :argsList ""
    """
**  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Method-anyOrNone :: /cmndDocStr/ retType=bool argsList=nil deco=default  [[elisp:(org-cycle)][| ]]
"""
    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmndDocStr(self):
####+END:        
        return """
***** TODO [[elisp:(org-cycle)][| *CmndDesc:* | ]]  Write as a FP the enabledControlProfile.
"""
    
####+BEGIN: bx:icm:python:cmnd:classHead :cmndName "enabledInMailAcctGet" :comment "" :parsMand "" :parsOpt "bxoId sr" :argsMin "0" :argsMax "0" :asFunc "" :interactiveP ""
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || ICM-Cmnd       :: /enabledInMailAcctGet/ parsMand= parsOpt=bxoId sr argsMin=0 argsMax=0 asFunc= interactive=  [[elisp:(org-cycle)][| ]]
"""
class enabledInMailAcctGet(icm.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ 'bxoId', 'sr', ]
    cmndArgsLen = {'Min': 0, 'Max': 0,}

    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
        interactive=False,        # Can also be called non-interactively
        bxoId=None,         # or Cmnd-Input
        sr=None,         # or Cmnd-Input
    ):
        cmndOutcome = self.getOpOutcome()
        if interactive:
            if not self.cmndLineValidate(outcome=cmndOutcome):
                return cmndOutcome

        callParamsDict = {'bxoId': bxoId, 'sr': sr, }
        if not icm.cmndCallParamsValidate(callParamsDict, interactive, outcome=cmndOutcome):
            return cmndOutcome
        bxoId = callParamsDict['bxoId']
        sr = callParamsDict['sr']

####+END:
    
        enabledInMailAcct = enabledInMailAcctObtain(bxoId=bxoId, sr=sr,)  # NOTYET
 
        if interactive:
            icm.ANN_write(enabledInMailAcct)

        return cmndOutcome.set(
            opError=icm.OpError.Success,
            opResults=enabledInMailAcct,
        )


####+BEGIN: bx:icm:python:cmnd:classHead :cmndName "enabledInMailAcctSet" :comment "" :parsMand "" :parsOpt "bxoId sr" :argsMin "1" :argsMax "1" :asFunc "" :interactiveP ""
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || ICM-Cmnd       :: /enabledInMailAcctSet/ parsMand= parsOpt=bxoId sr argsMin=1 argsMax=1 asFunc= interactive=  [[elisp:(org-cycle)][| ]]
"""
class enabledInMailAcctSet(icm.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ 'bxoId', 'sr', ]
    cmndArgsLen = {'Min': 1, 'Max': 1,}

    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
        interactive=False,        # Can also be called non-interactively
        bxoId=None,         # or Cmnd-Input
        sr=None,         # or Cmnd-Input
        argsList=[],         # or Args-Input
    ):
        cmndOutcome = self.getOpOutcome()
        if interactive:
            if not self.cmndLineValidate(outcome=cmndOutcome):
                return cmndOutcome
            effectiveArgsList = G.icmRunArgsGet().cmndArgs
        else:
            effectiveArgsList = argsList

        callParamsDict = {'bxoId': bxoId, 'sr': sr, }
        if not icm.cmndCallParamsValidate(callParamsDict, interactive, outcome=cmndOutcome):
            return cmndOutcome
        bxoId = callParamsDict['bxoId']
        sr = callParamsDict['sr']

        cmndArgsSpecDict = self.cmndArgsSpec()
        if not self.cmndArgsValidate(effectiveArgsList, cmndArgsSpecDict, outcome=cmndOutcome):
            return cmndOutcome
####+END:
        """
** Write as a FP  the enabledMailAcct.
"""

        icmRunArgs = G.icmRunArgsGet()
        for each in icmRunArgs.cmndArgs:
            icm.FILE_ParamWriteToPath(
                parNameFullPath=os.path.join(
                    controlBaseDirGet(bxoId=bxoId, sr=sr,),   # NOTYET
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


####+BEGIN: bx:icm:python:cmnd:classHead :cmndName "enabledOutMailAcctGet" :comment "" :parsMand "" :parsOpt "bxoId sr" :argsMin "0" :argsMax "0" :asFunc "" :interactiveP ""
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || ICM-Cmnd       :: /enabledOutMailAcctGet/ parsMand= parsOpt=bxoId sr argsMin=0 argsMax=0 asFunc= interactive=  [[elisp:(org-cycle)][| ]]
"""
class enabledOutMailAcctGet(icm.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ 'bxoId', 'sr', ]
    cmndArgsLen = {'Min': 0, 'Max': 0,}

    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
        interactive=False,        # Can also be called non-interactively
        bxoId=None,         # or Cmnd-Input
        sr=None,         # or Cmnd-Input
    ):
        cmndOutcome = self.getOpOutcome()
        if interactive:
            if not self.cmndLineValidate(outcome=cmndOutcome):
                return cmndOutcome

        callParamsDict = {'bxoId': bxoId, 'sr': sr, }
        if not icm.cmndCallParamsValidate(callParamsDict, interactive, outcome=cmndOutcome):
            return cmndOutcome
        bxoId = callParamsDict['bxoId']
        sr = callParamsDict['sr']

####+END:
        """
** Output the current enabledMailAcct
    """
    
        enabledOutMailAcct = enabledOutMailAcctObtain(bxoId=bxoId, sr=sr,)  # NOTYET
 
        if interactive:
            icm.ANN_write(enabledOutMailAcct)

        return cmndOutcome.set(
            opError=icm.OpError.Success,
            opResults=enabledOutMailAcct,
        )



####+BEGIN: bx:icm:python:cmnd:classHead :cmndName "enabledOutMailAcctSet" :comment "" :parsMand "" :parsOpt "bxoId sr" :argsMin "1" :argsMax "1" :asFunc "" :interactiveP ""
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || ICM-Cmnd       :: /enabledOutMailAcctSet/ parsMand= parsOpt=bxoId sr argsMin=1 argsMax=1 asFunc= interactive=  [[elisp:(org-cycle)][| ]]
"""
class enabledOutMailAcctSet(icm.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ 'bxoId', 'sr', ]
    cmndArgsLen = {'Min': 1, 'Max': 1,}

    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
        interactive=False,        # Can also be called non-interactively
        bxoId=None,         # or Cmnd-Input
        sr=None,         # or Cmnd-Input
        argsList=[],         # or Args-Input
    ):
        cmndOutcome = self.getOpOutcome()
        if interactive:
            if not self.cmndLineValidate(outcome=cmndOutcome):
                return cmndOutcome
            effectiveArgsList = G.icmRunArgsGet().cmndArgs
        else:
            effectiveArgsList = argsList

        callParamsDict = {'bxoId': bxoId, 'sr': sr, }
        if not icm.cmndCallParamsValidate(callParamsDict, interactive, outcome=cmndOutcome):
            return cmndOutcome
        bxoId = callParamsDict['bxoId']
        sr = callParamsDict['sr']

        cmndArgsSpecDict = self.cmndArgsSpec()
        if not self.cmndArgsValidate(effectiveArgsList, cmndArgsSpecDict, outcome=cmndOutcome):
            return cmndOutcome
####+END:
        """
** Write as a FP  the enabledMailAcct.
"""

        icmRunArgs = G.icmRunArgsGet()
        for each in icmRunArgs.cmndArgs:
            icm.FILE_ParamWriteToPath(
                parNameFullPath=os.path.join(
                    controlBaseDirGet(bxoId=bxoId, sr=sr,),  # NOTYET
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



####+BEGIN: bx:icm:python:cmnd:classHead :cmndName "enabledMailBoxGet" :comment "" :parsMand "" :parsOpt "bxoId sr" :argsMin "0" :argsMax "0" :asFunc "" :interactiveP ""
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || ICM-Cmnd       :: /enabledMailBoxGet/ parsMand= parsOpt=bxoId sr argsMin=0 argsMax=0 asFunc= interactive=  [[elisp:(org-cycle)][| ]]
"""
class enabledMailBoxGet(icm.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ 'bxoId', 'sr', ]
    cmndArgsLen = {'Min': 0, 'Max': 0,}

    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
        interactive=False,        # Can also be called non-interactively
        bxoId=None,         # or Cmnd-Input
        sr=None,         # or Cmnd-Input
    ):
        cmndOutcome = self.getOpOutcome()
        if interactive:
            if not self.cmndLineValidate(outcome=cmndOutcome):
                return cmndOutcome

        callParamsDict = {'bxoId': bxoId, 'sr': sr, }
        if not icm.cmndCallParamsValidate(callParamsDict, interactive, outcome=cmndOutcome):
            return cmndOutcome
        bxoId = callParamsDict['bxoId']
        sr = callParamsDict['sr']

####+END:
        """
** Output the current enabledMailBox
    """
    
        enabledMailBox = enabledMailBoxObtain(bxoId=bxoId, sr=sr,)
 
        if interactive:
            icm.ANN_write(enabledMailBox)

        return cmndOutcome.set(
            opError=icm.OpError.Success,
            opResults=enabledMailBox,
        )
    

####+BEGIN: bx:icm:python:cmnd:classHead :cmndName "enabledMailBoxSet" :comment "" :parsMand "" :parsOpt "bxoId sr" :argsMin "1" :argsMax "1" :asFunc "" :interactiveP ""
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || ICM-Cmnd       :: /enabledMailBoxSet/ parsMand= parsOpt=bxoId sr argsMin=1 argsMax=1 asFunc= interactive=  [[elisp:(org-cycle)][| ]]
"""
class enabledMailBoxSet(icm.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ 'bxoId', 'sr', ]
    cmndArgsLen = {'Min': 1, 'Max': 1,}

    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
        interactive=False,        # Can also be called non-interactively
        bxoId=None,         # or Cmnd-Input
        sr=None,         # or Cmnd-Input
        argsList=[],         # or Args-Input
    ):
        cmndOutcome = self.getOpOutcome()
        if interactive:
            if not self.cmndLineValidate(outcome=cmndOutcome):
                return cmndOutcome
            effectiveArgsList = G.icmRunArgsGet().cmndArgs
        else:
            effectiveArgsList = argsList

        callParamsDict = {'bxoId': bxoId, 'sr': sr, }
        if not icm.cmndCallParamsValidate(callParamsDict, interactive, outcome=cmndOutcome):
            return cmndOutcome
        bxoId = callParamsDict['bxoId']
        sr = callParamsDict['sr']

        cmndArgsSpecDict = self.cmndArgsSpec()
        if not self.cmndArgsValidate(effectiveArgsList, cmndArgsSpecDict, outcome=cmndOutcome):
            return cmndOutcome
####+END:
        """
** Write as a FP  the enabledMailBox.
"""

        icmRunArgs = G.icmRunArgsGet()
        for each in icmRunArgs.cmndArgs:
            icm.FILE_ParamWriteToPath(
                parNameFullPath=os.path.join(
                    controlBaseDirGet(bxoId=bxoId, sr=sr,),  # NOTYET
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
    
####+BEGIN: bx:icm:python:cmnd:classHead :cmndName "inMailAcctParsGet" :comment "" :parsMand "" :parsOpt "bxoId sr controlProfile inMailAcct" :argsMin "0" :argsMax "3" :asFunc "" :interactiveP ""
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || ICM-Cmnd       :: /inMailAcctParsGet/ parsMand= parsOpt=bxoId sr controlProfile inMailAcct argsMin=0 argsMax=3 asFunc= interactive=  [[elisp:(org-cycle)][| ]]
"""
class inMailAcctParsGet(icm.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ 'bxoId', 'sr', 'controlProfile', 'inMailAcct', ]
    cmndArgsLen = {'Min': 0, 'Max': 3,}

    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
        interactive=False,        # Can also be called non-interactively
        bxoId=None,         # or Cmnd-Input
        sr=None,         # or Cmnd-Input
        controlProfile=None,         # or Cmnd-Input
        inMailAcct=None,         # or Cmnd-Input
        argsList=[],         # or Args-Input
    ):
        cmndOutcome = self.getOpOutcome()
        if interactive:
            if not self.cmndLineValidate(outcome=cmndOutcome):
                return cmndOutcome
            effectiveArgsList = G.icmRunArgsGet().cmndArgs
        else:
            effectiveArgsList = argsList

        callParamsDict = {'bxoId': bxoId, 'sr': sr, 'controlProfile': controlProfile, 'inMailAcct': inMailAcct, }
        if not icm.cmndCallParamsValidate(callParamsDict, interactive, outcome=cmndOutcome):
            return cmndOutcome
        bxoId = callParamsDict['bxoId']
        sr = callParamsDict['sr']
        controlProfile = callParamsDict['controlProfile']
        inMailAcct = callParamsDict['inMailAcct']

        cmndArgsSpecDict = self.cmndArgsSpec()
        if not self.cmndArgsValidate(effectiveArgsList, cmndArgsSpecDict, outcome=cmndOutcome):
            return cmndOutcome
####+END:
        parTypes = self.cmndArgsGet("0&2", cmndArgsSpecDict, effectiveArgsList)
        
        if parTypes:
            if parTypes[0] == "all":
                    cmndArgsSpec = cmndArgsSpecDict.argPositionFind("0&2")
                    argChoices = cmndArgsSpec.argChoicesGet()
                    argChoices.pop(0)
                    parTypes = argChoices

        for each in parTypes:
            fpBaseDir = os.path.join(
                inMailAcctDirGet(controlProfile, inMailAcct, bxoId=bxoId, sr=sr,),
                each,
            )
            icm.LOG_here(
                "controlProfile={controlProfile} -- inMailAcct={inMailAcct} -- fpBaseDir={fpBaseDir}".format(
                    controlProfile=controlProfile, inMailAcct=inMailAcct, fpBaseDir=fpBaseDir,)
            )
            FP_readTreeAtBaseDir_CmndOutput(
                interactive=interactive,
                fpBaseDir=fpBaseDir,
                cmndOutcome=cmndOutcome,
            )

        return cmndOutcome

####+BEGIN: bx:icm:python:method :methodName "cmndArgsSpec" :methodType "anyOrNone" :retType "bool" :deco "default" :argsList ""
    """
**  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Method-anyOrNone :: /cmndArgsSpec/ retType=bool argsList=nil deco=default  [[elisp:(org-cycle)][| ]]
"""
    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmndArgsSpec(self):
####+END:        
        """
***** Cmnd Args Specification
"""
        cmndArgsSpecDict = icm.CmndArgsSpecDict()
        cmndArgsSpecDict.argsDictAdd(
            argPosition="0&2",
            argName="parTypes",
            argDefault="all",	    	    
            argChoices=['all', 'access', 'controllerInfo', 'retrieval'],
            argDescription="Action to be specified by rest"
        )

        return cmndArgsSpecDict
    

####+BEGIN: bx:icm:python:cmnd:classHead :cmndName "inMailAcctAccessParsSet" :comment "" :parsMand "" :parsOpt "bxoId sr controlProfile inMailAcct userName userPasswd imapServer" :argsMin "0" :argsMax "0" :asFunc "" :interactiveP ""
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || ICM-Cmnd       :: /inMailAcctAccessParsSet/ parsMand= parsOpt=bxoId sr controlProfile inMailAcct userName userPasswd imapServer argsMin=0 argsMax=0 asFunc= interactive=  [[elisp:(org-cycle)][| ]]
"""
class inMailAcctAccessParsSet(icm.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ 'bxoId', 'sr', 'controlProfile', 'inMailAcct', 'userName', 'userPasswd', 'imapServer', ]
    cmndArgsLen = {'Min': 0, 'Max': 0,}

    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
        interactive=False,        # Can also be called non-interactively
        bxoId=None,         # or Cmnd-Input
        sr=None,         # or Cmnd-Input
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

        callParamsDict = {'bxoId': bxoId, 'sr': sr, 'controlProfile': controlProfile, 'inMailAcct': inMailAcct, 'userName': userName, 'userPasswd': userPasswd, 'imapServer': imapServer, }
        if not icm.cmndCallParamsValidate(callParamsDict, interactive, outcome=cmndOutcome):
            return cmndOutcome
        bxoId = callParamsDict['bxoId']
        sr = callParamsDict['sr']
        controlProfile = callParamsDict['controlProfile']
        inMailAcct = callParamsDict['inMailAcct']
        userName = callParamsDict['userName']
        userPasswd = callParamsDict['userPasswd']
        imapServer = callParamsDict['imapServer']

####+END:

        inMailAcctDir = os.path.join(
            inMailAcctDirGet(inMailAcct, bxoId=bxoId, sr=sr,),
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


####+BEGIN: bx:icm:python:cmnd:classHead :cmndName "inMailAcctControllerInfoParsSet" :comment "" :parsMand "" :parsOpt "bxoId sr controlProfile inMailAcct firstName lastName" :argsMin "0" :argsMax "0" :asFunc "" :interactiveP ""
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || ICM-Cmnd       :: /inMailAcctControllerInfoParsSet/ parsMand= parsOpt=bxoId sr controlProfile inMailAcct firstName lastName argsMin=0 argsMax=0 asFunc= interactive=  [[elisp:(org-cycle)][| ]]
"""
class inMailAcctControllerInfoParsSet(icm.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ 'bxoId', 'sr', 'controlProfile', 'inMailAcct', 'firstName', 'lastName', ]
    cmndArgsLen = {'Min': 0, 'Max': 0,}

    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
        interactive=False,        # Can also be called non-interactively
        bxoId=None,         # or Cmnd-Input
        sr=None,         # or Cmnd-Input
        controlProfile=None,         # or Cmnd-Input
        inMailAcct=None,         # or Cmnd-Input
        firstName=None,         # or Cmnd-Input
        lastName=None,         # or Cmnd-Input
    ):
        cmndOutcome = self.getOpOutcome()
        if interactive:
            if not self.cmndLineValidate(outcome=cmndOutcome):
                return cmndOutcome

        callParamsDict = {'bxoId': bxoId, 'sr': sr, 'controlProfile': controlProfile, 'inMailAcct': inMailAcct, 'firstName': firstName, 'lastName': lastName, }
        if not icm.cmndCallParamsValidate(callParamsDict, interactive, outcome=cmndOutcome):
            return cmndOutcome
        bxoId = callParamsDict['bxoId']
        sr = callParamsDict['sr']
        controlProfile = callParamsDict['controlProfile']
        inMailAcct = callParamsDict['inMailAcct']
        firstName = callParamsDict['firstName']
        lastName = callParamsDict['lastName']

####+END:

        inMailAcctDir = os.path.join(
            inMailAcctDirGet(inMailAcct, bxoId=bxoId, sr=sr,),
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

####+BEGIN: bx:icm:python:cmnd:classHead :cmndName "inMailAcctRetrievalParsSet" :comment "" :parsMand "" :parsOpt "bxoId sr controlProfile inMailAcct inMailAcctMboxesPath mboxesList ssl" :argsMin "0" :argsMax "0" :asFunc "" :interactiveP ""
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || ICM-Cmnd       :: /inMailAcctRetrievalParsSet/ parsMand= parsOpt=bxoId sr controlProfile inMailAcct inMailAcctMboxesPath mboxesList ssl argsMin=0 argsMax=0 asFunc= interactive=  [[elisp:(org-cycle)][| ]]
"""
class inMailAcctRetrievalParsSet(icm.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ 'bxoId', 'sr', 'controlProfile', 'inMailAcct', 'inMailAcctMboxesPath', 'mboxesList', 'ssl', ]
    cmndArgsLen = {'Min': 0, 'Max': 0,}

    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
        interactive=False,        # Can also be called non-interactively
        bxoId=None,         # or Cmnd-Input
        sr=None,         # or Cmnd-Input
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

        callParamsDict = {'bxoId': bxoId, 'sr': sr, 'controlProfile': controlProfile, 'inMailAcct': inMailAcct, 'inMailAcctMboxesPath': inMailAcctMboxesPath, 'mboxesList': mboxesList, 'ssl': ssl, }
        if not icm.cmndCallParamsValidate(callParamsDict, interactive, outcome=cmndOutcome):
            return cmndOutcome
        bxoId = callParamsDict['bxoId']
        sr = callParamsDict['sr']
        controlProfile = callParamsDict['controlProfile']
        inMailAcct = callParamsDict['inMailAcct']
        inMailAcctMboxesPath = callParamsDict['inMailAcctMboxesPath']
        mboxesList = callParamsDict['mboxesList']
        ssl = callParamsDict['ssl']

####+END:

        inMailAcctDir = os.path.join(
            inMailAcctDirGet(controlProfile, inMailAcct, bxoId=bxoId, sr=sr,),
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


####+BEGIN: bx:icm:python:cmnd:classHead :cmndName "outMailAcctParsGet" :comment "" :parsMand "" :parsOpt "bxoId sr controlProfile outMailAcct" :argsMin "0" :argsMax "3" :asFunc "" :interactiveP ""
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || ICM-Cmnd       :: /outMailAcctParsGet/ parsMand= parsOpt=bxoId sr controlProfile outMailAcct argsMin=0 argsMax=3 asFunc= interactive=  [[elisp:(org-cycle)][| ]]
"""
class outMailAcctParsGet(icm.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ 'bxoId', 'sr', 'controlProfile', 'outMailAcct', ]
    cmndArgsLen = {'Min': 0, 'Max': 3,}

    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
        interactive=False,        # Can also be called non-interactively
        bxoId=None,         # or Cmnd-Input
        sr=None,         # or Cmnd-Input
        controlProfile=None,         # or Cmnd-Input
        outMailAcct=None,         # or Cmnd-Input
        argsList=[],         # or Args-Input
    ):
        cmndOutcome = self.getOpOutcome()
        if interactive:
            if not self.cmndLineValidate(outcome=cmndOutcome):
                return cmndOutcome
            effectiveArgsList = G.icmRunArgsGet().cmndArgs
        else:
            effectiveArgsList = argsList

        callParamsDict = {'bxoId': bxoId, 'sr': sr, 'controlProfile': controlProfile, 'outMailAcct': outMailAcct, }
        if not icm.cmndCallParamsValidate(callParamsDict, interactive, outcome=cmndOutcome):
            return cmndOutcome
        bxoId = callParamsDict['bxoId']
        sr = callParamsDict['sr']
        controlProfile = callParamsDict['controlProfile']
        outMailAcct = callParamsDict['outMailAcct']

        cmndArgsSpecDict = self.cmndArgsSpec()
        if not self.cmndArgsValidate(effectiveArgsList, cmndArgsSpecDict, outcome=cmndOutcome):
            return cmndOutcome
####+END:
        parTypes = self.cmndArgsGet("0&2", cmndArgsSpecDict, effectiveArgsList)
        
        if parTypes:
            if parTypes[0] == "all":
                    cmndArgsSpec = cmndArgsSpecDict.argPositionFind("0&2")
                    argChoices = cmndArgsSpec.argChoicesGet()
                    argChoices.pop(0)
                    parTypes = argChoices

        for each in parTypes:
            fpBaseDir = os.path.join(
                outMailAcctDirGet(controlProfile, outMailAcct, bxoId=bxoId, sr=sr,),
                each,
            )
            icm.LOG_here(
                "controlProfile={controlProfile} -- outMailAcct={outMailAcct} -- fpBaseDir={fpBaseDir}".format(
                    controlProfile=controlProfile, outMailAcct=outMailAcct, fpBaseDir=fpBaseDir,)
            )
            FP_readTreeAtBaseDir_CmndOutput(
                interactive=interactive,
                fpBaseDir=fpBaseDir,
                cmndOutcome=cmndOutcome,
            )

        return cmndOutcome

####+BEGIN: bx:icm:python:method :methodName "cmndArgsSpec" :methodType "anyOrNone" :retType "bool" :deco "default" :argsList ""
    """
**  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Method-anyOrNone :: /cmndArgsSpec/ retType=bool argsList=nil deco=default  [[elisp:(org-cycle)][| ]]
"""
    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmndArgsSpec(self):
####+END:        
        """
***** Cmnd Args Specification
"""
        cmndArgsSpecDict = icm.CmndArgsSpecDict()
        cmndArgsSpecDict.argsDictAdd(
            argPosition="0&2",
            argName="parTypes",
            argDefault="all",	    	    
            argChoices=['all', 'access', 'controllerInfo', 'submission'],
            argDescription="Action to be specified by rest"
        )

        return cmndArgsSpecDict
    

####+BEGIN: bx:icm:python:cmnd:classHead :cmndName "outMailAcctParsSet" :comment "" :parsMand "" :parsOpt "bxoId sr controlProfile outMailAcct userName userPasswd mtaRemHost mtaRemProtocol firstName lastName sendingMethod envelopeAddr" :argsMin "1" :argsMax "1" :asFunc "" :interactiveP ""
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || ICM-Cmnd       :: /outMailAcctParsSet/ parsMand= parsOpt=bxoId sr controlProfile outMailAcct userName userPasswd mtaRemHost mtaRemProtocol firstName lastName sendingMethod envelopeAddr argsMin=1 argsMax=1 asFunc= interactive=  [[elisp:(org-cycle)][| ]]
"""
class outMailAcctParsSet(icm.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ 'bxoId', 'sr', 'controlProfile', 'outMailAcct', 'userName', 'userPasswd', 'mtaRemHost', 'mtaRemProtocol', 'firstName', 'lastName', 'sendingMethod', 'envelopeAddr', ]
    cmndArgsLen = {'Min': 1, 'Max': 1,}

    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
        interactive=False,        # Can also be called non-interactively
        bxoId=None,         # or Cmnd-Input
        sr=None,         # or Cmnd-Input
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
        argsList=[],         # or Args-Input
    ):
        cmndOutcome = self.getOpOutcome()
        if interactive:
            if not self.cmndLineValidate(outcome=cmndOutcome):
                return cmndOutcome
            effectiveArgsList = G.icmRunArgsGet().cmndArgs
        else:
            effectiveArgsList = argsList

        callParamsDict = {'bxoId': bxoId, 'sr': sr, 'controlProfile': controlProfile, 'outMailAcct': outMailAcct, 'userName': userName, 'userPasswd': userPasswd, 'mtaRemHost': mtaRemHost, 'mtaRemProtocol': mtaRemProtocol, 'firstName': firstName, 'lastName': lastName, 'sendingMethod': sendingMethod, 'envelopeAddr': envelopeAddr, }
        if not icm.cmndCallParamsValidate(callParamsDict, interactive, outcome=cmndOutcome):
            return cmndOutcome
        bxoId = callParamsDict['bxoId']
        sr = callParamsDict['sr']
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

        cmndArgsSpecDict = self.cmndArgsSpec()
        if not self.cmndArgsValidate(effectiveArgsList, cmndArgsSpecDict, outcome=cmndOutcome):
            return cmndOutcome
####+END:
        # cmndArgsSpec = {0: ['access', 'controllerInfo', 'submission']}

        # NOTYET
        parGroup = self.cmndArgsGet("0", cmndArgsSpecDict, effectiveArgsList)
        

        validParGroups = self.__class__.cmndArgsSpec[0]

        if not parGroup:
            parGroup = G.icmRunArgsGet().cmndArgs[0]

        if not parGroup in validParGroups:
            return icm.EH_problem_usageError("mis-match")

        outMailAcctDir = os.path.join(
            outMailAcctDirGet(controlProfile, outMailAcct, bxoId=bxoId, sr=sr,),
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

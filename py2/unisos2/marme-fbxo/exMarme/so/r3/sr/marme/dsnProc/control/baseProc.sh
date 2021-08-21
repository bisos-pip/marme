#!/bin/bash

IimBriefDescription="iimsProc.sh: A scattered IIM extensions based on seedIimsProc.sh"

ORIGIN="
* Revision And Libre-Halaal CopyLeft -- Part Of ByStar -- Best Used With Blee
"

####+BEGIN: bx:dblock:bash:top-of-file :vc "cvs" partof: "bystar" :copyleft "halaal+minimal"
typeset RcsId="$Id: baseProc.sh,v 1.1 2017-10-21 22:51:46 lsipusr Exp $"
# *CopyLeft*
#  This is a Halaal Poly-Existential. See http://www.freeprotocols.org

####+END:

__author__="
* Authors: Mohsen BANAN, http://mohsen.banan.1.byname.net/contact
"
####+BEGIN: bx:dblock:lsip:bash:seed-spec :types "seedIimsProc.sh"
SEED="
*  /[dblock]/ /Seed/ :: [[file:/opt/public/osmt/bin/seedIimsProc.sh]] | 
"
FILE="
*  /This File/ :: /de/bx/nne/dev-py/iimsPkgs/remoteMailActions/envelopeDsn/iimsProc.sh 
"
if [ "${loadFiles}" == "" ] ; then
    /opt/public/osmt/bin/seedIimsProc.sh -l $0 "$@" 
    exit $?
fi
####+END:

_CommentBegin_
####+BEGIN: bx:dblock:global:file-insert-cond :cond "./blee.el" :file "/libre/ByStar/InitialTemplates/software/plusOrg/dblock/inserts/topControls.org"
*  /Controls/ ::  [[elisp:(org-cycle)][| ]]  [[elisp:(show-all)][Show-All]]  [[elisp:(org-shifttab)][Overview]]  [[elisp:(progn (org-shifttab) (org-content))][Content]] | [[file:Panel.org][Panel]] | [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] | [[elisp:(bx:org:run-me)][Run]] | [[elisp:(bx:org:run-me-eml)][RunEml]] | [[elisp:(delete-other-windows)][(1)]] | [[elisp:(progn (save-buffer) (kill-buffer))][S&Q]]  [[elisp:(save-buffer)][Save]]  [[elisp:(kill-buffer)][Quit]] [[elisp:(org-cycle)][| ]]
** /Version Control/ ::  [[elisp:(call-interactively (quote cvs-update))][cvs-update]]  [[elisp:(vc-update)][vc-update]] | [[elisp:(bx:org:agenda:this-file-otherWin)][Agenda-List]]  [[elisp:(bx:org:todo:this-file-otherWin)][ToDo-List]] 

####+END:
_CommentEnd_

_CommentBegin_
*      ================
*  [[elisp:(beginning-of-buffer)][Top]] ################ [[elisp:(delete-other-windows)][(1)]] CONTENTS-LIST ################
*  [[elisp:(org-cycle)][| ]]  Info          :: *[Current-Info:]*  Status, Notes (Tasks/Todo Lists, etc.) [[elisp:(org-cycle)][| ]]
_CommentEnd_


_CommentBegin_
*  [[elisp:(beginning-of-buffer)][Top]] ################ [[elisp:(delete-other-windows)][(1)]]  *Seed Extensions*
_CommentEnd_


_CommentBegin_
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || IIF       ::  IIM Profile / Characteristic Definitions    [[elisp:(org-cycle)][| ]]
_CommentEnd_

# Types are defined as associative arrays in /opt/public/osmt/lib/visLib.sh

G_iimGroupingType=${IimGroupingType[pkged]}

G_myPanel=$(FN_prefix ${G_myName})-Panel.org

G_iimCmndParts="
${IimCmndParts[common]}
"


_CommentBegin_
*  [[elisp:(org-cycle)][| ]]  Examples      :: Examples Hook Post [[elisp:(org-cycle)][| ]]
_CommentEnd_


_CommentBegin_
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || IIF       ::  examplesHookPost    [[elisp:(org-cycle)][| ]]
_CommentEnd_

function examplesHookPost {
cat  << _EOF_
$( examplesSeperatorChapter "*Extentions* (examplesHookPost)" )
${G_myName} ${extraInfo} -i tarPrepsFull
${G_myName} ${extraInfo} -i icmsPkgTarUpdate
_EOF_
 return
}



_CommentBegin_
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || IIF       ::  vis_icmsPkgTarUpdate    [[elisp:(org-cycle)][| ]]
_CommentEnd_

function vis_controlExamplesUpdate {
    G_funcEntry
    function describeF {  G_funcEntryShow; cat  << _EOF_
_EOF_
    }
    EH_assert [[ $# -eq 0 ]]

    local icmsPkgBaseDir=$( FN_absolutePathGet .. )
    local icmsPkgName=$( cat _icmsPkgName )
    local icmsBxoBaseDir=$( FN_absolutePathGet ../../.. )  #

    local marmeControlBaseDir=$( FN_absolutePathGet ../../marme.control )

    local tarDestBaseDir="/lcnt/lgpc/bystar/permanent/facilities/marmee"

    opDo tarPkgManage.sh -h -v -n showRun -p inBase="${icmsPkgBaseDir}" -p outBase="marme" -p result="${tarDestBaseDir}/marme.tar"  -i basesCombine

    opDo tarPkgManage.sh -h -v -n showRun -p inBase="${marmeControlBaseDir}" -p outBase="marme.control" -p result="${tarDestBaseDir}/marmeControl.tar"  -i basesCombine common example.com
    
    lpReturn
}




_CommentBegin_
*  [[elisp:(beginning-of-buffer)][Top]] ################ [[elisp:(delete-other-windows)][(1)]]  *End Of Editable Text*
_CommentEnd_

####+BEGIN: bx:dblock:bash:end-of-file :types ""
_CommentBegin_
*  [[elisp:(org-cycle)][| ]]  Common        ::  /[dblock] -- End-Of-File Controls/ [[elisp:(org-cycle)][| ]]
_CommentEnd_
#+STARTUP: showall
#local variables:
#major-mode: sh-mode
#fill-column: 90
# end:
####+END:

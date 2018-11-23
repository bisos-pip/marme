#! /bin/bash

if ! which bx-platformInfoManage.py > /dev/null ; then
    echo "E: Missing bx-platformInfoManage.py"
    exit 1
fi


function platformInfoParsSet {
    local here=$(pwd)
    local foreignBxoBase=$(dirname ${here})

    local currentUser=$(id -un)
    local currentUserGroup=$(id -g -n ${currentUser})

    bx-platformInfoManage.py --bisosUserName="${currentUser}"  -i pkgInfoParsSet
    bx-platformInfoManage.py --bisosGroupName="${currentUserGroup}"  -i pkgInfoParsSet     
    bx-platformInfoManage.py --rootDir_foreignBxo="${foreignBxoBase}"  -i pkgInfoParsSet

    bx-platformInfoManage.py --rootDir_deRun="/de/run"  -i pkgInfoParsSet

    echo "========= bx-platformInfoManage.py -i pkgInfoParsGet ========="
    bx-platformInfoManage.py -i pkgInfoParsGet
}

function bxoSrCurrentsSet {

    bx-currentsManage.py --bxoId="mcm"  -i pkgInfoParsSet
    bx-currentsManage.py --sr="marme/dsnProc"  -i pkgInfoParsSet

    echo "========= bx-currentsManage.py -i pkgInfoParsGet ========="
    bx-currentsManage.py -i pkgInfoParsGet
}

platformInfoParsSet

bxoSrCurrentsSet

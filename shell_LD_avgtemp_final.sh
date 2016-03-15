#!/bin/bash
list="19001 19002 19003 19004 19005 19006 19007 19008 19009 19010"
#echo $list

INDIR="/N/dc2/scratch/pkgandhi/subjects/LONGITUDINAL_DATA_CFN"
OUTDIR="/N/dc2/scratch/pkgandhi/subjects/LONGITUDINAL_DATA_CFN_RES"
PREFIX="recon-all"
for index in $list; do
	
	##scans=$(ls -d "$index"_?)
	##tpoints=$(echo $scans | wc -w)
	
	for i in $(ls -d "$index"_?); do	

		point="-tp "$INDIR"/"$i""
		points="$points $point"
		unset point
	done
		echo "recon-all -base "$index"_temp$points -all 1>$OUTDIR/$PREFIX.$index.out 2>$OUTDIR/$PREFIX.$index.err &"
		unset points

#recon-all -base "$index"_temp '-tp $INDIR/"$index"_%s\t' $no -all 1>$OUTDIR/$PREFIX.$index.out 2>$OUTDIR/$PREFIX.$index.err &
done
wait


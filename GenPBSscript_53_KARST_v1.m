function GenPBSscript_53_KARST_v1(DirPathLC,Email)
%09/11/2015
% Modification by pkgandhi to make log files and store under log
% directory.
% Changed ppn from 8(Quarry) to 16 for KARST. This are the maximum number
% of processors a node can contain on KARST.
% KARST has inbuilt ccm module environment. Thus it does not need to load
% the ccm module as required by BigRed2.
%
% 12/18/2013
% Modification by jdwest to allow any directory to be used, not just those in
% /N/dc/projects/shenlab/subjects
%
% 10/3/2013
% Modification by sk31 to redirect each subject's output directory to
% $DirPathLCroot_RES
%
% 9/2/11
% Modification by JDWest to process in 51.  Added path definitions to be sure
% Freesurfer 5.1 is being used. 
%
% 9/1/11
% Modification by JDWest to increase walltime to 120, change last loop to wait
% command and include echo statement so subjects can be linked to job number.
% Also changed to function rather than a script to edit.
%
% e.g. GenPBSscript('CHEMO3T_FREESURFER_QUA','jdwest@iupui.edu');
%
% PBSSRIPTGEN(DIRPATHONLC, DIRPATHONSC, PREFIX, WALLTIME, FOLDERNAME, EMAIL, LIST):
% generates a PBS sripts for each subject located in DIRPATHONLC. These
% files will be saved in a folder that will be, created under DIRPATHLC,
% named FOLDERNAME (optional). If not provided, the generic name PBSscripts_KT
% will be used instead. PBS files are used to run Freesurfer software(c)
% on Quarry, a supercomputer at Indiana University under the UITS.
% Beginning, abort, and/or complete notifications will be sent to EMAIL
% (optional). hfirpi@iupui.edu is the default email. Output from Freesurfer
% will be saved under DIRPATHSC/<subject name>.
%
%
% Example:
% DirPathLC = '/net/cancer_study/study_cas/freesurfer_sidgrid_subjects';
% DirPathSC = '/N/gpfs/hfirpi/freesurfer_sidgrid_subjects/';
% PBSscriptgen(DirPathLC, DirPathSC);
%


% Original Author: Hiram Firpi
% NIC Revision Info:
%    $Author: hfirpi $
%    $Date: 2008/01/06 8:03 $
%    $Revision: 0.0 $
%
% Copyright (C) 2007,
% Indiana University-Purdue University (Indianapolis, IN). 
% All rights reserved.


% Modified by Li and Sungeun on 10/23/08


warning('off')

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Edit the following two lines accordingly
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% DirPathLC = ['/N/dc/projects/shenlab/subjects/' DirPathLCroot]; % specify the directory containing your data
%Email = 'sk31@iupui.edu'; % put your email address here
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

Prefix = 'recon-all'; % prefix for log file names
WallTime = 20;
FolderName = 'PBSscripts_KT';
D = ''; % run a set of specified subjects
OutDir = sprintf('%s/logs_KT',DirPathLC);
DirPathSC = DirPathLC;

DirPathSC2 = [DirPathSC '_RES'];
if ~exist(DirPathSC2,'dir')
    mkdir(DirPathSC2);
    estr = sprintf('!chown -R :shenlab %s',DirPathSC2); eval(estr);
end

if isempty(D)
    D = dir(DirPathLC);
    idx = find([D.isdir]); D = D(idx); % remove file names, keep dir names only
    N = length(D); idx = [];
    for i=1:N
        switch D(i).name
            case '.'
                idx(end+1) = i;
            case '..'
                idx(end+1) = i;
            case 'logs_KT'
                idx(end+1) = i;
            case FolderName
                idx(end+1) = i;         
        end
    end
    D = D(setdiff(1:N,idx));    
    NoOfSubjs = length(D);
%     for i = 1:N,
%         if D(i).isdir == 1
%             NoOfSubjs = NoOfSubjs + 1;
%         else
%             NoOfSubjs = NoOfSubjs;
%         end
%     end
%     a = 3;
else
    NoOfSubjs = length(D(:));
    for i = 1:NoOfSubjs,
        D(i).isdir = 1;
    end
%     a = 1;
end

if ~exist(OutDir,'dir')
    mkdir(OutDir);
    estr = sprintf('!chown -R :shenlab %s',OutDir); eval(estr);
end
outdirstr = sprintf('OUTDIR="%s"\n',OutDir); % specify output directory


Success = mkdir(DirPathLC, FolderName);
if Success ~= 1
    rmdir(fullfile(DirPathLC, FolderName), 's');
    Success = mkdir(DirPathLC, FolderName);
end
estr = sprintf('!chown -R :shenlab %s',fullfile(DirPathLC, FolderName)); eval(estr);

ModN = ceil(NoOfSubjs/16);

count = 0;
for i = 1:16:NoOfSubjs,
    count = count + 1;
    if D(i).isdir == 1 & ~strcmp(D(i).name, 'PBSscripts_KT') & ~strcmp(D(i).name, 'MGZ_FILES'),
        D1 = dir([DirPathLC '/' D(i).name]);
        FirstImage = D1(1).name; % Skip dirs '.' and '..'
        [pathstr,name,ext] = fileparts(FirstImage);
        if strcmp(ext, 'mgz')
	
        elseif count < ModN
            fid = fopen([DirPathLC '/' FolderName '/PBS_' D(i).name 'to' D(i+15).name], 'w');
            fprintf(fid, '#!/bin/bash\n');
            fprintf(fid, '#PBS -k o\n');
            fprintf(fid, ['#PBS -l nodes=1:ppn=16:dc2,mem=12000mb,walltime=' num2str(WallTime) ':00:00\n']);
            fprintf(fid, ['#PBS -M ' Email '\n']);
            fprintf(fid, '#PBS -m abe\n');
            fprintf(fid, ['#PBS -N recon-all_' D(i).name 'to' D(i+15).name '\n']);
            fprintf(fid, ['#PBS -o recon-all_' D(i).name 'to' D(i+15).name '.log\n']);
            fprintf(fid, '#PBS -j abe\n\n');
	    fprintf(fid, 'module unload freesurfer\n');
	    fprintf(fid, 'module load freesurfer/5.3.0\n');
	    fprintf(fid, ['export SUBJECTS_DIR=' DirPathLC '\n']);
	    fprintf(fid, 'source /N/soft/cle4/freesurfer/5.3.0/FreeSurferEnv.sh\n\n');
	    fprintf(fid, ['list="' D(i).name ' ' D(i+1).name ' ' D(i+2).name ' ' D(i+3).name ' ' D(i+4).name ' ' D(i+5).name ' ' D(i+6).name ' ' D(i+7).name ' ' D(i+8).name ' ' D(i+9).name ' ' D(i+10).name ' ' D(i+11).name ' ' D(i+12).name ' ' D(i+13).name ' ' D(i+14).name ' ' D(i+15).name '"\n']);
            fprintf(fid, ['echo $list\n']);
	    fprintf(fid, outdirstr);
            fprintf(fid, ['PREFIX="' Prefix '"\n\n']);
            fprintf(fid, 'for index in $list; do\n');
            fprintf(fid, ['recon-all -i ' DirPathSC '/$index/"$index".nii -subject $index -sd ' DirPathSC '_RES -all -hippo-subfields 1>$OUTDIR/$PREFIX.$index.out 2>$OUTDIR/$PREFIX.$index.err &\n']);
            fprintf(fid, 'done\n');
	    fprintf(fid, 'wait\n');
            fclose(fid);
            
             elseif count < ModN
            fid = fopen([DirPathLC '/' FolderName '/PBS_' D(i+16).name 'to' D(i+31).name], 'w');
            fprintf(fid, '#!/bin/bash\n');
            fprintf(fid, '#PBS -k o\n');
            fprintf(fid, ['#PBS -l nodes=1:ppn=16:dc2,mem=12000mb,walltime=' num2str(WallTime) ':00:00\n']);
            fprintf(fid, ['#PBS -M ' Email '\n']);
            fprintf(fid, '#PBS -m abe\n');
            fprintf(fid, ['#PBS -N recon-all_' D(i+16).name 'to' D(i+31).name '\n']);
            fprintf(fid, ['#PBS -o recon-all_' D(i+16).name 'to' D(i+31).name '.log\n']);
            fprintf(fid, '#PBS -j abe\n\n');
	    fprintf(fid, 'module unload freesurfer\n');
	    fprintf(fid, 'module load freesurfer/5.3.0\n');
	    fprintf(fid, ['export SUBJECTS_DIR=' DirPathLC '\n']);
	    fprintf(fid, 'source /N/soft/cle4/freesurfer/5.3.0/FreeSurferEnv.sh\n\n');
	    fprintf(fid, ['list="' D(i+16).name ' ' D(i+17).name ' ' D(i+18).name ' ' D(i+19).name ' ' D(i+20).name ' ' D(i+21).name ' ' D(i+22).name ' ' D(i+23).name ' ' D(i+24).name ' ' D(i+25).name ' ' D(i+26).name ' ' D(i+27).name ' ' D(i+28).name ' ' D(i+29).name ' ' D(i+30).name ' ' D(i+31).name '"\n']);
            fprintf(fid, ['echo $list\n']);
	    fprintf(fid, outdirstr);
            fprintf(fid, ['PREFIX="' Prefix '"\n\n']);
            fprintf(fid, 'for index in $list; do\n');
            fprintf(fid, ['recon-all -i ' DirPathSC '/$index/"$index".nii -subject $index -sd ' DirPathSC '_RES -all -hippo-subfields 1>$OUTDIR/$PREFIX.$index.out 2>$OUTDIR/$PREFIX.$index.err &\n']);
            fprintf(fid, 'done\n');
	    fprintf(fid, 'wait\n');
            fclose(fid);
            
            else
            fid = fopen([DirPathLC '/' FolderName '/PBS_' D(i).name 'to' D(NoOfSubjs).name], 'w');
            fprintf(fid, '#!/bin/bash\n');
            fprintf(fid, '#PBS -k o\n');
            fprintf(fid, ['#PBS -l nodes=1:ppn=16:dc2,mem=12000mb,walltime=' num2str(WallTime) ':00:00\n']);
            fprintf(fid, ['#PBS -M ' Email '\n']);
            fprintf(fid, '#PBS -m abe\n');
            fprintf(fid, ['#PBS -N recon-all_' D(i).name 'to' D(NoOfSubjs).name '\n']);
            fprintf(fid, ['#PBS -N recon-all_' D(i).name 'to' D(NoOfSubjs).name '.log\n']);
            fprintf(fid, '#PBS -j oe\n\n');
            fprintf(fid, 'module unload freesurfer\n');
	    fprintf(fid, 'module load freesurfer/5.3.0\n');
	    fprintf(fid, ['export SUBJECTS_DIR=' DirPathLC '\n']);
	    fprintf(fid, 'source /N/soft/cle4/freesurfer/5.3.0/FreeSurferEnv.sh\n\n');
	    X = [];
            for j = i:NoOfSubjs,
                X = [X D(j).name ' '];
            end
            fprintf(fid, ['list="' X '"\n']);
            fprintf(fid, ['echo $list\n']);
	    fprintf(fid, outdirstr);
            fprintf(fid, ['PREFIX="' Prefix '"\n\n']);
            fprintf(fid, 'for index in $list; do\n');
            fprintf(fid, ['recon-all -i ' DirPathSC '/$index/"$index".nii -subject $index -sd ' DirPathSC2 ' -all -hippo-subfields 1>$OUTDIR/$PREFIX.$index.out 2>$OUTDIR/$PREFIX.$index.err &\n']);
            fprintf(fid, 'done\n');
            fprintf(fid, 'wait\n');
	    fclose(fid);
            
        
        end
    end
end

cmdstr = sprintf('!chmod a+x %s/%s/*',DirPathLC,FolderName); eval(cmdstr);
cmdstr = sprintf('!chmod -R g+w %s/%s',DirPathLC,FolderName); eval(cmdstr);
cmdstr = sprintf('!chmod -R g+w %s/logs_KT',DirPathLC); eval(cmdstr);

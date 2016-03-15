function GenPBSscript_53_BR2_v1(DirPathLC,Email)
%03/14/2016
% Modification by pkgandhi to source freesurfer to the changed directory and also make 
% the script more shorter. Removed the Quarry Part.
%
% 12/04/2014
% Modification of Quarry script to be functional on BR2.  Added appropriate flags for PBS
% as well as generation of shell script for each PBS to allow multiple subjects to be run
% on one node
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
% named FOLDERNAME (optional). If not provided, the generic name PBSscripts
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
WallTime = 30;
FolderName = 'PBSscripts_BR2';
D = ''; % run a set of specified subjects
OutDir = sprintf('%s/logs_BR2',DirPathLC);
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
            case 'logs'
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

ModN = ceil(NoOfSubjs/32);

count = 0;
for i = 1:32:NoOfSubjs,
    count = count + 1;
    if D(i).isdir == 1 & ~strcmp(D(i).name, 'PBSscripts_BR2') & ~strcmp(D(i).name, 'MGZ_FILES'),
        D1 = dir([DirPathLC '/' D(i).name]);
        FirstImage = D1(1).name; % Skip dirs '.' and '..'
        [pathstr,name,ext] = fileparts(FirstImage);
        if strcmp(ext, 'mgz')
	
        elseif count < ModN
            % write out PBS file
	    fidpbs = fopen([DirPathLC '/' FolderName '/PBS_' D(i).name 'to' D(i+31).name], 'w');
	    fprintf(fidpbs, '#!/bin/bash\n');
            fprintf(fidpbs, ['#PBS -l walltime=' num2str(WallTime) ':00:00\n']);
            fprintf(fidpbs, '#PBS -l nodes=1:ppn=32:dc2\n');
	    fprintf(fidpbs, '#PBS -l gres=ccm\n');
	    fprintf(fidpbs, '#PBS -q cpu\n');
            fprintf(fidpbs, ['#PBS -N recon-all_' D(i).name 'to' D(i+31).name '\n']);
            fprintf(fidpbs, '#PBS -j oe\n');
	    fprintf(fidpbs, ['#PBS -o recon-all_' D(i).name 'to' D(i+31).name '.log\n']);
            fprintf(fidpbs, '#PBS -V\n');
            fprintf(fidpbs, '#PBS -m abe\n');
            fprintf(fidpbs, ['#PBS -M ' Email '\n\n']);
	    fprintf(fidpbs, 'module unload freesurfer\n');
	    fprintf(fidpbs, 'module load freesurfer/5.3.0\n');
	    fprintf(fidpbs, ['export SUBJECTS_DIR=' DirPathLC '\n']);
	    fprintf(fidpbs, 'source /N/soft/cle4/freesurfer/5.3.0/FreeSurferEnv.sh\n');
	    fprintf(fidpbs, '\n');
	    fprintf(fidpbs, 'module load ccm\n');
            fprintf(fidpbs, '\n');
            fprintf(fidpbs, 'START=`/bin/date +%%s`\n');
            fprintf(fidpbs, 'echo $START\n');
            fprintf(fidpbs, '\n');
            fprintf(fidpbs, ['ccmrun ' DirPathLC '/' FolderName '/shell_' D(i).name 'to' D(i+31).name '.sh\n']);
            fprintf(fidpbs, '\n');
            fprintf(fidpbs, 'END=`/bin/date +%%s`\n');
            fprintf(fidpbs, 'echo $END\n');
	    fprintf(fidpbs, '\n');
            fprintf(fidpbs, 'echo $((END-START))\n');
	    fclose(fidpbs);

	    % Write out shell script file
	    fidsh = fopen([DirPathLC '/' FolderName '/shell_' D(i).name 'to' D(i+31).name '.sh'], 'w');
            fprintf(fidsh, '#!/bin/bash\n');
	    X = [];
            for j = i:i+31,
                X = [X D(j).name ' '];
            end
            fprintf(fidsh, ['list="' X '"\n']);	
            fprintf(fidsh, ['echo $list\n']);
	    fprintf(fidsh, outdirstr);
            fprintf(fidsh, ['PREFIX="' Prefix '"\n\n']);
            fprintf(fidsh, 'for index in $list; do\n');
            fprintf(fidsh, ['recon-all -i ' DirPathSC '/$index/"$index".nii -subject $index -sd ' DirPathSC '_RES -all -hippo-subfields 1>$OUTDIR/$PREFIX.$index.out 2>$OUTDIR/$PREFIX.$index.err &\n']);
            fprintf(fidsh, 'done\n');
	    fprintf(fidsh, 'wait\n');
            fclose(fidsh);
        else
            % write out PBS file
            fidpbs = fopen([DirPathLC '/' FolderName '/PBS_' D(i).name 'to' D(NoOfSubjs).name], 'w');
            fprintf(fidpbs, '#!/bin/bash\n');
            fprintf(fidpbs, ['#PBS -l walltime=' num2str(WallTime) ':00:00\n']);
            fprintf(fidpbs, '#PBS -l nodes=1:ppn=32:dc2\n');
            fprintf(fidpbs, '#PBS -l gres=ccm\n');
            fprintf(fidpbs, '#PBS -q cpu\n');
            fprintf(fidpbs, ['#PBS -N recon-all_' D(i).name 'to' D(NoOfSubjs).name '\n']);
            fprintf(fidpbs, '#PBS -j oe\n');
            fprintf(fidpbs, ['#PBS -o recon-all_' D(i).name 'to' D(NoOfSubjs).name '.log\n']);
            fprintf(fidpbs, '#PBS -V\n');
            fprintf(fidpbs, '#PBS -m abe\n');
            fprintf(fidpbs, ['#PBS -M ' Email '\n\n']);
            fprintf(fidpbs, 'module unload freesurfer\n');
	    fprintf(fidpbs, 'module load freesurfer/5.3.0\n');
	    fprintf(fidpbs, ['export SUBJECTS_DIR=' DirPathLC '\n']);
	    fprintf(fidpbs, 'source /N/soft/cle4/freesurfer/5.3.0/FreeSurferEnv.sh\n');
            fprintf(fidpbs, '\n');
            fprintf(fidpbs, 'module load ccm\n');
            fprintf(fidpbs, '\n');
            fprintf(fidpbs, 'START=`/bin/date +%%s`\n');
            fprintf(fidpbs, 'echo $START\n');
            fprintf(fidpbs, '\n');
            fprintf(fidpbs, ['ccmrun ' DirPathLC '/' FolderName '/shell_' D(i).name 'to' D(NoOfSubjs).name '.sh\n']);
            fprintf(fidpbs, '\n');
            fprintf(fidpbs, 'END=`/bin/date +%%s`\n');
            fprintf(fidpbs, 'echo $END\n');
            fprintf(fidpbs, '\n');
            fprintf(fidpbs, 'echo $((END-START))\n');
            fclose(fidpbs);

            % Write out shell script file
            fidsh = fopen([DirPathLC '/' FolderName '/shell_' D(i).name 'to' D(NoOfSubjs).name '.sh'], 'w');
            fprintf(fidsh, '#!/bin/bash\n');
            X = [];
            for j = i:NoOfSubjs,
                X = [X D(j).name ' '];
            end
            fprintf(fidsh, ['list="' X '"\n']);
            fprintf(fidsh, ['echo $list\n']);
            fprintf(fidsh, outdirstr);
            fprintf(fidsh, ['PREFIX="' Prefix '"\n\n']);
            fprintf(fidsh, 'for index in $list; do\n');
            fprintf(fidsh, ['recon-all -i ' DirPathSC '/$index/"$index".nii -subject $index -sd ' DirPathSC '_RES -all -hippo-subfields 1>$OUTDIR/$PREFIX.$index.out 2>$OUTDIR/$PREFIX.$index.err &\n']);
            fprintf(fidsh, 'done\n');
            fprintf(fidsh, 'wait\n');
            fclose(fidsh);     
        end
    end
end

cmdstr = sprintf('!chmod a+x %s/%s/*',DirPathLC,FolderName); eval(cmdstr);
cmdstr = sprintf('!chmod -R g+w %s/%s',DirPathLC,FolderName); eval(cmdstr);
cmdstr = sprintf('!chmod -R g+w %s/logs_BR2',DirPathLC); eval(cmdstr);




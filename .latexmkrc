$jobname = 'poster';
$lualatex = 'lualatex -interaction nonstopmode';

$do_cd = 1;
ensure_path('TEXINPUTS', '../lib//');
$out_dir = '../build';
$out2_dir = '..';

$clean_ext = 'nav snm';
$bibtex_use = 2;

#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
yaml2doc – A  Tool for Documenting YML Files
"""

import argparse
import sys
from datetime import date
import yaml
import os.path
import subprocess

STATE_TEXT = 0
STATE_YAML = 1

validated_str = "YAML validation:"
START_YAML = "```yaml"
END_YAML= "```"
LATEX_NOTE=r"\marginpar{\raggedleft\small %s}"
NOTE_STR = "note:"
MAX_LINE_LEN = 70

def convert(lines,is_latex=True):
    state = STATE_TEXT
    last_text_line = ''
    latex_setup = False
    status = "OK"
    try:
        yamlstr = yaml.load('\n'.join(lines), Loader=yaml.Loader)
    except:
        status = "Fail"

        
    for line in lines:
        line = line.rstrip()
        if not line:
            # do not change state if the line is empty
            yield ''
        elif line.startswith('# ') or line == '#':
            if state != STATE_TEXT:
                yield END_YAML
            line = last_text_line = line[2:]
            if line.startswith(validated_str):
                yield validated_str + '*%s* on %s'%(status,date.today().strftime('%d/%m/%Y'))
            else:
                yield line
            state = STATE_TEXT
        elif line == '---':
            pass
        else:
            if line.startswith('-'):
                yield '# '+line[1:-1].strip()
            if state != STATE_YAML:
                yield START_YAML
            start_comment = line.find('#'+NOTE_STR)
            if  start_comment!= -1 and is_latex:
                yield END_YAML
                if not latex_setup:
                    yield r'\reversemarginpar'
                    latex_setup=True
                yield LATEX_NOTE%(line[start_comment+1+len(NOTE_STR):])
                line = line[:start_comment]
                yield START_YAML
            state = STATE_YAML
            if len(line)>MAX_LINE_LEN:
                line=line[:MAX_LINE_LEN-2]+'..'
            yield line
            
    if state == STATE_YAML:
        yield END_YAML
    yield "---- \n\nProduced by [yaml2md](https://www.google.com) and [pandoc](pandoc.org)"

def convert_file(infilename, outfilename,is_latex):
    with open(infilename) as infh:
        with open(outfilename, "w") as outfh:
            for l in convert(infh.readlines(),is_latex):
                print(l.rstrip(),file=outfh)


def which(program):
    for path in os.environ["PATH"].split(os.pathsep):
        exe_file = os.path.join(path, program)
        if  os.path.isfile(exe_file) and os.access(exe_file, os.X_OK):
            return exe_file
    return None

def main(infilename, outfilename):
    ext = os.path.splitext(outfilename)[1]
    md_outfilename = outfilename 
    if ext == '.yaml':
        print(f'Error yaml file should not output.',file=sys.stderr)
        sys.exit(-1)
    elif ext != '.md':
        md_outfilename = outfilename+'.md'
        
    convert_file(infilename, md_outfilename, ext=='.pdf')

    if ext != '.md':
        extra =''
        if ext == '.html':
            extra='--highlight-style pygments -s'
        options = "-o %s -N --toc %s %s"%(outfilename,extra,md_outfilename)
        to_doc_exe='pandoc'
        if which(to_doc_exe) is not None:
            output=subprocess.check_output(f'{to_doc_exe} {options}',shell=True)
            os.remove(md_outfilename) # remove the temporary file
            if len(output)>0:
                print(output)
        else:
            print(f'Error {to_doc_exe} cannot be found! Try installing {to_doc_exe}.',file=sys.stderr)
            sys.exit(-1)
        



def run():
    parser = argparse.ArgumentParser()
    parser.add_argument('infilename', metavar='infile',
                        help="YAML-file to read")
    parser.add_argument('outfilename', metavar='outfile',
                        help="makdown-file to write")
    args = parser.parse_args()
    main(**vars(args))


if __name__ == "__main__":
    run()

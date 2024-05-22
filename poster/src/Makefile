.PHONY: main clean FORCE

main: poster.pdf

poster.pdf: FORCE
	latexmk -pdflatex='lualatex -interaction nonstopmode' -pdf -jobname=poster -outdir=.. -auxdir=build main.ltx

clean:
	latexmk -pdf -C

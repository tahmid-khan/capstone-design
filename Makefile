.PHONY: main clean FORCE

main: poster.pdf

poster.pdf: FORCE
	latexmk -r src/.latexmkrc \
	 	-jobname=poster \
		-pdflatex='lualatex -interaction nonstopmode' -pdflua \
		-cd -outdir=.. -auxdir=../build \
		src/main.ltx

clean:
	latexmk -pdf -C

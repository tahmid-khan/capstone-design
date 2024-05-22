.PHONY: main clean FORCE

main: poster

poster: FORCE
	latexmk -r src/.latexmkrc -pdflua -cd src/main.ltx

clean:
	latexmk -r src/.latexmkrc -C -cd src/

pretty:
	latexindent -l -s -c build -w src/main.ltx

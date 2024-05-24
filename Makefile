.PHONY: main clean FORCE

main: poster

poster: FORCE
	latexmk -lualatex src/main.ltx

clean:
	latexmk -c src/main.ltx

veryclean:
	latexmk -C src/main.ltx

realclean: veryclean
	rm -rf build

pretty:
	latexindent -local -silent -checkv -overwriteIfDifferent -cruft=build/latexindent src/*.ltx src/*.bib

lint: style-check lacheck chktex

style-check:
	style-check.rb src/*.ltx

lacheck:
	lacheck src/*.ltx

chktex:
	chktex --quiet src/*.ltx

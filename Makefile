embed:
	ls ../gossa.go
	echo "embedding css and js into binary"
	perl -pe 's/template_will_be_here/`cat ui.tmpl`/ge' -i ../gossa.go
	perl -pe 's/css_will_be_here/`cat style.css`/ge' -i ../gossa.go
	perl -pe 's/js_will_be_here/`cat script.js`/ge' -i ../gossa.go
	perl -pe 's/favicon_will_be_here/`base64 -w0 favicon.png`/ge' -i ../gossa.go

embed:
ifdef branch
	echo "~~~ will checkout ui branch" $(branch)
	git checkout $(branch)
endif
	ls ../gossa.go
	echo "embedding css and js into binary"
	subs_by_file.exe ../gossa.go template_will_be_here ui.tmpl
	subs_by_file.exe ../gossa.go css_will_be_here style.css
	subs_by_file.exe ../gossa.go js_will_be_here script.js
	subs_by_file.exe ../gossa.go favicon_will_be_here favicon.png -b

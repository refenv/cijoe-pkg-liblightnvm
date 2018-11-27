PROJECT_NAME=cijoe-pkg-liblightnvm

.PHONY: install
install:
	pip install .

.PHONY: uninstall
uninstall:
	pip uninstall ${PROJECT_NAME} --yes || true

.PHONY: dev
dev: uninstall install
	@echo -n "# dev: "; date

.PHONY: clean
clean:
	rm -r build
	rm -r dist

.PHONY: release-build
release-build:
	python setup.py sdist
	python setup.py bdist_wheel

.PHONY: release-upload
release-upload:
	twine upload dist/*

.PHONY: release
release: release-build release-upload
	@echo -n "# rel: "; date

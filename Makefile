
ifeq ($(OS),Windows_NT)
    YOUR_OS := Windows
    INSTALL_TARGET := install-windows
    OPEN_EDITORS_VERSION_TARGET := open-editors-version-windows
    OPEN_RELEASE_VERSION_TARGET := open-release-version-windows
else
    YOUR_OS := $(shell sh -c 'uname 2>/dev/null || echo Unknown')
    ifeq ($(YOUR_OS), Linux)
    INSTALL_TARGET := install-linux
    OPEN_EDITORS_VERSION_TARGET := open-editors-version-linux
    OPEN_RELEASE_VERSION_TARGET := open-release-version-linux
	MKDOCS = $(shell asdf where python)/bin/mkdocs
    endif
    ifeq ($(YOUR_OS), Darwin)
    INSTALL_TARGET := install-macos
    OPEN_EDITORS_VERSION_TARGET := open-editors-version-macos
    OPEN_RELEASE_VERSION_TARGET := open-release-version-macos
	MKDOCS = $(shell asdf where python)/bin/mkdocs
    endif
endif
DOC_ORG_NAME := ekgf
DOC_ROOT_NAME := usecase
CURRENT_BRANCH := $(shell git branch --show-current)

.PHONY: info
info:
	@echo "MkDocs: ${MKDOCS}"
	@echo "Document Version: ${DOC_VERSION}"
	@echo "Git Branch: ${CURRENT_BRANCH}"

.PHONY: install
install: docs-install

.PHONY: docs-install
docs-install: docs-install-python-packages
	brew upgrade cairo || brew install cairo
	brew upgrade freetype || brew install freetype
	brew upgrade libffi || brew install libffi
	brew upgrade libjpeg || brew install libjpeg
	brew upgrade libpng || brew install libpng
	brew upgrade zlib || brew install zlib

.PHONY: docs-install-asdf
docs-install-asdf:
ifeq ($(GITHUB_TOKEN),)
	brew upgrade asdf || brew install asdf
	asdf plugin add python || true
	asdf plugin add nodejs || true
endif

.PHONY: docs-install-python
docs-install-python: docs-install-asdf
ifeq ($(GITHUB_TOKEN),)
	asdf install
	asdf exec python -m pip install --upgrade pip
endif

.PHONY: docs-install-python-packages
docs-install-python-packages: docs-install-python
	pip install --upgrade mkdocs
	pip install --upgrade mkdocs-material
	pip install --upgrade mkdocs-localsearch
	pip install --upgrade mdx-spanner
	pip install --upgrade mkdocs-awesome-pages-plugin
	pip install --upgrade mkdocs-macros-plugin
	pip install --upgrade markdown-emdash

.PHONY: docs-build
docs-build:
	$(MKDOCS) build

.PHONY: docs-serve
docs-serve: docs-assets
	$(MKDOCS) serve --livereload --strict --watch-theme

.PHONY: docs-serve-debug
docs-serve-debug:
	$(MKDOCS) serve --livereload --strict --watch-theme --verbose

.PHONY: docs-deploy
docs-deploy:
	$(MKDOCS) gh-deploy --verbose

docs/index.html: $(wildcard docs/*.md) mkdocs.yml
	$(MKDOCS) build
	open site/index.html

.PHONY: docs-assets
docs-assets:


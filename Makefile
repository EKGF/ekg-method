
ifeq ($(OS),Windows_NT)
    YOUR_OS := Windows
    INSTALL_TARGET := install-windows
    OPEN_EDITORS_VERSION_TARGET := open-editors-version-windows
    OPEN_RELEASE_VERSION_TARGET := open-release-version-windows
    MKDOCS := mkdocs
else
    YOUR_OS := $(shell sh -c 'uname 2>/dev/null || echo Unknown')
ifeq ($(YOUR_OS), Linux)
    INSTALL_TARGET := install-linux
    OPEN_EDITORS_VERSION_TARGET := open-editors-version-linux
    OPEN_RELEASE_VERSION_TARGET := open-release-version-linux
ifneq ($(wildcard /home/runner/.*),)
	MKDOCS := mkdocs
else
	MKDOCS := $(shell asdf where python)/bin/mkdocs
endif
endif
ifeq ($(YOUR_OS), Darwin)
    INSTALL_TARGET := install-macos
    OPEN_EDITORS_VERSION_TARGET := open-editors-version-macos
    OPEN_RELEASE_VERSION_TARGET := open-release-version-macos
	MKDOCS := $(shell asdf where python)/bin/mkdocs
endif
endif
DOC_ORG_NAME := ekgf
DOC_ROOT_NAME := usecase
CURRENT_BRANCH := $(shell git branch --show-current)
PAT_MKDOCS_INSIDERS := $(shell cat ../.secrets/PAT_MKDOCS_INSIDERS.txt 2>/dev/null)
ifeq ($(PAT_MKDOCS_INSIDERS),)
	MKDOCS_CONFIG_FILE := 'mkdocs.outsiders.yml'
else
	MKDOCS_CONFIG_FILE := 'mkdocs.yml'
endif

.PHONY: info
info:
	@echo "MkDocs: ${MKDOCS}"
	@echo "Document Version: ${DOC_VERSION}"
	@echo "Git Branch: ${CURRENT_BRANCH}"

.PHONY: install
install: docs-install

.PHONY: docs-install
docs-install: docs-install-brew-packages docs-install-python-packages

.PHONY: docs-install-brew-packages
docs-install-brew-packages: docs-install-brew
	@echo "Install packages via HomeBrew:"
	brew upgrade cairo || brew install cairo
	brew upgrade freetype || brew install freetype
	brew upgrade libffi || brew install libffi
	brew upgrade libjpeg || brew install libjpeg
	brew upgrade libpng || brew install libpng
	brew upgrade zlib || brew install zlib

.PHONY: docs-install-brew
ifeq ($(YOUR_OS), Linux)
docs-install-brew: docs-install-brew-linux
endif
ifeq ($(YOUR_OS), Windows)
docs-install-brew: docs-install-brew-windows
endif
ifeq ($(YOUR_OS), Darwin)
docs-install-brew: docs-install-brew-macos
endif

.PHONY: docs-install-brew-linux
docs-install-brew-linux:
	@if ! command -v brew >/dev/null 2>&1 ; then echo "Install HomeBrew" ; exit 1 ; fi

.PHONY: docs-install-brew-windows
docs-install-brew-windows:
	@if ! command -v brew >/dev/null 2>&1 ; then echo "Install HomeBrew" ; exit 1 ; fi

.PHONY: docs-install-brew-macos
docs-install-brew-macos:
	@if ! command -v brew >/dev/null 2>&1 ; then echo "Install HomeBrew" ; exit 1 ; fi

.PHONY: docs-install-asdf
docs-install-asdf: docs-install-brew
	@echo "Install the asdf package manager:"
	brew upgrade asdf || brew install asdf
	asdf plugin add python || true
	asdf plugin add nodejs || true

.PHONY: docs-install-python
docs-install-python: docs-install-asdf
	@echo "Install packages via asdf:"
	asdf install
	asdf exec python -m pip install --upgrade pip

.PHONY: docs-install-python-packages
ifneq ($(wildcard /home/runner/.*),)
docs-install-python-packages:
else
docs-install-python-packages: docs-install-python
endif
	@echo "Install packages via pip:"
	pip install --upgrade mkdocs
	pip install --upgrade mkdocs-localsearch
	pip install --upgrade mkdocs-include-markdown-plugin
	pip install --upgrade mkdocs-awesome-pages-plugin
	pip install --upgrade mkdocs-macros-plugin
	pip install --upgrade mkdocs-mermaid2-plugin
	pip install --upgrade mkdocs-git-revision-date-plugin
	pip install --upgrade mkdocs-minify-plugin
	pip install --upgrade mkdocs-redirects
	pip install --upgrade mdx-spanner
	pip install --upgrade markdown-emdash
ifeq ($(PAT_MKDOCS_INSIDERS),)
	pip install --upgrade --force-reinstall mkdocs-material
else
	pip install --upgrade --force-reinstall git+https://$(PAT_MKDOCS_INSIDERS)@github.com/squidfunk/mkdocs-material-insiders.git
endif

.PHONY: docs-build
docs-build:
	$(MKDOCS) build --config-file $(MKDOCS_CONFIG_FILE)

.PHONY: docs-serve
docs-serve: docs-assets
	$(MKDOCS) serve --config-file $(MKDOCS_CONFIG_FILE) --livereload --strict

.PHONY: docs-serve-debug
docs-serve-debug:
	$(MKDOCS) serve --config-file $(MKDOCS_CONFIG_FILE) --livereload --strict --verbose

.PHONY: docs-deploy
docs-deploy:
	$(MKDOCS) gh-deploy --config-file $(MKDOCS_CONFIG_FILE) --verbose

.PHONY: docs-assets
docs-assets:


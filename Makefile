
ifeq ($(OS),Windows_NT)
    YOUR_OS := Windows
    INSTALL_TARGET := install-windows
    OPEN_EDITORS_VERSION_TARGET := open-editors-version-windows
    OPEN_RELEASE_VERSION_TARGET := open-release-version-windows
    MKDOCS := mkdocs
    PIP := pip
else
    YOUR_OS := $(shell sh -c 'uname 2>/dev/null || echo Unknown')
ifeq ($(YOUR_OS), Linux)
    INSTALL_TARGET := install-linux
    OPEN_EDITORS_VERSION_TARGET := open-editors-version-linux
    OPEN_RELEASE_VERSION_TARGET := open-release-version-linux
ifneq ($(wildcard /home/runner/.*),) # this means we're running in Github Actions
	MKDOCS := mkdocs
	PIP := pip
else
	MKDOCS := $(shell asdf where python)/bin/mkdocs
	PIP := $(shell asdf where python)/bin/python -m pip
endif
endif
ifeq ($(YOUR_OS), Darwin)
    INSTALL_TARGET := install-macos
    OPEN_EDITORS_VERSION_TARGET := open-editors-version-macos
    OPEN_RELEASE_VERSION_TARGET := open-release-version-macos
	MKDOCS := $(shell asdf where python)/bin/mkdocs
	PIP := $(shell asdf where python)/bin/python -m pip
endif
endif
DOC_ORG_NAME := ekgf
DOC_ROOT_NAME := use-case-tree-method
CURRENT_BRANCH := $(shell git branch --show-current)
PAT_MKDOCS_INSIDERS := $(shell cat $(HOME)/.secrets/PAT_MKDOCS_INSIDERS.txt 2>/dev/null)
ifeq ($(PAT_MKDOCS_INSIDERS),)
MKDOCS_CONFIG_FILE := 'mkdocs.outsiders.yml'
$(info You don't have the $(HOME)/.secrets/PAT_MKDOCS_INSIDERS.txt file so we are using the open source version of MkDocs)
else
MKDOCS_CONFIG_FILE := 'mkdocs.yml'
endif

.PHONY: all
all: docs-build

.PHONY: info
info:
	@echo "Git Branch: ${CURRENT_BRANCH}"
	@echo "MkDocs: ${MKDOCS}"
	@echo "Operating System: ${YOUR_OS}"
	@echo "MkDocs: ${MKDOCS}"
	@echo "MkDocs config file: ${MKDOCS_CONFIG_FILE}"
	@echo "Python pip: ${PIP}"
	@echo "install target: ${INSTALL_TARGET}"
	@echo "Document Version: ${DOC_VERSION}"

.PHONY: install
install: docs-install

.PHONY: docs-install
docs-install: info docs-install-brew docs-install-brew-packages docs-install-python-packages

.PHONY: docs-install-github-actions
docs-install-github-actions: info docs-install-brew-packages docs-install-python-packages

.PHONY: docs-install-brew-packages
docs-install-brew-packages:
	@echo "Install packages via HomeBrew:"
	brew upgrade cairo || brew install cairo
	brew upgrade freetype || brew install freetype
	brew upgrade libffi || brew install libffi
	brew upgrade libjpeg || brew install libjpeg
	brew upgrade libpng || brew install libpng
	brew upgrade zlib || brew install zlib
	brew upgrade plantuml || brew install plantuml
	brew upgrade graphviz || brew install graphviz

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
	brew --version

#
# not sure if HomeBrew can be installed on Windows, this part has not been tested yet!
#
.PHONY: docs-install-brew-windows
docs-install-brew-windows:
	@if ! command -v brew >/dev/null 2>&1 ; then echo "Install HomeBrew" ; exit 1 ; fi
	brew --version

.PHONY: docs-install-brew-macos
docs-install-brew-macos:
	@if ! command -v brew >/dev/null 2>&1 ; then echo "Install HomeBrew" ; exit 1 ; fi
	brew --version

.PHONY: docs-install-asdf
docs-install-asdf: docs-install-brew
	@echo "Install the asdf package manager:"
	brew upgrade asdf || brew install asdf
	asdf plugin add python || true
	asdf plugin add nodejs || true
	asdf plugin add java || true

.PHONY: docs-install-asdf-packages
docs-install-asdf-packages: docs-install-asdf
	@echo "Install packages via asdf:"
	asdf install

.PHONY: docs-install-python-packages
ifneq ($(wildcard /home/runner/.*),)
docs-install-python-packages: docs-install-asdf
docs-install-python-packages: docs-install-asdf
else
docs-install-python-packages: docs-install-asdf-packages
endif
	@echo "Install packages via pip:"
	$(PIP) install --upgrade pip
	$(PIP) install --upgrade wheel
	$(PIP) install --upgrade pipenv
#	$(PIP) install --upgrade plantuml-markdown
	$(PIP) install --upgrade mkdocs-build-plantuml-plugin
	$(PIP) install --upgrade mkdocs
	$(PIP) install --upgrade mkdocs-localsearch
	$(PIP) install --upgrade mkdocs-graphviz
	$(PIP) install --upgrade mkdocs-exclude
	$(PIP) install --upgrade mkdocs-include-markdown-plugin
	$(PIP) install --upgrade mkdocs-awesome-pages-plugin
	$(PIP) install --upgrade mkdocs-macros-plugin
	$(PIP) install --upgrade mkdocs-mermaid2-plugin
	$(PIP) install --upgrade mkdocs-git-revision-date-plugin
	$(PIP) install --upgrade mkdocs-minify-plugin
	$(PIP) install --upgrade mkdocs-redirects
	$(PIP) install --upgrade mdx-spanner
	$(PIP) install --upgrade markdown-emdash
ifeq ($(PAT_MKDOCS_INSIDERS),)
	$(PIP) install --upgrade --force-reinstall mkdocs-material
else
	@$(PIP) install --upgrade --force-reinstall git+https://$(PAT_MKDOCS_INSIDERS)@github.com/squidfunk/mkdocs-material-insiders.git
endif

.PHONY: docs-build
docs-build:
	$(MKDOCS) build --config-file $(MKDOCS_CONFIG_FILE)

.PHONY: serve
serve: docs-serve

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

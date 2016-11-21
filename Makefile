# set shell to bash
SHELL = bash

# figure out absolute path of source repo
ROOT_DIR:=$(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))

# gather uname info
UNAME := $(shell uname)

# set python interpreter to venv
PYTHON='$(ROOT_DIR)/venv/bin/python'

# gather sub directory list
SUBDIRS:=${shell find ./ -type d -print | grep -v venv }
     
.PHONY: subdirs $(SUBDIRS)
 
# helpful debug sequence
print-%  : ; @echo $* = $($*)
    
subdirs: $(SUBDIRS)

# instantiate VENV
venv: venv/bin/activate
venv/bin/activate: requirements.txt
	test -d venv || virtualenv venv
	venv/bin/pip install -Ur requirements.txt
	touch venv/bin/activate

.PHONY: clean destroyvenv

# remove venv
destroyvenv: 
	rm -rf venv

# clean repo of build files
clean: destroyvenv
	rm -rf build
	rm -rf dist
	rm -rf *.egg-info
	rm -rf .tox
	rm -rf tests/.tox
	rm -rf build
	rm -f code_quality.html
	rm -f pylint_report.txt
	rm -f nosetests.xml
	unset APP_VERSION

# only build on Linux
ifeq ($(UNAME), Linux)
# build specific subdir
$(SUBDIRS): venv
	# run code_quality tests
	# tox
	# build the python app
	cd $(@); $(PYTHON) setup.py install --verbose
	# set the venv relocatable / helps with portability
	virtualenv --relocatable $(ROOT_DIR)/venv
	# change activate path to /opt path
	sed -i -e 's/^VIRTUAL_ENV.*/directory_bin="\/opt\/$(shell basename $(CURDIR))\/bin\/"\n\
	directory_env="\/opt\/$(shell basename $(CURDIR)))\/"\n\
	VIRTUAL_ENV="\/opt\/$(shell basename $(CURDIR))\/venv\/"\n/' venv/bin/activate
	# set the app version var
	$(eval APP_VERSION := $(shell cat $(@)/setup.py | grep version | cut -d \' -f2 ))
	# build RPM
	fpm -s dir -t rpm --rpm-os linux --name symphony-es-$(shell basename $(CURDIR)) --version $(APP_VERSION) --iteration 1 --after-install ./post-install/run.sh --rpm-auto-add-directories --description "$(shell basename $(CURDIR))" ./venv/=/opt/$(shell basename $(CURDIR))/venv/ ./post-install/=/opt/$(shell basename $(CURDIR))/post-install/
	# put the rpm in a build dir
	test -d $(ROOT_DIR)/build || mkdir $(ROOT_DIR)/build
	mv *.rpm build/
	# remove the venv we built in
	rm -rf $(ROOT_DIR)/venv
endif

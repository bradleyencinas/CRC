.PHONY: build

build:
	sam build

deploy-infra:
	sam build && aws-vault exec bradleyencinas --no-session -- sam deploy

deploy-site:
	aws-vault exec bradleyencinas  --no-session -- aws s3 sync ./website-html s3://bradleyencinaswebsite

invoke-put:
	sam build && aws-vault exec bradleyencinas --no-session -- sam local invoke PutFunction